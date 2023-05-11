def main():
    frase = input()
    print(convert(frase))


def convert(emoji):
    if ":)" in emoji or ":(" in emoji:
        emoji = emoji.replace(":)","🙂")
        emoji = emoji.replace(":(","🙁")
    return emoji

main()