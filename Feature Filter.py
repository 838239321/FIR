import nltk
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from collections import Counter
from wordcloud import WordCloud
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

from PIL import Image
import numpy as np


def _remove_stopwords(txt):
    words = txt.split()
    for i, word in enumerate(words):
        if word in STOPWORDS:
            words[i] = " "
    return (" ".join(words))


# stop words in English
out = []
example_sent = ' '.join(out)
stop_words = set(stopwords.words('english'))
stop_words_list = list(stopwords.words('english'))
STOPWORDS2 = ["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3",
              "a4", "ab", "able", "about", "above", "abst", "ac", "accordance",
              "according", "accordingly", "across", "act", "actually", "ad",
              "added", "adj", "ae", "af", "affected", "affecting", "affects",
              "after", "afterwards", "ag", "again", "against", "ah", "ain",
              "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone",
              "along", "already", "also", "although", "always", "am", "among",
              "amongst", "amoungst", "amount", "an", "and", "announce",
              "another", "any", "anybody", "anyhow", "anymore", "anyone",
              "anything", "anyway", "anyways", "anywhere", "ao", "ap",
              "apart", "apparently", "appear", "appreciate", "appropriate",
              "approximately", "ar", "are", "aren", "arent", "aren't",
              "arise", "around", "as", "a's", "aside", "ask", "asking",
              "associated", "at", "au", "auth", "av", "available", "aw",
              "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3",
              "ba", "back", "bc", "bd", "be", "became", "because", "become",
              "becomes", "becoming", "been", "before", "beforehand", "begin",
              "beginning", "beginnings", "begins", "behind", "being", "believe",
              "below", "beside", "besides", "best", "better", "between",
              "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both",
              "bottom", "bp", "br", "brief", "briefly", "bs", "bt", "bu",
              "but", "bx", "by", "c", "c1", "c2", "c3", "ca", "call", "came",
              "can", "cannot", "cant", "can't", "cause", "causes", "cc", "cd",
              "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci",
              "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com",
              "come", "comes", "con", "concerning", "consequently", "consider",
              "considering", "contain", "containing", "contains",
              "corresponding", "could", "couldn", "couldnt", "couldn't",
              "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu",
              "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date",
              "dc", "dd", "de", "definitely", "describe", "described",
              "despite", "detail", "df", "di", "did", "didn", "didn't",
              "different", "dj", "dk", "dl", "do", "does", "doesn", "doesn't",
              "doing", "do", "an", "a", "the", "or", "and", "thou", "must",
              "that", "this", "self", "unless", "behind", "for", "which",
              "whose", "can", "else", "some", "will", "so", "from", "to", "by",
              "within", "of", "upon", "th", "with", "it"]
STOPWORDS = ["gta", "game", "good", "fun", "still", "one", "much", "really", "many",
             "rockstar", "v", "time", "play", "dont", "even", "make", "games", "great",
             "best", "bad", "better", "now", "feel", "nothing", "well", "lot", "i",
             "is", "im", "in", "on", "are", 'quite', 'gb', 'sure', 'takes', 'gets',
             'yet', 'seems', 'try', 'might', 'extremely', 'someone', 'worst',
             'making', 'until', 'took', 'once', 'taketwo', 'y', 'itself', 'maybe',
             'having', 'come', 'absolutely', 'days', 'away', 'however', 'etc',
             'trying', 'especially', 'isnt', 'before', 'right', 'put', 'three',
             'always', 'able', 'find', 'here', 'done', 'la', 's', 'anything',
             'already', 'getting', 'los', 'through', 'use', 'doing', 'makes',
             'nice', 'less', 'wait', 'end', 'stuff', 'side', 'continue', 'worth',
             'random', 'week', 'break', 'bit', 'join', 'thank', 'remember',
             'two', 'soon', 'later', 'zero', 'stay', 'san', 'say', 'thouht',
             'everything', 'favorite', 'care', 'una', 'expect', 'opinion',
             'bring', 'negative', 'think', 'choose', 'part', 'se', 'add',
             'hand', 'give', 'keep', 'second', 'kind']
expanded_stopWords = stop_words_list + STOPWORDS + STOPWORDS2

#Open text
with open('meta.txt',encoding ="utf8") as f:
    lines = f.readlines()
for word in lines:
    cleantextprep = str(word)
    expression = "[^a-zA-Z ]"  # keep only letters, numbers and whitespace
    cleantextCAP = re.sub(expression, '', cleantextprep)
    cleantext = cleantextCAP.lower()
    cleantext = _remove_stopwords(cleantext)
    bound = ''.join(cleantext)
    out.append(bound)


word_tokens = word_tokenize(' '.join(out))
# standard syntax
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

my_dict = {i:filtered_sentence.count(i) for i in filtered_sentence}
my_dict


keyword_df = pd.DataFrame.from_dict(my_dict, orient='index', columns = ['counts'])
keyword_df = keyword_df.reset_index()
keyword_df.rename(columns = {'index' : 'word', 'counts' : 'counts'}，inplace = True)
keyword_df = keyword_df.sort_values(by=['counts'], ascending = False)
keyword_df

keyword_df.to_csv('feature_ranking.csv')