import sys
linesNoDup=[]
for line in sys.stdin:
    if line in linesNoDup:
        continue
    linesNoDup.append(line)
    print line,
