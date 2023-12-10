class Grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.size = 30
        self.grid=[[0 for j in range(self.cols)] for i in range(self.rows)]