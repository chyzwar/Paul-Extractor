from Tkinter import Tk
from tkFileDialog import askopenfilename, askdirectory
import zipfile
import os
import shutil


Tk().withdraw()

zip_file = askopenfilename(
    initialdir="/home/grigori/Dropbox", title='Please select a zip file')
targ_dir = askdirectory(
    initialdir="/home/grigori/Dropbox", title='Please select a directory')

print(targ_dir)

dir_name = targ_dir + os.sep + zip_file.split(os.sep)[-1].split("_")[0]
print(dir_name)


os.mkdir(dir_name)

fh = open(zip_file, 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    print(name)
    doc_name = name.split(os.sep)[-1].split(" ")[1] + ".docx"
    source = z.open(name)
    target = file(os.path.join(dir_name, doc_name), "wb")
    with source, target:
        shutil.copyfileobj(source, target)

fh.close()
