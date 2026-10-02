from models.piece import Piece

class Pawn(Piece):

    def __init__(self,color,position):
        super().__init__(color,position)
        