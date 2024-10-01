import os
import cv2
import numpy as np
from glob import glob

# Set the paths
input_folder = '/path/to/extracted/Data'
output_folder = '/path/to/preprocessed/Data'
os.makedirs(output_folder, exist_ok=True)

# CLAHE function
def apply_clahe(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    if len(image.shape) == 2:  # Grayscale
        return clahe.apply(image)
    elif len(image.shape) == 3:  # RGB
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        l = clahe.apply(l)
        return cv2.merge((l, a, b))

# Process the dataset
for img_path in glob(os.path.join(input_folder, "*.jpg")):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # Load MRI as grayscale
    img_clahe = apply_clahe(img)
    img_normalized = img_clahe / 255.0  # Normalize to range [0, 1]
    output_path = os.path.join(output_folder, os.path.basename(img_path))
    cv2.imwrite(output_path, (img_normalized * 255).astype(np.uint8))
