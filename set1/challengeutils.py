import operator

def xor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def score_key(key, ciphertext):
    key = key * len(ciphertext)
    res = xor(key, ciphertext)
    return (res, sum(1 for c in res if c in ('a', 'e', 'i', 'o', 'u')))


def score_keys(ciphertext, n=3):
    scores = ((chr(c), score_key(chr(c), ciphertext)[1]) for c in range(256))
    return sorted(scores, key=operator.itemgetter(1), reverse=True)[:n]


def ngrams(s, n):
    return list(s[i:i+n] for i in range(len(s)-n+1))


def bigrams_score_key(key, ciphertext, targets):
    key = key * len(ciphertext)
    res = xor(key, ciphertext)
    res_bigrams = ngrams(res.lower(), 2)
    return (res,
            sum(targets[b] for b in res_bigrams if b in targets))


def repeating_key_xor(atomic_key, s):
    key = atomic_key * (len(s) / len(atomic_key)) + \
          atomic_key[:(len(s) % len(atomic_key))]
    return xor(key, s)


def hamming_dist(s1, s2):
    return sum(bin(ord(c)).count('1') for c in xor(s1, s2))
