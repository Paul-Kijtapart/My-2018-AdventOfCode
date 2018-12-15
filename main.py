from day1.Solution import Solution
from day2.Solution import Solution as Solution2
from day3.Solution import Solution as Solution3
from day4.Solution import Solution as Solution4
from day5.Solution import Solution as Solution5
from day6.Solution import Solution as Solution6

# DAY 1
# total_frequency = Solution.sum_frequency_changes()
# print('Sum of all frequency changes: ', total_frequency)
# first_repeated_change = Solution.find_first_repeated_frequency_change()
# print("First repeated frequency change: ", first_repeated_change)

# DAY 2
# checksum for your list of box IDs?
# checksum = Solution2.calc_checksum()
# print('Checksum : ', checksum)
# common = Solution2.get_common_from_boxes()
# print('Common from two boxes: ', common)


# DAY 3
# Solution3.analyze_fabric()

# DAY 4
# Solution4.question_2()

# DAY 5
# polymer = 'dabAcCaCBAcCcaDA'  # Solution5.load_polymer()
# polymer = Solution5.load_polymer()
# print('Total unit count : ', len(polymer))
# units = Solution5.scan_polymer(polymer)
# shortest_polymer = Solution5.find_shortest_polymer(polymer)
# print('Units: {}'.format(units))
# print('Num units: {}'.format(len(units)))
# print('Shortest polymer: ', shortest_polymer)

# DAY 6
# answer1 = Solution6.question_1()


from collections import Counter

def file_cleanup(f):
    coords = []
    max_x = 0
    max_y = 0
    for line in f:
        line = [int(i) for i in line.strip().split(', ')]
        max_x, max_y = max(max_x, line[0]), max(max_y, line[1])
        coords.append((line[1], line[0],))
    return max_x, max_y, coords


def empty_matrix(max_x, max_y):
    return [[(0, 0) for i in range(max_x + 2)] for n in range(max_y + 2)]


def find_closest(coords, max_x, max_y):
    matrix = empty_matrix(max_x, max_y)
    for idx, (x, y) in enumerate(coords):
        matrix[x][y] = (idx+1, 0,)
        for r_idx, row in enumerate(matrix):
            for c_idx, col in enumerate(row):
                dist = abs(x - r_idx) + abs(y - c_idx)
                if col[0] == 0 or dist < col[1]:
                    matrix[r_idx][c_idx] = (idx+1, dist,)
                elif dist == col[1] and col[0] != idx+1:
                    matrix[r_idx][c_idx] = (None, dist,)
    return matrix


with open('day6/input/coordinates.txt', 'r') as f:
    max_x, max_y, coords = file_cleanup(f)

matrix = find_closest(coords, max_x, max_y)

matrix = [[i[0] for i in sublist] for sublist in matrix]
flipped_matrix = matrix[::-1]
to_filter = set(matrix[0] + matrix[-1] + flipped_matrix[0] + flipped_matrix[-1])
list_matrix = []

for row in matrix:
    for col in row:
        if col not in to_filter:
            list_matrix.append(col)


print(Counter(list_matrix).most_common(1)[0][1])