import sys

state_as_hex_string = sys.argv[1]
state_array = []
for idx in range(0, len(state_as_hex_string), 2):
    entry = state_as_hex_string[idx:idx+2]
    state_array.append(entry)

state_array = [ 'chr(0x{})'.format(entry) for entry in state_array ]

state = []
for row_idx in range(0, 4):
    row = [ state_array[row_idx],
            state_array[row_idx + 4],
            state_array[row_idx + 8],
            state_array[row_idx + 12] ]
    state.append(row)

pretty_rows = [ ', '.join(row) for row in state ]
pretty_rows = [ '[{}]'.format(row) for row in pretty_rows ]
pretty_state = ',\n'.join(pretty_rows)
pretty_state = '[ {} ]'.format(pretty_state)

print(pretty_state)
