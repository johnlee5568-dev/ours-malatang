#!/usr/bin/env python3
import cv2
import numpy as np
from PIL import Image

def remove_object(image_path, output_path):
    # Read image
    img = cv2.imread(image_path)
    
    # Create mask for the clip area (right side of the bowl)
    # Based on the image, the clip is on the right edge
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    
    # Define the region where the clip is (right side of the bowl)
    height, width = img.shape[:2]
    
    # Roughly the region: right 1/4 of the image, middle height
    # Adjust based on the actual clip position
    x_start = int(width * 0.75)
    x_end = int(width * 0.95)
    y_start = int(height * 0.35)
    y_end = int(height * 0.65)
    
    # Create elliptical mask for the clip area
    mask[y_start:y_end, x_start:x_end] = 255
    
    # Apply inpainting (Telea method)
    result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    
    # Save
    cv2.imwrite(output_path, result)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    remove_object("images/day1/enhanced_6.jpg", "images/day1/enhanced_6_fixed.jpg")
