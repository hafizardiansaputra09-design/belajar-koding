import os
import shutil

file_mapping = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.pdf': 'Documents',
    '.py': 'Scripts',
    '.txt': 'TextFiles',
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.ttf': 'Fonts',
}

def organize_files(folder_test):
    print(f"Organizing files in: {folder_test}")

    for filename in os.listdir(folder_test):
        if filename == 'smart-file-organizer.py':
            continue
        
        file_path = os.path.join(folder_test, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)

            if ext in file_mapping:
                folder_name = file_mapping[ext]

                target_folder = os.path.join(folder_test, folder_name)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                try:
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved: {filename} to {folder_name}")
                except Exception as e:
                    print(f"Error moving {filename}: {e}")

    print(f"Finished organizing files in: {folder_test}")

if __name__ == "__main__":
    organize_files('folder-test')
