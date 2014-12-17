from Tkinter import Tk
from tkFileDialog import askopenfilename, askdirectory
import zipfile
import os
import shutil


Tk().withdraw()

zip_file = askopenfilename(
    initialdir="/", title='Please select a zip file')
targ_dir = askdirectory(
    title='Please select a directory')


dir_name = targ_dir + "/" + zip_file.split("/")[-1].split("_")[0]
print(dir_name)


os.mkdir(dir_name)

fh = open(zip_file, 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    print(name)
    doc_name = name.split("/")[-1].split("-")[1] + ".doc"
    source = z.open(name)
    target = file(os.path.join(dir_name, doc_name), "wb")
    with source, target:
        shutil.copyfileobj(source, target)

fh.close()
