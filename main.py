from quickshot import Screenshot
from ocr import OCR_Grab
import argparse
import os

parser = argparse.ArgumentParser(description="Capture screenshots of selected regions.")
parser.add_argument("--target_folder", type=str, default="", help="Where screenshot will be placed and then read/deleted from.")
args = parser.parse_args()

folder = os.path.expanduser(args.target_folder) 

quickshot_instance = Screenshot(folder)
quickshot_instance.run()
if quickshot_instance.screenshotTaken:
    ocr_instance = OCR_Grab(folder)
    ocr_instance.run()

