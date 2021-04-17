import sys
import re
import random

def validate(dice):
    regex = re.compile('([1-9]\d*)*[dD][1-9]+\d*')

    if not regex.match(dice.strip()):
        raise Exception('Malformatted command')

    (throws, die) = parse_params(dice.lower())

    if throws > 10:
        raise Exception('Cannot compute that many throws')

    if die not in [4, 6, 8, 10, 12, 20, 100]:
        raise Exception('Invalid die. Valid dice: 4, 6, 8, 10, 12, 20, 100')
    
    return True 

def err_msg(err):
    return '_invalid input_```{}\n\nUse !help for details.```'.format(err)

def info_msg():
    return ('```ARPANOID (BETA)\nautomatic dice roller\n\n'
           'usage:\n!roll <throws>d<die>\n\n' 
           'e.g:\n!roll d20\n!roll 1d6\n!roll 3d4\n\n'
           'accepted throws: 1-10\naccepted dice:\n4, 6, 8, 10, 12, 20, 100```')

def parse_params(dice):
    params = dice.partition('d') 
    throws = params[0] or 1
    die = params[2]

    return (int(throws), int(die))

def result(action, rolls):

    total = sum(rolls)
    rolls = ' '.join('[{}]'.format(str(roll)) for roll in rolls)

    return '**{}**:```rolls: {}\ntotal: {}```'.format(action, rolls, total)

def get_rolls(throws, die):
    rolls = []

    for throw in range(throws):
        rolls.append(random.randint(1, die))

    return rolls

def roll(dice):
    try:
        validate(dice)
    except Exception as err:
        return err_msg(err)
    
    dice = dice.lower()
    (throws, die) = parse_params(dice)
    
    rolls = get_rolls(throws, die)
    return result(dice, rolls)


cli_input = sys.argv[1:]

for arg in cli_input:
    print(roll(arg))
