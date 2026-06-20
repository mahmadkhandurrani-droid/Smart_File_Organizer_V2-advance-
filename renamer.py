import os


def get_unique_name(folder, filename):

    base, ext = os.path.splitext(filename)

    i = 1
    new_name = filename

    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{base}({i}){ext}"
        i += 1

    return new_name


def rename_file(folder, old_name):

    try:
        old_path = os.path.join(folder, old_name)

        if not os.path.exists(old_path):
            print(f"[ERROR] File not found: {old_name}")
            return

        new_name = get_unique_name(folder, old_name)
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)

        print(f"[OK] Renamed: {old_name} → {new_name}")

    except PermissionError:
        print("[ERROR] Permission denied")

    except OSError as e:
        print(f"[ERROR] OS error: {e}")

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
