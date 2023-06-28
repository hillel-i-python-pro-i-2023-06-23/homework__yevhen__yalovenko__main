import random
import emoji


def welcome_message():
    message = """
       We happy to see you in our greatest game "GUESS THE NUMBER"!
       Rules very easy: 
       You must to guess the number from 0 to 100.
       You have 5 attempts!
       If you're enter non correct number - game inform about it.
       You have 100 points at start and wrong attempt cost -20 point.
       Good luck!!!
       """
    print(message)


def validate_number(number):
    """
    This function check user input and return integer if input is number
    or Error text
    :param number: user input
    :return: int or Error text
    """

    try:
        validated_number = int(number)
        return validated_number
    except ValueError as e:
        print("Please enter the number, not literal")
        return e


def generate_numbers():
    gener_number = random.randint(0, 5)
    return gener_number


def comparing_numbers(player_name):
    """
    Compares the user's numbers and the generated numbers to determine the user's score

    """
    result = 100
    tries = 5
    gener_number = generate_numbers()

    while result > 0:
        user_num = validate_number(input(f"Please, {player_name} specify the magic number: "))

        if type(user_num) == ValueError:
            continue
        elif user_num > gener_number:
            print(f"Sorry, not match. God of random not on your side"
                  f" Try a smaller number")
            result -= 20
            tries -= 1
        elif user_num < gener_number:
            print(f"Sorry, not match. God of random not on your side"
                  f" Try a larger number")
            result -= 20
            tries -= 1
        else:
            win_tries = 6 - tries
            print(f"{emoji.emojize(':star-struck:')} You lucky! {emoji.emojize(':star-struck:')} "
                  f"You guessed it, it's in {win_tries} tries")
            break
    if result <= 0:
        print(f"GAME OVER {player_name}! Try your luck another time {emoji.emojize(':winking_face:')}")


def start_game(players_num):
    """
    Check number of players and change turn when one player guessed number
    or ran out of tries
    :param players_num: number of players (int)
    """
    players = []
    current_player = 0

    for i in range(1, players_num + 1):
        players_name = input(f"Enter nickname of Player {i}: ")
        players.append(players_name)

    while True:
        num_players = len(players)
        current_player = (current_player + 1) % num_players
        comparing_numbers(players[current_player])

        if current_player == 0:
            break


if __name__ == '__main__':
    welcome_message()
    players_num = validate_number(input("Please enter the number of players: "))
    start_game(players_num)
