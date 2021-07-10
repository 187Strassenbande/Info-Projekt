from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.set_stroke(BLUE_E, width=4)

        self.play(ShowCreation(square))