# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/image0.py --output documentation/image0.png

# Import moduels from external python packages: https://pypi.org/
from drawbot_skia.drawbot import *
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

# Import moduels from the Python Standard Library: https://docs.python.org/3/library/
import subprocess
import sys
import argparse

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 2048, 320, 64, 1
FONT_PATH = "fonts/ttf/Alyamama-Black.ttf"

BIG_TEXT = "اليمامة"
BIG_TEXT_FONT_SIZE = 200
BIG_TEXT_SIDE_MARGIN = WIDTH - MARGIN * 1
BIG_TEXT_BOTTOM_MARGIN = MARGIN * 1.7


# Handel the "--output" flag
# For example: $ python3 documentation/image0.py --output documentation/image0.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Load the font with the parts of fonttools that are imported with the line:
# from fontTools.ttLib import TTFont
# Docs Link: https://fonttools.readthedocs.io/en/latest/ttLib/ttFont.html
ttFont = TTFont(FONT_PATH)

# Constants that are worked out dynamically
MY_URL = subprocess.check_output("git remote get-url origin", shell=True).decode()
MY_HASH = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode()
FONT_NAME = ttFont["name"].getDebugName(4)
FONT_VERSION = "v%s" % floatToFixedToStr(ttFont["head"].fontRevision, 16)

# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)


# Draw main text
def draw_main_text():
    fill(1)
    stroke(None)
    font(FONT_PATH)
    fontSize(BIG_TEXT_FONT_SIZE)
    # Adjust this line to center main text manually.
    # TODO: This should be done automatically when drawbot-skia
    # has support for textBox() and FormattedString
    #text(BIG_TEXT, ((WIDTH / 2) - MARGIN * 4.75, (HEIGHT / 2) - MARGIN * 2.5))
    #text(BIG_TEXT, (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN))
    text("Alyamama", (MARGIN, BIG_TEXT_BOTTOM_MARGIN), align="left")
    text("اليمامـــة", (BIG_TEXT_SIDE_MARGIN, BIG_TEXT_BOTTOM_MARGIN), align="right")



# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    # Print done in the terminal
    print("DrawBot: Done")
