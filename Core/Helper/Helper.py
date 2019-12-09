import os

import yaml


def get_file_from_dir(dir_path: str, ext=None):
    allfiles = []
    need_ext_filter = (ext is not None)
    for root, dirs, files in os.walk(dir_path):
        for file_path in files:
            filepath = os.path.join(root, file_path)
            extension = os.path.splitext(filepath)[1][1:]
            if need_ext_filter and extension in ext:
                allfiles.append(filepath)
            elif not need_ext_filter:
                allfiles.append(filepath)
    return allfiles


def parseYaml(yaml_file: str):
    with open(yaml_file, 'r', encoding="utf-8") as file:
        file_data = file.read()
    return yaml.load(file_data, Loader=yaml.FullLoader)
