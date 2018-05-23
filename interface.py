import time

sleep = time.sleep


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def logo():
    prRed('   _____________ ')
    sleep(0.1)
    prRed('  | ____________|')
    sleep(0.1)
    prRed('  | |')
    sleep(0.1)
    prRed('  | |')
    sleep(0.1)
    prCyan('  | |')
    sleep(0.1)
    prCyan('  | |   ')
    sleep(0.1)
    prCyan('  | |    _______    _________   _          _')
    sleep(0.1)
    prCyan('  | |   |  ___  |  |  _____  | \ \        / /')
    sleep(0.1)
    prCyan('  | |   | |   | |  | |     | |  \ \      / /')
    sleep(0.1)
    prCyan('  | |   | |   | |  | |     | |   \ \    / /')
    sleep(0.1)
    prGreen('  | |___| |   | |  | |_____| |    \ \__/ /')
    sleep(0.1)
    prGreen('  |_______|   | |  |_________|     \____/')
    sleep(0.1)
    prGreen('              | |')
    sleep(0.1)
    prGreen('              | |')
    sleep(0.1)
    prGreen('              |_|')

def input_profile():
    print('Choose a profile')
    prRed('1 - Battery')
    prCyan('2 - Balanced')
    prGreen('3 - Performance')
    choice = input('> ')
    return choice 
