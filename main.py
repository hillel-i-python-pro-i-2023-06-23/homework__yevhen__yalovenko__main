# ~*~ coding: utf-8 ~*~

import random
import sys


config = {
    "gamers": None,
}

user_config_template = {
    "total_points": 100,
    "correct_answers": 0,
    "first_match": 0
}


def welcome_page() -> None:
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

def number_input(message:str) -> int:
    """
    Request for number. Check entered data validity
    and re-asking input if data not valid
    """
    amount = input(message)

    result = None
    while result:
        try:
            int_amount = int(amount)
            result = True
            return int_amount
        except ValueError as e:
            print("Error! Please, specify a number!")


def gamers_amount() -> bool:
    """
    Save the number of gamers to config
    """
    number_of_gamers = number_input(
            "Please, specify the number of gamers: "
        )

    try:
        gamers = config.get("gamers")
    except KeyError as e:
        print("ERROR! Config doesn't have key 'gamers'!")
        return None

    if gamers == None:
        config["gamers"] = number_of_gamers
        return True
    else:
        if type(config["gamers"]) == int:
            return True
        else:
            print("ERROR! Config parameter \"gamers\" have no valid value!")
            return False

def gamers_usernames(gamers_amount:int) -> dict:
    """
    This function ask users to their usernames and save data to config
    :param gamers_amount: Number of gamers
    :return: Dict with saved usernames
    """

    def check_username_availability(username:str) -> bool:
        result = config.get(username)
        if result == None:
            return True
        else:
            return None

    number_of_gamer = 1
    while number_of_gamer >= gamers_amount:
        welcome_message = "Please, enter the username for {} gamer".format(
            number_of_gamer
        )
        username = input(welcome_message)

        if check_username_availability(username):
            config[username] = user_config_template
        else:
            print("ERROR! Username {} has already exists!".format(
                username
                )
            )

        number_of_gamer += 1

def generate_numbers():
    gener_number = random.randint(0, 100)
    return gener_number


def comparing_numbers() -> int:
    """
    Сompares the user's numbers and the generated numbers to determine the user's score
    :param gener_number: The entered number and the generated number
    :return: Players result
    """
    result = 100
    while result > 0:
        user_num = int(input(
            "Please, specify the magic number: "
        ))
        gener_number = generate_numbers()
        if user_num > gener_number:
            print(f"Sorry, not match. God of random threw out the number {gener_number}"
                  f" Try a smaller number")
            result -= 20
        elif user_num < gener_number:
            print(f"Sorry, not match. God of random threw out the number {gener_number}"
                  f" Try a larger number")
            result -= 20
        else:
            print("You lucky!")
            break

    return result


if __name__ == '__main__':
    welcome_page()
    gamers_amount()
    #gamers_usernames(config.get("gamers"))

    comparing_numbers()
