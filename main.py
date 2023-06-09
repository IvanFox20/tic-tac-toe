import pygame
import sys


def is_game_over(arr, sign):
    empty_fields = 0
    for row in arr:
        empty_fields += row.count(0)
        if row.count(sign) == 3:
            return sign + ' WIN`s'
    for col in range(3):
        if arr[0][col] == sign and arr[1][col] == sign and arr[2][col] == sign:
            return sign + ' WIN`s'
    if arr[0][0] == sign and arr[1][1] == sign and arr[2][2] == sign:
        return sign + ' WIN`s'
    if arr[0][2] == sign and arr[1][1] == sign and arr[2][0] == sign:
        return sign + ' WIN`s'
    if empty_fields == 0:
        return 'DRAW'
    return False


pygame.init()
size_block = 200
margin = 10
width = height = size_block * 3 + margin * 4

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-tac-toe")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
green_blue = (0, 255, 175)
arr = [[0] * 3 for i in range(3)]
queue = 0
gameover = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)  # узнаём в какой колонке кликнули
            row = y_mouse // (size_block + margin)  # узнаем в какой строке кликнули
            if arr[row][col] == 0:
                if queue % 2 == 0:
                    arr[row][col] = 'X'
                else:
                    arr[row][col] = 'O'
                queue += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            gameover = False
            arr = [[0] * 3 for i in range(3)]
            queue = 0
            screen.fill(black)
    if not gameover:
        for row in range(3):
            for col in range(3):
                if arr[row][col] == 'X':
                    color = red
                elif arr[row][col] == 'O':
                    color = green_blue
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin  # Координаты левого верхнего угла квадрата
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, black, (x + 10, y + 10), (x + size_block - 10, y + size_block - 10), 10)
                    pygame.draw.line(screen, black, (x + size_block - 10, y + 10), (x + 10, y + size_block - 10), 10)
                if color == green_blue:
                    pygame.draw.circle(screen, black, (x + size_block // 2, y + size_block // 2), size_block // 2 - 10, 10)
    if (queue - 1) % 2 == 0:
        gameover = is_game_over(arr, 'X')
    else:
        gameover = is_game_over(arr, 'O')
    if gameover:
        screen.fill(black)
        font = pygame.font.SysFont('font_name', 80)
        text1 = font.render(gameover, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])
    pygame.display.update()
