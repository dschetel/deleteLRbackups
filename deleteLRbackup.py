import os, os.path, time
import shutil

# specify path
# path = '/Users/dgs/Desktop/test'
path = '/Volumes/YosemiteData/Pictures/Lightroom/Backups'

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

number_of_subfolders = get_immediate_subdirectories(path)
print number_of_subfolders[0]

if len(number_of_subfolders) > 3:
	for i in range(0, len(number_of_subfolders)-3):
		print path+'/'+number_of_subfolders[i]
		shutil.rmtree(path+'/'+number_of_subfolders[i])