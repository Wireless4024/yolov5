#!/usr/bin/env python3
from pathlib import Path
import shutil
import sys

BASE_DIR = sys.argv[1]
print(f"Using base directory: {BASE_DIR}")
# --- Constants (mirroring your Rust code) ---
IMAGE_PATH = Path(f"{BASE_DIR}/images/")
IMAGE_EXT = "png"
LABEL_PATH = Path(f"{BASE_DIR}/labels/")

RATIO = 0.9
IMAGE_TRAIN = Path(f"{BASE_DIR}/dataset/images/train")
IMAGE_VALIDATE = Path(f"{BASE_DIR}/dataset/images/validation")
LABEL_TRAIN = Path(f"{BASE_DIR}/dataset/labels/train")
LABEL_VALIDATE = Path(f"{BASE_DIR}/dataset/labels/validation")


def main() -> int:
    # Collect (stem, full_label_path) for all files in LABEL_PATH
    files = []
    for entry in LABEL_PATH.iterdir():
        if not entry.is_file():
            continue
        name = entry.stem  # file_stem in Rust
        files.append((name, entry))

    base_image = IMAGE_PATH
    base_label = LABEL_PATH

    train_amount = int(len(files) * RATIO)
    train = files[:train_amount]
    validate = files[train_amount:]

    # Create output directories
    IMAGE_TRAIN.mkdir(parents=True, exist_ok=True)
    LABEL_TRAIN.mkdir(parents=True, exist_ok=True)

    for name, label_path in train:
        im_name = f"{name}.{IMAGE_EXT}"
        shutil.copy2(base_image / im_name, IMAGE_TRAIN / im_name)
        shutil.copy2(base_label / label_path.name, LABEL_TRAIN / label_path.name)

    IMAGE_VALIDATE.mkdir(parents=True, exist_ok=True)
    LABEL_VALIDATE.mkdir(parents=True, exist_ok=True)

    for name, label_path in validate:
        im_name = f"{name}.{IMAGE_EXT}"
        shutil.copy2(base_image / im_name, IMAGE_VALIDATE / im_name)
        shutil.copy2(base_label / label_path.name, LABEL_VALIDATE / label_path.name)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
