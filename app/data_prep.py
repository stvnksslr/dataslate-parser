import zipfile


def unzip_roser(self):
    with zipfile.ZipFile("file.zip","r") as zip_ref:
        zip_ref.read("targetdir")