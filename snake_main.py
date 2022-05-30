import game_parameters
from game_display import GameDisplay
import snake_helper


def main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    x, y = snake_helper.snake_initial()
    snake_position = snake_helper.snake_position(x, y)
    i, j, r, t = snake_helper.place_bomb(snake_position)
    apples = snake_helper.place_apples(snake_position, i, j)
    while True:
        for x, y in snake_position:
            gd.draw_cell(x, y, "black")
        gd.draw_cell(i, j, 'red')
        for apple in apples:
            gd.draw_cell(apple[0], apple[1], 'green')
        key_clicked = gd.get_key_clicked()
        snake_position = snake_helper.snake_update(snake_position, key_clicked)
        # if (key_clicked == 'Left') and (x > 0):
        #     snake_position[0] = (x - 1, y)
        # elif (key_clicked == 'Right') and (x < game_parameters.WIDTH):
        #     x += 1
        gd.draw_cell(snake_position[0][0], snake_position[0][1], "black")
        gd.end_round()

