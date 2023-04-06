import zipfile
from io import BytesIO


async def check_if_zipped(file):
    if file.filename.endswith("rosz"):
        file_contents = await file.read()

        with zipfile.ZipFile(BytesIO(file_contents)) as unzipped_contents:
            upload_contents = unzipped_contents.read(unzipped_contents.infolist()[0])
    else:
        upload_contents = await file.read()
    return upload_contents
