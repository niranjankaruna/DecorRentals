#!/usr/bin/env python3
"""
Simple script to generate `data.json` and download images into `images/`.
This uses only the Python standard library so no extra dependencies are required.
Run it with: python fetch_data.py
"""
import os
import json
import urllib.request

HERE = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(HERE, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# Sample data to fetch - replace or extend as needed
ITEMS = [
    {
        "id": "vase",
        "title": "Ceramic Vase",
        "description": "Elegant ceramic vase for table decor.",
        "image_url": "https://via.placeholder.com/800x600.png?text=Ceramic+Vase",
    },
    {
        "id": "lamp",
        "title": "Vintage Lamp",
        "description": "Warm vintage lamp for cozy lighting.",
        "image_url": "https://via.placeholder.com/800x600.png?text=Vintage+Lamp",
    },
]

output = []
for item in ITEMS:
    url = item.get("image_url")
    # derive extension from URL path (fallback to .png)
    path_part = url.split("?")[0]
    ext = os.path.splitext(path_part)[1] or ".png"
    filename = f"{item['id']}{ext}"
    dest_path = os.path.join(IMAGES_DIR, filename)
    try:
        print(f"Downloading {url} -> {dest_path}")
        urllib.request.urlretrieve(url, dest_path)
        local_image = os.path.join("images", filename)
    except Exception as exc:
        print("Warning: failed to download", url, "->", exc)
        # fall back to remote URL if download fails
        local_image = url

    output.append({
        "id": item["id"],
        "title": item["title"],
        "description": item["description"],
        "image": local_image,
    })

out_file = os.path.join(HERE, "data.json")
with open(out_file, "w", encoding="utf-8") as fh:
    json.dump(output, fh, indent=2, ensure_ascii=False)

print(f"Wrote {out_file} ({len(output)} items)")
