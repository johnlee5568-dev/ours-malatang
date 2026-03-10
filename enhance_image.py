#!/usr/bin/env python3
from PIL import Image, ImageEnhance
import sys

def enhance_image(input_path, output_path):
    img = Image.open(input_path)
    
    # Convert to RGB if needed
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Enhance brightness (+15%)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.15)
    
    # Enhance contrast (+20%)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    
    # Enhance color/saturation (+15%)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.15)
    
    # Sharpen (+30%)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.3)
    
    img.save(output_path, quality=95)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.jpg', '_enhanced.jpg')
    enhance_image(input_file, output_file)
