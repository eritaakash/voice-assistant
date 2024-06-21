from helpers.vitals import init, listen
from helpers.helper import detect_and_respond

def main():
    init()

    while True:
        instruction = listen()
        detect_and_respond(instruction)

if __name__ == '__main__':
    main()