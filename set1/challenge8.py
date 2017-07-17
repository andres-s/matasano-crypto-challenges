# The answer is line 132:
#   d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a
# It is the only line with a repeated block,
#   08649af70dc06f4fd5d2d69c744cd283
# occurs 4 times

from collections import defaultdict

NUM_BITS_IN_BLOCK = 16 * 8
NUM_BITS_PER_HEX_CHARACTER = 4
NUM_HEX_CHARACTERS_IN_BLOCK = NUM_BITS_IN_BLOCK / NUM_BITS_PER_HEX_CHARACTER

with open('8.txt') as fp:
    hex_encoded_lines = fp.readlines()

hex_encoded_lines = map(lambda s: s.strip(), hex_encoded_lines)

all_block_counts = []
for line_number, line in enumerate(hex_encoded_lines):
    block_counts = defaultdict(int)
    idx = 0
    while idx < len(line):
        block = line[idx:idx + NUM_HEX_CHARACTERS_IN_BLOCK]
        block_counts[block] += 1
        idx += NUM_HEX_CHARACTERS_IN_BLOCK
    all_block_counts.append((line_number, line, block_counts))

all_block_counts.sort(key=(lambda t: len(t[2])))
