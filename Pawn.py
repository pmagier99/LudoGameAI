class Pawn:
    position = 0
    complete_path = 0
    active = False
    inHome = False
    home_coordinates_x = []
    home_coordinates_y = []

    def __init__(self, colour, no):
        self.set_base_pos(no, colour)
        self.colour = colour
        self.no = no

    def reset_pawn(self):
        self.set_base_pos(self.no, self.colour)
        self.complete_path = 0
        self.active = False



    def move(self, place):
        self.set_position(self.colour)
        self.position += place

    def is_active(self):
        if self.active:
            return True

        return False

    def set_position(self, colour):
        if colour == "yellow":
            self.position = 0
        elif colour == "blue":
            self.position = 10
        elif colour == "red":
            self.position = 20
        else:
            self.position = 30

    def set_base_pos(self, no, colour):
        if colour == "yellow":
            if no == 0:
                self.position = 56
            elif no == 1:
                self.position = 57
            elif no == 2:
                self.position = 58
            elif no == 3:
                self.position = 59
        if colour == "red":
            if no == 0:
                self.position = 60
            elif no == 1:
                self.position = 61
            elif no == 2:
                self.position = 62
            elif no == 3:
                self.position = 63
        if colour == "blue":
            if no == 0:
                self.position = 64
            elif no == 1:
                self.position = 65
            elif no == 2:
                self.position = 66
            elif no == 3:
                self.position = 67
        if colour == "green":
            if no == 0:
                self.position = 68
            elif no == 1:
                self.position = 69
            elif no == 2:
                self.position = 70
            elif no == 3:
                self.position = 71
