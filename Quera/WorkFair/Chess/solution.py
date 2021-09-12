class Piece:
    def __init__(self, sort: str, color: str, position: tuple):
        self.sort = sort
        self.color = color
        self.position = position


class Board:
    invalid_query = "invalid query"
    king = "K"
    soldier = "P"
    white = "white"
    black = "black"

    def __init__(self):
        king_white = Piece(Board.king, Board.black, (10, 10))
        king_black = Piece(Board.king, Board.white, (-10, -10))
        self.position = {
            king_black.position: king_black,
            king_white.position: king_white,
        }

    def add(self, piece: Piece):
        valid_condition = (not self.find_piece(piece)) and (piece.sort != Board.king)
        if valid_condition:
            self.position.update({piece.position: piece})
        else:
            print(Board.invalid_query)
            # return Board.invalid_query

    def remove(self, position, remove_king=False):
        found_piece = self.find_piece(position)
        if remove_king:
            valid_condition = found_piece
        else:
            valid_condition = (found_piece) and (found_piece.sort != Board.king)
        if valid_condition:
            self.position.pop(position)
        else:
            print(Board.invalid_query)
            # return Board.invalid_query

    def move(self, piece, position2):
        found_piece = self.find_piece(piece)
        found_piece2 = self.find_piece(position2)
        valid_condition = found_piece
        if valid_condition:
            # if the second position is empty
            if not found_piece2:
                self.move_to_empty_position(found_piece, position2)
            # if the second postion piece is the same as first and is not a king
            elif (
                (found_piece2)
                and (found_piece2.color != found_piece.color)
                and (found_piece2.sort != "K")
            ):
                self.remove(found_piece2.position)
                self.move_to_empty_position(found_piece, position2)
            else:
                print(Board.invalid_query)
                # return Board.invalid_query
        else:
            print(Board.invalid_query)

    def is_mate(self, color):
        king = self.find_king(color)
        king_pos = king.position
        for position, piece in self.position.items():
            if piece.sort == Board.soldier and piece.color != color:
                # if the soldier is around the king
                if (position[0] in range(king_pos[0] - 1, king_pos[0] + 2)) and (
                    position[1] in range(king_pos[1] - 1, king_pos[1] + 2)
                ):
                    return True
        return False

    def find_piece(self, piece):
        if type(piece) is Piece:
            found_piece = self.position.get(piece.position)
        elif type(piece) is tuple:
            found_piece = self.position.get(piece)
        return found_piece if found_piece else None

    def move_to_empty_position(self, piece: Piece, position2: tuple):
        if piece.sort == Board.king:
            self.remove(piece.position, remove_king=True)
        else:
            self.remove(piece.position)
        piece.position = position2
        self.position.update({position2: piece})

    def find_king(self, color):
        for piece in self.position.values():
            if piece.sort == Board.king and piece.color == color:
                return piece

    def clear_board(self):
        self.position.clear()
        self.__init__()


# def main():
# board = Board()
# king_white = Piece(Board.king, Board.white, (-10, -10))
# king_black = Piece(Board.king, Board.black, (10, 10))
# king_white = board.add(Piece(Board.king, Board.white, (-10, -10)))
# king_black = board.add(Piece(Board.king, Board.black, (10, 10)))
# board.move(Piece(Board.king, Board.white, (-10, -10)), (11, 11))
# board.move(Piece(Board.king, Board.white, (11, 11)), (10, 10))
# w1 = Piece(Board.soldier, Board.white, (9, 9))
# board.add(w1)
# board.add(Piece(Board.soldier, Board.white, (9, 9)))
# b1 = Piece(Board.soldier, Board.black, (8, 9))
# board.add(b1)
# board.move(b1, w1.position)
# print(board.is_mate(Board.white))
# print(board.is_mate(Board.black))
# board.move(w1, king_white.position)
# board.move(king_white, king_black.position)
# board.remove(b1.position)
# board.remove(king_black.position)
# print("done")


# if __name__ == "__main__":
#     main()
