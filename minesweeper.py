from board import Board

board = Board(15, 10)
# print(board.draw_board())
board.update_board((2, 5))
board.update_board((13, 13))
board.update_board((15, 2))
board.update_board((12, 3))
board.update_board((13, 4))
board.update_board((9, 3))
board.update_board((7, 9))
board.update_board((3, 11))
board.update_board((11, 4))
print(board.update_board((1, 8)))
