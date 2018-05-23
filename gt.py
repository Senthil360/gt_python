import interface as inter
import os

def file_contents(x, y):
   a = open(x, "r")
   b = a.read()
   y = b.split()
   return(y)
   x.close()
   del a, b, y


little_freq = (file_contents("work/sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies", "z"))

little_min_freq = (little_freq[0])
little_max_freq = (little_freq[-1])

little_gov = (file_contents("work/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor", "z"))

big_freq = (file_contents("work/sys/devices/system/cpu/cpu2/cpufreq/scaling_available_frequencies", "z"))

big_min_freq = (big_freq[0])
big_max_freq = (big_freq[-1])

big_gov = (file_contents("work/sys/devices/system/cpu/cpu2/cpufreq/scaling_governor", "z"))

little_gov_dir = "work/sys/devices/system/cpu/cpu0/cpufreq/%s" % "".join(little_gov)
little_tunables = (os.listdir(little_gov_dir))
#little cpu governor tunables are stored in 'little_tunables'

big_gov_dir = "work/sys/devices/system/cpu/cpu2/cpufreq/%s" % "".join(big_gov)
big_tunables = (os.listdir(big_gov_dir))
#big cpu governor tunables are stored in 'big_tunables'

inter.logo()

a = inter.input_profile()
if a == '1':
    fn1()
elif a == '2':
    fn2()
elif a == '3':
    fn3()

