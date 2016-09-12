def sing_beers(n):
    beers = n
    str_beers = str(beers)

    if n <= 0:
        print "No more bottles of beer on the wall"

    else:
        print str_beers + " bottles of beer on the wall " + str_beers + " if one of those bottles should happen to fall "
        sing_beers(n-1)

print sing_beers(99)
