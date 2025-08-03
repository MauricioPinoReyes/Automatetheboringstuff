import zipfile
import os
import shutil
from pathlib import Path

directorio_actual = Path.cwd()
#print(directorio_actual)

""" (h / 'spam').mkdir(exist_ok=True)
with open(h / 'spam/file1.txt', 'w', encoding='utf-8') as file:
    file.write('Hello') """

#shutil.copy(h / 'spam/file1.txt', h)

#shutil.copy(h / 'spam/file1.txt', h / 'spam/file2.txt')

#shutil.copytree(h / 'spam', h / 'spam_backup')

#(h / 'spam2').mkdir()
#shutil.move(h / 'spam/file1.txt', h / 'spam2')

#shutil.move(h / 'spam/file2.txt', h / 'spam2/new_name.txt')

""" for filename in (Path.cwd()/ 'spam_backup').glob('*.txt'):
    #os.unlink(filename)
    print('Deleting', filename) """

#print(list(directorio_actual.iterdir()))

""" (directorio_actual / 'spam').mkdir(exist_ok=True)
(directorio_actual / 'spam/eggs').mkdir(exist_ok=True)
(directorio_actual / 'spam/eggs2').mkdir(exist_ok=True)
(directorio_actual / 'spam/eggs/bacon').mkdir(exist_ok=True)
 """

""" for f in ['spam/file1.txt', 'spam/eggs/file2.txt', 'spam/eggs/file3.txt',
'spam/eggs/bacon/file4.txt']:
    with open(directorio_actual / f, 'w', encoding='utf-8') as file:
         file.write('Hello') """


""" for folder_name, subfolders, filenames in os.walk(directorio_actual / 'spam'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': '+ filename)
        # Rename file to uppercase:
        p = Path(folder_name)
        shutil.move(p / filename, p / filename.upper())
   
    print('')
 """
""" with open('file1.txt', 'w', encoding='utf-8') as file_obj:
    file_obj.write('Hello' * 10000)

with zipfile.ZipFile('example.zip', 'w') as example_zip:
   example_zip.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED,compresslevel=9) """

""" example_zip = zipfile.ZipFile('example.zip')
print(example_zip.namelist()) """

#print(h)
