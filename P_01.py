import codecs

dataFile_pos = codecs.open('/home/local/STUDENT-CIT/r00171231/PycharmProjects/ML/dataFiles/train/trainPos.txt', 'r', encoding = 'ISO-8859-1', errors='ignore')
dataFile_neg = codecs.open('/home/local/STUDENT-CIT/r00171231/PycharmProjects/ML/dataFiles/train/trainNeg.txt', 'r', encoding = 'ISO-8859-1', errors='ignore')

data_pos = dataFile_pos.read()
data_neg = dataFile_neg.read()
print(len(data_pos))

words_pos_list = data_pos.split()
words_neg_list = data_neg.split()
print(len(words_pos))

vocab = set()
vocab.update(words_pos_list)
vocab.update(words_neg_list)
print(len(vocab))

posDict = dict.fromkeys(vocab, 0)
negDict = dict.fromkeys(vocab, 0)

for words in vocab:
    posDict.update(vocab=words)
    negDict.update(vocab=words)
    
count_p = 0
count_n = 0
i = 0
j = 0

for item in vocab:
    count_p = words_pos_list.count(item)
    count_n = words_neg_list.count(item)
    for (vocab, count) in posDict:
        posDict.update(count=count_p)
    # negDict[item] = count_n
    # print(item, count_p, count_n)


print(posDict)
# for item in dict





