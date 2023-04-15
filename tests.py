import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        game = Game()

        game.players[0].pawn_out()
        game.players[3].pawn_out()

        yellow = game.players[0].get_active_pawn()
        green = game.players[3].get_active_pawn()

        game.players[0].move_piece(yellow, 1)
        game.players[3].move_piece(green, 11)
        game.check_for_collision(green)

        self.assertEqual(56, yellow.position)
        self.assertEqual(0, yellow.complete_path)
        self.assertEqual(0, game.players[0].active_pawns)

    def test_home(self):
        game = Game()

        game.players[0].pawn_out()
        yellow1 = game.players[0].get_active_pawn()
        game.players[0].move_piece(yellow1, 40)

        game.players[0].pawn_out()
        yellow2 = game.players[0].get_active_pawn()
        game.players[0].move_piece(yellow2, 40)

        self.assertEqual(1, game.players[0].home_pawns)

    def test_strike_own_pawn(self):
        game = Game()

        game.players[0].pawn_out()
        yellow1 = game.players[0].get_active_pawn()
        game.players[0].move_piece(yellow1, 2)
        yellow1.active = False

        game.players[0].pawn_out()
        yellow2 = game.players[0].get_active_pawn()
        game.players[0].move_piece(yellow2, 2)

        game.check_for_collision(yellow2)

        self.assertEqual(2, yellow2.position)
        self.assertEqual(2, yellow1.position)
        self.assertEqual(2, game.players[0].active_pawns)

    def test_strike_when_two_pawns(self):
        game = Game()

        game.players[0].pawn_out()
        yellow1 = game.players[0].get_active_pawn()
        game.players[0].move_piece(yellow1, 2)

        game.players[0].pawn_out()

        yellow1.active = False

        yellow2 = game.players[0].get_active_pawn()
        game.players[0].move_piece(yellow2, 2)

        game.players[3].pawn_out()
        green1 = game.players[3].get_active_pawn()
        game.players[3].move_piece(green1, 12)

        game.check_for_collision(green1)

        self.assertEqual(1, game.players[0].active_pawns)
        self.assertNotEquals(yellow2.position, yellow1.position)


if __name__ == '__main__':
    unittest.main()
