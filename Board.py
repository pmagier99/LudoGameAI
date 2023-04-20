import pygame

import BOARD_COORDINATES


class Board:
    W, H = 600, 600
    SCREEN = pygame.display.set_mode((W, H))
    SURF = pygame.image.load("img/board.png").convert()
    Y_PAWN = pygame.image.load("img/yellowPawn.png")
    G_PAWN = pygame.image.load("img/greenPawn.png")
    B_PAWN = pygame.image.load("img/bluePawn.png")
    R_PAWN = pygame.image.load("img/redPawn.png")

    GP_Board = []

    def __init__(self, y, b, r, g):
        self.my_font = pygame.font.SysFont('Arial', 30)
        self.y_pawns = y
        self.b_pawns = b
        self.r_pawns = r
        self.g_pawns = g
        self.draw_window()
        self.draw_pawns(dice="")
        pygame.display.update()

    def draw_window(self):
        pygame.display.set_caption("Ludo Game")
        self.SCREEN.blit(self.SURF, (0, 0))

    def draw_pawns(self, dice):
        self.SCREEN.blit(self.SURF, (0, 0))
        self.SCREEN.fill(pygame.Color("black"), (290, 285, 30, 30))
        txt_dice = self.my_font.render(str(dice), False, (255, 255, 255))
        self.SCREEN.blit(txt_dice, (290, 285))

        cell_size = 50
        b = BOARD_COORDINATES.bc
        y_pawn_0 = self.y_pawns[0].position
        y_pawn_1 = self.y_pawns[1].position
        y_pawn_2 = self.y_pawns[2].position
        y_pawn_3 = self.y_pawns[3].position

        b_pawn_0 = self.b_pawns[0].position
        b_pawn_1 = self.b_pawns[1].position
        b_pawn_2 = self.b_pawns[2].position
        b_pawn_3 = self.b_pawns[3].position

        r_pawn_0 = self.r_pawns[0].position
        r_pawn_1 = self.r_pawns[1].position
        r_pawn_2 = self.r_pawns[2].position
        r_pawn_3 = self.r_pawns[3].position

        g_pawn_0 = self.g_pawns[0].position
        g_pawn_1 = self.g_pawns[1].position
        g_pawn_2 = self.g_pawns[2].position
        g_pawn_3 = self.g_pawns[3].position

        self.SCREEN.blit(self.Y_PAWN, (30 + (b[y_pawn_0][0] * cell_size), 30 + (b[y_pawn_0][1] * cell_size)))
        self.SCREEN.blit(self.Y_PAWN, (30 + (b[y_pawn_1][0] * cell_size), 30 + (b[y_pawn_1][1] * cell_size)))
        self.SCREEN.blit(self.Y_PAWN, (30 + (b[y_pawn_2][0] * cell_size), 30 + (b[y_pawn_2][1] * cell_size)))
        self.SCREEN.blit(self.Y_PAWN, (30 + (b[y_pawn_3][0] * cell_size), 30 + (b[y_pawn_3][1] * cell_size)))

        self.SCREEN.blit(self.B_PAWN, (30 + (b[b_pawn_0][0] * cell_size), 30 + (b[b_pawn_0][1] * cell_size)))
        self.SCREEN.blit(self.B_PAWN, (30 + (b[b_pawn_1][0] * cell_size), 30 + (b[b_pawn_1][1] * cell_size)))
        self.SCREEN.blit(self.B_PAWN, (30 + (b[b_pawn_2][0] * cell_size), 30 + (b[b_pawn_2][1] * cell_size)))
        self.SCREEN.blit(self.B_PAWN, (30 + (b[b_pawn_3][0] * cell_size), 30 + (b[b_pawn_3][1] * cell_size)))

        self.SCREEN.blit(self.R_PAWN, (30 + (b[r_pawn_0][0] * cell_size), 30 + (b[r_pawn_0][1] * cell_size)))
        self.SCREEN.blit(self.R_PAWN, (30 + (b[r_pawn_1][0] * cell_size), 30 + (b[r_pawn_1][1] * cell_size)))
        self.SCREEN.blit(self.R_PAWN, (30 + (b[r_pawn_2][0] * cell_size), 30 + (b[r_pawn_2][1] * cell_size)))
        self.SCREEN.blit(self.R_PAWN, (30 + (b[r_pawn_3][0] * cell_size), 30 + (b[r_pawn_3][1] * cell_size)))

        self.SCREEN.blit(self.G_PAWN, (30 + (b[g_pawn_0][0] * cell_size), 30 + (b[g_pawn_0][1] * cell_size)))
        self.SCREEN.blit(self.G_PAWN, (30 + (b[g_pawn_1][0] * cell_size), 30 + (b[g_pawn_1][1] * cell_size)))
        self.SCREEN.blit(self.G_PAWN, (30 + (b[g_pawn_2][0] * cell_size), 30 + (b[g_pawn_2][1] * cell_size)))
        self.SCREEN.blit(self.G_PAWN, (30 + (b[g_pawn_3][0] * cell_size), 30 + (b[g_pawn_3][1] * cell_size)))
        pygame.display.update()
