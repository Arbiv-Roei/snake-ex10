import game_parameters
from game_display import GameDisplay



def snake_initial():
    x = game_parameters.WIDTH//2
    y = game_parameters.HEIGHT//2
    return x, y


def snake_position(x, y):
    return [(x, y), (x, y - 1), (x, y - 2)]


def place_bomb(snake_list):
    x, y, radius, time = game_parameters.get_random_bomb_data()
    if (x, y) in snake_list:
        return place_bomb(snake_list)
    return x, y, radius, time


def one_apple(snake_lst, i, j):
    apple1 = game_parameters.get_random_apple_data()
    if (apple1[0], apple1[1]) in snake_lst or (apple1[0], apple1[1]) == (i, j):
        return one_apple(snake_lst, i, j)
    return apple1


def place_apples(snake, i, j):
    apples = []
    for k in range(3):
        apples.append(one_apple(snake, i, j))
    if apples[0] == apples[1] or apples[0] == apples[2] or apples[2] == apples[1]:
        place_apples(snake, i, j)
    return apples


def snake_update(snake_lst, move_key):
    if move_key == 'left':
        snake_lst.insert(0, (snake_lst[0][0]-1, snake_lst[0][1]))
        snake_lst.pop(-1)
    if move_key == 'right':
        snake_lst.insert(0, (snake_lst[0][0] + 1, snake_lst[0][1]))
        snake_lst.pop(-1)
    if move_key == 'up':
        snake_lst.insert(0, (snake_lst[0][0], snake_lst[0][1] + 1))
        snake_lst.pop(-1)
    if move_key == 'down':
        snake_lst.insert(0, (snake_lst[0][0], snake_lst[0][1] - 1))
        snake_lst.pop(-1)
    return snake_lst



snake = [(0,0), (0,1), (0,2)]
print(snake_update(snake, 'right'))









def place_snake(gd:GameDisplay, x,y):
    for x, y in snake_position(x,y):
        gd.draw_cell(x, y, 'black')
