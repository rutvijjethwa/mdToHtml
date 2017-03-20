import markdown
import sys

if sys.argv[1] == '':
    print("Invalid input")
    sys.exit(0)

try:
    with open(sys.argv[1],'r') as inputFile:
        markdownData = inputFile.read()

    htmlOutput = markdown.markdown(markdownData)
    fileName = sys.argv[1][:-3]
    fileName = fileName+".html"
    with open(fileName,'w') as outputFile:
        outputFile.write(htmlOutput)

except IOError:
    print("I//O Error")
