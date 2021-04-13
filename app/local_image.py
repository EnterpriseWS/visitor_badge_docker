from PIL import Image
from datetime import datetime
import sys
import base64
from io import BytesIO
import platform
import urllib.parse

IMG_FOLDER = ''
if platform.system() == 'Linux':
    IMG_FOLDER = 'images/'
elif platform.system() == 'Windows':
    IMG_FOLDER = '.\\images\\'


def get_base64_image(filename: str = '.\\images\\face_dither.png') -> str:
    try:
        encoded_image = b''
        image_format = ''
        with Image.open(filename) as image:
            image_format = image.format
            # print(f'Format is: {image_format}')
            # print(f'Mode is: {image.mode}')
            buffer = BytesIO()
            image.save(buffer, image.format)
            image_bytes = buffer.getvalue()
            encoded_image = base64.b64encode(image_bytes)
        # ****** Below is simply for testing if the image ******
        #        data stored in the file is correct or not.
        # ------------------------------------------------------
        # image_buffer = BytesIO(base64.b64decode(encoded_image))
        # with Image.open(image_buffer) as fil_image:
        #     new_filename = 'Robert' + datetime.now().strftime('_%Y%m%d_%H%M%S') \
        #                    + '.' + image_format.lower()
        #     fil_image.save(IMG_FOLDER + new_filename, image_format)
        # ------------------------------------------------------
        print(f'The Base64 image = {urllib.parse.quote(encoded_image.decode())}')
        return encoded_image.decode()
    except Exception as ex:
        print(f'No image found: {ex}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # print(f'The param = {sys.argv[1]}')
        get_base64_image(sys.argv[1])
    else:
        get_base64_image()
