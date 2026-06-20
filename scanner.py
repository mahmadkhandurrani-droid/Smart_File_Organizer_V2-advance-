import os

def scan_folder(folder_path):
    try:
        items = os.listdir(folder_path)

        files = []

        for item in items:
            full_path = os.path.join(folder_path, item)

            if os.path.isfile(full_path):
                files.append(item)

        return files

    except FileNotFoundError:
        return []

    except PermissionError:
        return []

