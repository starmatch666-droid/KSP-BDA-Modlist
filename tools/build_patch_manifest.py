#!/usr/bin/env python3
"""Rebuild patches/SHA256SUMS.txt and patches/MANIFEST.md."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATCHES = ROOT / "patches"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    files = sorted(
        path
        for path in PATCHES.rglob("*")
        if path.is_file()
        and path.name not in {"SHA256SUMS.txt", "MANIFEST.md"}
        and "__pycache__" not in path.parts
    )
    sums = []
    rows = []
    for path in files:
        relative = path.relative_to(PATCHES).as_posix()
        digest = sha256(path)
        sums.append(f"{digest} *{relative}")
        rows.append((relative, path.stat().st_size, digest))

    (PATCHES / "SHA256SUMS.txt").write_text("\n".join(sums) + "\n", encoding="utf-8")

    lines = [
        "# 补丁文件清单与校验和",
        "",
        f"共 {len(rows)} 个文件。SHA256 以 `patches/SHA256SUMS.txt` 为准。",
        "",
        "| 文件 | 大小 | SHA256（前 16 位） |",
        "|---|---:|---|",
    ]
    for relative, size, digest in rows:
        if size >= 1024 * 1024:
            size_text = f"{size / (1024 * 1024):.2f} MB"
        elif size >= 1024:
            size_text = f"{size / 1024:.1f} KB"
        else:
            size_text = f"{size} B"
        lines.append(f"| `{relative}` | {size_text} | `{digest[:16]}` |")
    (PATCHES / "MANIFEST.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} patch files.")


if __name__ == "__main__":
    main()
