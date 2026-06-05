import sys

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

def count_words2(fd) :

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


def main() :

    print(type(sys.argv), sys.argv)

    if len(sys.argv) < 2 :
        print("Must provide at least one argument")
        sys.exit(1)
    
    fd = open(sys.argv[1])
    wc = count_words1(fd)
    fd.close()
    
