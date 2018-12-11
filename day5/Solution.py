from collections import Counter


class Solution:

    @classmethod
    def load_polymer(cls):
        with open('day5/input/polymer.txt', 'r') as in_file:
            polymer = in_file.readline()
            return polymer

    @classmethod
    def scan_polymer(cls, polymer):
        """Scan and apply all reactive paris

        Return remaining units after triggering all reactive pairs

        Args:
            polymer (str):

        Returns:
            list

        """
        units = list(polymer)
        ret = []

        for i in range(len(units)):
            if len(ret) == 0:
                ret.append(units[i])
                continue

            peek = ret[-1]
            if cls.check_reactive(peek, units[i]):
                ret.pop()
            else:
                ret.append(units[i])
        return ret

    @classmethod
    def find_shortest_polymer(cls, polymer):
        genes = 'abcdefghijklmnopqrstuvwxyz'  # all possible genes
        shortest = None
        for gen in genes:
            curr_filtered_units = polymer.replace(gen, '').replace(gen.upper(), '')
            curr_scanned_units = cls.scan_polymer(curr_filtered_units)
            shortest = min(shortest, len(curr_scanned_units)) if shortest is not None else len(curr_scanned_units)

        return shortest

    @classmethod
    def check_reactive(cls, g1, g2):
        """Check if g1 is reactive with g2

        g1 is reactive with g2 only if its 'cC' or 'Cc'

        Args:
            g1 (str):
            g2 (str):

        Returns:
            bool

        """
        if g1 == -1 or g2 == -1:
            return False

        return g1 != g2 and g1.lower() == g2.lower()
