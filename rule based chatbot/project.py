import numpy as np
import nltk
import string
import random
import pyttsx3

def text_speech(sentence):
    py = pyttsx3.init()
    py.say(sentence)
    py.runAndWait()
    
# importing and read corpus
F = open('chatbot.txt.txt','r',errors = 'ignore')
raw_doc = F.read()
raw_doc = raw_doc.lower() #Converts text to lowercase
nltk.download('punkt',quiet = True) #Using the Punkt tokenizer
nltk.download('wordnet', quiet = True) #Using the WordNet dictionary
sent_tokens = nltk.sent_tokenize(raw_doc) #Converts doc to list of sentences 
word_tokens = nltk.word_tokenize(raw_doc) #Converts doc to list of words

sent_tokens[:2] # sentence 
word_tokens[:2] # word 

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
GREET_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greet(sentence):
 
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)
        
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
  robo1_response=''
  TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx=vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if(req_tfidf==0):
    robo1_response=robo1_response+"I am sorry! I don't understand you"
    return robo1_response
  else:
    robo1_response = robo1_response+sent_tokens[idx]
    return robo1_response

flag=True

text_speech("hey iam edith how can i help you")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            text_speech("You are welcome..")
        else:
            if(greet(user_response)!=None):
                temp = "BOT: "+greet(user_response)
                text_speech(temp)
                
               
            else:
                sent_tokens.append(user_response)
                word_tokens=word_tokens+nltk.word_tokenize(user_response)
                final_words=list(set(word_tokens))
                print("BOT: ",end="")
                ab = response(user_response) 
                text_speech(ab)
                sent_tokens.remove(user_response)
    else:
        flag=False
        text_speech(" Goodbye! Take care <3 ")