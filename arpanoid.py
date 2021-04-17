import sys
import re
import random

def valid(action):
    regex = re.compile('!([1-9]\d*)*[dD][1-9]+\d*')
    return regex.match(action.strip()) 

def err_msg(user_input):
    return 'invalid input: {} | usage examples: !d20, !1d6, !4d8'.format(user_input)

def parse_params(action):
    params = action.partition('d') 
    throws = params[0] or 1
    die = params[2]

    return (int(throws), int(die))

def result(action, rolls):
    if len(rolls) == 1:
        return '{}: {}'.format(action, str(rolls[0]))

    total = sum(rolls)
    rolls = ', '.join(str(roll) for roll in rolls)

    return '{}: rolls: {} | total: {}'.format(action, rolls, total)

def roll(throws, die):
    rolls = []

    for throw in range(throws):
        rolls.append(random.randint(1, die))

    return rolls

def initiate(action):
    if not valid(action):
        return err_msg(action)
    
    action = action[1:].lower()
    (throws, die) = parse_params(action)
    
    rolls = roll(throws, die)

    return result(action, rolls)


cli_input = sys.argv[1:]

for arg in cli_input:
    print(initiate(arg))
