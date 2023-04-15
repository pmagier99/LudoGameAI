from Pawn import Pawn


class Player:
    active_pawns = 0
    home_pawns = 0
    pawns = []

    def __init__(self, colour):
        self.colour = colour
        self.pawns = [Pawn(self.colour, x) for x in range(0, 4)]

    # Function move pawn
    def move_piece(self, pawn, dice):
        if 37 < pawn.complete_path + dice < 42:

            if pawn.colour == "yellow":
                if self.check_if_occupied(pawn.position + 2 + dice):
                    pawn.position += 2 + dice
                else:
                    pawn.position = pawn.position
                    return
            elif pawn.colour == "blue":
                if self.check_if_occupied(pawn.complete_path + 2 + 4 + dice):
                    pawn.position = pawn.complete_path + 2 + 4 + dice
                else:
                    pawn.position = pawn.position
                    return
            elif pawn.colour == "red":
                if self.check_if_occupied(pawn.complete_path + 2 + 8 + dice):
                    pawn.position = pawn.complete_path + 2 + 8 + dice
                else:
                    pawn.position = pawn.position
                    return
            elif pawn.colour == "green":
                if self.check_if_occupied(pawn.complete_path + 2 + 12 + dice):
                    pawn.position = pawn.complete_path + 2 + 12 + dice
                else:
                    pawn.position = pawn.position
                    return

            pawn.active = False
            pawn.inHome = True

            self.active_pawns -= 1
            self.home_pawns += 1

        elif pawn.complete_path + dice < 37:
            pawn.position += dice
            pawn.complete_path += dice
            if pawn.position >= 40:
                pawn.position -= 40
        else:
            pawn.position = pawn.position

    # Function to move out pawn
    def pawn_out(self):
        for pawn in self.pawns:
            if not pawn.active and not pawn.inHome:
                pawn.active = True
                self.active_pawns += 1
                pawn.set_position(self.colour)
                break

    # Return active pawn
    def get_active_pawn(self):
        for pawn in self.pawns:
            if pawn.active:
                if not pawn.inHome:
                    return pawn

    def check_if_occupied(self, pos):
        for pawn in self.pawns:
            if pawn.position == pos:
                return False
        return True
