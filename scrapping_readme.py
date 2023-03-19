#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing and downloading neccesary libraries
import os
from collections import Counter
from sklearn.utils import Bunch
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk import WordNetLemmatizer
import numpy as np
from github import Github
nltk.download('stopwords')
nltk.download('wordnet')


# In[ ]:




def process_words(data):   # FOR PROCESSING DOC (stop word)
  
    processed_data = []

    stop_words = set(stopwords.words('english'))
    word_splitter = RegexpTokenizer(r'\w+')
    lemmatizer = WordNetLemmatizer()
    processing = word_splitter.tokenize(data)
    for i in processing:
        i = i.lower()
        if i not in stop_words and i.isalpha() and len(i)>2:
            processed_data.append(i)
    for j in processed_data:
        lemmatizer.lemmatize(j)

    return processed_data

def get_unique(data):   # GET UNQUIE WORDS
    unique_list = []
    for word in data:
        if word in unique_list:
            "do nothing"
        else:
            unique_list.append(word)
    return(unique_list)


# In[ ]:


get_ipython().run_line_magic('env', 'github_token = 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   # picking up an enviromental variable that doesnt get saved to repo when pushed')


# In[ ]:


## CTC_COMMONWORDS DICTIONARY UPDATE

token = os.getenv('github_token')

g = Github(token)

my_repos = g.get_organization("codethecity").get_repos()
wordsfound = []
for repo in my_repos:
    try:
        readme = repo.get_readme().decoded_content
        cleaned_readme = process_words(str(readme))
        wordsfound+=get_unique(cleaned_readme)
    except Exception as e:
        print(e,", no readme!")


# In[ ]:


# SELECTING  TOP 15 MOST COMMON WORDS TO FILTER NEXT
percentage=15     
ctc_words = Counter(wordsfound)
x= round(percentage/100*len(ctc_words))
ctc_commonwords = ctc_words.most_common(x)


# In[ ]:


# RE PROCESSING WORDS REMOVING COMMON CTC WORDS FUNCTION


def process_words_ctc(data: str):
  
    processed_data = []

    stop_words = set(stopwords.words('english'))
    word_splitter = RegexpTokenizer(r'\w+')
    lemmatizer = WordNetLemmatizer()
    processing = word_splitter.tokenize(data)
    for i in processing:
        i = i.lower()
        if i not in stop_words and i.isalpha() and (len(i)>2) and (i not in [word[0] for word in ctc_commonwords]) and (i not in manual_filter):
            processed_data.append(i)
    for j in processed_data:
        lemmatizer.lemmatize(j)

    return processed_data


# In[ ]:


# OUTPUT REPONAME: TAG PAIRS

manual_filter = ['codethecity','ncodethecity','div', 'class', 'col','npercentage', 'mailto']

token = os.getenv('github_token')

g = Github(token)

my_repos = g.get_organization("codethecity").get_repos()
repo_tag = {}
for repo in my_repos:
    try:
        readme = repo.get_readme().decoded_content
        cleaned_readme = process_words_ctc(str(readme)) # ctc stop word are flitered but words are allowed to repeat to give potential tags more relevance
        tag = Counter(cleaned_readme+str(repo.name).split()) # using repo name to give potential tags more relevance
        top_tag = [item[0] for item in tag.most_common(10)]                  # repo name as key, tags as value
        repo_tag[repo.name] = top_tag
#        print(repo.name,' : ',top_tag)
    except:
        tag = Counter(repo.name.split()) # using repo name to give potential tags more relevance
        repo_tag[repo.name] = [item[0] for item in tag.most_common(10)]
#        print( "no readme!",repo.name,' : ',[item for item in tag])

    


# In[ ]:


len(repo_tag)


# In[ ]:


#repo_tag


# In[ ]:





# In[ ]:





# In[ ]:




