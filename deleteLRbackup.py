import os, os.path, time
import shutil

# specify path
path = 'path/to/Lightroom/Backups'

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def delete_old_backups(number_of_subfolders, path):
	if len(number_of_subfolders) > 3:
		for i in range(0, len(number_of_subfolders)-3):
			print path+'/'+number_of_subfolders[i]
			shutil.rmtree(path+'/'+number_of_subfolders[i])

number_of_subfolders = get_immediate_subdirectories(path)
delete_old_backups(number_of_subfolders, path)