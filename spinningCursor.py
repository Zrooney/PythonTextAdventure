#code from Damien, modified slightly
#https://stackoverflow.com/questions/4995733/how-to-create-a-spinning-command-line-cursor-using-python

import itertools, sys
spinner = itertools.cycle(['\\', '-', '|', '/', '-', '|', ])
while True:
    sys.stdout.write(next(spinner))  # write the next character
    sys.stdout.flush()       #need to flush+1         # flush stdout buffer (actual character display)
    sys.stdout.write('\r')          #carriage return