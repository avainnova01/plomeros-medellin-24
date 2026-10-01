import os
from PIL import Image

img_dir = "images"
for fname in os.listdir(img_dir):
    if fname.lower().endswith((".jpg", ".jpeg", ".png")):
        in_path = os.path.join(img_dir, fname)
        base = os.path.splitext(fname)[0]
        out_path = os.path.join(img_dir, base + ".webp")
        with Image.open(in_path) as im:
            im.save(out_path, "WEBP", quality=85)
            print(f"Converted {fname} -> {base}.webp")
print("Done converting to WebP!")
