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
        has_reactive = True

        while has_reactive:
            has_reactive = False
            i = 1

            while i < len(units):
                if cls.check_reactive(units[i], units[i - 1]):
                    units[i] = -1
                    units[i - 1] = -1
                    has_reactive = True
                    i += 1
                i += 1

            units = [unit for unit in units if unit != -1]
        return units

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
