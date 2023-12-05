import re

test_input = ("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n"
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n"
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n"
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n"
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n"
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")

# read in file
file = "d4_input.txt"
text_file = open(file, "r")
puzzle_input = text_file.read().split("\n")

############ SET VALUES
TEST_DATA = False


def get_card_score(players_numbers, winning_numbers):
    card_score = 0
    for player_number in players_numbers:
        if player_number in winning_numbers:
            card_score += 1
    return card_score

card_list = test_input.split("\n") if TEST_DATA else puzzle_input
card_scores = {}
for card in card_list:
    split_card_and_results = card.split(":")
    results = split_card_and_results[1].split("|")
    # lists for each part of card
    card_number = int(re.findall(r'\b\d+\b', split_card_and_results[0])[0])
    winning_numbers = [int(num) for num in re.findall(r'\b\d+\b', results[0])]
    players_numbers = [int(num) for num in re.findall(r'\b\d+\b', results[1])]

    card_scores[card_number] = get_card_score(players_numbers, winning_numbers)

### set initial card counts to be one of each
card_counts = {}
for card_number in card_scores:
    card_counts[card_number] = 1

### iterate through each card and increase card counts
for card_number in card_scores:
    if card_scores[card_number] > 0:
        # increase subsequents
        for scores in range(1, card_scores[card_number]+1):
            card_counts[card_number+scores] += card_counts[card_number]

print(card_counts)
answer = sum(card_counts.values())
print(answer)
if TEST_DATA:
    print("You got the right answer?", answer==30)
