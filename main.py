import os

from PIL import Image, ImageDraw, ImageFont

font_channel_path = 'fonts/text-font-3.ttf'


def coupons(names: list, certificate: str, channel_name: str, font_path: str):
    if not os.path.exists("certificates"):
        os.makedirs("certificates")
    for name in names:
        img = Image.open(certificate, mode='r')
        image_width = img.width
        image_height = img.height
        draw = ImageDraw.Draw(img)
        count_test = 10
        percentage = 80
        author_name = 'Malika Rustamova'
        channel_name = 1
        text = (
            f"{channel_name} - kodli testdan {count_test} ta savoldan {count_test} "
            f"tasiga to'g'ri javob berib,"
            f" {percentage}% natijani qayt etdingiz.\n",
            f"Shu sababli siz muallif {author_name} "
            f"tomonidan ushbu sertifikat bilan taqdirlandingiz.\n",
            f"Kelgusi testlarda omad tilaymiz!"
        )

        # user name
        name_size = 120
        font_name = ImageFont.truetype(font_path, name_size)
        text_bbox = draw.textbbox((0, 0), name, font=font_name)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
        text_x_position = (image_width - text_w) / 2
        text_y_position = (image_height - text_h) / 2 - 100
        draw.text((text_x_position, text_y_position), name, font=font_name, fill=(134, 91, 52))

        # channel name
        # TODO textbbox usage ... # noqa
        text_size = 35
        font_text = ImageFont.truetype(font_channel_path, text_size)
        total_text_height = sum(draw.textsize(line, font=font_text)[1] for line in text)
        y = (image_height - total_text_height) / 2 + 150
        for line in text:
            text_w, text_h = draw.textsize(line, font=font_text)
            x = (image_width - text_w) / 2
            draw.text((x, y), line, font=font_text, fill=(134, 91, 52))
            y += text_h - 10
        # author_size = 40
        # author_font_path = 'fonts/text-font-2.otf'
        # text_w, text_h = draw.textsize(name, )
        img.save(os.path.join("certificates", "{}.png".format(name)))


FONT = "fonts/font5.otf"
CERTIFICATE = "templates/template2.png"
NAMES = ['Hasanjon Mamadaliyev']
coupons(NAMES, CERTIFICATE, 'devmasters', FONT)
