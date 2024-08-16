import cv2
import numpy as np
import os

def decimal_to_binary(num):
    # Split the number into integer and fractional parts
    integer_part = int(num)
    fractional_part = num - integer_part
    
    # Convert integer part to binary
    integer_binary = bin(integer_part).replace("0b", "")
    
    # Convert fractional part to binary
    fractional_binary = ""
    while fractional_part:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary += str(bit)
        fractional_part -= bit
        if len(fractional_binary) > 10:  # Limit the length of the fractional part to avoid infinite loop
            break
    
    return f"{integer_binary}.{fractional_binary}"

def calculate_ratios(image_path, output_dir):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Thresholding to segment the object
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    
    # Detect edges to find boundaries
    edges = cv2.Canny(gray, 100, 200)
    
    # Calculate areas
    object_area = cv2.countNonZero(binary)
    boundary_area = cv2.countNonZero(edges)
    background_area = binary.size - object_area - boundary_area
    
    # Calculate ratios
    total_pixels = binary.size
    object_ratio = round((object_area / total_pixels)*100, 1)
    boundary_ratio = round((boundary_area / total_pixels)*100, 1)
    background_ratio = round((background_area / total_pixels)*100, 1)
    
    # Create output images for object, boundary and background
    background = np.ones_like(binary) * 255 - binary - edges
    
    # Save the images in the specified directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cv2.imwrite(os.path.join(output_dir, 'object.png'), binary)
    cv2.imwrite(os.path.join(output_dir, 'boundary.png'), edges)
    cv2.imwrite(os.path.join(output_dir, 'background.png'), background)
    
    return object_ratio, boundary_ratio, background_ratio

# Example usage
image_path = 'Original_Dataset/selfieman.webp'
output_dir = 'Original_Dataset'
object_ratio, boundary_ratio, background_ratio = calculate_ratios(image_path, output_dir)

# Print the rounded ratios and their binary representations
print(f"Object Ratio: {object_ratio} (Binary: {decimal_to_binary(object_ratio)})")
print(f"Boundary Ratio: {boundary_ratio} (Binary: {decimal_to_binary(boundary_ratio)})")
print(f"Background Ratio: {background_ratio} (Binary: {decimal_to_binary(background_ratio)})")
print(f"overall ratio: {decimal_to_binary(background_ratio)}:{decimal_to_binary(background_ratio)}:{decimal_to_binary(background_ratio)}")
