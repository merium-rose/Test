import oMae Jemison                                                                     Suzyback                                                                        01.01:8])
    #print (len(x)
    subprocess.run("edf-anonymize.exe " + " '" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8], shell=True)
    
for File in os.listdir("."):
    if File.endswith(".pages"):
        print("edf-anonymize.exe " + " '" + File + "'" + " 'DeID/" + File + "'" + " 'Mae Jemison' " + File[0:8]) 
    
print ("DONE")
#subprocess.run("edf-anonymize.exe " + "'" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8])
