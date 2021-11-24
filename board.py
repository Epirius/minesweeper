# https://en.m.wikipedia.org/wiki/Box_Drawing
from random import randrange


class Board:
	# you only need to use update_board() outside this class.
	# the board size has to be a multiple of 3.

	def __init__(self, size, mine_numbers):
		self.size = size
		self.board_data = self.create_board(self.size)
		self.mine_positions = self.generate_mines(mine_numbers)

	def create_board(self, size):
		board_data = []
		for x in range(size):
			row = []
			for y in range(size):
				row.append(" ◌ ")
			board_data.append(row)
		return board_data

	def internal_board(self):
		internal_board = ""
		for x in range(len(self.board_data)):
			drawn_line = ""
			for y in range(len(self.board_data)):
				drawn_line += self.board_data[x][y]
				if y != len(self.board_data) - 1:
					drawn_line += "│"
			internal_board += drawn_line + "\n"
			if x < len(self.board_data) - 1:
				internal_board += "───┼" * \
					(len(self.board_data) - 1) + "───" + "\n"
		return internal_board

	def draw_board(self):
		internal_board = self.internal_board()
		drawn_board = ""

		# drawing the boarder around the internal board
		internal_board = internal_board.split("\n")
		drawn_board += "╔═══" + "╤═══" * (self.size - 1) + "╗" + "\n"
		for x in range(0, self.size * 2, 2):
			drawn_board += "║" + \
				internal_board[x] + "║" + f" :{int(x/2 +1)}" + "\n"
			if x != (self.size * 2) - 2:
				drawn_board += "╟" + internal_board[x + 1] + "╢" + "\n"
		drawn_board += "╚═══" + "╧═══" * (self.size - 1) + "╝" + "\n"

		for x in range(self.size):
			number = x + 1
			if number < 10:
				drawn_board += f"  {number} "
			else:
				drawn_board += f"  {number}"
		return drawn_board

	def generate_mines(self, mine_numbers):
		mine_list = []

		while len(mine_list) < mine_numbers:
			x = randrange(1, self.size + 1)
			y = randrange(1, self.size + 1)

			if (x, y) not in mine_list:
				mine_list.append((x, y))

		return mine_list

	def update_board(self, position):
		"""Takes position [x,y] as input
			returns a updated board as a string
		"""

		mine = " ◉ "
		empty = "   "

		x = position[0] - 1
		y = position[1] - 1

		# adding the player icon to the board
		self.board_data[x][y] = mine

		return self.draw_board()
