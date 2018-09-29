#!/bin/bash

###############################################################################
## Arch Linux Pacman Package Checker
## ---------------------------------
## This package will open all the packages that are to be installed in a new
## chrome (incognito) tab, which will *hopefully* help with checking packages.
## I'm a bit horrible where I search all the packages before I install to make
## sure that they are all good.
## Hope it helps!
## -natc
###############################################################################

RANGE=6

for pkg in "$@"
do
    echo "[$pkg]"
    # google-chrome-stable --incognito "https://google.com.au/search?q=$pkg"
    APKG=`echo "$pkg" | awk '!/^lib.*/' | awk '{ split($0,a,/\-[0-9]/); print a[1]}'`
    echo $APKG
    if [[ $APKG == "" ]]; then
        continue
    fi
    google-chrome-stable --incognito "https://www.archlinux.org/packages/?q=$APKG"
    # Sleep for a random time between 2 and 6 seconds to avoid spamming
    number=$RANDOM
    let "number %= $RANGE"
    let number+=2
    sleep $number
done
