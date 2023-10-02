# TODO: A text-based Python program to convert Strings into Morse Code.
morse_dict = {
    'A': '.-',
    'B': '-···',
    'C': '−·−·',
    'D': '−··',
    'E': '·',
    'F': '··−·',
    'G': '−−·',
    'H': '····',
    'I': '··',
    'J': '·−−−',
    'K': '−·−',
    'L': '·−··',
    'M': '−−',
    'N': '−·',
    'O': '−−−',
    'P': '·−−·',
    'Q': '−−·−',
    'R': '·−·',
    'S': '···',
    'T': '−',
    'U': '··−',
    'V': '···−',
    'W': '·−−',
    'X': '−··−',
    'Y': '−·−−',
    'Z': '−−··',
    ' ': ' ',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·',
}


def split(word):
    return list(word)


def converter():
    word = input('please input your word to be converted: ').upper()
    for w in word:
        if morse_dict[w] == ' ':
            print('\n')
        else:
            print(f"{w}: {morse_dict[w]}")


converter()

