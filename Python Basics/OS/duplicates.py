def get_file_catalog(dir_info, file_catalog={}):
    for file_name, file_info in dir_info['files'].items():
        hash = file_info['hash']
        file_catalog[hash] = file_catalog.get(hash, {})
        file_catalog[hash]['count'] = file_catalog[hash].get('count', 0) + 1
        file_catalog[hash]['size'] = file_catalog[hash].get('size', file_info['size'])
        file_catalog[hash]['names'] = file_catalog[hash].get('names', []) + [file_name]

    for directory in dir_info['directories'].values():
        file_catalog = get_file_catalog(directory, file_catalog)

    return file_catalog


def get_duplicates(file_catalog):
    duplicates = []
    for hash, info in file_catalog.items():
        file_name = sorted(info['names'], key=lambda name: len(name))[0]
        file_count = info['count']
        file_size = info['size']
        if file_count > 1:
            duplicates.append((file_name, file_size, file_count))
    return duplicates
