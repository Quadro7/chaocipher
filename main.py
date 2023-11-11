from const import LOGO, LEFT_DISK, RIGHT_DISK
from copy import deepcopy

def rotate(arr, n):
    return arr[-n:] + arr[:-n]

def chaocipher(text: str, mode: str):
    rd = deepcopy(RIGHT_DISK)
    ld = deepcopy(LEFT_DISK)
    result = ""
    for symbol in text:
        if symbol.lower() in RIGHT_DISK:
            if mode == 'e' or mode == 'encode':
                index = rd.index(symbol.lower())
                if symbol.isupper():
                    result += ld[26 - index].upper()
                else:
                    result += ld[26 - index]
            else:
                # Decryption
                index = ld.index(symbol.lower())
                if symbol.isupper():
                    result += rd[-index].upper()
                else:
                    result += rd[-index]
            # Disk permutation
            removed_letter = ld.pop(-1)
            ld.insert(13, removed_letter)
            rotate(rd, -1)
            removed_letter = rd.pop(2)
            rd.insert(13, removed_letter)
        else:
            result += symbol
    return result


if __name__ == "__main__":
    while True:
        print(LOGO)
        answerMode = input("[e]ncode or [d]ecode? ").lower()
        if answerMode not in 'de' or answerMode not in 'decodeencode':
            continue
        answerText = input(f"Enter text to {'cipher' if answerMode == 'e' or answerMode == 'encode' else 'decipher'}: ")
        cipher = chaocipher(answerText, answerMode)
        print(f"Here is ciphered text: {cipher}")
        runAgain = input("Run again? [y]es or [n]o: ").lower()
        if runAgain == 'n' or runAgain == 'no':
            break