import os

files = os.listdir('your_images')
files_formats = []
[files_formats.append(i.split('.')[1]) for i in files]

def get_files_formats():
    global files_formats
    return files_formats

def rename_all():
    global files
    global files_formats
    [os.rename(f'your_images/{files[i]}', f'your_images/{i}.{files_formats[i]}') for i in range(len(files))]
    pass