from models.piece import Piece
from models.pawn import Pawn
from models.rook import Rook
from models.knight import Knight
from models.bishop import Bishop
from models.queen import Queen
from models.king import King

from game.board import Board




board = Board()
board.setup_pieces()
board.print_board()













pawn = Pawn("White", (6, 0))
rook = Rook("White", (7, 0))
knight = Knight("White", (7, 1))
bishop = Bishop("White", (7, 2))
queen = Queen("White", (7, 3))
king = King("White", (7, 4))

print(pawn.color, pawn.position)
print(rook.color, rook.position)
print(knight.color, knight.position)
print(bishop.color, bishop.position)
print(queen.color, queen.position)
print(king.color, king.position)

print(board.board[7][0].__class__.__name__)
print(board.board[6][0].__class__.__name__)
print(board.board[0][4].__class__.__name__)
print(board.board[1][4].__class__.__name__)