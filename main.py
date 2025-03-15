import os
from os.path import isfile, join
import json
from distutils import dir_util
from pathlib import Path

OUTPUT_DIR = "build"
STARTING_PATH = "./src/sounds/edited"
FINAL_PATH = "./sounds"
FULL_FINAL_PATH = f"./{OUTPUT_DIR}/sounds"

def get_files_list(path, results, key=''):
    for file in os.listdir(path):
        new_path = join(path, file)
        if isfile(new_path):
            if ".DS_Store" in file:
                continue
            if not key in results:
                results[key] = []
            results[key].append(
                new_path.replace(STARTING_PATH, FINAL_PATH)
            )
        else:
            get_files_list(new_path, results, key=file)
    return results

def copy_files():
    try:
        os.rmdir(f"./{OUTPUT_DIR}/sounds")
    except:
        pass
    dir_util.copy_tree(STARTING_PATH, FULL_FINAL_PATH)

def create_page():
    files_list = get_files_list(STARTING_PATH, {})
    with open("./src/index.html", "r") as f:
        template = f.read()

    Path(f"./{OUTPUT_DIR}").mkdir(exist_ok=True)

    with open(f"./{OUTPUT_DIR}/index.html", "w") as f:
        f.write(template.replace('SOUND_FILE_LIST', json.dumps(files_list)))
    copy_files()

if __name__ == "__main__":
    create_page()