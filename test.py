import re

def words_to_numbers(input_string):
    word_mapping = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
        # Add more words as needed
    }

    pattern = re.compile(r'\b(?:' + '|'.join(word_mapping.keys()) + r')\b')

    result = ""
    matches = pattern.findall(input_string)

    for match in matches:
        result += word_mapping.get(match, match)

    return result

# Example usage
input_string = "eightwothree"
result = words_to_numbers(input_string)
print(result)