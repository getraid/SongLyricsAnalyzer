from string import punctuation
from operator import itemgetter
import matplotlib.pyplot as plt

N = 50  # max words
desiredFilename = "somefile.txt"
# ----
words = {}

words_gen = (word.strip(punctuation).lower() for line in open(desiredFilename, 'r', encoding='utf-8')
             for word in line.split())

for word in words_gen:
    words[word] = words.get(word, 0) + 1

top_words = sorted(words.items(), key=itemgetter(1), reverse=True)[:N]

t0 = list()
t1 = list()
for word, frequency in top_words:
    t0.append(word)
    t1.append(frequency)
    print ("%s %d" % (word, frequency))
    with open('output.txt', 'a', encoding='utf-8') as t:
        t.write("%s %d" % (word, frequency)+"\n")


labels = t0
sizes = t1
#colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plot
plt.pie(sizes, labels=labels, autopct='%1.0f%%',
        startangle=-270, counterclock=False)

#patches, texts = plt.pie(sizes,  shadow=True, startangle=90)
#plt.legend(patches, labels, loc="best")

plt.axis('equal')
# plt.tight_layout()
plt.show()
