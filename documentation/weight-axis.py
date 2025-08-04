# RENDER THIS DOCUMENT WITH DRAWBOT: https://www.drawbot.com
# $ pip install git+https://github.com/typemytype/drawbot
# $ gifsicle -i animated-vf-specimen-001.gif -O3 --colors 32 -o anim-001.gif

# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/image0.py --output documentation/image0.png

from drawBot import *
import math

# CONSTANTS
W = 1024  # Width
H = 256  # Height
M = 64  # Margin
U = 32  # Unit (Grid Unit)
F = 64  # Frames (Animation)

# REMAP INPUT RANGE TO VARIABLE FONT AXIS RANGE
# (E.G. SINE WAVE(-1,1) to WGHT(100,900))
def remap(value, input_min, input_max, output_min, output_max):
    input_span = input_max - input_min  # FIND INPUT RANGE SPAN
    output_span = output_max - output_min  # FIND OUTPUT RANGE SPAN
    value_scaled = float(value - input_min) / float(input_span)
    return output_min + (value_scaled * output_span)


# NEW PAGE
def new_page():
    newPage(W, H)
    frameDuration(1 / 24)
    fill(0)
    rect(-2, -2, W + 2, H + 2)


# START DRAWBOT
newDrawing()

# SET ANIMATION VARIABLES
varWght = 0
varWdth = 0
step = -1


# MAIN
for frame in range(F - 1):
    new_page()
    font("fonts/variable/Alyamama[wght].ttf")
    fontSize(U * 3.5)
    stroke(None)
    fill(1)
    varWght = remap(sin(step), -1, 1, 300, 900)
    fontVariations(wght=varWght)
    text("حجر اليمامة", ( M+(-10), U * 2.25 ))
    step += 0.1
    # AUXILIARY TEXT INFO
    font("Helvetica")
    stroke(None)
    fontSize(U / 1.5)
    text("Alyamama Variable Font: Weight Axis Range (300 - 900) wght = ", (M, U * 6.25))
    text(str(int(varWght)), (M * 10.6, U * 6.25))
    stroke(1)
    strokeWidth(2)
    line((M, H - M - 10), (W - M, H - M - 10))

# SAVE THE ANIMATION IN THIS SCRIPT'S DIRECTORY
saveImage("documentation/weight-axis.gif")
print("DrawBot: Done")
# END DRAWBOT
endDrawing()