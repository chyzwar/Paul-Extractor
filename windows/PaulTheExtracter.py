from Tkinter import Tk
from tkFileDialog import askopenfilename, askdirectory
import zipfile
import os
import shutil


Tk().withdraw()

zip_file = askopenfilename(
    initialdir="/", title='Please select a zip file')
targ_dir = askdirectory(
    initialdir="/", title='Please select a directory')

dir_name = targ_dir + os.pathsep + zip_file.split(os.pathsep)[-1].split("_")[0]

os.mkdir(dir_name)


fh = open(zip_file, 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    doc_name = name.split(os.pathsep)[0].split(" ")[1] + ".docx"
    source = z.open(name)
    target = file(os.path.join(dir_name, doc_name), "wb")
    with source, target:
        shutil.copyfileobj(source, target)

fh.close()
