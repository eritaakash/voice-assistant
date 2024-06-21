from .assist import get_current_time, evaluate
from .vitals import speak

def detect_and_respond (instruction):

    if "the current time" in instruction.lower():
        response = get_current_time()
        speak(response)

    elif 'evaluate' in instruction.lower():
        response = evaluate(instruction)
        speak(response)

    else:
        speak("I'm sorry, I don't understand that command.")