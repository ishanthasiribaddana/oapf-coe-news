from PIL import Image
import os

# Images to optimize
images = [
    "20251214_154113.jpg",
    "20251214_160111.jpg",
    "20251214_160124.jpg",
    "20251214_160249.jpg",
    "20251214_165934.jpg",
    "Untitled-2.jpg"
]

# Max width for web
MAX_WIDTH = 1200

for img_name in images:
    if os.path.exists(img_name):
        img = Image.open(img_name)
        
        # Calculate new height maintaining aspect ratio
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_height = int(img.height * ratio)
            img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)
        
        # Convert to RGB if necessary (for JPEG)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Save with optimization
        img.save(img_name, 'JPEG', quality=80, optimize=True)
        
        # Get new size
        new_size = os.path.getsize(img_name) / 1024
        print(f"Optimized {img_name}: {new_size:.1f} KB")

print("\nDone! All images optimized.")
