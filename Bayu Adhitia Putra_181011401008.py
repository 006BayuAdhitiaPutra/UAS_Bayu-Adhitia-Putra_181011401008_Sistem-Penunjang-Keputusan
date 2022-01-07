import nltk
from nltk.stem import PorterStemmer

porter = PorterStemmer()

tns = ['eat','eating','eats','ate']

for token in ts:
    print(token + " : " + porter.stem(token))
eat : makan
eating :makan
eates : makan
ate : makan
from nltk.stem import SnowballStemmer

snowball = SnowballStemmer(language='english')

for token in ts:
    print(token + " : " + snowball.stem(token))
eat : makan
eating :makan
eates : makan
ate : makan
from nltk.stem import LancasterStemmer

lancaster = LancasterStemmer()

for token in ts:
    print(token + " : " + lancaster.stem(token))
eat : makan
eating :makan
eates : makan
ate : makan
nltk.download('wordnet')
[nltk_data] Downloading package wordnet to /Users/bsi-00/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
True
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

for token in tkns:
    print(token + " :  " + lemmatizer.lemmatize(token))
eat : makan
eating :makan
eates : makan
ate : makan
from nltk.stem import PorterStemmer

porter = PorterStemmer()

tkns = ['player','players','plays','playing','played']

for token in tkns:
    print(token + " : " + porter.stem(token))
player : player
players : player
plays : play
playing : play
played : play
from nltk.stem.snowball import SnowballStemmer

snowball = SnowballStemmer(language='english')

for token in tkns:
    print(token + " : " + snowball.stem(token))
player : player
players : player
plays : play
playing : play
played : play
from nltk.stem.lancaster import LancasterStemmer

lancaster = LancasterStemmer()

for token in tkns:
    print(token + " : " + lancaster.stem(token))
player : play
players : play
plays : play
playing : play
played : play
nltk.download('wordnet')
[nltk_data] Downloading package wordnet to /Users/bsi-00/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
True
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

for token in tkns:
    print(token + " : " + lemmatizer.lemmatize(token))
player : player
players : player
plays : play
playing : playing
played : played
