# https://en.m.wikipedia.org/wiki/Box_Drawing
from random import randrange


class Board:
	# you only need to use update_board() outside this class.

	def __init__(self, size, mine_numbers):
		self.size = size
		self.board_data = self.create_board(self.size)
		self.mine_board = self.generate_mine_board(mine_numbers)

	def create_board(self, size):
		board_data = []
		for x in range(size):
			row = []
			for y in range(size):
				#this is the "default" icon.
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
			x = randrange(self.size)
			y = randrange(self.size)

			if (x, y) not in mine_list:
				mine_list.append((x, y))
		return mine_list

	def generate_mine_board(self, mine_numbers):
		mine_list = self.generate_mines(mine_numbers)
		mine_board = []
		for x in range(self.size):
			line = []
			for y in range(self.size):
				line.append(0)
			mine_board.append(line)

		for mine in mine_list:
			#add a mine to the mine position, and add 1 to all adjecent spots
			x = mine[0]
			y = mine[1]
			mine_board[y][x] = "◉"  # negative = mine

			try:
				mine_board[y - 1][x - 1] += 1
			except Exception:
				pass
			try:
				mine_board[y - 1][x + 1] += 1
			except Exception:
				pass
			try:
				mine_board[y - 1][x] += 1
			except Exception:
				pass

			try:
				mine_board[y][x - 1] += 1
			except Exception:
				pass
			try:
				mine_board[y][x + 1] += 1
			except Exception:
				pass

			try:
				mine_board[y + 1][x - 1] += 1
			except Exception:
				pass
			try:
				mine_board[y + 1][x + 1] += 1
			except Exception:
				pass
			try:
				mine_board[y + 1][x] += 1
			except Exception:
				pass

		return mine_board

	def flood_fill(self, x, y):
		if self.board_data[y][x] == " ◌ " and self.mine_board[y][x] == "◉":
			raise Exception("the flood fill algo hit a mine, but it shouldn't because it will stop when it hits a number.")

		elif self.board_data[y][x] == " ◌ " and self.mine_board[y][x] > 0:
			self.board_data[y][x] = " " + str(self.mine_board[y][x]) + " "

		elif self.board_data[y][x] == " ◌ " and self.mine_board[y][x] == 0:
			self.board_data[y][x] = "   "
			try:
				if x > 0:
					self.flood_fill(x - 1, y)
				if x < self.size:
					self.flood_fill(x + 1, y)
				if y > 0:
					self.flood_fill(x, y - 1)
				if y < self.size:
					self.flood_fill(x, y + 1)
			except:
				pass

	def reveal_board(self):
		for x in range(self.size):
			for y in range(self.size):
				if self.board_data[y][x] == " ◌ ":
					if self.mine_board[y][x] == "◉":
						self.board_data[y][x] = " ◉ "
					elif self.mine_board[y][x] == 0:
						self.board_data[y][x] = "   "
					elif self.mine_board[y][x] > 0:
						self.board_data[y][x] = " " + str(self.mine_board[y][x]) + " "
		return self.draw_board()

	def check_winning(self):
		flag = True
		for x in range(self.size):
			for y in range(self.size):
				if self.board_data[y][x] == " ◌ " and self.mine_board[y][x] != "◉":
					flag = False
		return flag

	def update_board(self, position):
		"""Takes position [x,y] as input
			returns a updated board as a string
		"""

		x = position[0] - 1
		y = position[1] - 1

		if self.mine_board[y][x] == "◉":
			self.board_data[y][x] = " ◉ "
			return False

		elif isinstance(self.mine_board[y][x], int) and self.mine_board[y][x] > 0:
			self.board_data[y][x] = " " + str(self.mine_board[y][x]) + " "

		else:
			self.flood_fill(x, y)

		return self.draw_board()
