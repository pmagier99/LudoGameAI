import random
import numpy as np
import pygame
from Player import Player
from Board import Board

class Game:
    number_of_players = 4
    game_on = True
    players = []
    current_player = 0
    dice_res = 0
    colours = ["yellow", "blue", "red", "green"]
    pygame.init()
    pygame.font.init()
    FPS = 30

    def __init__(self):
        # Statistics
        self.bad_dec = 0
        self.good_dec = 0
        self.new_pawn = 0
        self.striking_pawn = 0
        self.thrown_6 = 0
        self.moves = 0

        self.score = 0
        self.board = None
        self.reset()

    def reset(self):

        self.players = [Player(self.colours[x]) for x in range(0, self.number_of_players)]
        self.board = Board(self.get_player("yellow").pawns, self.get_player("blue").pawns, self.get_player("red").pawns,
                           self.get_player("green").pawns)
        self.score = 0

        # Statistics
        self.thrown_6 = 0
        self.striking_pawn = 0
        self.new_pawn = 0
        self.moves = 0
        self.good_dec = 0
        self.bad_dec = 0

    def play(self, action, dice, idx):

        clock = pygame.time.Clock()
        for event in pygame.event.get():
            clock.tick(self.FPS)
            if event.type == pygame.QUIT:
                self.game_on = False
                pygame.quit()
                quit()

        player = self.players[idx]
        reward = 0

        if dice == 6:
            self.thrown_6 += 1

        # If player adds the pawn because this is only what he can do
        if dice == 6 and player.active_pawns == 0:
            if np.array_equal(action, [1, 0, 0]):
                player.pawn_out()
                self.new_pawn += 1
                self.good_dec += 1
                reward = 5
            else:
                player.pawn_out()
                self.new_pawn += 1
                self.bad_dec += 1
                reward = -10

        elif dice != 6 and player.active_pawns == 0:
            if np.array_equal(action, [1, 0, 0]):
                reward = 1
                self.good_dec += 1
            else:
                reward = -10
                self.bad_dec += 1

        elif player.active_pawns > 0 and dice == 6:
            # player adds the pawn because this is one of his options
            if np.array_equal(action, [1, 0, 0]):
                player.pawn_out()
                self.new_pawn += 1
                self.good_dec += 1
                reward = 5

            # player moves the pawn but no strike
            elif np.array_equal(action, [0, 1, 0]):
                pawn = self.get_random_pawn(player)

                if self.check_for_collision(pawn):
                    reward = -10
                    self.striking_pawn += 1
                    self.bad_dec += 1
                else:
                    self.moves += 1
                    self.good_dec += 1
                    reward = 1

            # player moves the pawn to strike
            elif np.array_equal(action, [0, 0, 1]):
                cond, pawn = self.check_strike(player)
                if cond:
                    reward = 10
                    self.check_for_collision(pawn)
                    self.striking_pawn += 1
                    self.good_dec += 1
                else:
                    player.move_piece(pawn, dice)
                    self.moves += 1
                    self.bad_dec += 1
                    reward = -10

            # for wrong generated action
            else:
                player.pawn_out()
                self.new_pawn += 1
                self.bad_dec += 1
                reward = -10

        else:
            # player moves the pawn but no strike
            if np.array_equal(action, [0, 1, 0]):
                pawn = player.get_active_pawn()
                player.move_piece(pawn, dice)
                if self.check_for_collision(pawn):
                    self.striking_pawn += 1
                    reward = -10
                    self.bad_dec += 1
                else:
                    self.moves += 1
                    reward = 1
                    self.good_dec += 1

            # player moves the pawn to strike
            elif np.array_equal(action, [0, 0, 1]):
                cond, pawn = self.check_strike(player)
                if cond:
                    reward = 10
                    self.check_for_collision(pawn)
                    self.striking_pawn += 1
                    self.good_dec += 1
                else:
                    self.moves += 1
                    player.move_piece(self.get_random_pawn(player), dice)
                    reward = -10
                    self.bad_dec += 1
            # for wrong generated action
            else:
                pawn = self.get_random_pawn(player)
                player.move_piece(pawn, dice)
                self.moves += 1
                self.bad_dec += 1
                reward = -10

        statistics = [self.thrown_6, self.striking_pawn, self.moves, self.new_pawn, self.good_dec, self.bad_dec]

        # Check if game is finished

        # If player lose the game
        if self.is_playing() == False and player.home_pawns != 4:
            reward = -10
            self.score = -1
            return reward, not self.game_on, self.score, statistics

        # If player wins the game
        if self.is_playing() == False and player.home_pawns == 4:
            reward = 10
            self.score += 1
            return reward, not self.game_on, self.score, statistics

        self.next_player()
        self.board.draw_pawns(dice)

        return reward, not self.game_on, self.score, statistics

    def next_player(self):
        return self.players[self.current_player]

    def is_playing(self):
        if self.players[0].home_pawns == 4:
            self.game_on = False
            print("Yellow won!")
        elif self.players[1].home_pawns == 4:
            self.game_on = False
            print("Blue won!")
        elif self.players[2].home_pawns == 4:
            self.game_on = False
            print("Red won!")
        elif self.players[3].home_pawns == 4:
            self.game_on = False
            print("Green won!")
        else:
            self.game_on = True

        return self.game_on

    def roll_dice(self):
        dice = random.randint(1, 6)
        self.dice_res = dice
        pygame.display.update()
        return dice

    def check_for_collision(self, player_pawn):
        for player in self.players:
            for pawn in player.pawns:
                if pawn.position == player_pawn.position and pawn.colour != player_pawn.colour:
                    player.active_pawns -= 1
                    pawn.reset_pawn()
                    return True

        return False

    def check_strike(self, p):
        for pawn in p.pawns:
            for player in self.players:
                for enemy_pawn in player.pawns:
                    if enemy_pawn.position == pawn.position and enemy_pawn.colour != pawn.colour:
                        return True, pawn
        return False, self.get_random_pawn(p)

    def get_random_pawn(self, player):
        active_pawns = []

        for pawn in player.pawns:
            if pawn.active:
                active_pawns.append(pawn)

        return active_pawns[random.randint(0, len(active_pawns) - 1)]

    def get_player(self, c):
        for i in range(0, 4):
            if self.players[i].colour == c:
                return self.players[i]
