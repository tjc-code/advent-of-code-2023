example_text = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
    ]

# read in file
file = "d1_input.txt"
text_file = open(file, "r")
d1_input = text_file.read().split("\n")


def get_numbers_from_string(input_string):
    output_string = ""
    for character in input_string:
        if character in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            output_string += character
    return output_string

numbers_from_example = [get_numbers_from_string(cal_string) for cal_string in d1_input] 

sum = 0
for number in numbers_from_example:
    two_pertinent_digits = number[0] + number[-1]
    sum += int(two_pertinent_digits)

print(sum)