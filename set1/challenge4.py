# Detect single-character XOR
# ===========================

# One of the 60-character strings in 4.txt has been encrypted by
# single-character XOR.

# Find it. 

import codecs
import operator
import challengeutils as utes

REL_FREQS = {
    'th': 36,
    'he': 31,
    'in': 24,
    'er': 21,
    'an': 20,
    're': 19,
    'on': 18,
}

with open('4.txt') as fp:
    cipher_texts = fp.readlines()

cipher_texts = map(lambda s: codecs.decode(s.strip(), 'hex'), cipher_texts)
cipher_texts = list(enumerate(cipher_texts))

xored_texts = []
for idx, txt in cipher_texts:
    for c in range(256):
        xored_txt, score = utes.bigrams_score_key(chr(c), txt,
                                                  targets=REL_FREQS)
        xored_texts.append((idx, chr(c), score, xored_txt))

for cipher_idx, key, score, xored_text in \
    sorted(xored_texts, key=operator.itemgetter(2), reverse = True)[:10]:
    print "XORing cipher text " + str(cipher_idx) + " with key " + key + \
        " has score " + str(score) + " XORed text " + xored_text



# The text is "Now that the party is jumping\n"

# XORing cipher text 170 with key § has score 127 XORed text nOW THAT THE PARTY IS JUMPING*
# XORing cipher text 170 with key 5 has score 127 XORed text Now that the party is jumping

# XORing cipher text 230 with key M has score 103 XORed text X_z\THAA\☼i↨M☻N{↔♣U}nGThE◄WZjk
# XORing cipher text 230 with key m has score 103 XORed text x⌂Z|thaa|/I7m"n[=%u]NgtHe1wzJK
# XORing cipher text 151 with key F has score 72 XORed text A♀Thª]QUed´►JóTHq▲mbºE)»yv
# XORing cipher text 151 with key f has score 72 XORed text a,tHå}qux(t(ED¤0jéthQ>MBçe    ÅYV
# XORing cipher text 16 with key G has score 67 XORed text WMv☼OHe8íMThKWñ▒z]→⌂¼♠♂´»hlB
# XORing cipher text 16 with key g has score 67 XORed text wmV/ohE↑ümtHkwp(äæZ}:_î&+¤ÅHLb
# XORing cipher text 84 with key S has score 67 XORed text yo←↓F↕^hEd♫§6tH☼▼┤¢d[nm☻x▬s∟DÑ
# XORing cipher text 84 with key s has score 67 XORed text YO;9f2~HeD.5▬Th/?öØD{NM"X6S<dà