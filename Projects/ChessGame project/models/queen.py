from models.piece import Piece

class Queen(Piece):

    def __init__(self,color,position):
        super().__init__(color,position)