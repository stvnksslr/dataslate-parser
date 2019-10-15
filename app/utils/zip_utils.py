import zlib


def unzip(zipped_string):
    unzipped_string = zlib.decompress(zipped_string).decode("utf8")
    return unzipped_string
