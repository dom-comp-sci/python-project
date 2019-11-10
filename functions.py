

# Function: Print When Debug Set
def printDebug (message):

    if (DEBUG):

        print (message)

# end function

# Function: Changes 24hour time to 12 hour time
def time24to12 (h24,mins):

    if (h24 == 0):

        h12 = 12
        suff = "am"
        printDebug ("Special case h12 = 12, suff = am")

    elif (h24 == 12):

        h12 = 12
        suff = "pm"
        printDebug("Special case h12 = 12, suff = pm")

    elif (h24 > 12):

        h12 = h24 - 12
        suff = "pm"

    else:
        h12 = h24
        suff = "am"

    return("%2d:%02d %s" % (h12, mins, suff))

# end function



# Main Program Code

DEBUG = False

for h in range(24):
    printDebug(h)
    for m in range(60):
        printDebug (m)
        time24 = ("%02d%02d" % (h, m))
        time12 = time24to12 (h, m)
        print (time24, time12)

        #print("%2d:%02d %s" % (h12, mins, suff))