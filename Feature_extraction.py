import cv2
import numpy as np
import os

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
    object_ratio = round((object_area / total_pixels) * 100, 1)
    boundary_ratio = round((boundary_area / total_pixels) * 100, 1)
    background_ratio = round((background_area / total_pixels) * 100, 1)
    
    return object_ratio, boundary_ratio, background_ratio

def rename_image(image_path, output_dir, object_ratio, boundary_ratio, background_ratio):
    # Construct the new filename
    new_filename = f"{object_ratio}_{boundary_ratio}_{background_ratio}.jpeg"
    
    # Get the full path for the new filename
    new_filepath = os.path.join(output_dir, new_filename)
    
    # Rename the image file
    os.rename(image_path, new_filepath)
    
    return new_filepath

def process_images_in_directory(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Check if it is a file
        if os.path.isfile(file_path):
            # Calculate ratios
            object_ratio, boundary_ratio, background_ratio = calculate_ratios(file_path)
            
            # Rename the image based on the calculated ratios
            new_filepath = rename_image(file_path, directory, object_ratio, boundary_ratio, background_ratio)
            
            # Print the new file path
            print(f"Image renamed to: {new_filepath}")

# Example usage
directory = 'Original_Dataset'
process_images_in_directory(directory)
