import os
import os.path

# TODO Lista plików posortowana po rozmiarze
# TODO Lista plików o tym skrócie (MD5, SHA-1/SHA-2)


def przegladanie(root):
    file_list = os.listdir(root)
    dir_list = []
    size_list = {}
    for item in file_list:
        if os.path.isfile(os.path.join(root, item)):
            full_name = os.path.join(root, item)
            file_size = os.path.getsize(full_name)
            if file_size not in size_list:
                size_list[file_size] = [full_name]
            else:
                size_list[file_size].append(full_name)

        if os.path.isdir(os.path.join(root, item)):
            dir_list.append(item)
        for dirname in dir_list:
            przegladanie(os.path.join(root, dirname))
    return size_list
