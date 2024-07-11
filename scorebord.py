from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 18, "normal")
GAMEOVERTEXT="     GAME OVER \n Your Final score : "

class ScoreBord(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"score:{self.score}", move=False, align=ALIGNMENT, font=FONT)




    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def walltouch(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"{GAMEOVERTEXT} {self.score}", move=False,align=ALIGNMENT,font=FONT)

