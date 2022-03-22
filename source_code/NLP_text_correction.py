import textblob

# Import TextBlob class from textblob library
from textblob import  TextBlob

# Get text as user input
text = input('Enter a text:')

# Use TextBlob.correct() method to get the predicted correction of the text
textcorrection = TextBlob(text).correct()

print("Correction :" + str(textcorrection))
