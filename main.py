import random
import pygame
from Player import Player
from Pawn import Pawn
from Board import Board
from pygame.locals import *


class Game:
    number_of_players = 4
    game_on = True
    FPS = 30
    players = []
    current_player = 0

    def __init__(self):
        pygame.init()
        pygame.font.init()

        colours = ["yellow", "blue", "red", "green"]
        self.players = [Player(colours[x]) for x in range(0, self.number_of_players)]
        self.board = Board(self.players[0].pawns, self.players[1].pawns, self.players[2].pawns, self.players[3].pawns, )

    def play(self):

        player = self.next_player()
        dice = self.roll_dice()
        if dice == 6 and player.active_pawns == 0:
            player.pawn_out()

        elif player.active_pawns > 0:
            # Decide between moving out new pawn and moving active pawn
            pawn = player.get_active_pawn()
            player.move_piece(pawn, dice)
            self.check_for_collision(pawn)

        self.is_playing()

        self.current_player = (self.current_player + 1) % 4
        self.next_player()
        self.board.draw_pawns(dice)

    def next_player(self):
        return self.players[self.current_player]

    def is_playing(self):
        for player in self.players:
            if player.home_pawns == 4:
                self.game_on = False
                print(player.colour, " has won!")
                return self.game_on
            else:
                return self.game_on

    def roll_dice(self):
        dice_res = random.randint(1, 6)
        pygame.display.update()
        return dice_res

    def check_for_collision(self, player_pawn):
        for player in self.players:
            for pawn in player.pawns:
                if pawn.position == player_pawn.position and pawn.colour != player_pawn.colour:
                    player.active_pawns -= 1
                    pawn.reset_pawn()
                    return True

        return False


def main():
    game = Game()
    clock = pygame.time.Clock()
    while game.game_on:
        clock.tick(game.FPS)
        game.play()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game.game_on = False
                if event.key == K_SPACE:
                    game.play()
            elif event.type == pygame.QUIT:
                game.game_on = False
    pygame.quit()


if __name__ == "__main__":
    main()
