import torch
import random
import numpy as np
from collections import deque

from model import Linear_QNet, QTrainer

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001
class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0.8  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(6, 20, 3)  # State, Hidden , Actions
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def get_state(self, game, dice_res, x):

        player = game.players[x]
        state = [0, 0, 0, 0, 0, 0]  # dice,waiting pawns, pawn in range to attack, pawn in range to be attacked, close to home, home pawns

        enemy_pawns = []
        for p in range(0, 4):
            if p == x:
                pass
            else:
                for pawn in game.players[p].pawns:
                    if pawn.active:
                        enemy_pawns.append(pawn)

        state[0] = dice_res  # Dice
        # waiting pawns
        if len(player.pawns) - player.active_pawns - player.home_pawns > 0:
            state[1] = 1
        else:
            state[1] = 0

        # pawn in range to attack
        if player.active_pawns == 0:
            state[2] = 0
        else:
            for p_pawn in player.pawns:
                for e_pawn in enemy_pawns:
                    if e_pawn.position - dice_res == p_pawn.position:
                        state[2] = 1
                        break
                    elif p_pawn.position + dice_res >= 40:
                        temp_pos = p_pawn.position + dice_res - 40
                        if e_pawn.position == temp_pos:
                            state[2] = 1
                        else:
                            state[2] = 0
                        break
                    else:
                        state[2] = 0

                if state[2] == 1:
                    break

        # pawn in range to be attacked
        if player.active_pawns == 0:
            state[3] = 0
        else:
            for p_pawn in player.pawns:
                for e_pawn in enemy_pawns:
                    if e_pawn.position + 6 > p_pawn.position > e_pawn.position:
                        state[3] = 1
                        break
                    elif e_pawn.position + 6 >= 40:
                        if (e_pawn.position + 6) - 40 >= p_pawn.position:
                            state[3] = 1
                        else:
                            state[3] = 0
                        break
                    else:
                        state[3] = 0

                if state[3] == 1:
                    break

        # in range to enter home
        if player.active_pawns == 0:
            state[4] = 0
        else:
            for p_pawn in player.pawns:
                if 37 < p_pawn.complete_path + dice_res < 42:
                    state[4] = 1
                    break
                else:
                    state[4] = 0

        # in home pawns
        state[5] = player.home_pawns

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, game_over):
        self.memory.append((state, action, reward, next_state, game_over))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory

        for states, actions, rewards, next_states, dones in mini_sample:
            self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, states, actions, rewards, next_states, dones):
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def get_action(self, state):
        # random moves
        self.epsilon = 80 - self.n_games
        final_move = [0, 0, 0]

        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move



