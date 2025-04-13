import sys

def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            raise Exception("The script does not support your language yet.")
        
        if 'a' <= char <= 'z':
            start = ord('a')
            offset = (ord(char) - start + shift) % 26 if mode == "encode" else (ord(char) - start - shift) % 26
            result += chr(start + offset)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            offset = (ord(char) - start + shift) % 26 if mode == "encode" else (ord(char) - start - shift) % 26
            result += chr(start + offset)
        else:
            result += char

    return result

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception("Invalid number of arguments")

    mode = sys.argv[1]
    if mode not in ["encode", "decode"]:
        raise Exception("Invalid mode. Use 'encode' or 'decode'.")

    text = sys.argv[2]

    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer.")
    print(caesar_cipher(text, shift, mode))
