#!/usr/bin/env python
import fileinput, os

cwd = os.getcwd()
var = "variables.csv"
bash = "testbash"
bash_temp = bash + ".temp"

bash_fd = open(bash, "r")
bash_temp_fd = open(bash_temp, "w+")

bash_lines = [line.rstrip('\n') for line in bash_fd]

makefeat_exists = "alias makefeat"
maketemp_exists = "alias maketemp"
alias_feat = "%s='%s/makefeat.py %s'" % (makefeat_exists, cwd, var)
alias_temp = "%s='%s/maketemp.py %s'" % (maketemp_exists, cwd, var)

for line in bash_lines:
    #if makefeat_exists in line:
    bash_temp_fd.write(alias_feat + "\n" if makefeat_exists in line else line + "\n")
        #continue
    #else:
        #bash_temp_fd.write(line + "\n")
        #continue
    #if maketemp_exists in line:
    bash_temp_fd.write(alias_temp + "\n" if maketemp_exists in line else line + "\n")
        #continue
    #else:
        #bash_temp_fd.write(line + "\n")
        #continue
    #print(line)
    #bash_temp_fd.write(this_line)
