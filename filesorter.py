
import os
import shutil

folder_path="test2_folder"

file_type={
    "Images": [".png",".jpg"],
    "Videos":[".mp4",".mkv"],
    "Music": [".mp3", ".wav"],
    "Documents": [".pdf", ".txt", ".docx"]
}
for file in os.listdir(folder_path):
    file_path=os.path.join(folder_path,file)

    if os.path.isdir(file_path):
        continue

    _,ext=os.path.splitext(file)

    moved=False

    for folder_name,extensions in file_type.items():
        if ext.lower() in extensions:
            new_folder=os.path.join(folder_path,folder_name)

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            shutil.move(file_path,os.path.join(new_folder,file))
            print(f"{file}-->{folder_name}")
            moved=True
            break
    
    if not moved:
        other_folder=os.path.join(folder_path,"others")
        if not os.path.exists(other_folder):
            os.makedirs(other_folder)

        shutil.move(file_path,os.path.join(other_folder,file))
        print(f"{file}-->{folder_name}")
