#This code requires the edf-anonymize.exe installed in Path and computer
#Code also requires the os, sys, and subprocess modules
#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import os
import subprocess
import sys

cal = os.listdir('.')

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
PatientID = sys.argv[1]
print 'Argument 3 is' , PatientID

print(cal)

#for x in cal:
    #print("edf-anonymize.exe " + " '" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8])
    #subprocess.run("edf-anonymize.exe " + " '" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8], shell=True)

for File in os.listdir("."):
    if File.endswith(".edf"):
        print("edf-anonymize.exe " + " '" + File + "'" + " 'DeID/" + File + "'" + ' ' + "'" + PatientID + "'" + ' ' + File[0:8])
        

print ("DONE")
