from file_type_detection import get_file_type


def test_images():
    assert get_file_type("photo.jpg") == "Images"
    assert get_file_type("image.png") == "Images"


def test_documents():
    assert get_file_type("file.pdf") == "Documents"
    assert get_file_type("note.txt") == "Documents"


def test_videos():
    assert get_file_type("movie.mp4") == "Videos"


def test_unknown():
    assert get_file_type("archive.zip") == "Others"
