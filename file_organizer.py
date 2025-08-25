import os
import shutil

def organize_folder(folder_path):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav'],
        'Archives': ['.zip', '.rar'],
        'Scripts': ['.py', '.js']
    }

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    break  # stop checking once a match is found

if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    if os.path.isdir(folder):
        organize_folder(folder)
        print("✅ Folder organized successfully!")
    else:
        print("❌ Invalid folder path. Please try again.")
