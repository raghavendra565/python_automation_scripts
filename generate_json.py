import os
import glob
import re
import json

# Main Path of Lua files
main_path = os.getcwd()

files_details = []
for file in glob.glob("*.lua"):
    CHUNK_SIZE = 1000
    file_number = 0
    with open(file) as f:
        chunk = f.read(CHUNK_SIZE)
        while chunk:
            with open(file + str(file_number), "w") as chunk_file:
                chunk_file.write(chunk)
            file_number += 1
            chunk = f.read(CHUNK_SIZE)

    # Reading a lua file
    with open(file, "r") as fh:
        file_content = fh.read()

        # Finding version in lua file
        match_string = re.search('function(\s)([a-zA-Z0-9_\./\\-]*).version\(\)(\s+)return(\s)"([A-Za-z0-9_\./\\-]*)"(\s+)end', file_content).group()
        version = re.search('"([A-Za-z0-9_\./\\-]*)"', match_string).group()
        version = version.strip('"')

    fd = [file, os.path.getsize(file), version, file_number]
    # ch_files_count = 0
    # for ch_file in glob.glob(file + "*"):
    #     ch_files_count += 1
    # fd.append(ch_files_count)
    files_details.append(fd)
    # break

# Writing output to json file
with open("LuaFileVersions.json", "w", encoding='utf-8') as fh:
    json.dump({"available_files": files_details}, fh, ensure_ascii=False, indent=4)

