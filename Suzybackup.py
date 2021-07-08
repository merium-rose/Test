#This code requires the edf-anonymize.exe installed in Path and computer
#Code also requires the os and subprocess modules
#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import os
import subprocess

cal = os.listdir('.')

print(cal)

for x in cal:
    print("edf-anonymize.exe " + " '" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8])
    subprocess.run("edf-anonymize.exe " + " '" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8], shell=True)

for File in os.listdir("."):
    if File.endswith(".pages"):
        print("edf-anonymize.exe " + " '" + File + "'" + " 'DeID/" + File + "'" + " 'Mae Jemison' " + File[0:8])

print ("DONE")
