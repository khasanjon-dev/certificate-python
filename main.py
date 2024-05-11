import os

from PIL import Image, ImageDraw, ImageFont

font_channel_path = 'fonts/font-channel.ttf'


def coupons(names: list, certificate: str, channel_name: str, font_path: str):
    if not os.path.exists("certificates"):
        os.makedirs("certificates")
    for name in names:
        img = Image.open(certificate, mode='r')
        image_width = img.width
        image_height = img.height
        draw = ImageDraw.Draw(img)

        font_size_name = 120
        font_name = ImageFont.truetype(font_path, font_size_name)
        text_width, text_height = draw.textsize(name, font=font_name)
        text_x_position = (image_width - text_width) / 2
        text_y_position = (image_height - text_height) / 2 - 100
        draw.text((text_x_position, text_y_position), name, font=font_name, fill=(134, 91, 52))

        font_channel_size = 17.5
        font_channel = ImageFont.truetype(font_channel_path, )
        img.save(os.path.join("certificates", "{}.png".format(name)))


if __name__ == "__main__":
    # some example of names
    NAMES = ['Hasanjon Mamadaliyev']

    # path to font
    FONT = "/home/khasanjon/projects/learn/certificate-python/fonts/font5.otf"

    # path to sample certificate
    CERTIFICATE = "/home/khasanjon/projects/learn/certificate-python/template-2.png"

    coupons(NAMES, CERTIFICATE, 'devmasters', FONT)
