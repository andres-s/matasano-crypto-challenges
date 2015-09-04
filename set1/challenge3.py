# Single-byte XOR cipher

# The hex encoded string:

# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

# ... has been XOR'd against a single character. Find the key, decrypt the message.

# You can do this by hand. But don't: write code to do it for you.

# How? Devise some method for "scoring" a piece of English plaintext. Character
# frequency is a good metric. Evaluate each output and choose the one with the best score. 

import codecs
import operator
import challengeutils as utes

CIPHER_TEXT = codecs.decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736',
                           'hex')

def score_key(key, ciphertext):
    key = key * len(ciphertext)
    res = utes.xor(key, ciphertext)
    return (res, sum(1 for c in res if c in ('a', 'e', 'i', 'o', 'u')))

scores = {}
for c in range(256):
    c_chr = chr(c)
    plaintext, score = score_key(c_chr, CIPHER_TEXT)
    scores[(c_chr, plaintext)] = score

for key, score in sorted(scores.items(), key=operator.itemgetter(1))[-10:]:
    c, plaintext = key
    print str(c) + " has score " + str(score) + " and plaintext " + plaintext

# Outputs key ('X') at the bottom:
#
# ↨ has score 6 and plaintext ♀  $&!(o☻♀h<o#&$*o.o? :!+o )o-., !
# ◄ has score 6 and plaintext
# &&" '.i♦
# n:i% ",i(i9&<'-i&/i+(*&'
# ↓ has score 6 and plaintext ☻..*(/&a♀☻f2a-(*$a a1.4/%a.'a# "./
# ↔ has score 6 and plaintext ♠**.,+"♠b6e),. e$e5*0+!e*#e'$&*+
#  has score 6 and plaintext ▬::><;2u↑▬r&u9<>0u4u%: ;1u:3u746:;
# B has score 7 and plaintext Yuuqst}:WY=i:vsq⌂:{:juot~:u|:x{yut
# R has score 9 and plaintext Ieeacdm*GI-y*fcao*k*ze⌂dn*el*hkied
# ^ has score 10 and plaintext Eiimoha&KE!u&jomc&g&vishb&i`&dgeih
# V has score 10 and plaintext Maaeg`i.CM)}.bgek.o.~a{`j.ah.loma`
# X has score 11 and plaintext Cooking MC's like a pound of bacon
#