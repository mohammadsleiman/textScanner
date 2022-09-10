import sys

def getSysArgs():
	if not len(sys.argv) == 3 or not ".txt" in sys.argv[1]:
		print("usage: python textMatch.py [path to text.txt] ['input string in quotes']")
		exit()
	return {"textFilePath": sys.argv[1],"stringToMatch": sys.argv[2]}

def getStringMatchCount(textFilePath, stringToMatch):
	try:
		textFile = open(textFilePath, 'r')
	except Exception as e:
		return -1
	textFileLines = textFile.readlines()
	stringMatchCount = 0
	for textFileLine in textFileLines:
		stringMatchCount+=textFileLine.count(stringToMatch)
	textFile.close()
	return stringMatchCount

def main():
	args = getSysArgs()
	stringMatchCount = getStringMatchCount(args["textFilePath"], args["stringToMatch"])
	if stringMatchCount == -1:
		print(f"textMatch failed. ERROR: File \'{args['textFilePath']}\' not found. Check file name exists.")
	else:
		print(f"textMatch result: {stringMatchCount} occurences of \'{args['stringToMatch']}\' found in {args['textFilePath']}" );

if __name__ == "__main__":
   main()




