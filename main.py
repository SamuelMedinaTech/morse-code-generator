from logo import logo
from morse_code import MORSE_CODE_DICT


def encode(string):
    """Encodes a string into Morse Code"""
    morse_code_array = []
    for char in string:
        char = char.upper()
        if char in MORSE_CODE_DICT:
            morse_code_array.append(MORSE_CODE_DICT[char])
        else:
            morse_code_array.append(char)

    return ' '.join(morse_code_array)


if __name__ == '__main__':
    print(logo)

    # Input the string to encode
    user_input = input('Enter the string to encode: ')
    output = encode(user_input)
    print(f'The output is: {encode(user_input)}')
