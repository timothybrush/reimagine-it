#!/usr/bin/env python3
"""Render desktop + phone stills for the public-source proof lane.

Outputs docs/examples/public-sources/<slug>/auto-desktop.png (1400x1100)
and auto-phone.png (480x960) from each folder's committed auto.html —
the same shapes the end-user renderer produces, so the docs site can
treat both lanes identically.

Usage: python scripts/render-public-shots.py [slug ...]
"""

from pathlib import Path
import subprocess
import sys

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


def find_browser() -> str:
    for candidate in (
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
    ):
        if Path(candidate).is_file():
            return candidate
    raise SystemExit("no headless-capable browser found")


def screenshot(browser: str, page: Path, output: Path, width: int, height: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            browser,
            "--headless",
            "--hide-scrollbars",
            "--no-sandbox",
            "--disable-extensions",
            "--disable-sync",
            "--disable-background-networking",
            f"--window-size={width},{height}",
            "--virtual-time-budget=4000",
            f"--screenshot={output}",
            page.resolve().as_uri(),
        ],
        check=True,
        capture_output=True,
        timeout=90,
    )
    if not output.is_file() or output.stat().st_size < 1024:
        raise SystemExit(f"could not render {page} -> {output}")


def render_slug(browser: str, slug: str) -> None:
    folder = ROOT / "examples" / "public-sources" / slug
    auto = folder / "auto.html"
    if not auto.is_file():
        raise SystemExit(f"missing {auto} — run Auto on the source first")
    out_dir = ROOT / "docs" / "examples" / "public-sources" / slug
    screenshot(browser, auto, out_dir / "auto-desktop.png", 1400, 1100)
    screenshot(browser, auto, out_dir / "auto-phone.png", 480, 960)
    print(f"  {slug}: auto desktop + phone")


def main() -> int:
    public_dir = ROOT / "examples" / "public-sources"
    slugs = sys.argv[1:] or sorted(
        d.name for d in public_dir.iterdir() if d.is_dir()
    )
    browser = find_browser()
    for slug in slugs:
        render_slug(browser, slug)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
