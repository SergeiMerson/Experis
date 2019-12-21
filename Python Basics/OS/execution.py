import csv
import os
import duplicates, system_scan, tree


def scan(path):
    try:
        root_name = os.path.split(path)[1]
        root_info = system_scan.get_dir_info(path, save_hashes=True)
        print(f"Successfully scanned {path}")
        return root_name, root_info
    except IOError:
        print(f"Can't scan {path}")
    except NameError:
        print('scan requires argument "path"')
    except TypeError:
        print('Couldn\'t recognize provided path')


def dup(csv_file, dir_info):
    try:
        file_catalog = duplicates.get_file_catalog(dir_info)
        dup_list = duplicates.get_duplicates(file_catalog)
        with open(csv_file, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"')
            csv_writer.writerow(('file_name', 'file_size', 'number_of_duplicates'))
            for row in dup_list:
                csv_writer.writerow(row)
        print(f"Successfully exported to csv")
    except TypeError:
        print("Please scan some folder first")


def dirsize(root_info, root_name, depth=False):
    try:
        tree.print_tree(root_info, root_name, depth)
    except TypeError:
        print("Please scan some folder first")
