import os
import sys
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

# Version of the application
app_version = "0.2.1"


def display_help():
    """
    Display a help message in the console with usage instructions.
    """
    help_message = r"""
    --- Welcome ---
    
    Hi, I'm Alireza Fazeli, and I created this application with love.
    This application is designed to make your life easier. Please follow my LinkedIn and GitHub:
    https://linkedin.com/in/alirezafazeli
    https://github.com/alirezafazeli8
    
    You need two paths: 
    1. The path to your JPEG file.
       Example: "D:\\3- photo\\yakuza.jpg"
    2. The destination path where you want to save the PNG.
       Example: "C:\\Users\\Alireza\\Desktop"
       
    Commands:
    -c, --convert : Convert your JPEG file to PNG.
                    Example: python JpegToPngConverter.py -c "D:\\3- photo\\yakuza.jpg" "C:\\Users\\Alireza\\Desktop"
                    
    -h, --help : Display this help message.
    
    -v : Show the current version of the application.
    
    Bye bye :))))
    
    ---------------
    """
    print(help_message)


def convert_image(file_path, save_file_path):
    """
    Convert a JPEG image to PNG and save it to the specified path.
    
    Parameters:
    - file_path (str): Path of the JPEG file.
    - save_file_path (str): Directory to save the PNG file.
    """
    try:
        # Open the JPEG image file
        user_image = Image.open(file_path)

        # Extract the base name of the file without extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]

        # Construct the full path for the PNG output
        png_file_path = os.path.join(save_file_path, f"{file_name}.png")

        # Save the image as PNG
        user_image.save(png_file_path, "PNG")

        # Show a success message
        messagebox.showinfo("Conversion Successful", f"File saved at: {png_file_path}")
    except FileNotFoundError:
        # Show an error message if file not found
        messagebox.showerror("Error", "File not found. Please provide a valid file path.")
    except Exception as e:
        # Show any unexpected error
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


def open_file_dialog():
    """
    Open a file dialog to select a JPEG file, and insert the file path in the entry widget.
    """
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])
    if file_path:
        entry_file_path.delete(0, tk.END)  # Clear any existing text
        entry_file_path.insert(0, file_path)  # Insert the selected file path


def save_directory_dialog():
    """
    Open a dialog to select a directory to save the PNG file.
    """
    directory_path = filedialog.askdirectory()
    if directory_path:
        entry_save_path.delete(0, tk.END)  # Clear any existing text
        entry_save_path.insert(0, directory_path)  # Insert the selected directory path


def convert_button_action():
    """
    Action triggered when the convert button is pressed. It checks for file path and save path
    and calls the convert_image function if both are provided.
    """
    file_path = entry_file_path.get()
    save_file_path = entry_save_path.get()
    if file_path and save_file_path:
        convert_image(file_path, save_file_path)
    else:
        # Show a warning if either file path or save path is missing
        messagebox.showwarning("Warning", "Please select both file and save path.")


# Set up the main application window
root = tk.Tk()
root.title("JPEG to PNG Converter")
root.geometry("400x250")

# Label and entry for selecting the JPEG file path
label_file_path = tk.Label(root, text="Select JPEG File:")
label_file_path.pack(pady=5)
entry_file_path = tk.Entry(root, width=40)
entry_file_path.pack(pady=5)
button_file_browse = tk.Button(root, text="Browse", command=open_file_dialog)
button_file_browse.pack(pady=5)

# Label and entry for selecting the save directory path
label_save_path = tk.Label(root, text="Select Destination Directory:")
label_save_path.pack(pady=5)
entry_save_path = tk.Entry(root, width=40)
entry_save_path.pack(pady=5)
button_save_browse = tk.Button(root, text="Browse", command=save_directory_dialog)
button_save_browse.pack(pady=5)

# Convert button
button_convert = tk.Button(root, text="Convert to PNG", command=convert_button_action)
button_convert.pack(pady=20)

# Start the Tkinter main event loop
root.mainloop()