class Paint:
    """ base class for simple drawing tool """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[x for x in " " * self.width] for y in " " * self.height]

    def draw_me(self):
        """ draw borders of the field and figures"""
        pict = "-" * (self.width + 2) + "\n"
        for line in self.canvas:
            pict += "|" + "".join(line) + "|\n"
        pict += "-" * (self.width + 2)
        return pict

    def line(self, x1, y1, x2, y2):
        """draw vertical and horizontal lines"""
        inside1 = (0 < x1 <= self.width) and (0 < y1 <= self.height)
        inside2 = (0 < x2 <= self.width) and (0 < y2 <= self.height)
        if inside1 and inside2:
            if x1 == x2:
                for i in range(y1 - 1, y2):
                    self.canvas[i][x1 - 1] = "x"
            elif y1 == y2:
                for j in range(x1 - 1, x2):
                    self.canvas[y1 - 1][j] = "x"

    def rectangle(self, x1, y1, x2, y2):
        """draw rectangle"""
        inside1 = (0 < x1 <= self.width) and (0 < y1 <= self.height)
        inside2 = (0 < x2 <= self.width) and (0 < y2 <= self.height)
        if inside1 and inside2:
            self.line(x1, y1, x1, y2)
            self.line(x1, y1, x2, y1)
            self.line(x2, y1, x2, y2)
            self.line(x1, y2, x2, y2)

    def change_col(self, x, y, new_col, cur_col):
        # maybe i should do this reqursivly line by line

        inside = (0 < x <= self.width) and (0 < y <= self.height)

        if inside:
            if self.canvas[y - 1][x - 1] == cur_col:
                self.canvas[y - 1][x - 1] = new_col
                self.change_col(x, y + 1, new_col, cur_col)
                self.change_col(x + 1, y, new_col, cur_col)
                self.change_col(x, y - 1, new_col, cur_col)
                self.change_col(x - 1, y, new_col, cur_col)

    def bucket_fill(self, x, y, col):
        inside = (0 < x <= self.width) and (0 < y <= self.height)
        if inside:
            cur_col = self.canvas[y - 1][x - 1]
            if cur_col != col:
                self.change_col(x, y, col, cur_col)

