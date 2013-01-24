import sys, codecs

def segment_bitstring(a):
    a = a.strip()
    a = a[1:]
    a += ' ' # add a space at the end for the last char
    bitstring = '0'
    for i in a:
        if i == ' ':
            bitstring += '1'
        else:
            bitstring += '0'
    return bitstring

def print_utf8(a):
    old = sys.stdout
    sys.stdout = codecs.lookup('utf-8')[-1](sys.stdout)
    utf8str = unicode(a, 'utf-8')
    print utf8str
    print segment_bitstring(utf8str)
    sys.stdout = old

for i in sys.stdin:
    print_utf8(i)
