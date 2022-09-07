sampleTextFilePath = "sampletext.txt" 
sampleText = open(sampleTextFilePath, 'r')
sampleTextLines = sampleText.readlines()
stringToMatch = ""
stringMatchCount = 0


print("Path to current text file: ", sampleTextFilePath)


while len(stringToMatch) == 0:
	print("Enter a non-empty string to match")
	stringToMatch = str(input())


for sampleTextLine in sampleTextLines:
	stringMatchCount+=sampleTextLine.count(stringToMatch);
print(stringMatchCount, " occurences of: ",stringToMatch, " found in ", sampleTextFilePath);




