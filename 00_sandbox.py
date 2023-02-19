import random

def scramble_text(text):
    words = text.split()
    scrambled_words = []
    for word in words:
        if len(word) > 3:
            mid = list(word[1:-1])
            random.shuffle(mid)
            scrambled_word = word[0] + ''.join(mid) + word[-1]
        else:
            scrambled_word = word
        scrambled_words.append(scrambled_word)
    return ''.join(scrambled_words)

text = scramble_text("this is a test for letter scramble")
print(text)
