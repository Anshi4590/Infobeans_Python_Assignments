from models.pawn import Pawn
from models.rook import Rook
from models.knight import Knight
from models.bishop import Bishop
from models.queen import Queen
from models.king import King

class Board:

    def __init__(self):

        self.board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]


    def setup_pieces(self):
       

        white_back_row = [
            Rook("White", (7, 0)),
            Knight("White", (7, 1)),
            Bishop("White", (7, 2)),
            Queen("White", (7, 3)),
            King("White", (7, 4)),
            Bishop("White", (7, 5)),
            Knight("White", (7, 6)),
            Rook("White", (7, 7))
        ]

        for column in range(8):
            self.board[7][column] = white_back_row[column]

        for column in range(8):
            self.board[6][column] = Pawn("White", (6, column)) 

        print()

        black_back_row = [
            Rook("Black", (0, 0)),
            Knight("Black", (0, 1)),
            Bishop("Black", (0, 2)),
            Queen("Black", (0, 3)),
            King("Black", (0, 4)),
            Bishop("Black", (0, 5)),
            Knight("Black", (0, 6)),
            Rook("Black", (0, 7))
        ]
        for column in range(8):
            self.board[0][column] = black_back_row[column]


        for column in range(8):
            self.board[1][column] = Pawn("Black",(1,column))


    def print_board():

            symbols = {
                "Pawn": "P",
                "Rook": "R",
                "Knight": "N",
                "Bishop": "B",
                "Queen": "Q",
                "King": "K"
            }

            for row in range(8):

                for column in range(8):

                    piece = self.board[row][column]

                    if piece is None:
                        print(".", end=" ")

                    else:
                        symbol = symbols[piece.__class__.__name__]

                        if piece.color == "Black":
                            symbol = symbol.lower()

                        print(symbol, end=" ")

                print()