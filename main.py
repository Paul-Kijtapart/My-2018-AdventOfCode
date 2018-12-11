from day1.Solution import Solution
from day2.Solution import Solution as Solution2
from day3.Solution import Solution as Solution3
from day4.Solution import Solution as Solution4
from day5.Solution import Solution as Solution5

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
polymer = Solution5.load_polymer()
units = Solution5.scan_polymer(polymer)
# print('Units: {}'.format(units))
print('Num units: {}'.format(len(units)))
