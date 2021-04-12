from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

BADGE_HEIGHT = 230
BADGE_WIDTH = 384


def create_badge(name: str, print_date: str, face_photo: bytes) -> bytes:
    print('->> Enter create_badge function...')
    font_header = ImageFont.truetype(".fonts/arial.ttf", 40)
    font_name = ImageFont.truetype(".fonts/arial.ttf", 35)
    font_date = ImageFont.truetype(".fonts/arial.ttf", 25)
    badge = Image.new('L', (BADGE_WIDTH, BADGE_HEIGHT), 'white')
    badge_canvas = ImageDraw.Draw(badge)
    badge_canvas.rectangle([(2, 2), (BADGE_WIDTH - 2, BADGE_HEIGHT - 2)], outline='gray', width=2)
    badge_canvas.rectangle([(5, 5), (BADGE_WIDTH - 5, int(BADGE_HEIGHT / 4))], fill='gray', width=2)
    badge_canvas.text((115, 7), 'VISITOR', fill='white', font=font_header, stroke_width=1)
    badge_canvas.text((120, 80), name, fill='black', font=font_header, stroke_width=1)
    badge_canvas.text((120, 130), f'Date: {print_date}', fill='black', font=font_date)
    print('->> Completed badge framing...')

    face_buffer = BytesIO(face_photo)
    with Image.open(face_buffer) as fil_face:
        face_height = int(BADGE_HEIGHT / 2)
        print('->> Started vistior photo paste...')
        if fil_face.height > face_height:
            face_width = int((face_height * fil_face.width) / fil_face.height)
            new_fil_face = fil_face.resize((face_width, face_height), Image.NEAREST)
            badge.paste(new_fil_face, (5, face_height - 5))
            print('->> Completed vistior photo paste...')

    badge_rotate = badge.rotate(90, expand=True)
    badge_dither = badge_rotate.convert(mode='1', dither=Image.FLOYDSTEINBERG)
    # badge_dither.show()
    badge_buffer = BytesIO()
    badge_dither.save(badge_buffer, 'PNG')
    return badge_buffer.getvalue()
