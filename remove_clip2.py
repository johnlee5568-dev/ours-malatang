#!/usr/bin/env python3
import cv2
import numpy as np

def remove_left_clip(image_path, output_path):
    img = cv2.imread(image_path)
    
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    height, width = img.shape[:2]
    
    # Left side clip area - based on the green circle
    # The clip is on the left edge of the bowl
    x_start = int(width * 0.02)
    x_end = int(width * 0.20)
    y_start = int(height * 0.40)
    y_end = int(height * 0.65)
    
    # Create elliptical mask
    center = ((x_start + x_end) // 2, (y_start + y_end) // 2)
    axes = ((x_end - x_start) // 2, (y_end - y_start) // 2)
    cv2.ellipse(mask, center, axes, 0, 0, 360, 255, -1)
    
    # Apply inpainting
    result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    
    cv2.imwrite(output_path, result)
    print(f"Saved: {output_path}")

remove_left_clip("images/day1/enhanced_6.jpg", "images/day1/enhanced_6_v2.jpg")
