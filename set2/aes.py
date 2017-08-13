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

def mix_columns(state):
    pass

MAX_BYTE = 255
MINIMAL_POLYNOMIAL = 0x1b

def _multiply_by_x(p):
    product = p << 1
    if product > MAX_BYTE:
        product ^ MINIMAL_POLYNOMIAL
    return product

def _multiply(p, q):
    product = 0
    
