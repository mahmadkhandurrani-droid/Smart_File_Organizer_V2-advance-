from renamer import get_unique_name

def test_unique_name(tmp_path):

    folder = tmp_path

    result = get_unique_name(folder, "file.txt")

    assert result == "file.txt"
