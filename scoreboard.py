from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        file = open("data.txt")
        self.highest_score = file.read()
        file.close()
        self.hideturtle()
        self.goto(0, 270)
        self.pencolor("white")
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", False, "center", ('Arial', 12, 'normal'))

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", False, "center", ('Arial', 12, 'normal'))

    def reset(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            file = open("data.txt", "w")
            file.write(str(self.highest_score))
            file.close()
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", False, "center", ('Arial', 12, 'normal'))

    # def gameoff(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, "center", ('Arial', 12, 'normal'))
