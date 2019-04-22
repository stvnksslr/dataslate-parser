from PIL import Image, ImageDraw


def render_roster(roster):
    height = 600
    width = 600
    image = Image.new(mode='L', size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)

    x_start = 0
    y = 0
    x_end = image.width

    for item in roster:
        line = ((x_start, y), (x_end, y))
        y = y + 60
        draw.line(line, fill=128)
        draw.text(xy=(x_start, y), text=item.name)

    del draw

    # image.show()
