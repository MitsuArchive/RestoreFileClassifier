import os
import shutil
import subprocess
import datetime
from pathlib import Path
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_VIDEO_DIR = BASE_DIR / "output/videos"
OUTPUT_IMAGE_DIR = BASE_DIR / "output/images"
OUTPUT_OTHER_DIR = BASE_DIR / "output/others"
LOG_DIR = BASE_DIR / "log"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff"}

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
log_path = LOG_DIR / f"result_{timestamp}.csv"
log_lines = ["filename,result"]

def is_valid_video(path: Path) -> bool:
    try:
        result = subprocess.run(
            [
                "ffprobe", "-v", "error",
                "-select_streams", "v",
                "-show_entries", "stream=codec_type",
                "-of", "default=noprint_wrappers=1:nokey=1",
                str(path)
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        return "video" in result.stdout.strip().lower()
    except Exception:
        return False

def is_valid_image(path: Path) -> bool:
    try:
        with Image.open(path) as img:
            img.verify()
        with Image.open(path) as img:
            img.load()
        return True
    except Exception:
        return False

def process_file(file_path: Path):
    ext = file_path.suffix.lower()

    try:
        if ext in IMAGE_EXTENSIONS:
            if is_valid_image(file_path):
                dest = OUTPUT_IMAGE_DIR / file_path.name
                shutil.move(str(file_path), str(dest))
                log_lines.append(f"{file_path.name},image")
                return

        if is_valid_video(file_path):
            dest = OUTPUT_VIDEO_DIR / file_path.name
            shutil.move(str(file_path), str(dest))
            log_lines.append(f"{file_path.name},video")
            return

        dest = OUTPUT_OTHER_DIR / file_path.name
        shutil.move(str(file_path), str(dest))
        log_lines.append(f"{file_path.name},other")

    except Exception as e:
        dest = OUTPUT_OTHER_DIR / file_path.name
        shutil.move(str(file_path), str(dest))
        log_lines.append(f"{file_path.name},error:{str(e)}")

def main():
    for d in [OUTPUT_VIDEO_DIR, OUTPUT_IMAGE_DIR, OUTPUT_OTHER_DIR, LOG_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    files = [f for f in INPUT_DIR.iterdir() if f.is_file()]
    print(f"🔍 Processing {len(files)} files...")

    with ThreadPoolExecutor() as executor:
        executor.map(process_file, files)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))

    print(f"✅ Done. Log saved to: {log_path.name}")


if __name__ == "__main__":
    main()
