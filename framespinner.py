#!/usr/bin/env python3
import time

frames = "\\|/-"
for i in range(20):
    print("\r%c" % frames[i % len(frames)], end="")
    time.sleep(0.1)
print("")
