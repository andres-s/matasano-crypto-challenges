from set2.substitutionbox import AES_SUBSTITUTION_BOX

RCON_SIZE = 11

class AES128:
    def __init__(self, key):
        self._key = key
        self._expanded_key = expand_key(self._key, num_rounds??)
        self._RCON = _build_rcon()

    def encrypt(self, plaintext):
        pass

    def decrypt(self, ciphertext):
        pass

    def _expanded_key(self):
        if self._exp

def aes128(block, key):
    state = block

    add_round_key(state, ???)

    NUM_ROUNDS = 10
    for round in range(NUM_ROUNDS - 1):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, ???)

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, ???)

    return state

def expand_key(key, num_rounds):
    num_words_in_key = len(key) // 4
    expanded_key_in_uint32 = []
    for key_idx in range(0, len(key), 4):
        uint32_word = (ord(key[key_idx]) << 24) + (ord(key[key_idx + 1]) << 16) +
                      (ord(key[key_idx + 2]) << 8) + ord(key[key_idx + 3])
        expanded_key_in_uint32.append(uint32_word)

    num_words_in_expanded_key = STATE_NUM_UINT32 * (num_rounds + 1)
    for key_idx in range(num_words_in_key, num_words_in_expanded_key):
        temp = expanded_key_in_uint32[-1]
        if key_idx % num_words_in_key == 0:
            round_constant = self._RCON[key_idx/num_words_in_key - 1]
            temp = _sub_word(_rot_word(temp)) ^ round_constant
        else if num_words_in_key > 6 and key_idx % num_words_key == 4:
            temp = _sub_word(temp)
        next_uint32 = temp ^ expanded_key_in_uint32[key_idx - num_words_in_key]
        expanded_key_in_uint32.append(next_uint32)

    expanded_key = []
    for uint32_word in expanded_key_in_uint32:
        for bite in _uint32_word_to_chr_array(uint32_word):
            expanded_key.append(bite)

    return expanded_key

def _sub_word(word_uint32):
    bites = []
    for bit_offset in [24, 16, 8, 0]:
        bite = (word_uint32 >> bit_offset) & 0xff
        bites.append(bite)

    bites = [ord(AES_SUBSTITUTION_BOX[chr(bite)]) for bite in bites]

    sub_word = 0
    for bite in bites:
        sub_word = (sub_word << 8) + bite

    return sub_word

def _rot_word(word_uint32):
    bottom_24_bits = word_uint32 & 0x00ffffff
    top_8_bits = word_uint32 >> 24
    return (bottom_24_bits << 8) + top_8_bits

def _build_rcon():
    uint32_words = [1 << 24]
    top_8_bits = 1
    for _ in range(1, RCON_SIZE):
        uint32_word = top_8_bits << 24
        uint32_words.append(uint32_word)
        top_8_bits = _multiply_by_x(top_8_bits)
    return uint32_words

def _uint32_word_to_chr_array(word):
    return [
        chr(word >> 24),
        chr((word >> 16) & 0xff),
        chr((word >> 8) & 0xff),
        chr(word & 0xff),
    ]

def sub_bytes(state):
    next_state = [[AES_SUBSTITUTION_BOX[b] for b in row] for row in state]
    return next_state

def shift_rows(state):
    next_state = [
        state[0],
        _cycle_row_left(state[1], 1),
        _cycle_row_left(state[2], 2),
        _cycle_row_left(state[3], 3),
    ]
    return next_state

def _cycle_row_left(arr, cycle_distance):
    return arr[cycle_distance:] + arr[0:cycle_distance]

STATE_NUM_ROWS = 4
STATE_NUM_COLS = 4

def mix_columns(state):
    next_state = [4 * [None], 4 * [None], 4 * [None], 4 * [None]]
    for col_idx in range(0, STATE_NUM_COLS):
        mixed_column = _mix_column(state, col_idx)
        _set_column(next_state, col_idx, mixed_column)
    return next_state

def _mix_column(state, col_idx):
    col= (
        ord(state[0][col_idx]),
        ord(state[1][col_idx]),
        ord(state[2][col_idx]),
        ord(state[3][col_idx]),
    )
    return (
        chr(_multiply(2, col[0]) ^ _multiply(3, col[1]) ^ col[2] ^ col[3]),
        chr(col[0] ^ _multiply(2, col[1]) ^ _multiply(3, col[2]) ^ col[3]),
        chr(col[0] ^ col[1] ^ _multiply(2, col[2]) ^ _multiply(3, col[3])),
        chr(_multiply(3, col[0]) ^ col[1] ^ col[2] ^ _multiply(2, col[3])),
    )

def _set_column(state, col_idx, new_column):
    for row_idx in range(0, STATE_NUM_ROWS):
        state[row_idx][col_idx] = new_column[row_idx]

MAX_BYTE = 255
MINIMAL_POLYNOMIAL = 0x11b

def _multiply_by_x(p):
    # p is in the polynomial field F(2**8)
    product = p << 1
    if product > MAX_BYTE:
        product = product ^ MINIMAL_POLYNOMIAL
    return product

def _multiply(p, q):
    # p, q are in the polynomial field F(2**8)
    product = 0
    curr_term = p
    while q > 0:
        if q & 1 == 1:
            product = product ^ curr_term
        curr_term = _multiply_by_x(curr_term)
        q = q >> 1
    return product

def add_round_key(state, round_key):
    next_state = [4 * [None], 4 * [None], 4 * [None], 4 * [None]]
    for col_idx in range(STATE_NUM_COLS):
        for row_idx in range(STATE_NUM_ROWS):
            old = ord(state[row_idx][col_idx])
            key = ord(round_key[STATE_NUM_ROWS * col_idx + row_idx])
            next_state[row_idx][col_idx] = chr(old ^ key)
    return next_state
