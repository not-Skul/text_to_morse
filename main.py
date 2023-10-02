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
}


def split(word):
    return list(word)


def converter():
    word = input('please input your word to be converted: ').upper()
    for w in word:
        print(f"{w}: {morse_dict[w]}")


converter()

