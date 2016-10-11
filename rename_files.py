import os


def rename_files():
    file_names = os.listdir("resources/prank")
    print(file_names)
    o_dir = os.getcwd()
    os.chdir("prank")
    for file_name in file_names:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(o_dir)

rename_files()
