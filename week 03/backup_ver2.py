# FileName: backup_ver2.py
import os, sys, time, zipfile

source_dir = [r'D:\\Artificial_Intelligence']
target_dir = r'D:\\backup\\'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print 'Successfully created directory', target_dir

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today) # make directory
    print 'Successfully created directory', today
# The name of the zip file
target = today + os.sep + now + '.zip'

f = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)

for source in source_dir:
    for dirpath, dirnames, filenames in os.walk(source):
        for filename in filenames:
            print filename  
            f.write(os.path.join(dirpath,filename))
f.close()