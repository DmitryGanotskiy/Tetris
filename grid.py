class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.size = 30
        self.grid=[[0 for j in range(self.cols)] for i in range(self.rows)]

    def PrintGrid(self):
        for row in range(self.rows):
            for column in range(self.cols):
                print(self.grif[row][column], end=" ")
            print()