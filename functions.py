

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

# Function: Changes 12hour time to 24 hour time
def time12to24 (h12,mins,suff):


    if (suff == "am"):

        h24 = h12

    else:

        h24 = h12 + 12

    return("%02d%02d" % (h24, mins))

# end function


def testtime24to12 ():

    for h in range(24):
        printDebug(h)
        for m in range(60):
            printDebug(m)
            time24 = ("%02d%02d" % (h, m))
            time12 = time24to12(h, m)
            print(time24, time12)


def testtime12to24 ():

    for s in "am", "pm":
        printDebug(s)

        for h in range(12):
            printDebug(h)

            if (h == 0):

                h = 12

            for m in range(60):
                printDebug (m)

                time12 = ("%2d:%02d %s" % (h, m, s))
                time24 = time12to24 (h, m, s)
                print (time12, time24)


# Main Program Code

DEBUG = False

print ("-- Testing time12to24...")
testtime12to24 ()
print ("-- Finished")
print ("-- Testing time24to12...")
testtime24to12 ()
print ("-- Finished")