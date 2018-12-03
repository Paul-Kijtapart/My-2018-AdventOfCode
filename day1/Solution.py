class Solution:

    @staticmethod
    def sum_frequency_changes():
        """Sum all frequency changes in the 'day1/input/frequencyChanges.txt'

        Returns:
            int
        """
        ret = 0
        with open('day1/input/frequencyChanges.txt', 'r') as in_file:
            frequency_change_list = in_file.readlines()
            for fc in frequency_change_list:
                current_change = int(fc)
                ret += current_change
        return ret

    @staticmethod
    def find_first_repeated_frequency_change():
        """Find first repeated frequency change in 'day1/input/frequencyChanges.txt'

        Returns:
            int - first repeated frequency change
            None - otherwise
        """
        appeared = set()
        ret = 0
        loop_index = 0
        max_loop = 500
        while True:
            loop_index += 1

            if loop_index == max_loop:
                print('Cannot find first repeated change from {} loops'.format(max_loop))
                return None

            with open('day1/input/frequencyChanges.txt', 'r') as in_file:
                frequency_change_list = in_file.readlines()
                for fc in frequency_change_list:
                    current_change = int(fc)
                    ret += current_change
                    if ret in appeared:
                        return ret
                    else:
                        appeared.add(ret)
