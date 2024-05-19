import os

from PIL import Image, ImageDraw, ImageFont


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


def generate_certificate(data: dict) -> None:
    names = data['names']
    channel_name = data['channel_name']
    author_name = data['author_name']
    bot_username = data['bot_username']
    rank_number = data['rank_number']
    length_test = data['length_test']
    solved_test_length = data['solved_test_length']
    percentage_test = round(solved_test_length / length_test * 100, 2)
    # fonts
    text_font_path = 'fonts/text-font-3.ttf'
    author_font_path = 'fonts/text-font-2.otf'
    name_font_path = 'fonts/font5.otf'
    bot_font_path = 'fonts/text-font-2.otf'
    rank_font_path = 'fonts/text-font-2.otf'
    # template
    template = 'templates/template.png'

    if not os.path.exists("certificates"):
        os.makedirs("certificates")

    for name in names:
        img = Image.open(template, mode='r')
        image_width = img.width
        image_height = img.height
        draw = ImageDraw.Draw(img)

        text = (
            f"Siz {channel_name.upper()} - jamoasi tomonidan o'tqazilgan testda {length_test} ta savoldan {solved_test_length} "
            f"tasiga to'g'ri javob berib,"
            f" {percentage_test}% natijani qayt etdingiz.",
            f"Shu sababli siz muallif {author_name} "
            f"tomonidan ushbu sertifikat bilan taqdirlandingiz.",
            f"Kelgusi testlarda omad tilaymiz!"
        )

        # writing name
        name_size = 120
        name_font = ImageFont.truetype(name_font_path, name_size)
        name_font = fit_text_to_width(draw, name, name_font, image_width - 40)
        name_bbox = draw.textbbox((0, 0), name, font=name_font)
        text_w = name_bbox[2] - name_bbox[0]
        text_h = name_bbox[3] - name_bbox[1]
        text_x_position = (image_width - text_w) / 2
        text_y_position = (image_height - text_h) / 2 - 100
        draw.text((text_x_position, text_y_position), name, font=name_font, fill=(134, 91, 52))

        # writing text
        text_size = 35
        text_font = ImageFont.truetype(text_font_path, text_size)
        wrapped_text = []
        for line in text:
            wrapped_lines = wrap_text_to_width(draw, line, text_font, image_width - 40)
            wrapped_text.extend(wrapped_lines)
        total_text_height = sum(
            draw.textbbox((0, 0), line, font=text_font)[3] - draw.textbbox((0, 0), line, font=text_font)[1] for line in
            wrapped_text)
        y = (image_height - total_text_height) / 2 + 80
        for line in wrapped_text:
            font_text = fit_text_to_width(draw, line, text_font, image_width - 40)
            bbox = draw.textbbox((0, 0), line, font=font_text)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
            x = (image_width - text_w) / 2
            draw.text((x, y), line, font=font_text, fill=(134, 91, 52))
            y += text_h + 20

        # writing author name
        author_name_size = 40
        font_author = ImageFont.truetype(author_font_path, author_name_size)
        author_bbox = draw.textbbox((0, 0), author_name, font=font_author)
        text_w = author_bbox[2] - author_bbox[0]
        text_h = author_bbox[3] - author_bbox[1]
        text_x_position = (image_width - text_w) / 2 - 385
        text_y_position = (image_height - text_h) / 2 + 365
        draw.text((text_x_position, text_y_position), author_name, font=font_author, fill=(134, 91, 52))

        # writing bot name
        bot_size = 40
        bot_font = ImageFont.truetype(bot_font_path, bot_size)
        bot_bbox = draw.textbbox((0, 0), bot_username, font=bot_font)
        text_w = bot_bbox[2] - bot_bbox[0]
        text_h = bot_bbox[3] - bot_bbox[1]
        text_x_position = (image_width - text_w) / 2 + 395
        text_y_position = (image_height - text_h) / 2 + 365
        draw.text((text_x_position, text_y_position), bot_username, font=bot_font, fill=(134, 91, 52))

        # writing rank
        rank_size = 35
        rank_text = 'Reyting: TOP #' + str(rank_number)
        rank_font = ImageFont.truetype(rank_font_path, rank_size)
        rank_bbox = draw.textbbox((0, 0), rank_text, font=rank_font)
        text_w = rank_bbox[2] - rank_bbox[0]
        text_h = rank_bbox[3] - rank_bbox[1]
        text_x_position = (image_width - text_w) / 2
        text_y_position = (image_height - text_h) / 2 + 515
        draw.text((text_x_position, text_y_position), rank_text, font=rank_font, fill=(134, 91, 52))

        img.save(os.path.join("certificates", "{}.png".format(name)))


NAMES = ['Hasanjon Mamadaliyev']
data = {
    'names': NAMES,
    'channel_name': 'matematika',
    'author_name': 'Malika Rustamova',
    'bot_username': 'exam_e_bot',
    'rank_number': 1400,
    'length_test': 90,
    'solved_test_length': 75,
}
generate_certificate(data)
