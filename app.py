"""
Eric Tolson
Project for CS361
CLI app that generates BJJ technique based on user input.
"""
import json
from time import sleep

# constants for file references
JSON_FILE = 'techniques.json'
TXT_FILE = 'technique.txt'

# game intro
introduction = "\nHi! Thank you for using BJJ Technique Generator"
instructions = "\nDon't know what to focus on? You will be asked three questions and \
a technique will be generated based on your answers."

# user prompts for data
game_prompt = "\nWhat kind of game do you want to play? Please enter 'top', 'bottom',\
or 1 to learn more: "
position_prompt = """\nWhat position do you want to work on? Please enter 'neutral', 'side mount', \
'mount', 'rear mount', or 1 to learn more: """
skill_prompt = "\nWhat is your skill level? Please enter 'beginner', 'intermediate', 'advanced',\
 or 1 to learn more: "
energy_prompt = "\nWhat is your energy level? Please enter 'high', 'low', or 1 to learn more: "
redo_prompt = "\nWould you like to re-enter your choices? PLease enter 'yes' or 'no': "
learn_prompt = "\nWould you like to learn more about this technique? PLease enter 'yes' or 'no': "
reset_prompt = "\nWould you like to generate a different technique? Please enter 'yes' or 'no': "
techniques_prompt = "\nWould you like to view all techniques? Please enter 'yes' or 'no': "

# information on user prompts
game_info = """\nIf you want to work on passing or top control or submissions, enter 'top'.
If you want to work on sweeping, bottom escapes or submissions, enter 'bottom'.\
\n\nPlease enter 'top' or 'bottom': """
position_info = """\nIf you want to work on your guard or passing, enter 'neutral'.\
\n'side mount' is when the top player is passed the guard and \
controlling from the side.\n'mount' is when the top player is controlling on top of \
the bottom.\n'rear mount' is when the top player is controlling the bottom player \
from the back. \n\nPlease enter 'neutral', 'side mount', 'mount', or 'rear mount': """
skill_info = """\nIf you have been training for less than 2 years, enter 'beginner'.\
\nIf you have been training for 2-4 years, enter 'intermediate'.\
\nIf you have been training for more than 4 years, enter 'advanced'.\
\n\nPlease enter 'beginner', 'intermediate', or 'advanced': """
energy_info = """\nIf you are fatigued, enter 'low'.\
\nIf you fell normal, enter 'high'.\
\n\nPlease enter 'low' or 'high': """


# user input functions
def get_game_input() -> str:
    """
    Gets 'game' input from user/
    :return: string with input
    """
    game_type = input(game_prompt)
    if game_type == "1":
        game_type = input(game_info)
    while game_type.lower() != "top" and game_type.lower() != "bottom":
        game_type = input("Please enter 'top' or 'bottom': ")
    return game_type

def get_position_type()-> str:
    """
    Gets position input from user/
    :return: string with input
    """
    position_type = input(position_prompt)
    if position_type == "1":
        position_type = input(position_info)
    while position_type.lower() != 'neutral' and position_type.lower() != 'side mount' \
        and position_type.lower() != 'mount' and position_type.lower() != 'rear mount':
        position_type = input("Please enter 'neutral', 'side mount', 'mount', or 'rear mount': ")
    return position_type


def get_skill_level() -> str:
    """
    Gets get skill level input from user
    :return: string with input
    """
    skill_level = input(skill_prompt)
    if skill_level == "1":
        skill_level = input(skill_info)
    while skill_level.lower() != 'beginner' and skill_level.lower() != 'intermediate'\
         and skill_level.lower() != 'advanced':
        skill_level = input("Please enter 'beginner', 'intermediate', or 'advanced': ")
    return skill_level


def choice_display(game, position, skill) -> None:
    """
    Print user input to console.
    :param: user input strings
    """
    print(f"\nYour input:\n \nGame Type: {game}\nPosition: {position}\nSkill Level: {skill}\n")


def get_redo() ->int:
    """
    If user wants to redo input
    :return: 1 or 2 for redo logic in main
    """
    redo_choice = input(redo_prompt)
    while redo_choice.lower() != "yes" and redo_choice.lower() != "no":
        redo_choice = input("Please enter 'yes' or 'no': ")
    if redo_choice.lower() == "yes":
        return 1
    else:
        return 2


def view_all() ->None:
    """
    Display technique names if user wants
    """
    view_choice = input(techniques_prompt)
    while view_choice.lower() != "yes" and view_choice.lower() != "no":
        view_choice = input("Please enter 'yes' or 'no': ")
    if view_choice == 'yes':
        with open(JSON_FILE, 'r') as infile:
            techniques = json.load(infile)

        for key_val in techniques:
            print(key_val['name'])


def get_reset() -> int:
    """
    If user wants to reset app
    :return: 1 or 2 for reset logic in main
    """
    reset_choice = input(reset_prompt)
    while reset_choice.lower() != "yes" and reset_choice.lower() != "no":
        reset_choice = input("Please enter 'yes' or 'no': ")
    if reset_choice.lower() == "yes":
        return 1
    else:
        return 2


def technique_search(game, position, skill) -> str:
    """
    Reads json file and returns technique name based on user input
    :param: user input strings
    :return: technique name as string
    """
    with open(JSON_FILE, 'r') as infile:
        techniques = json.load(infile)

    for key_val in techniques:
        if game == key_val['game']:
            if position == key_val['position']:
                if skill == key_val['skill']:
                    return key_val['name']


def learn_more(technique) -> None:
    """
    Communicates with microservice.py to generate youtube video if needed
    :param: technique name as string
    """
    learn_choice = input(learn_prompt)
    while learn_choice.lower() != "yes" and learn_choice.lower() != "no":
        learn_choice = input("Please enter 'yes' or 'no': ")
    if learn_choice == "yes":
        with open(TXT_FILE, 'w') as outfile:
            outfile.write(technique)
    sleep(1)
    with open(TXT_FILE, 'w') as outfile:
            outfile.write('QUIT')

def main():
    print(introduction)
    print(instructions)

    # optional full reset cycling
    full_reset = 0
    while full_reset == 0 or full_reset == 1:

    # optional input cycling
        redo = 0
        while redo == 0 or redo == 1:

        # get user input
            game_input = get_game_input()
            position_input = get_position_type()
            skill_input = get_skill_level()

        # display user input
            choice_display(game_input, position_input, skill_input)

        # ask user if they would like to re-enter data
            if redo == 0:
                redo = get_redo()
            else:
                redo = 2
        # display technique chosen from db based on user input
        technique_choice = technique_search(game_input.lower(), position_input.lower(), skill_input.lower())
        print("\nYour technique for today is: " + technique_choice)

    # ask user if they would like to see all techniques
        view_all()

    # ask user if they want full reset
        if full_reset == 0:
            full_reset = get_reset()
        else:
            full_reset = 2

    # ask user if they want to learn more
    learn_more(technique_choice)


if __name__ == "__main__":
    main()
