# Python program to print
# colored text and background
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

prRed('   _____________ ')
prRed('  | ____________|')
prRed('  | |')
prRed('  | |')
prCyan('  | |')
prCyan('  | |   ')
prCyan('  | |    _______    _________   _          _')
prCyan('  | |   |  ___  |  |  _____  | \ \        / /')
prCyan('  | |   | |   | |  | |     | |  \ \      / /')
prCyan('  | |   | |   | |  | |     | |   \ \    / /')
prGreen('  | |___| |   | |  | |_____| |    \ \__/ /')
prGreen('  |_______|   | |  |_________|     \____/')
prGreen('              | |')
prGreen('              | |')
prGreen('              |_|')

def file_contents(x, y):
   a = open(x, "r")
   b = a.read()
   y = b.split()
   return(y)
   x.close()
   del a, b, y

little_freq = (file_contents("/sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies", "z"))

little_gov = (file_contents("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor", "z"))

big_freq = (file_contents("/sys/devices/system/cpu/cpu2/cpufreq/scaling_available_frequencies", "z"))

big_gov = (file_contents("/sys/devices/system/cpu/cpu2/cpufreq/scaling_governor", "z"))



import os
little_gov_dir = "/sys/devices/system/cpu/cpu0/cpufreq/%s" % little_gov
little_tunables = (os.listdir(little_gov_dir))
print(little_tunables)
#little cpu governor tunables are stored in 'little_tunables'

import os
big_gov_dir = "/sys/devices/system/cpu/cpu2/cpufreq/%s" % big_gov
big_tunables = (os.listdir(big_gov_dir))
print(big_tunables)
#big cpu governor tunables are stored in 'big_tunables'


#TO-DO Write the above stuff in functions




