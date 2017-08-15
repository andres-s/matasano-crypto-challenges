from set2.substitutionbox import AES_SUBSTITUTION_BOX

class AES128:
    def __init__(self, key):
        self._key = key

    def encrypt(self, plaintext):
        pass

    def decrypt(self, ciphertext):
        pass

#  def aes128(block, key):
    #  state = block

    #  add_round_key(state, ???)

    #  NUM_ROUNDS = 10
    #  for round in range(NUM_ROUNDS - 1):
        #  state = sub_bytes(state)
        #  state = shift_rows(state)
        #  state = mix_columns(state)
        #  state = add_round_key(state, ???)

    #  state = sub_bytes(state)
    #  state = shift_rows(state)
    #  state = add_round_key(state, ???)

    #  return state

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
