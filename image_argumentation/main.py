import tkinter as tk
from tkinter import filedialog
from image_augmentation import augment_and_visualize

def select_image_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    return file_path

def main():
    image_path = select_image_file()
    if image_path:
        augment_and_visualize(image_path)
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()