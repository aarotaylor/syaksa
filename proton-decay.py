# Proton Decay script for later...
# TODO: have the lines render like they're being typed, sequentially instead of just appearing all at once

import time

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd) # have the percentage become more corrupt over time
    # https://github.com/combatwombat/Lunicode.js this repo, but it is for js
    # Print New Line on Complete
    if iteration == total: 
        print()


def deltaTime(start, era, isStart=False):
    end = time.time()
    diff = end-start
    if (isStart):
        print(f'{diff:3.7}', "..: "+era)
    else:
        print(f'{diff:3.7}', "End: "+era)


def bar(title="Loading...", prefix="", suffix="", list=list(range(0, 51)), int_one=1.7, int_two=0.1):
    
    l = len(list)
    time_passed = l

    print(title)
    # Initial call to print 0% progress
    printProgressBar(0, l, prefix = prefix, suffix = suffix, length = 50)
    time.sleep(int_one)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(int_two)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = prefix, suffix = suffix, length = 50)
    print()
    print()

# -----------------------------------------------------------------------------

print("---------------------------------------------------------")
print("Initiate Simulation: Proton Decay")
print("---------------------------------------------------------")




time.sleep(2)

print(".......")

constants = "...Constants"




start = time.time()
# A List of Items
items = list(range(0, 51))
l = len(items)
time_passed = l

bar("Loading: Constants", "Entropic Maximum", "Entropic Minimum", items, 1.7, 0.1)

# print("Loading.....Constants")
# # Initial call to print 0% progress
# printProgressBar(0, l, prefix = 'Entropic Maximum:', suffix = 'Entropic Minimum', length = 50)
# time.sleep(1.7)
# for i, item in enumerate(items):
#     # Do stuff...
#     time.sleep(0.1)
#     # Update Progress Bar
#     if (i%4):
#         i+=6
#     printProgressBar(i + 1, l, prefix = 'Entropic Maximum:', suffix = 'Entropic Minimum', length = 50)
# print()
# print()

#time_remaining = time_passed*time_passed

items = list(range(0, 5))
bar("Loading: Force Carriers", "Field Saturation", "", items, 0.27, 2.3)
# print("Loading.....Force Carriers")
# time.sleep(0.27)
# # Initial call to print 0% progress
# printProgressBar(0, 5, prefix = 'Field Saturation', length = 50)
# for i, item in enumerate(items):
#     # Do stuff...
#     time.sleep(2.3)
#     # Update Progress Bar
#     printProgressBar(i+1, 5, prefix = 'Field Saturation', length = 50)
# print()
# print()

time_passed += 5
items = list(range(0, 4))
bar("Loading: Thermodynamics", "Field Saturation", "", items, 0.27, 2.3)
# print("Loading.....Thermodynamics")
# time.sleep(0.27)
# # Initial call to print 0% progress
# printProgressBar(0, 4, prefix = 'Field Saturation', length = 50)
# for i, item in enumerate(items):
#     # Do stuff...
#     time.sleep(1.3)
#     # Update Progress Bar
#     printProgressBar(i+1, 4, prefix = 'Field Saturation', length = 50)
# print()
    
# ~42 seconds should have passed after instantiation
deltaTime(start, "Inflation Initiated", True)
start = time.time()
# End Stelliferous Era | ~42 seconds should have passed
deltaTime(start, "Stelliferous Era")
# End Degenerate Era | ~43 seconds should have passed
deltaTime(start, "Degenerate Era")
# End Darkness Abounds| ~42 seconds should have passed
deltaTime(start, "Darkness Abounds")
# End A Peculiar Process | ~47 seconds should have passed
deltaTime(start, "A Peculiar Process")
# End Battle Against Oblivion | ~18 seconds should have passed
deltaTime(start, "Battle Against Oblivion")
# End Rudderless in the Night | ~21 seconds should have passed
deltaTime(start, "Rudderless in the Night")
# Signal Echoes | leave the total running higher
deltaTime(start, "Signal Echoes -..--..-..---.-..-") # turn this into some morse code message, or binary
# ~42 seconds should have passed