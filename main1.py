import os

from PIL import Image, ImageDraw, ImageFont

font_channel_path = 'fonts/text-font-3.ttf'


def fit_text_to_width(draw, text, font, max_width):
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    if text_width <= max_width:
        return font
    font_size = font.size
    while text_width > max_width and font_size > 10:
        font_size -= 1
        font = ImageFont.truetype(font.path, font_size)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
    return font


def wrap_text_to_width(draw, text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        text_bbox = draw.textbbox((0, 0), test_line, font=font)
        text_width = text_bbox[2] - text_bbox[0] + 400

        if text_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    lines.append(current_line.strip())
    return lines


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
        channel_name = 'devmasters'
        text = (
            f"Siz {channel_name.upper()} - jamoasi tomonidan o'tqazilgan testda {count_test} ta savoldan {count_test} "
            f"tasiga to'g'ri javob berib,"
            f" {percentage}% natijani qayt etdingiz.",
            f"Shu sababli siz muallif {author_name} "
            f"tomonidan ushbu sertifikat bilan taqdirlandingiz.",
            f"Kelgusi testlarda omad tilaymiz!"
        )

        # writing name
        name_size = 120
        font_name = ImageFont.truetype(font_path, name_size)
        font_name = fit_text_to_width(draw, name, font_name, image_width - 40)
        text_bbox = draw.textbbox((0, 0), name, font=font_name)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
        text_x_position = (image_width - text_w) / 2
        text_y_position = (image_height - text_h) / 2 - 100
        draw.text((text_x_position, text_y_position), name, font=font_name, fill=(134, 91, 52))

        # writing text
        text_size = 35
        font_text = ImageFont.truetype(font_channel_path, text_size)
        wrapped_text = []
        for line in text:
            wrapped_lines = wrap_text_to_width(draw, line, font_text, image_width - 40)
            wrapped_text.extend(wrapped_lines)
        total_text_height = sum(
            draw.textbbox((0, 0), line, font=font_text)[3] - draw.textbbox((0, 0), line, font=font_text)[1] for line in
            wrapped_text)
        y = (image_height - total_text_height) / 2 + 80
        for line in wrapped_text:
            font_text = fit_text_to_width(draw, line, font_text, image_width - 40)
            bbox = draw.textbbox((0, 0), line, font=font_text)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
            x = (image_width - text_w) / 2
            draw.text((x, y), line, font=font_text, fill=(134, 91, 52))
            y += text_h + 20

        # writing author name
        author_name_size = 40
        author_font_path = 'fonts/text-font-2.otf'
        author_name = 'Malika Rustamova'
        font_author = ImageFont.truetype(author_font_path, author_name_size)
        author_bbox = draw.textbbox((0, 0), author_name, font=font_author)
        text_w = author_bbox[2] - author_bbox[0]
        text_h = author_bbox[3] - author_bbox[1]
        text_x_position = (image_width - text_w) / 2 - 385
        text_y_position = (image_height - text_h) / 2 + 365
        draw.text((text_x_position, text_y_position), author_name, font=font_author, fill=(134, 91, 52))

        # writing rank
        rank_size = 30
        rank_font_path = 'fonts/text-font-2.otf'
        rank_number = 120
        rank_text = 'Reyting: TOP #' + str(rank_number)
        rank_font = ImageFont.truetype(rank_font_path, rank_size)
        rank_bbox = draw.textbbox((0, 0), rank_text, font=rank_font)
        text_w = rank_bbox[2] - rank_bbox[0]
        text_h = rank_bbox[3] - rank_bbox[1]
        text_x_position = (image_width - text_w) / 2
        text_y_position = (image_height - text_h) / 2 + 527
        draw.text((text_x_position, text_y_position), rank_text, font=rank_font, fill=(134, 91, 52))

        img.save(os.path.join("certificates", "{}.png".format(name)))


FONT = "fonts/font5.otf"
CERTIFICATE = "templates/template2.png"
NAMES = ['Hasanjon Mamadaliyev']
coupons(NAMES, CERTIFICATE, 'devmasters', FONT)
