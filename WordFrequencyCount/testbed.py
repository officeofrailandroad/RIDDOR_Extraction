from textcleaner import textcleaner, listclean

from gensim.summarization import keywords

testtext = """Clarbeston Road signaller reported that 0A11 1655 Margam to Robeston had not shown as having occupied track circuit 'KK'. Initially the report received stated that 0A11 had failed to occupy the circuit and as a precaution the wheelsets of 66194 were to be checked. All previous circuits operatated correctly for the train. \
\
The electronics were in system 1 and had now been switched to system 2. 'KK' then operated correctly and showed occupied. The driver of 0A11 checked the wheelsets and reported that there were slight signs of rust on the track and wheels, but nothing other than what would normally be expected. S&T Level 2 and Tech Support Level 3 were consulted with regards to the fault and stated that the circuit could be used normally.\

During the initial phase of the incident, 0A11 was confirmed as stationary and that the train would not move from Haverfordwest Loop and the signaller isolated the route to ensure no conflicts could occur. \
\
Level 3 Tech support advised that the signaller was able to use the loop as it was a technical issue that was rectified when they swapped systems. Faulty TXE card and RXE card changed to restore at 1638."""


#print(testtext)
#print("after cleaning.... \n")
#print(textcleaner(testtext))
print(type(keywords(testtext)))
print (keywords(testtext)) 