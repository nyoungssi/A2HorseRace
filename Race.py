from graphics import GraphWin, Line, Image, Point
from Dice import Dice

class Horse:
    def __init__(self, speed, y_pos, image, window):
        self.x_pos = 0
        self.dice = Dice(speed)
        self.y_pos = y_pos
        self.window = window
        self.image = Image(Point(self.x_pos+25, self.y_pos), image)
        self.image.draw(self.window)

    def move(self):
        roll = self.dice.roll()
        self.x_pos += roll
        self.image.move(roll, 0)

    def draw(self):
        self.image.draw(self.window)

    def crossed_finish_line(self, finish_line_x):
        return self.x_pos >= finish_line_x

def main():
    win = GraphWin("Horse Race", 700, 350)

    horse1_image = "Horse_1.gif"
    horse2_image = "Horse_2.gif"

    horse1 = Horse(4, 100, horse1_image, win)
    horse2 = Horse(4, 250, horse2_image, win)

    finish_line = Line(Point(650, 0), Point(650, 350))
    finish_line.setWidth(7)
    finish_line.draw(win)

    win.getMouse()

    race_over = False

    while not race_over:
        horse1.move()
        horse2.move()

        if horse1.crossed_finish_line(650) and horse2.crossed_finish_line(650):
            race_over = True
            print("Tie :(")
        elif horse1.crossed_finish_line(650):
            race_over = True
            print("Horse 1 is the winner!")
        elif horse2.crossed_finish_line(650):
            race_over = True
            print("Horse 2 is the winner!")

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()