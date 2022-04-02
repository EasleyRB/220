from random import randint


def get_words(file_name):
    file_name = open(file_name, 'r')
    words = file_name.readlines()
    return words


def get_random_word(words):
    random_word = randint(0, len(words) - 1)
    secret_word = words[random_word].strip('\n')
    return secret_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    return False


def make_hidden_secret(secret_word, guesses):
    word = ''
    for letter in secret_word:
        if letter in guesses:
            word = word + letter + ' '
        else:
            word = word + '_ '
    guessed_word = word.strip()
    return guessed_word


def won(guessed):
    guessed = guessed.split(' ')
    not_guessed = guessed.count('_')
    if not_guessed == 0:
        return True
    return False


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    words = get_words("words.txt")
    secret_word = get_random_word(words)


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
