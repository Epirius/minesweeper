#https://www.youtube.com/watch?v=G8MYGDf_9ho
import pygame
from board_gui import Board

Screen_height = 768
Screen_width = 768
board_size = 12
num_mines = 10
screen = pygame.display.set_mode((Screen_height, Screen_width))
pygame.display.set_caption("Minesweeper")

#load images
box_size = 64
box_default = pygame.image.load("gui/img/default.png").convert_alpha()
box_empty = pygame.image.load("gui/img/empty.png").convert_alpha()
box_flag = pygame.image.load("gui/img/flag.png").convert_alpha()
box_mine = pygame.image.load("gui/img/mine.png").convert_alpha()
box_num = {}
box_num[1] = pygame.image.load("gui/img/1.png").convert_alpha()
box_num[2] = pygame.image.load("gui/img/2.png").convert_alpha()
box_num[3] = pygame.image.load("gui/img/3.png").convert_alpha()
box_num[4] = pygame.image.load("gui/img/4.png").convert_alpha()
box_num[5] = pygame.image.load("gui/img/5.png").convert_alpha()
box_num[6] = pygame.image.load("gui/img/6.png").convert_alpha()
box_num[7] = pygame.image.load("gui/img/7.png").convert_alpha()
box_num[8] = pygame.image.load("gui/img/8.png").convert_alpha()

board = Board(board_size, num_mines)


class Box():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.pos = (x, y)
		self.value = "◌"

	def draw(self, matrix):
		x = int(self.pos[0] / 64)
		y = int(self.pos[1] / 64)

		if matrix[y][x] != self.value:
			self.value = matrix[y][x]

			for i in range(1, 9):
				if self.value == i:
					self.image = box_num[i]
			if self.value == "1":
				self.image = box_num[1]
			if self.value == "▶":
				self.image = box_flag
			if self.value == "◉":
				self.image = box_mine
			if self.value == " ":
				self.image = box_empty

		screen.blit(self.image, (self.rect.x, self.rect.y))


#creating matrix NB: this is temp, use the one from bord.py after prototyping.
matrix = board.create_board(board_size)
box_matrix = []
for y in range(board_size):
	for x in range(board_size):
		name = f"{x},{y}"
		name = Box(x * box_size, y * box_size, box_default)
		box_matrix.append(name)

#game loop
run = True
first_click = True
while run:

	screen.fill((76, 76, 76))
	for box in box_matrix:
		box.draw(matrix)

	mouse_location = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			x = int(mouse_location[0] / 64)
			y = int(mouse_location[1] / 64)

			print(x, y)

			if first_click:
				board.find_valid_starting_mine_board(x, y)
				first_round = False

			update = board.update_board((x, y))
			if update == False:
				#TODO: make an animation here
				print(board.reveal_board())
				input("You hit a mine!")
				break
			else:
				matrix = update
				# print(matrix)
				if board.check_winning():
					#TODO: display win screen
					print(board.reveal_board())
					input("you won!")
					break

		# if "event: right mouse button"
		# 	"player is placing a flag"
		# 	print(board.update_board((x, y), True))

			#############

	pygame.display.update()

pygame.quit()
