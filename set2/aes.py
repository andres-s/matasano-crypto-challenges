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
