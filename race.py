# Comp 1020 A2 Horse Race
# By Nayoung Lim u1542543

from graphics import *
from Dice import Dice

class Horse: #class of Horses

    def __init__(self, speed, y_pos, image_file, window):
        self.speed = speed
        self.dice = Dice(speed) #creat a dice object with given speed
        self.x_position = 0
        self.y_position = y_pos
        self.window = window
        self.image = Image(Point(self.x_position, self.y_position), image_file) # Create horse image
        self.image.draw(self.window)  # Draw horse in window


    def move(self):
        if not self.crossed_finish_line(650):
            roll = self.dice.roll()
            self.x_position += roll # Update x position
            self.image.move(roll, 0) # Move the image in the window

    def draw(self):
        self.image.draw(self.window)

    def crossed_finish_line(self, finish_line_x):
        return self.x_position >= finish_line_x # Check if the horse has crossed the finish line.

def main():
    # Creating window
    win = GraphWin("Horse Race", 700, 350, autoflush=False)
    win.setBackground('purple')

    # Set horse1,2
    horse1 = Horse(6, 100, "Horse_1.gif", win)
    horse2 = Horse(6, 150, "Horse_2.gif", win)

    # Draw finish line
    finish_line = Line(Point(650, 0), Point(650, 350))
    finish_line.draw(win)

    win.getMouse() #click for start teh race

    race_over = False


    while not race_over:

        horse1.move()

        horse2.move()

        update(10)  # Refresh screen so movement is visible

        if horse1.crossed_finish_line(650) and horse2.crossed_finish_line(650):
                race_over = True
                print("Tie")

        elif horse1.crossed_finish_line(650):
                race_over = True
                print("!!!Horse 1 is the winner!!!")

        elif horse2.crossed_finish_line(650):
                race_over = True
                print("!!!Horse 2 is the winner!!!")

    win.getMouse() #click for closing
    win.close()

if __name__ == "__main__":
    main()