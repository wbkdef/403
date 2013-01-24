# logging demo
# run as: python logdemo.py < hw1.txt > output
# check the log file: logdemo.log
# to append to the log file instead of zeroing it for each run, remove the 'w' in line 11
import sys, logging
from collections import defaultdict

def logdemo():
    log = logging.getLogger('logdemo')
    log.setLevel(logging.DEBUG)
    log.addHandler(logging.FileHandler('logdemo.log', 'w')) # default is to append to logfile
    wc = defaultdict(int)
    for line in sys.stdin:
        for w in line.split():
            wc[w] += 1
            if wc[w] == 1: 
                log.debug("NEW_WORD: %s" % (w))
    for w in wc.keys():
        # print to standard output
        print wc[w], w
    logging.shutdown()
            
if __name__ == '__main__':
    # print a message to standard error
    print >>sys.stderr, "logging demo ..."
    logdemo()

