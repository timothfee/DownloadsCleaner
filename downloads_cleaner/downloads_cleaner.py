import os ##When imported, it lets the user interact with the native OS Python is currently running on.
import collections ##built-in Python module that implements specialized container datatypes providing alternatives to Python's general purpose built-in containers such as dict , list , set , and tuple .

##This portion creates a path for the downloads folder by finding the user and then adding Downloads to the end.
DOWNLOADS_PATH = os.path.join(
    os.path.expanduser('~'),
    'Downloads'
)

##This creates folders by the file type.
file_mappings = collections.defaultdict()
for filename in os.listdir(DOWNLOADS_PATH):
    file_type = filename.split('.')[-1]
    file_mappings.setdefault(file_type, []).append(filename)

##This iterates through all the files and places them in new folders if the folder does not already exist.
for folder_name, folder_items in file_mappings.items():
    folder_path = os.path.join(DOWNLOADS_PATH, folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    for folder_item in folder_items:
        source = os.path.join(DOWNLOADS_PATH, folder_item)
        destination = os.path.join(folder_path, folder_item)
        print(f'Moving {source} to {destination}')
        os.rename(source, destination)

