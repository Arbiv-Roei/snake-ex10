# gd.show_score(0)
#     x, y = snake_helper.snake_initial()
#     bomb_place = snake_helper.place_bomb(gd)
#     while bomb_place in snake_helper.snake_position(x, y):
#         bomb_place = snake_helper.place_bomb(gd)
#     apples = snake_helper.place_apples()
#     for x, y in snake_helper.snake_position(x, y):
#         gd.draw_cell(x, y, 'black')
#     for x, y in bomb_place:
#         gd.draw_cell(x, y, 'red')
#     for apple in apples:
#         for x, y in apple:
#             gd.draw_cell(x, y, 'green')
#     while True:
#         key_clicked = gd.get_key_clicked()
#         if (key_clicked == 'Left') and (x > 0):
#             x -= 1
#         elif (key_clicked == 'Right') and (x < game_parameters.WIDTH):
#             x += 1
#         gd.draw_cell(x, y, "black")
#         gd.end_round()