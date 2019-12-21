import os
import hashlib


def hash_file(file_path, block_size=65536):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(block_size), b''):
            hasher.update(block)
    return hasher.hexdigest()


def get_dir_info(dir_path, save_hashes=False):
    dir_info = {'files': {}, 'directories': {}, 'size': 0}
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            dir_info['files'][item] = {}
            dir_info['files'][item]['name'] = item
            dir_info['files'][item]['size'] = os.path.getsize(item_path)
            dir_info['size'] += dir_info['files'][item]['size']
            if save_hashes:
                print('\t' * 2 + f"Calculating hash for {dir_info['files'][item]['name']}")
                dir_info['files'][item]['hash'] = hash_file(item_path)
        else:
            dir_info['directories'][item] = get_dir_info(item_path, save_hashes)
            dir_info['size'] += dir_info['directories'][item]['size']
    return dir_info
