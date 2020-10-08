#
# pref
#set download dir in config to
# /usr/local/lib/nltk_data
#nltk.download('stopwords')
#nltk.download('wordnet')


#
import nltk
from nltk.tokenize import word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer 
from nltk.tokenize import RegexpTokenizer  
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist

import pdb

def loadStopWords(path="stopwords.txt"):
	with open('filename') as f:
    		lines = [line.rstrip() for line in f]
	return lines

def getStopWords():    
	"""
    	Creating a list of stop words and adding custom stopwords
 	""" 

	stop_words = set(stopwords.words("english"))  

	##Add a list of custom stopwords
	stop_words = stop_words.union(new_words)
	return stop_words



def procText(text):
	preProcessedWords = preProc(text)

 	#tokenize
	tokens = nltk.word_tokenize(preProcessedWords)

	is_adjective = lambda pos: pos[:2] == 'JJ'
	adjectives = [word for (word, pos) in nltk.pos_tag(tokens) if is_adjective(pos)]


	return { 'adjectives':adjectives}

def preProc(text):
	stop_words = getStopWords()

	#remove punctuations
	text = re.sub('[^a-zA-Z]', ' ', text)
	text = text.lower()

	#remove tags
	text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    
	# remove special characters and digits
	text=re.sub("(\\d|\\W)+"," ",text)
    
 	#Convert to list from string
	text = text.split()
    
 	#Lemmatisation
	lem = WordNetLemmatizer()
 	text = [lem.lemmatize(word) for word in text if not word in stop_words] 
	return " ".join(text)

    
if __name__=='__main__':

 	text = """
    [Verse 1]
Dark in the city, night is a wire
Steam in the subway, earth is afire
Do do do do do do do dodo dododo dodo
Woman you want me, give me a sign
And catch my breathing even closer behind
Do do do do do do do dodo dododo dodo

[Chorus]
In touch with the ground
I'm on the hunt, I'm after you
Smell like I sound, I'm lost in a crowd
And I'm hungry like the wolf
Straddle the line, in discord and rhyme
I'm on the hunt, I'm after you
Mouth is alive, with juices like wine
And I'm hungry like the wolf

[Verse 2]
Stalked in the forest, too close to hide
I'll be upon you by the moonlight side
Do do do do do do do dodo dododo dodo
High blood drumming on your skin, it's so tight
You feel my heat, I'm just a moment behind
Do do do do do do do dodo dododo dodo
"""

    x= procText(text)
    print (x)
