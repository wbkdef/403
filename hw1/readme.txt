
The filenames for each question are given below.  We will grade
only the questions marked with a dagger in the PDF file.  They are
marked with + below.

All text output should be printed to standard output (just use
print).

Programs that take input must read it from standard input (sys.stdin).
The sample program "stdin.py" explains how to do this.  On a Linux
command line run it as: "python stdin.py < hw1.txt"

Test your programs by running: "python check-hw1.py". Run without
arguments and it will print out a detailed help text about usage
and grading.

If there is an additional file to be created the output filename
is given below.

Use svn for your homeworks (more details on course web page).

$ svn co https://punch.cs.sfu.ca/svn/CMPT413-1131-(your-userid)
$ cd CMPT413-1131-(your-userid)
$ scp -r fraser.sfu.ca:~anoop/cmpt413/hw1 .
$ svn add hw1 
$ cd hw1/answer # put all your python programs here
# svn add each file you add to this directory
$ svn commit -m 'commit message'

To continue working at a later date:

$ cd CMPT413-1131-<userid>/hw1/answer
$ svn update
# work on your homework
$ svn commit -m 'commit message'

When you submit HW1 on courses.cs.sfu.ca submit the following URL:

https://punch.cs.sfu.ca/svn/CMPT413-1131-(your-userid)/hw1/answer

%%

q1: silly.py
q2: devowel.py
q3: reversefile.py
q4: vsequences.py
+q5: noduplicates.py
+q6: soundex.py
q7: urlwc.py
q8: shufflewords.py
+q9: freq.py
+q10a: zipf.py # output: zipfplot.png
+q10c: stem_zipf.py # output: stemplot.png
q11: dispersion.py
+q12: paircount.py
++q13: virahanka.py
++q14: segment.py

