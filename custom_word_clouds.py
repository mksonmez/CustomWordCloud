import io
import sys
import wordcloud
import numpy as np

from matplotlib import pyplot as plt

def custom_word_clouds(file_contents):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # feel free to edit this list
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "thus", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    frequencies = {}
    seperate = file_contents.split()

    for word in seperate:
        # disregard the words that are in our uninteresting_words list
        if word in uninteresting_words:
            pass
        else:
            for letter in word:
                # remove/replace punctuations
                if letter in punctuations:
                    word.replace(letter,'')
            if word not in frequencies.keys():
                frequencies[word] = 1
            else:
                frequencies[word] += 1
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

# location of our txt file
file_contents = open('sample.txt').read()
# creating the image
myimage = custom_word_clouds(file_contents)
plt.imshow(np.real(myimage), interpolation = 'nearest')
plt.axis('off')
plt.show()