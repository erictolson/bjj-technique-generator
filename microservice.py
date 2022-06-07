"""
Lucas Jensen
Microservice for CS361
Watched a txt file and opens a YouTube video when prompted
"""
import webbrowser
from time import sleep

FILENAME = 'technique.txt'


def get_contents() -> str:
    """
    Opens FILENAME and reads the contents
    :return: the contents of the file
    """
    with open(FILENAME, 'rt') as infile:
        text = infile.read()

    return text


def clear_file() -> None:
    """
    Clears the contents
    :return: nothing
    """
    with open(FILENAME, 'wt') as outfile:
        outfile.truncate(0)


def main() -> None:
    """
    Opens YouTube based on contents provided in a txt file
    :return: nothing
    """
    previous = get_contents()
    while True:
        curr = get_contents()

        if previous != curr:
            if curr == 'QUIT':
                clear_file()
                break
            webbrowser.open(f'http://www.youtube.com/results?search_query={curr}')
            sleep(0.25)
            clear_file()
            previous = get_contents()

        sleep(0.25)


if __name__ == "__main__":
    print(f'watching {FILENAME} . . .')
    main()