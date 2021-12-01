from board import Board
size = 12
mines = 13


def main():
	board = Board(size, mines)

	print("\n" * 50)
	print("use '-' between x and y if you want to place a flag. else use ','")
	print("\n" * 2)
	print(board.draw_board())

	first_round = True
	while True:
		xy = xy_input()
		if first_round:
			board.find_valid_starting_mine_board(xy[0], xy[1])
			first_round = False
		print("\n" * 50)

		if xy[2] == False:  # normal move (not placing a flag)
			xy.pop()
			update = board.update_board((xy[0], xy[1]))
			if update == False:
				print("\n" * 50)
				print(board.reveal_board())
				input("You hit a mine!")
				break
			else:
				print(update)
				if board.check_winning():
					print("\n" * 50)
					print(board.reveal_board())
					input("you won!")
					break
		else:  # player is placing a flag
			print(board.update_board((xy[0], xy[1]), xy[2]))


def xy_input():
	"""Returns x,y from user input
	"""
	while True:
		flag_coordinates = False
		coordinates = input("Position (x,y): ")
		if "," in coordinates:
			coordinates = coordinates.split(",")
		elif "-" in coordinates:
			coordinates = coordinates.split("-")
			flag_coordinates = True

		if len(coordinates) != 2:
			print("Invalid input: expected 2 numbers")
			continue
		try:
			coordinates[0] = int(coordinates[0])
		except ValueError:
			print("Invalid input: x and y must be integers")
			continue
		try:
			coordinates[1] = int(coordinates[1])
		except ValueError:
			print("Invalid input: x and y must be integers")
			continue

		if coordinates[0] not in range(1, size + 1) or coordinates[1] not in range(1, size + 1):
			print(f"Invalid input: x and y need to be between 1 and {size}")
			continue

		coordinates.append(flag_coordinates)
		return coordinates


if __name__ == "__main__":
	main()
