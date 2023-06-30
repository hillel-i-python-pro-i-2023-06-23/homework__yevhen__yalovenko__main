import random
import emoji

winner = []


def welcome_message():
    message = """
       We happy to see you in our greatest game "GUESS THE NUMBER"!
       Rules very easy: 
       You must to guess the number from 0 to 100.
       You have 7 attempts!
       If you're enter non correct number - game inform about it.
       You have 140 points at start and wrong attempt cost -20 point.
       Good luck!!!
       """
    print(message)


def validate_number(number):
    """
    This function check user input and return integer if input is number
    or Error text
    :param number: user input
    :return: int or None
    """

    while True:
        try:
            validated_number = int(number)
            return validated_number
        except ValueError:
            print("Please enter a number, not a letter or symbol.")
            number = input("Enter a valid number: ")


def generate_numbers():
    gener_number = random.randint(0, 100)
    return gener_number


def comparing_numbers(player_name):
    """
    Compares the user's numbers and the generated numbers to determine the user's score

    """
    result = 140
    tries = 7
    generated_number = generate_numbers()

    while tries > 0:
        user_number = validate_number(input(f"Please, {player_name} specify the magic number: "))

        if user_number is None:
            continue
        elif user_number > generated_number:
            print("Sorry, it's not a match. The random god is not on your side."
                  " Try a smaller number.")
            result -= 7
            tries -= 1
        elif user_number < generated_number:
            print("Sorry, it's not a match. The random god is not on your side."
                  " Try a larger number.")
            result -= 7
            tries -= 1
        else:
            win_tries: int = 8 - tries
            print(f"{emoji.emojize(':star-struck:')} You're lucky! {emoji.emojize(':star-struck:')} "
                  f"You guessed it right in {win_tries} tries.")
            return winner.append({'Player': player_name.upper(), 'Tries': win_tries, 'Result': result})

        if tries == 0:
            print(f"GAME OVER, {player_name}! Try your luck another time. {emoji.emojize(':winking_face:')}")


def unpack_winner(winner_list):
    for el in winner_list:
        print(f"Our {winner_list.index(el) + 1} winner is:")
        for k, v in el.items():
            print(k, v)


def start_game(players_num):
    """
    Check number of players and change turn when one player guessed number
    or ran out of tries
    :param players_num: number of players (int)
    """
    players = []

    for i in range(1, players_num + 1):
        players_name = input(f"Enter nickname of Player {i}: ")
        players.append(players_name)

    current_player = 0

    while True:
        comparing_numbers(players[current_player])

        current_player = (current_player + 1) % players_num

        if current_player == 0:
            break


if __name__ == '__main__':
    welcome_message()
    players_num = validate_number(input("Please enter the number of players: "))

    if players_num is not None:
        start_game(players_num)

    unpack_winner(winner) if len(winner) > 0 else print("No winners today")
