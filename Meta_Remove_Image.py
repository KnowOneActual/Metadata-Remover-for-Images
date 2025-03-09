import os
from PIL import Image


def remove_metadata(image_path, output_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Save the image without metadata
        img.save(output_path)
        print(f"Processed and saved: {output_path}")


# Get input and output file paths from the user
image_path = input("Enter the path to the image file: ")
output_path = input("Enter the path to save the image without metadata: ")

# Ensure the output path has a valid file extension
if not output_path.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
    print("Please provide a valid output file name with an appropriate extension.")
else:
    # Call the function
    remove_metadata(image_path, output_path)
