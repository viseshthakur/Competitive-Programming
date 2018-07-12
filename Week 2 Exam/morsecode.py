dict1={'A':".-",
'B':"-...",
'C' :"-.-.",
'D' :"-..",
'E':".",
'F' :"..-.",
'G' :"--.",
'H' :"....",
'I':"..",
'J':".---",
'K':"-.-",
'L':".-..",
'M':"--",	
'N':"-.",
'O':"---",
'P':".--.",
'Q':"--.-",
'R':".-.",
'S':"...",
'T':"-",
'U':"..-",
'V':"...-",
'W':".--",
'X' :"-..-",
'Y' :"-.--",
'Z' :"--.."}

def morsecode(list1):
	dict2={}
	for i in range(0,len(list1)):
		str1=list1[i].upper()
		original=""
		for j in range(0,len(str1)):
			original+=dict1.get(str1[j])
		dict2[original]=1

	return len(dict2)

print(morsecode(['gin','zen','gig','msg']))
print(morsecode(['a','z','g','m']))
print(morsecode(['bhi','vsv','sgh','vbi']))
print(morsecode(['a','b','c','d']))
print(morsecode(['hig','sip','pot']))



















