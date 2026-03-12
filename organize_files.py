import os
import shutil

folder = 'test_folder'

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.avi', '.mkv'],
    'Audios': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isfile(file_path):
        for category, extensions in file_types.items():
            if any(filename.endswith(ext) for ext in extensions):
                category_folder = os.path.join(folder, category)

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                shutil.move(file_path, os.path.join(category_folder, filename))

print("Files have been organized.")