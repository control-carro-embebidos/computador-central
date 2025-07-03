import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image
import os

def save_channel_as_pgm(image, channel, output_path):
    width, height = image.size
    pixels = list(image.getdata())
    
    # Extract the specified channel (0=Red, 1=Green, 2=Blue)
    channel_data = [pixel[channel] for pixel in pixels]
    
    with open(output_path, 'w') as f:
        # Write the width, height, and maximum grayscale value
        f.write(f'{height} {width}\n')
        
        # Write the pixel data
        for i, value in enumerate(channel_data):
            f.write(f'{value} ')
            # Optional: add a newline after every width number of pixels for readability
            if (i + 1) % width == 0:
                f.write('\n')

def select_file_and_convert():
    # Open a file dialog to select an image file
    input_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff *.ico *.webp *.ppm *.pgm")]
    )

    if not input_path:
        print("No file selected.")
        return

    # Open the image using Pillow
    try:
        with Image.open(input_path) as img:
            # Ensure the image is in RGB mode
            img = img.convert("RGB")
            
            # Get the base name and directory of the input file
            base_name = os.path.basename(input_path)
            file_name, _ = os.path.splitext(base_name)
            output_dir = os.path.dirname(input_path)
            
            # Define the output file names for each channel
            red_output_path = os.path.join(output_dir, f"{file_name}_red.pgm")
            green_output_path = os.path.join(output_dir, f"{file_name}_green.pgm")
            blue_output_path = os.path.join(output_dir, f"{file_name}_blue.pgm")

            # Convert and save each channel
            save_channel_as_pgm(img, 0, red_output_path)
            save_channel_as_pgm(img, 1, green_output_path)
            save_channel_as_pgm(img, 2, blue_output_path)

            print(f"Red channel saved as {red_output_path}")
            print(f"Green channel saved as {green_output_path}")
            print(f"Blue channel saved as {blue_output_path}")
    except Exception as e:
        print(f"Failed to convert image: {e}")

# Create the Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Run the file dialog and conversion function
select_file_and_convert()
