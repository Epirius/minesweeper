from board import Board
size = 12
mines = 13


def main():
	board = Board(size, mines)
	print("\n" * 50)
	print(board.draw_board())

	while True:
		xy = xy_input()
		print("\n" * 50)
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


def xy_input():
	"""Returns x,y from user input
	"""
	while True:
		coordinates = input("Position (x,y): ")
		coordinates = coordinates.split(",")

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

		return coordinates


if __name__ == "__main__":
	main()
