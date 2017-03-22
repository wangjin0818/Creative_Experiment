# FileName: backup_ver2.py
import os, sys, time, zipfile

source_dir = [r'D:\\Artificial_Intelligence']
target_dir = r'D:\\backup\\'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = raw_input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today) # make directory
    print 'Successfully created directory', today

f = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED)

for source in source_dir:
    for dirpath, dirnames, filenames in os.walk(source):
        for filename in filenames:
            print filename  
            f.write(os.path.join(dirpath,filename))
f.close()