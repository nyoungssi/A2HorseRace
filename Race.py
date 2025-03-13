# Comp 1020 A2 Horse Race
# By Nayoung Lim u1542543


from graphics import GraphWin, Line, Image, Point, update
from Dice import Dice

class Horse:
    def __init__(self, speed, y_pos, image, window):
        self.x_pos = 0
        self.dice = Dice(speed)
        self.y_pos = y_pos
        self.image = Image(Point(self.x_pos+25, self.y_pos), image)
        self.window = window
        self.image.draw(self.window)

    def move(self):
        roll = self.dice.roll()
        self.x_pos += roll
        self.image.move(roll, 0)

    def draw(self):
        self.image.draw(self.window)

    def crossed_finish_line(self, finish_line_x):
        return self.x_pos >= finish_line_x #check when the horses cross the end line

def main():
    win = GraphWin("Horse Racefield", 700, 350,autoflush=False) # make window
    win.setBackground('purple')

#set horses!
    horse_1_image = "Horse_1.gif"
    horse_2_image = "Horse_2.gif"

    horse1 = Horse(4, 100, horse_1_image, win)
    horse2 = Horse(4, 250, horse_2_image, win)

#draw end line
    finish_line = Line(Point(650, 0), Point(650, 350))
    finish_line.draw(win)

    win.getMouse() #start race when the user click the win

    race_over = False

    while not race_over:
        horse1.move()
        horse2.move()

        update(10) #make animation smoother

        #main race & result
        if horse1.crossed_finish_line(650) and horse2.crossed_finish_line(650):
            race_over = True
            print("Tie")

        elif horse1.crossed_finish_line(650):
            race_over = True
            print("!!!Horse 1 is the winner!!!")

        elif horse2.crossed_finish_line(650):
            race_over = True
            print("!!!Horse 2 is the winner!!!")

    win.getMouse() #wait for users click to close the program
    win.close()

if __name__ == "__main__":
    main()