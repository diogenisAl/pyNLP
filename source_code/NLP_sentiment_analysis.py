# Import the TextBlob class from the textblob library
from textblob import TextBlob

# Set a text to analyze
text = "Today is a beautiful day. Tomorrow looks like bad weather."

# Create a blob object using the TextBlob class, with the text variable as a parameter
blob = TextBlob(text)

# Sentiment Analysis
# The blob.sentiment is an object that shows the polarity and subjectivity values of the text.
# Polarity (or sentiment) is whether the text shows positive (+1) or negative (-1) emotions
# Subjectivity is whether the text is objective (0.0) or subjective (1.0)
print("\nSentiment of the whole text")
print(blob.sentiment)

# TODO
# Find the sentiment of every sentence in the given text

sentences = blob.sentences
for x in sentences:
    print("\nThe sentiment of the sentence part is: ", x.sentiment)

# Optionally you can use a different analyzer algorithm by specifying it as a parameter
# In this example we use the NaiveBayesAnalyzer from the textblob module.
# Note that an important difference is that the NaiveBayesAnalyzer algorithm also classifies
# the text (neg or pos), while it does not display its subjectivity.
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
print("\n", blob.sentiment)
