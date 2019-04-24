from PIL import Image, ImageFont, ImageDraw
from pathlib import Path

from app.models.killteam_unit import KillteamUnit


def render_roster(roster):
    height = 600
    width = 600
    image = Image.new(mode="L", size=(height, width), color=255)

    # Draw some lines
    draw = ImageDraw.Draw(image)

    font = Path.cwd() / "assets" / "kt_font.ttf"

    get_font = ImageFont.truetype(str(font), 16)

    x_start = 0
    y = 0
    x_end = image.width

    y_start = 0

    name_cord = 0
    movement_skill_cord = 200
    weapons_skill_cord = 250
    ballistic_skill_cord = 300
    strength_skill_cord = 350
    toughness_skill_cord = 400

    draw.text(xy=(name_cord, y_start), text="Name", font=get_font)
    draw.text(xy=(movement_skill_cord, y_start), text="M", font=get_font)
    draw.text(xy=(weapons_skill_cord, y_start), text="WS", font=get_font)
    draw.text(xy=(ballistic_skill_cord, y_start), text="BS", font=get_font)
    draw.text(xy=(strength_skill_cord, y_start), text="T", font=get_font)
    draw.text(xy=(toughness_skill_cord, y_start), text="S", font=get_font)

    item: KillteamUnit
    for item in roster:
        y = y + 20
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

        draw.text(xy=(x_start, y), text=item.name, font=get_font)
        draw.text(xy=(movement_skill_cord, y), text=item.movement, font=get_font)
        draw.text(xy=(weapons_skill_cord, y), text=item.weapon_skill, font=get_font)
        draw.text(
            xy=(ballistic_skill_cord, y), text=item.ballistic_skill, font=get_font
        )
        draw.text(xy=(toughness_skill_cord, y), text=item.toughness, font=get_font)
        draw.text(xy=(strength_skill_cord, y), text=item.strength, font=get_font)
        y = y + 60

    del draw

    # image.show()

    return image
