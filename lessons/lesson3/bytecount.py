import sys
import time

def count_bytes(filename, buflen=2048) :
    
    fd = open(filename, 'rb')

    bc = [0] * 256

    buf = fd.read(buflen)
    while len(buf) > 0 :
        for b in buf :
            bc[int(b)]+=1
        buf = fd.read(buflen)
        
    return bc

import matplotlib.pyplot as plt

def plot_histogram(counts) :
    x = [z for z in range(len(counts))]
    plt.bar(x, counts)
    plt.show()
    

def main() :

    if len(sys.argv) < 2 :
        print("Must provide at least one argument")
        sys.exit(1)
    
    bc = count_bytes(sys.argv[1])

    plot_histogram(bc)
    

if __name__ == "__main__":
    main()
    
