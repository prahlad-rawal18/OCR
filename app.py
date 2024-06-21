import tkinter as tk
from tkinter import filedialog, Listbox, Button, Label, Text
from PIL import Image, ImageTk
import pytesseract
import os

class ImageTextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Text Extractor")

        self.label = Label(root, text="Select images from a folder:")
        self.label.pack(pady=5)

        self.select_button = Button(root, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=5)

        self.image_listbox = Listbox(root, selectmode=tk.SINGLE)
        self.image_listbox.pack(pady=5, fill=tk.BOTH, expand=True)

        self.extract_button = Button(root, text="Extract Text", command=self.extract_text)
        self.extract_button.pack(pady=5)

        self.text_label = Label(root, text="Extracted Text:")
        self.text_label.pack(pady=5)

        self.textbox = Text(root, height=10)
        self.textbox.pack(pady=5, fill=tk.BOTH, expand=True)

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.image_listbox.delete(0, tk.END)
            for filename in os.listdir(folder_selected):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
                    self.image_listbox.insert(tk.END, os.path.join(folder_selected, filename))

    def extract_text(self):
        selected_index = self.image_listbox.curselection()
        if selected_index:
            selected_image = self.image_listbox.get(selected_index)
            extracted_text = self.perform_ocr(selected_image)
            self.display_extracted_text(extracted_text)
        else:
            self.textbox.delete("1.0", tk.END)
            self.textbox.insert(tk.END, "No image selected.")

    def perform_ocr(self, image_path):
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            print(f"Error performing OCR: {e}")
            return ""

    def display_extracted_text(self, text):
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageTextExtractorApp(root)
    root.mainloop()
