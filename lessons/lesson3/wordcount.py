import sys
import time

def count_words1(fd) :

    wc = {}
    
    for l in fd :
        words = l.strip().split()
        for w in words :
            if w not in wc :
                wc[w]=0

            wc[w]+=1
        #
    #

    return wc

def count_words2(fd, wc) :

    wc.clear()
    
    for l in fd :
        words = l.strip().split()
        for w in words :
            if w not in wc :
                wc[w]=0

            wc[w]+=1
        #
    #


def main() :

    print("sys.argv", type(sys.argv), sys.argv)

    if len(sys.argv) < 2 :
        print("Must provide at least one argument")
        sys.exit(1)
    
    fd = open(sys.argv[1])
    wc = count_words1(fd)
    fd.close()

    print("wc", type(wc))
    
    firstwords=list(wc)
    print(firstwords[0:10])

    start = time.perf_counter()
    if ("petard" in firstwords) :
        print("Found it")
    end = time.perf_counter()
    print("Lookup took", (end-start)*1e3, "ms")

    start = time.perf_counter()
    if ("petard" in wc) :
        print("Found it")
    end = time.perf_counter()
    print("Lookup took", (end-start)*1e3, "ms")

    
    wc2 = {}
    fd = open(sys.argv[1])
    count_words2(fd, wc2)
    fd.close()

    firstwords=list(wc)
    print(firstwords[0:10])

if __name__ == "__main__":
    main()
    
