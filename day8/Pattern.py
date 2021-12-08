class Pattern:
    def __init__(self, horizontal_upper, horizontal_middle, horizontal_lower, vertical_left_upper, vertical_right_upper,
                 vertical_left_lower, vertical_right_lower):
        self.nodes = []
        self.horizontal_upper = horizontal_upper, "horizontal_upper"
        self.horizontal_middle = horizontal_middle, "horizontal_middle"
        self.horizontal_lower = horizontal_lower, "horizontal_lower"
        self.vertical_left_upper = vertical_left_upper, "vertical_left_upper"
        self.vertical_right_upper = vertical_right_upper, "vertical_right_upper"
        self.vertical_left_lower = vertical_left_lower, "vertical_left_lower"
        self.vertical_right_lower = vertical_right_lower, "vertical_right_lower"
        self.nodes = self.nodes + [self.horizontal_upper,self.horizontal_middle,self.horizontal_lower,self.vertical_left_upper,self.vertical_right_upper,self.vertical_left_lower,self.vertical_right_lower]

    def getPositionOfLetter(self, letter):
        for n in self.nodes:
            if n[0] == letter: return n[1]
