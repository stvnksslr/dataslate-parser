from dataclasses import dataclass

from fastapi import UploadFile
from fastapi.params import File


@dataclass
class FileUpload:
    file: UploadFile = File(...)
