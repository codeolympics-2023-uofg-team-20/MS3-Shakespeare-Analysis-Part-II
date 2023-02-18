from pprint import pprint as print

def load_contents(filename):
    res = []
    with open(filename) as f:
        for line in f.readlines():
            for word in line.strip().split(' '):
                if word.lower() == '':
                    continue
                res.append(word.lower())
    return res
    

def get_n_grams(words, n):
    res = []
    for i in range(len(words) - n + 1):
        res.append(" ".join(words[i:i+n]))
    return res


def run():
    words = load_contents('main.txt')
    ngrams = {}
    for i in range(2,6):
        ngrams[i] = get_n_grams(words, i)

    # return the most used 10 ngrams for each 2 <= n <= 5
    res = {}
    for n in ngrams:
        d = {}
        for word in ngrams[n]:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        res[n] = sorted(d.items(), key=lambda x: x[1], reverse=True)[:10]
    return res
       
print(run())
