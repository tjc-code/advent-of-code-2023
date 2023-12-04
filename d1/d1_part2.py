#########
#CHOOSE WHICH DATA TO USE
example = False
#########

def calculate_sum():
    numbers_from_data = [
        convert_word_to_number(cal_string)
         for cal_string in data
        ] 

    #### Can be used for debugging
    # with open('your_file.txt', 'w') as f:
    #     for line in numbers_from_data:
    #         f.write(f"{line}\n")

    sum = 0
    for number in numbers_from_data:
        two_pertinent_digits = number[0] + number[-1]
        sum += int(two_pertinent_digits)

    print(sum)


example_text = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
    ]

# read in file
file = "d1_input.txt"
text_file = open(file, "r")
d1_input = text_file.read().split("\n")

data = example_text if example else d1_input

word_to_number_dict = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4", 
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine": "9",
}

def convert_word_to_number(input_string: str):
    output_string = ""
    for start_index in range(len(input_string)+1):
        for end_index in range(len(input_string)-start_index+1):
            slice = input_string[start_index:start_index+end_index]
            if slice in word_to_number_dict.keys():
                output_string += word_to_number_dict[slice]
            elif slice in word_to_number_dict.values():
                output_string += slice
    return output_string


if __name__ == "__main__":
    calculate_sum()