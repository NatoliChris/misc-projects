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
    if [[ $pkg == *"/"* ]]; then
        APKG=`echo "$pkg" | awk '{ split($0, a, /\//); print a[2]}' | awk '!/^lib.*/'`
        if [[ $APKG == "" ]]; then
            continue
        fi
        echo "[$APKG]"

        google-chrome-stable --incognito "https://www.archlinux.org/packages/?q=$APKG" &
        # Sleep for a random time between 2 and 6 seconds to avoid spamming
        number=$RANDOM
        let "number %= $RANGE"
        let number+=2
        sleep $number
    fi
done
