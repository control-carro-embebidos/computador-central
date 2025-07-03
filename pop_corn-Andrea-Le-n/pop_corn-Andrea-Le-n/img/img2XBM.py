import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def image_to_xbm(image_path, output_path, threshold=128):
    # Open the image and convert to grayscale
    image = Image.open(image_path).convert('L')
    width, height = image.size
    pixels = list(image.getdata())

    # Create a list of lists for pixel data
    pixel_data = [pixels[i * width:(i + 1) * width] for i in range(height)]

    # Initialize the XBM header
    xbm_data = []
    xbm_data.append(f'{height} {width}')
#     xbm_data.append(f'#define image_width {width}')
#     xbm_data.append(f'#define image_height {height}')
#     xbm_data.append('static char image_bits[] = {')
#     
    # Convert each row of grayscale data to XBM format
    for y in range(height):
        row_data = []
        for x in range(0, width, 8):
            byte = 0
            for bit in range(8):
                if x + bit < width:
                    if pixel_data[y][x + bit] >= threshold:
                        byte |= (1 << bit)
            row_data.append(f'0x{byte:02x}')
        xbm_data.append('    ' + ' '.join(row_data) )

    # Close the XBM data array
    xbm_data[-1] = xbm_data[-1].rstrip(',')  # Remove trailing comma from the last row
    xbm_data.append('};')

    # Write the XBM data to the output file
    with open(output_path, 'w') as f:
        f.write('\n'.join(xbm_data))

def select_file_and_convert():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff *.ico *.webp")]
    )

    if not file_path:
        print("No file selected.")
        return

    # Define the output file path
    output_dir = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    file_name, _ = os.path.splitext(base_name)
    output_path = os.path.join(output_dir, f"{file_name}.xbm")
    
    try:
        # Convert the image to XBM format
        image_to_xbm(file_path, output_path)
        print(f"XBM file saved as {output_path}")
    except Exception as e:
        print(f"Failed to convert image: {e}")

# Create the Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Run the file dialog and conversion function
select_file_and_convert()
