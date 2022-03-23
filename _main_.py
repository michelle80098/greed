import os
import random

from game.casting.actor import Actor
from game.casting.gemstone import Gemstone
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_GEMSTONES = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the collector
    x = int(MAX_X / 2)
    y = int(MAX_Y - 50)
    position = Point(x, y)

    collector = Actor()
    collector.set_text("#")
    collector.set_font_size(FONT_SIZE)
    collector.set_color(WHITE)
    collector.set_position(position)
    cast.add_actor("collectors", collector)
    
    # create the gemstones
    for n in range(DEFAULT_GEMSTONES):
        symbol = ['o', '*']
        text = random.choice(symbol)
        if text == 'o':
            message = '-100'
        else:
            message = '100'


        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS -1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        gemstone = Gemstone()
        gemstone.set_text(text)
        gemstone.set_font_size(FONT_SIZE)
        gemstone.set_color(color)
        gemstone.set_position(position)
        gemstone.set_message(message)
        cast.add_actor("gemstones", gemstone)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()