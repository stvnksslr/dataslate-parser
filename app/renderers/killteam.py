from PIL import Image, ImageDraw


def render_roster(roster):
    height = 600
    width = 600
    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)

    x_start = 0
    y = 0
    x = 0
    x_end = image.width

    y_start = 0
    y_end = image.height

    weapons_skill_cord = 160

    list_of_field_names = ['name', 'ws']

    for field_name in list_of_field_names:
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)
        draw.text(xy=(x, y_start), text=field_name)
        x = x + 60

    for item in roster:
        y = y + 20
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)
        draw.text(xy=(x_start, y), text=item.name)
        draw.text(xy=(weapons_skill_cord, y), text=item.weapon_skill)
        y = y + 60

    del draw

    image.show()
