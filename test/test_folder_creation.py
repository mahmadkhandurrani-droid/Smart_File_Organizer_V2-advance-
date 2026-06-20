from folder_creation import ensure_folder_exists
import os

def test_folder_creation(tmp_path):

    new_folder = tmp_path / "Images"

    ensure_folder_exists(str(new_folder))

    assert os.path.exists(new_folder)
