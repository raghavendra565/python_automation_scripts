import os
import glob
import re
import json

# Main Path of Lua files
main_path = os.getcwd()
# Lua Chunk files Path
os.chdir("..")
child_path = os.getcwd()

# Changing directory to main path
os.chdir(main_path)

files_details = []
for file in glob.glob("*.lua"):
    # Reading a lua file
    with open(file, "r") as fh:
        file_content = fh.read()
        # Finding version in lua file
        match_string = re.search('function(\s)([a-zA-Z0-9_\./\\-]*).version\(\)(\s+)return(\s)"([A-Za-z0-9_\./\\-]*)"(\s+)end', file_content).group()
        version = re.search('"([A-Za-z0-9_\./\\-]*)"', match_string).group()
        version = version.strip('"')
    fd = [file, os.path.getsize(file), version]
    os.chdir(child_path)
    ch_files_count = 0
    for ch_file in glob.glob(file + "*"):
        print(ch_file)
        ch_files_count += 1
    os.chdir(main_path)
    fd.append(ch_files_count)
    files_details.append(fd)

# Writing output to json file
with open("LuaFileVersions.json", "w", encoding='utf-8') as fh:
    json.dump({"available_files": files_details}, fh, ensure_ascii=False, indent=4)

# function scheduler_02.version()
# 	return "2.0"
# end

# function powerfail.version()
# 	return "1.0.2"
# end

# function api32.version()
# 	return "2.0"
# end
