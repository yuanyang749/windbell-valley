#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Resample a verified equal-duration loop using sprite-gen's guarded RIFE.

Input is an asset descriptor supported by sprite-gen. Output is a new directory
of PNGs, asset.json, and a provenance report. No generation or downloads occur.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path

from PIL import Image
from sprite_gen.spec.assets import load_asset
from sprite_gen.video.align import resample
from sprite_gen.video.rife import Rife


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--asset", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--factor", type=int, default=2)
    parser.add_argument("--mask", type=Path,
                        help="Fixed L-mode PNG matte for an opaque environment plate")
    args = parser.parse_args()
    if args.factor < 2:
        parser.error("--factor must be at least 2")
    if args.out_dir.exists():
        parser.error("output exists; choose a new directory")

    source = load_asset(args.asset)
    if len(source.frames) < 2:
        parser.error("a loop needs at least two source frames")
    if not all(math.isclose(d, source.durations[0], rel_tol=1e-9, abs_tol=1e-12)
               for d in source.durations):
        parser.error("variable frame durations require time-aware resampling")

    mask = None
    if args.mask:
        with Image.open(args.mask) as image:
            if image.format != "PNG" or image.mode != "L" or image.size != source.size:
                parser.error("mask must be an L-mode PNG matching the source canvas")
            mask = image.copy()
        if mask.getbbox() is None:
            parser.error("mask has no visible region")
        mask_bytes = mask.tobytes()
        opaque_bytes = bytes([255]) * (source.size[0] * source.size[1])
        if any(frame.getchannel("A").tobytes() not in (mask_bytes, opaque_bytes)
               for frame in source.frames):
            parser.error("fixed mask cannot replace variable subject transparency")

    model = Rife()
    provenance = []
    frames, facts = resample(source.frames, len(source.frames) * args.factor,
                            model, between="auto", cells_from=provenance)
    if len(frames) != len(source.frames) * args.factor:
        raise RuntimeError("engine returned an unexpected output frame count")
    if any(frame.size != source.size for frame in frames):
        raise RuntimeError("engine changed the canvas size")
    duration = source.duration / len(frames)

    args.out_dir.mkdir(parents=True, exist_ok=False)
    frame_dir = args.out_dir / "frames"
    frame_dir.mkdir()
    records = []
    for index, frame in enumerate(frames):
        frame = frame.convert("RGBA")
        if mask is not None:
            frame.putalpha(mask)
        name = f"frames/frame-{index:05d}.png"
        frame.save(args.out_dir / name)
        records.append({"file": name, "duration": duration})

    model_description = model.describe()
    report = {
        "source_descriptor": args.asset.name,
        "source_descriptor_sha256": hashlib.sha256(args.asset.read_bytes()).hexdigest(),
        "source_file_sha256": list(source.source_digests),
        "method": "sprite_gen.video.align.resample; between=auto",
        "model": model_description.get("model"),
        "binary_name": Path(model_description.get("binary", "")).name,
        "input_frames": len(source.frames), "output_frames": len(frames),
        "input_duration_seconds": source.duration,
        "output_duration_seconds": duration * len(frames),
        "input_fps": len(source.frames) / source.duration,
        "output_fps": 1 / duration,
        "canvas_size": list(source.size), "anchor": list(source.anchor),
        "fixed_mask_sha256": hashlib.sha256(args.mask.read_bytes()).hexdigest()
        if args.mask else None,
        "facts": facts, "cells_from": provenance,
    }
    (args.out_dir / "rife-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Write the descriptor last: an interrupted directory is not a ready asset.
    (args.out_dir / "asset.json").write_text(json.dumps({
        "kind": "sprite-gen-asset", "version": 1,
        "anchor": list(source.anchor), "frames": records,
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.out_dir), "frames": len(frames),
                      "seconds": report["output_duration_seconds"],
                      "rife_frames": facts["made_by_rife"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
