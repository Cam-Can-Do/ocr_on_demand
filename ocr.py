from PIL import Image
import time
import pyperclip
import pytesseract
import os

class OCR_Grab():
    def __init__(self, target_folder):
        self.target_folder = os.path.expanduser(target_folder) if target_folder else ""


    # Uses Tesseract (pytesseract) OCR to extract text from image and return without leading/trailing whitespace.
    def extractText(self, imagePath):
        text = (pytesseract.image_to_string(Image.open(imagePath), lang='jpn+eng'))
        return text.strip()

    # Returns true if file at `image_path` is a valid image, false otherwise.
    def is_valid_image(self, image_path):
        if image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            try:
                image = Image.open(image_path)
                image.verify()  # Verify the image integrity
                return True
            except (IOError, SyntaxError):
                return False

    # TODO: Make `source_folder` into command line argument.
    # IMPORTANT: Use a dedicated folder for `source_folder`!
    # Program will OCR and delete any images in `source_folder` that contain text.

    def run(self):
        print(f"Scanning: {self.target_folder}")
        # List filenames in source_folder.
        if self.target_folder:
            files = os.listdir(self.target_folder) 
        else:
            files = os.listdir()
        for file in files:
            full_path = os.path.join(self.target_folder, file)
            if self.is_valid_image(full_path):
                text = self.extractText(full_path)
                if text != "":
                    print(f"{file} contains text: \n{text}")
                    pyperclip.copy(text)
                    print("Text copied to clipboard")
                    os.remove(full_path)
                    print("Temp image deleted: ", full_path)

            #time.sleep(0.1)