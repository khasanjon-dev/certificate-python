import os

from PIL import Image, ImageDraw, ImageFont


def coupons(names: list, certificate: str, font_path: str):
    if not os.path.exists("certificates"):
        os.makedirs("certificates")
    for name in names:
        img = Image.open(certificate, mode='r')
        image_width = img.width
        image_height = img.height
        draw = ImageDraw.Draw(img)
        font_size = 140
        font = ImageFont.truetype(font_path, font_size)

        text_width, text_height = draw.textsize(name, font=font)
        text_x_position = (image_width - text_width) / 2
        text_y_position = (image_height - text_height) / 2 - 90
        draw.text((text_x_position, text_y_position), name, font=font, fill=(134, 91, 52))

        img.save(os.path.join("certificates", "{}.png".format(name)))


if __name__ == "__main__":
    # some example of names
    NAMES = ['Hasanjon Mamadaliyev']

    # path to font
    FONT = "/home/khasanjon/projects/learn/certificate-python/font-1.ttf"

    # path to sample certificate
    CERTIFICATE = "/home/khasanjon/projects/learn/certificate-python/template.png"

    coupons(NAMES, CERTIFICATE, FONT)
