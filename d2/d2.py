import re

test_input = ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n"
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n"
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n"
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red \n"
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")

# read in file
file = "d2_input.txt"
text_file = open(file, "r")
puzzle_input = text_file.read().split("\n")

############ SET VALUES
MAX_COLOUR_ALLOWED = {"red": 12, "green": 13, "blue": 14}
TEST_DATA = True

### split game and results
game_list = test_input.split("\n") if TEST_DATA else puzzle_input
game_dictionary = {}
for game in game_list:
    split_game_and_results = game.split(":")
    game_results_list = split_game_and_results[1].split(";")
    for index, turn in enumerate(game_results_list):
        split_turn = turn.split(",")
        balls_dict = {}
        for balls in split_turn:
            number = int(re.findall(r'\b\d+\b', balls)[0])
            colour = balls.split()[-1]
            balls_dict[colour] = number
        game_results_list[index] = balls_dict
    game_dictionary[int(split_game_and_results[0].split(" ")[1])] = game_results_list

# check values
sum = 0
for game_number, game_result in game_dictionary.items():
    game_allowed = True
    for turn in game_result:
        for colour in MAX_COLOUR_ALLOWED:
            if colour in turn and turn[colour] > MAX_COLOUR_ALLOWED[colour]:
                # game not allowed
                game_allowed = False
    sum += game_number if game_allowed else 0

print(sum)
