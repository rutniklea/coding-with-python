import re

besedilo = (input("Vnesi poljubno besedilo: \n"))

sum_besed=(len(re.findall("", besedilo)))

print("Vsota besed, povedi, črk in znakov je: ", str(sum_besed) )
