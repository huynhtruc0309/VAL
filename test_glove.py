filename = "glove/glove.42B.300d.txt"
# glove_vocab = []
# glove_embed = []
# embedding_dict = {}

# file = open(filename, 'r', encoding='UTF-8')
# print('0')
# print((list(file.readlines())))
# for line in file.readlines():
#     print(line)
# #   row = line.strip().split(' ')
# #   print(row)
# #   vocab_word = row[0]
# #   glove_vocab.append(vocab_word)
# #   embed_vector = [float(i) for i in row[1:]]  # convert to list of float
# #   print(vocab_word)
# #   embedding_dict[vocab_word] = embed_vector
# #   glove_embed.append(embed_vector)

# # print('1')
# # print(embedding_dict.keys())

import numpy as np

def loadGloveModel(File):
    print("Loading Glove Model")
    f = open(File,'r')
    gloveModel = {}
    for line in f:
        splitLines = line.split()
        word = splitLines[0]
        wordEmbedding = np.array([float(value) for value in splitLines[1:]])
        gloveModel[word] = wordEmbedding
    print(len(gloveModel)," words loaded!")
    return gloveModel

print(loadGloveModel(filename))