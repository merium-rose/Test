#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
#This code requires the edf-anonymize.exe installed in Path and computer
#Code also requires the os, sys, and subprocess modules
#Suzybackup.py -- mimics EDF-Anonymize.exe software
#This program is to run with the name Suzybackup.py with the synopsis Suzybackup.py [args ...]
#The program is executed with "python Suzybackup.py [args ...]"
#Args will be used to replace patient information. Multiple word arguments should be enclosed in double quotation marks
#Written by Merium Easterling, 07/12/2021

import os
import subprocess
import sys

cal = os.listdir('.')

#assigns the second argument as the name replacement
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
PatientID = sys.argv[1]
print 'Argument 2 is' , PatientID

print(cal)

#user can uncomment code below if printing out directory is needed.
#for x in cal:
    #print("edf-anonymize.exe " + " '" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8])
    #subprocess.run("edf-anonymize.exe " + " '" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8], shell=True)

#Applys anonymization to edf files only
for File in os.listdir("."):
    if File.endswith(".edf"):
        print("edf-anonymize.exe " + " '" + File + "'" + " 'DeID/" + File + "'" + ' ' + "'" + PatientID + "'" + ' ' + File[0:8])
        subprocess.run(edf-anonymize.exe)
        

print ("DONE")
