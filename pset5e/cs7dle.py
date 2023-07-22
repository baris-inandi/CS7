"""
A wordle-like game that is almost done. See https://www.nytimes.com/games/wordle/index.html for the rules
Your goal is to complete the functions update_state and evaluate_guess to make the game work.
YOU SHOULD ONLY MAKE CHANGES TO THESE TWO FUNCTIONS!
"""
import random
import termcolor
import cs7dle_data

# Only words of length 5 supported
MAX_GUESSES = 6
WORD_LENGTH = 5

# GAME STATES
PLAYING = 0
WON = 1
LOST = 2

# CHARACTER SCORES
NOT_GUESSED = -1
WRONG = 0
ELSEWHERE = 1
MATCHES = 2

ALPHABET = "abcdefghijklmnopqrstuvwxyz "
INDENT = "     "


def score_to_color(score):
    """The colors to use for displayed letters"""
    if score == WRONG:
        return "grey"
    if score == ELSEWHERE:
        return "yellow"
    if score == MATCHES:
        return "green"
    return "white"


def set_color(string, color):
    """
    Adds invisible color control characters to a string so it
    prints with the specified color.
    Valid values for color are
    'grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
    See https://pypi.org/project/termcolor/
    for documentation on termcolor
    """
    return termcolor.colored(string, color, attrs=["bold"])


def print_word(word, colors):
    """
    Prints a word using the array of colors specified
    for each character. colors must be the same length as word
    """
    print(INDENT, end="")
    for i in range(len(word)):
        c = set_color(word[i], colors[i])
        print(f"{c} ", end="")
    print()


def print_keyboard(keyboard_state):
    """
    Prints the keyboard, coloring keys that
    have been guessed.
    """
    ROW1 = "qwertyuiop"
    ROW2 = "asdfghjkl"
    ROW3 = " zxcvbnm"
    for row in (ROW1, ROW2, ROW3):
        print(INDENT, end="")
        for c in row:
            color = score_to_color(keyboard_state[c])
            print(set_color(c, color), end="")
        print()

def print_debug_info(game_state):
    print("\n{")
    for key, value in game_state.items():
        print("    ", key, " : ", value, ",", sep='')
    print("}")

def update_display(game_state):
    """Reprints the display based on the current state"""
    # uncomment this to see the current state too.
    # print_debug_info(game_state)
    guess_list = game_state["guess_list"]
    score_list = game_state["score_list"]
    secret_word = game_state["secret_word"]
    print()
    for guess, scores in zip(guess_list, score_list):
        print_word(guess, [score_to_color(a) for a in scores])
    for i in range(MAX_GUESSES - len(guess_list)):
        print_word("_" * WORD_LENGTH, ["white"] * WORD_LENGTH)
    print()
    print_keyboard(game_state["keyboard_state"])
    print()
    if game_state["stage"] == WON:
        print("You guessed it!!")
    elif game_state["stage"] == LOST:
        print(f"You lose! The word was {secret_word}")


def is_valid_guess(guess):
    """Makes sure guess is an allowed one"""
    if len(guess) != WORD_LENGTH:
        print(f"The word must be {WORD_LENGTH} letters long!")
        return False
    # These lists are disjoint, so need to check both. valid_words is really
    # valid_words that are not possible answers.
    if (
        guess not in cs7dle_data.valid_words
        and guess not in cs7dle_data.possible_answers
    ):
        print(f"The word {guess} is not a valid word!")
        return False
    return True


def update_keyboard_state(keyboard_state, guess, scores):
    """
    Updates the colors of the keyboard based on the current
    guess and how it scored.
    """
    for i in range(len(guess)):
        keyboard_state[guess[i]] = max(keyboard_state[guess[i]], scores[i])


def evaluate_guess(secret_word, next_guess):
    """
    Returns a list scoring each character in the guess
    as a MATCH, WRONG, or a match ELSEWHERE in the secret word
    Careful:
    For example, for guess STUNS and secret BRATS
    the last char should match and the first one
    should not be an ELSEWHERE since there are not two S characters
    in the secret word.
    """
    # ADD YOUR CODE HERE


def update_state(game_state, next_guess):
    """
    Update the game state given the next guess.
    Evaluates the guess against the secret word.
    Calls update on the keyboard state.
    Checks for a win or loss.
    Updates the letters seen.
    """
    # ADD YOUR CODE HERE


def print_intro():
    print("Welcome to cs7dle")
    print("Guess the secret word!")
    green = set_color("Green", "green")
    yellow = set_color("Yellow", "yellow")
    grey = set_color("Grey", "grey")
    print(f"{green} letters are in the correct spot.")
    print(f"{yellow} letters are in the word, but in the wrong spot.")
    print(f"{grey} letters are not in the word.")


def init():
    game_state = {}
    game_state["stage"] = PLAYING
    game_state["secret_word"] = random.choice(cs7dle_data.possible_answers)
    game_state["guess_list"] = []
    game_state["score_list"] = []
    game_state["seen_letters"] = set()
    game_state["keyboard_state"] = {c: NOT_GUESSED for c in ALPHABET}
    return game_state


def main():
    print_intro()
    game_state = init()

    update_display(game_state)
    while game_state["stage"] == PLAYING:
        next_guess = input("Please enter a five letter word: ").lower()
        if is_valid_guess(next_guess):
            update_state(game_state, next_guess)
        update_display(game_state)


if __name__ == "__main__":
    main()
