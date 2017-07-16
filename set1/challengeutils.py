import operator
from collections import namedtuple
from collections import defaultdict

def xor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

RELATIVE_LETTER_FREQUENCIES = [
  ('e', 12),
  ('t', 9),
  ('a', 8),
  ('o', 8),
  ('i', 8),
  ('n', 7),
  ('s', 7),
  ('r', 6),
]
LETTER_TO_FREQ = defaultdict(int)
for letter, relative_frequency in RELATIVE_LETTER_FREQUENCIES:
    LETTER_TO_FREQ[letter] = relative_frequency

def score_key(key, ciphertext):
    key = key * len(ciphertext)
    res = xor(key, ciphertext)
    return (res, sum(LETTER_TO_FREQ[c] for c in res))

PotentialKey = namedtuple('PotentialKey', ['key', 'score'])

def score_keys(ciphertext, n=3):
    keys = (PotentialKey(key=chr(c), score=score_key(chr(c), ciphertext)[1])
            for c in range(256))
    return sorted(keys, key=operator.itemgetter(1), reverse=True)[:n]


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
