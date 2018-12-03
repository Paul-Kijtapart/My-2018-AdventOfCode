from collections import Counter


class Solution:

    @classmethod
    def calc_checksum(cls):
        num_appear_two = 0
        num_appear_three = 0

        with open('day2/input/box_ids.txt', 'r') as in_file:
            box_ids = in_file.readlines()
            for id in box_ids:
                curr_box = cls.check_box_id(id)
                if curr_box['appear_two']:
                    num_appear_two += 1

                if curr_box['appear_tree']:
                    num_appear_three += 1

        return num_appear_two * num_appear_three

    @classmethod
    def check_box_id(cls, id):
        char_counter = Counter(id)
        appear_two = False
        appear_tree = False

        for count in char_counter.values():
            if count == 2:
                appear_two = True
            elif count == 3:
                appear_tree = True

            # if already found both conditions
            if appear_two and appear_tree:
                break

        return {
            'appear_two': appear_two,
            'appear_tree': appear_tree
        }

    @staticmethod
    def get_box_ids():
        with open('day2/input/box_ids.txt', 'r') as in_file:
            box_ids = in_file.readlines()

        return box_ids

    @classmethod
    def get_common_from_boxes(cls):
        box_ids = cls.get_box_ids()

        try:
            matched_boxes = cls.get_matched_boxes(box_ids)

            b1 = matched_boxes['box1']
            b2 = matched_boxes['box2']

            return cls.get_common_chars(b1, b2)
        except Exception as error:
            print(error)

        return ''

    @staticmethod
    def is_diff_by_one(s1, s2):
        """Check if s1 and s2 differ by one char at same position

        Args:
            s1(str):
            s2(str):

        Returns:
            bool - True if s1 and s2 differ by one char at same position
                   False otherwise.

        """
        if len(s1) != len(s2):
            return False

        found_mismatch = False

        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]

            if c1 != c2:
                if found_mismatch:
                    return False
                else:
                    found_mismatch = True

        return True

    @staticmethod
    def get_common_chars(s1, s2):
        """Get common chars between the two strings

        common chars = same char at same location

        Args:
            s1(str):
            s2(str):

        Returns:
            str - common chars between s1 and s2
        """
        if len(s1) != len(s2):
            return False

        common_chars = []
        for i in range(len(s1)):
            c1 = s1[i]
            c2 = s2[i]

            if c1 == c2:
                common_chars.append(c1)

        return ''.join(common_chars)

    @classmethod
    def get_matched_boxes(cls, box_ids):
        """Return two matched box

        matched boxes = two boxes that differs by one char

        Args:
            box_ids(list):

        Returns:
            dict - with two boxes

        Raises:
            Exception - if there is no matched boxes

        """
        checked_boxes = set()
        for i in range(len(box_ids)):
            b1 = box_ids[i]

            # if this box has been processed before
            if b1 in checked_boxes:
                continue

            for j in range(i + 1, len(box_ids)):
                b2 = box_ids[j]
                if cls.is_diff_by_one(b1, b2):
                    return {
                        'box1': b1,
                        'box2': b2,
                    }

            checked_boxes.add(b1)
        raise Exception('No matched boxes')
