import pytesseract
import zipfile
import os
from PIL import Image
# Define paths
zip_file_path = ""
extracted_folder_path = ""
output_text_file_path = ""

# Step 1: Unzip the uploaded file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

# Step 2: Get a sorted list of directories based on the time-stamp in their names
# List directories in sorted order
sorted_directories = sorted(os.listdir(extracted_folder_path))

# Step 3: Extract text from each image in each directory in page order and combine in final text
full_text = []
for directory in sorted_directories:
    dir_path = os.path.join(extracted_folder_path, directory)
    if os.path.isdir(dir_path):
        # List all images in the directory and sort them by page number
        sorted_images = sorted(os.listdir(dir_path))
        for image_file in sorted_images:
            image_path = os.path.join(dir_path, image_file)
            # Perform OCR on each image
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            # Append the extracted text with directory and page info
            full_text.append(f"Directory: {directory}, Page: {image_file}\n{text}\n\n")

# Step 4: Save the full combined text into a text file
with open(output_text_file_path, "w") as output_file:
    output_file.write("\n".join(full_text))

output_text_file_path
