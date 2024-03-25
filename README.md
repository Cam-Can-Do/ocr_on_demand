# ocr_on_demand
A utility for quickly taking a screenshot and running OCR on it, copying any detected text to the clipboard.
I mostly use this for learning and working in Japanese, but I've also found it to be useful for general
productivity.

## Installation (Ubuntu)
```
sudo apt-get install python3-dev tesseract-ocr tesseract-ocr-jpn libtesseract-dev xclip
git clone https://github.com/Cam-Can-Do/ocr_on_demand
cd ocr_on_demand
python3 -m venv venv
source venv/bin/activate
pip3 insatll -r requirements.txt --usepep517
```
## Installation (Arch)
```
sudo pacman -Sy install python3-dev tesseract libtesseract-dev xclip (select option for desired language for OCR after running this command)
git clone https://github.com/Cam-Can-Do/ocr_on_demand
cd ocr_on_demand
python3 -m venv venv
source venv/bin/activate
pip3 insatll -r requirements.txt --usepep517
```

## Usage
Command I use to run (absolute path is nice as I can use it with a keyboard shortcut)
`~/ocr_on_demand/bin/python3 ~/ocr_on_demand/ocr_on_demand/main.py --target_folder=~/.ocr_temp/`
Hold alt+shift while moving the mouse to select a rectangular region (similar in behavior to clicking and dragging on the desktop).
Release alt+shift to select the region and have any detected text copied to clipboard.
