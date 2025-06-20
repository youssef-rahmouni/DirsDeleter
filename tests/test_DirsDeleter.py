import os
import shutil
import unittest
from DirsDeleter import DirsDeleter

class TestDirsDeleter(unittest.TestCase):
    def test_delete_folder(self):
        os.makedirs("testdir/subdir", exist_ok=True)
        with open("testdir/file.txt", "w") as f:
            f.write("hello")
        with open("testdir/subdir/file2.txt", "w") as f:
            f.write("world")

        DirsDeleter("testdir")

        self.assertFalse(os.path.exists("testdir"))

if __name__ == "__main__":
    unittest.main()
