# FileName: backup_ver1.py

import os
import sys
import time
import zipfile

source_dir = [r'D:\\Artificial_Intelligence']

target_dir = r'D:\\backup\\'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

f = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)

for source in source_dir:
    for dirpath, dirnames, filenames in os.walk(source):
        for filename in filenames:
            print filename  
            f.write(os.path.join(dirpath,filename))
f.close()