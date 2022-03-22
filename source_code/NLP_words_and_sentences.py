# Import the TextBlob class from the textblob library
from textblob import TextBlob

# Set a text to analyze
text = "Today is a beautiful day. Tomorrow looks like bad weather. is a"

# Create a blob object using the TextBlob class, with the text variable as a parameter
blob = TextBlob(text)

# We can see the sentences in the text by printing blob.sentences
# blob.sentences is a list, and every element is one sentence of the text
print("Sentences in the text:")
print(blob.sentences)

# We can see the words in the text by printing blob.words
# blob.words is a list, and every element is one word of the text
print("\nWords in the text:")
print(blob.words)

# TODO:
# 1. Print all the UNIQUE words in the text
all_items = blob.words
unique_items = []
for x in all_items:
    if x not in unique_items:
        unique_items.append(x)
print("\nUnique words in the text:")
print(unique_items)

# 2. Print the number of unique words in the text
print("\nThe number of unique words in the text:")
print(len(unique_items))