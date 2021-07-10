from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE, opacity=0.1)
        square.set_stroke(BLUE_E, width=3)

        self.play(ShowCreation(square))