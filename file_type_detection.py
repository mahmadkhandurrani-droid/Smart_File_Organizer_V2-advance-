import os

def get_file_type(filename):

    ext = os.path.splitext(filename)[1].lower()

    if ext in [".jpg", ".jpeg", ".png"]:
        return "Images"

    elif ext in [".pdf", ".txt"]:
        return "Documents"

    elif ext in [".mp4", ".mkv"]:
        return "Videos"

    else:
        return "Oth
