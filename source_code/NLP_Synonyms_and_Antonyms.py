import nltk

# Import wordnet class from nltk.corpus library
from nltk.corpus import wordnet

nltk.download('omw-1.4')

text = "Good"

# Create a synsets object from the given text
syns = wordnet.synsets(text)

# Print some details from the synset object
print("Name: ", syns[0].name())
print("Lemma Name: ", syns[0].lemmas()[0].name())
print("Definition", syns[0].definition())
print("Examples:", syns[0].examples())

synonyms = []
antonyms = []

# Get every meaning of the text get the synonyms and the antonyms (if there are any)
for syn in wordnet.synsets(text):
    for x in syn.lemmas():
        synonyms.append(x.name())
        if x.antonyms():
            antonyms.append(x.antonyms()[0].name())

print("Synonyms:")
print(set(synonyms))
print("Antonyms:")
print(set(antonyms))