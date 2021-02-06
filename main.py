import numpy as np

# The following code outputs an odometer based on a base and number of permutations

base = 6
permutations = 7
rows = np.power(base, permutations)
odo = np.empty([permutations, rows])

for a in range(rows):
    i = permutations-1
    for n in range(permutations):
        odo[n][a] = (int((a%(int(rows/(np.power(base, n)))))/np.power(base, i)))%base
        i -= 1

for j in range(rows):
    output_str = ""
    for i in range(permutations):
        output_str += f'{int(odo[i][j])} '
    print(output_str)