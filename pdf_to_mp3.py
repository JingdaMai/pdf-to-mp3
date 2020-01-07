from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pdftotext
from gtts import gTTS
from pathlib import Path

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file_location = askopenfilename() # open the dialog GUI

with open(file_location, "rb") as f:  # open the file in reading (rb) mode and call it f
    pdf = pdftotext.PDF(f)  # store a text version of the pdf file f in pdf variable

string_of_text = [text for text in pdf]
string_of_text = ''.join(string_of_text)

final_file = gTTS(text=string_of_text, lang='en')  # store file in variable
final_file.save(f'{Path(file_location).name}.mp3')  # save file to computer