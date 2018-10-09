import codecs

dataFile_pos = codecs.open('/home/local/STUDENT-CIT/r00171231/PycharmProjects/ML/dataFiles/train/trainPos.txt', 'r', encoding = 'ISO-8859-1', errors='ignore')
dataFile_neg = codecs.open('/home/local/STUDENT-CIT/r00171231/PycharmProjects/ML/dataFiles/train/trainNeg.txt', 'r', encoding = 'ISO-8859-1', errors='ignore')

data_pos = dataFile_pos.read()
data_neg = dataFile_neg.read()
print(len(data_pos))

words_pos = data_pos.split()
words_neg = data_neg.split()
print(len(words_pos))

vocab = set()
vocab.update(words_pos)
vocab.update(words_neg)
print(len(vocab))

posDict = dict.fromkeys(vocab, 0)
negDict = dict.fromkeys(vocab, 0)

for words in vocab:
    posDict.update(vocab=words)
    negDict.update(vocab=words)

    count = 0
for item in dict.keys(posDict):
    for word in words_pos_list:
        if item == word:
            count += 1
print(word, count)






