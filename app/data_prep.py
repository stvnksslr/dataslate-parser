import zipfile


def unzip_roster(self):
    with zipfile.ZipFile("file.zip", "r") as zip_ref:
        zip_ref.read("targetdir")
