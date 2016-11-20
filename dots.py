#!/usr/bin/env python3



for i in range(1,31):
    print(""".dot.b%d {
                -webkit-animation-delay: %.1fs;
                animation-delay: %.1fs;
            }""" % (i, (float(0.1*i)), (float(0.1*i))));
