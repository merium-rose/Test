import os
import subprocess

cal = os.listdir('.')

print(cal)

for x in cal:
    print("edf-anonymize.exe " + "'" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8])
    #print (len(x)
    #subprocess.run("edf-anonymize.exe " + "'" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8], shell=True, check=True)
    #subprocess.run("pwd", shell=True, check=True)
    
for File in os.listdir("."):
    if File.endswith(".pages"):
        print("edf-anonymize.exe " + "'" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8])         
    else:
        print("false")

print ("DONE")
#subprocess.run("edf-anonymize.exe " + "'" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8])
