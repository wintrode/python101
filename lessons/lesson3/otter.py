import sys
import math

def error(arm, leg, torso, head, otter) :
    val = math.sqrt((arm - otter)*(arm-otter)*2 +
                    (leg - otter)*(leg-otter)*2 +
                    (head - otter)*(head-otter) +
                    (torso - otter)*(torso-otter))

    return val


(arm, leg, torso, head, otterfile) = sys.argv[1:6]

arm = float(arm)
leg = float(leg)
torso = float(torso)
head = float(head)

fd = open(otterfile)

otters = {}

for l in fd :
    g = l.strip().split()
    name=g[0]
    value = float(g[1])
    otters[name]=value

fd.close()

print(otters)

for otter in otters :
    print(otter, error(arm, leg, head, torso, otters[otter]))
    
