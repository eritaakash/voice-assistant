import random
from datetime import datetime

def get_current_time():
    time = datetime.now()

    hour = time.hour
    minute = time.minute
    period = ''

    if 5 <= hour < 12: period = 'morning'
    elif 12 <= hour < 17: period = 'afternoon'
    elif 17 <= hour < 21: period = 'evening'
    else: period = 'night'

    adjectives = {
        'morning': [ 'Bright', 'Fresh', 'Crisp' ],
        'evening': [ 'Warm', 'Golden', 'Peaceful' ],
        'afternoon': [ 'Lazy', 'Long', 'Slow' ],
        'night': [ 'Dark', 'Quiet', 'Peaceful' ]
    }

    if period in [ 'afternoon', 'evening', 'night' ]:
        hour = 24 - hour

    return f"Currently, it's a {adjectives[period][random.randint(0, 2)]} {period}, at {hour} O' {minute}"

def evaluate (instruction):
    exp = instruction.lower().split('evaluate ')[1]
    
    exp = exp.replace('time', '*')
    exp = exp.replace('times', '*')
    exp = exp.replace('x', '*')

    answer = ''
    response = ''

    try:
        answer = eval(exp)
    except:
        answer = '?'


    if answer == '?':
        response = f"Sorry, I couldn't evaluate {exp}. Consider replacing phrases like 'times' with 'multiplied by'. Also, I can't evaluate complex expressions."
    else:
        response = f"The answer to {exp} is {answer}"

    response = response.replace('*', 'multiplied by')
    response = response.replace('/', 'divided by')

    return response