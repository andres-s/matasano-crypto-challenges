# Break repeating-key XOR
# =======================

# The file 6.txt has been base64'd after being encrypted with repeating-key XOR.

# Decrypt it.

# Here's how:

# 1.  Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
# 2.  Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:

#     this is a test

#     and

#     wokka wokka!!!

#     is 37. Make sure your code agrees before you proceed.

# 3.  For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second
#     KEYSIZE worth of bytes, and find the edit distance between them. 
#     Normalize this result by dividing by KEYSIZE.
# 4.  The KEYSIZE with the smallest normalized edit distance is probably the
#     key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or
#     take 4 KEYSIZE blocks instead of 2 and average the distances.
# 5.  Now that you probably know the KEYSIZE: break the ciphertext into
#     blocks of KEYSIZE length.
# 6.  Now transpose the blocks: make a block that is the first byte of every
#     block, and a block that is the second byte of every block, and so on.
# 7.  Solve each block as if it was single-character XOR. You already have
#     code to do this.
# 8.  For each block, the single-byte XOR key that produces the best looking
#     histogram is the repeating-key XOR key byte for that block. Put them
#     together and you have the key.

# This code is going to turn out to be surprisingly useful later on. Breaking
# repeating-key XOR ("Vigenere") statistically is obviously an academic
# exercise, a "Crypto 101" thing. But more people "know how" to break it than
# can actually break it, and a similar technique breaks something much more
# important. 


import codecs
import operator
import challengeutils as utes

with open('6.txt') as fp:
    input = fp.readlines()

input = ''.join(line.strip() for line in input)
input = codecs.decode(input, 'base64')


def normalised_dist(keysize, num_comparisons, s):
    blocks = list(s[i*keysize:(i+1)*keysize] for i in range(2*num_comparisons))
    block_pairs = zip(blocks[::2], blocks[1::2])
    dists = map(lambda (fst, snd): utes.hamming_dist(fst, snd), block_pairs)
    return float(sum(dists)) / float(len(dists) * keysize)


keysize_dists = ((ksize, normalised_dist(ksize, 4, input))
                 for ksize in range(2, 41))
candidate_keysizes = sorted(keysize_dists,
                            key=operator.itemgetter(1))[:3]

for ksize, ksize_score in candidate_keysizes:
    transposed_blocks = []
    for i in range(ksize):
        transposed_blocks.append(''.join(input[i::ksize]))

    key = ''.join(utes.score_keys(txt, n=1)[0][0] for txt in transposed_blocks)

    print(("For keysize {}, the best looking key is {}, "
           "which decrypts text to:").format(ksize, key))
    print(utes.repeating_key_xor(key, input[:50]) + "...\n")

THE_KEY = 'Terminator X: Bring the noise'
print('The key "{}" decrypts the text to:'.format(THE_KEY))
print(utes.repeating_key_xor(THE_KEY, input))
