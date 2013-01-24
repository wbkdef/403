from __future__ import division

def getFile():
    return 'HW1,4.py'

def Do2_RemoveVowels(str):
    print ''.join([i for i in str if i not in "aeiou"])
#Do2_RemoveVowels("This is some text!")

def Do3_ReverseLines():
    with open(getFile(),'r') as myFile:
        lines=myFile.readlines()
    lines.reverse()
    for line in lines:
        print line
#Do3_ReverseLinesDo3()

def Do4_ListComprehensions():
    words = ['attribution','confabulation','elocution','sequoia','tenacious','unidirectional']
    vsequences=set()
    vsequences=[''.join([char for char in word if char in 'aeiou']) for word in words]
    print vsequences
#Do4_ListComprehensionsDo4()

def Do5_DeDuplicate():
    with open(getFile(),'r') as myFile:
        lines=set(myFile.readlines())
        #lines=myFile.readlines()
    #lines.sort()
    for line in lines:
            print line,
#Duplicate Line
#Duplicate Line
#Duplicate Line
#Duplicate Line
#Duplicate Line
#Do5_DeDuplicate()

def Do5_DeDuplicate_Keep_Order():
    with open(getFile(),'r') as myFile:
        lines=myFile.readlines()
    linesNoDup=[]
        #lines=myFile.readlines()
    #lines.sort()
    for line in lines:
        if line in linesNoDup:
            continue
        linesNoDup.append(line)
        print line,
#Do5_DeDuplicate_Keep_Order()

def getLetterCode(char, p=False):
    soundDict={'bfpv':1,'cgikqsxz':2,'dt':3,'l':4,'m,n':5,'r':6,'aeiouy':'v','hw':''}
    for chars, num in soundDict.iteritems():
        if p: print 'num, chars', num, chars
        if char in chars:
            return num
    print "Couldn't find the character: "+char
    assert(False)

def Do6_Soundex(word):
    word=word.lower()
    codeStart=word[0]
    #Change to codes
    codeChars=[str(getLetterCode(i)) for i in word] 
    #Remove duplicates
    i=codeChars[0]
    codesND=[i]
    for i1 in codeChars[1:]:
        if i1 != i:codesND.append(i1)
        i=i1
    #Remove 'v's (indicating vowels)
    codesNV=[c for c in codesND if c != 'v'] 
    #Replace the first code with the first letter
    if codeStart not in 'hw':
        codesNV=codesNV[1:]
    codesNV.insert(0,codeStart)
    #Join Characters together to make a string
    code=''.join(codesNV)
    print "code: ", code
Do6_Soundex("wordc")
Do6_Soundex("supercalafragilisticexpialidocious")
Do6_Soundex("sp")
print 'p=? ',getLetterCode('p',True)
Do6_Soundex("This sentence will break this program!")


Do9_frequency():
    import nltk
    words=nltk.corpus.gutenberg.words('austen-sense.txt')
    fdist = nltk.FreqDist([w.lower() for w in words])
Do9_frequency()

















