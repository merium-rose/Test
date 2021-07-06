import os

cal = os.listdir('.')

print(cal)

#xl = 1

#subjectID = 'INMO-285'

#print("edf-anonymize.exe filename.edf DeID/filename.edf Mae Jemison " + subjectID)

#for item in cal:
    #print (item)
#for item in range (0,5):
    #print(cal[XL])
    #xl=xl + 1

#numbers = []
#strings = []
#names = ["John", "Eric", "Jessica"]

# write your code here
#second_name = 'Eric'


# this code should write out the filled arrays and the second name in the names list (Eric).
#print(numbers)
#print("The second name on the names list is %s" % second_name)
#print(names)

astring = "edf-anonymize.exe filename.edf DeID/filename.edf Mae Jemison"
astring = "edf-anonymize.exe filename.edf DeID/filename.edf Mae Jemi"

#astringtt = len(astring)
#print(astringtt)

#mylist = []
#mylist.append('INMO-283')
#mylist.append('INMO-278')
#mylist.append('INMO-294')
#mylist.append('INMO-276')
#print(mylist[0]) # prints 1
#print(mylist[1]) # prints 2
#print(mylist[2]) # prints 3
#print(mylist[3])


# prints out 1,2,3
for x in cal:
    print("edf-anonymize.exe " + "'" + x + "'" + " 'DeID/" + x + "'" + " 'Mae Jemison' " + x[0:8])
    #print (len(x))
print ("DONE")
