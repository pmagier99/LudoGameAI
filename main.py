import time
from Game import Game
from agent import Agent
from helper import *
import pandas as pd


def train():
    yellow_scores = []
    red_score = []
    blue_score = []
    green_score = []

    agent = Agent()
    agent_red = Agent()
    agent_blue = Agent()
    agent_green = Agent()

    agents = [agent, agent_blue, agent_red, agent_green]

    game = Game()

    red_won = 0
    blue_won = 0
    green_won = 0
    yellow_won = 0

    red_statistics = []
    blue_statistics = []
    green_statistics = []
    yellow_statistics = []

    y_bad = []
    y_good = []
    r_bad = []
    r_good = []
    g_bad = []
    g_good = []
    b_bad = []
    b_good = []

    number_games = 10000

    i = 0
    while i < number_games:

        finish = False

        for x in range(0, 4):
            dice = game.roll_dice()

            current_state = agents[x].get_state(game, dice, x)

            move = agents[x].get_action(current_state)

            reward, done, score, statistics = game.play(move, dice, x)

            next_state = agents[x].get_state(game, dice, x)

            agents[x].train_short_memory(current_state, move, reward, next_state, done)
            agents[x].remember(current_state, move, reward, next_state, done)

            # time.sleep(2)

            if game.players[x].colour == "yellow":
                yellow_statistics = statistics
            if game.players[x].colour == "red":
                red_statistics = statistics
            if game.players[x].colour == "green":
                green_statistics = statistics
            if game.players[x].colour == "blue":
                blue_statistics = statistics

            if done:
                finish = done
                break

        if finish:
            i += 1

            df1 = pd.DataFrame([["Yellow", i, yellow_statistics[0], yellow_statistics[1], yellow_statistics[2],
                                 yellow_statistics[3], yellow_statistics[4], yellow_statistics[5]]])
            df2 = pd.DataFrame([["Blue", i, blue_statistics[0], blue_statistics[1], blue_statistics[2],
                                 blue_statistics[3], blue_statistics[4], blue_statistics[5]]])
            df3 = pd.DataFrame([["Red", i, red_statistics[0], red_statistics[1], red_statistics[2], red_statistics[3],
                                 red_statistics[4], red_statistics[5]]])
            df4 = pd.DataFrame([["Green", i, green_statistics[0], green_statistics[1], green_statistics[2],
                                 green_statistics[3], green_statistics[4], green_statistics[5]]])

            df1.to_csv('stats/stats_10000.csv', mode='a', header=False)
            df2.to_csv('stats/stats_10000.csv', mode='a', header=False)
            df3.to_csv('stats/stats_10000.csv', mode='a', header=False)
            df4.to_csv('stats/stats_10000.csv', mode='a', header=False)

            for x in range(0, 4):
                if game.players[x].home_pawns != 4:
                    lost_state = agents[x].get_state(game, 0, 0)
                    move = [0, 0, 0]
                    reward = -10

                    agents[x].train_short_memory(lost_state, move, reward, lost_state, finish)
                    agents[x].remember(lost_state, move, reward, lost_state, finish)
                elif game.players[x].home_pawns == 4:
                    if game.players[x].colour == "yellow":
                        yellow_won += 1
                    if game.players[x].colour == "red":
                        red_won += 1
                    if game.players[x].colour == "green":
                        green_won += 1
                    if game.players[x].colour == "blue":
                        blue_won += 1

            game.reset()
            agents.append(agents.pop(agents.index(agents[0])))  # reorder order
            game.colours.append(game.colours.pop(game.colours.index(game.colours[0])))  # reorder order
            agents[0].n_games += 1
            agents[1].n_games += 1
            agents[2].n_games += 1
            agents[3].n_games += 1
            agents[0].train_long_memory()
            agents[1].train_long_memory()
            agents[2].train_long_memory()
            agents[3].train_long_memory()

            print('Game:', agent.n_games, 'Yellow:', yellow_won, 'Red:', red_won, 'Blue:', blue_won, 'Green:',
                  green_won)

            print('Yellow: Good decisions:', yellow_statistics[4], 'Bad decisions: ', yellow_statistics[5])
            print('Red: Good decisions:', red_statistics[4], 'Bad decisions: ', red_statistics[5])
            print('Blue: Good decisions:', blue_statistics[4], 'Bad decisions: ', blue_statistics[5])
            print('Green: Good decisions:', green_statistics[4], 'Bad decisions: ', green_statistics[5])

            yellow_scores.append(yellow_won)
            red_score.append(red_won)
            green_score.append(green_won)
            blue_score.append(blue_won)

            y_good.append(yellow_statistics[4])
            y_bad.append(yellow_statistics[5])
            r_good.append(red_statistics[4])
            r_bad.append(red_statistics[5])

            g_good.append(green_statistics[4])
            g_bad.append(green_statistics[5])
            b_good.append(blue_statistics[4])
            b_bad.append(blue_statistics[5])

            # plot(plot_scores, red_score, green_score, blue_score)
            plot_stats(y_good, r_good, g_good, b_good, y_bad, r_bad, g_bad, b_bad)


if __name__ == '__main__':
    train()
