import cv2
import numpy as np

def calculate_ratios(image_path):
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
    object_ratio = object_area / total_pixels
    boundary_ratio = boundary_area / total_pixels
    background_ratio = background_area / total_pixels
    
    return object_ratio, boundary_ratio, background_ratio

# Example usage
image_path = 'yOriginal_Dataset/selfieman.webp'
object_ratio, boundary_ratio, background_ratio = calculate_ratios(image_path)
print(f"Object Ratio: {object_ratio}")
print(f"Boundary Ratio: {boundary_ratio}")
print(f"Background Ratio: {background_ratio}")

def main():
    calculate_ratios()

if __name__=="__main__":
    main()
