class Solution:

    @classmethod
    def parse_claim(cls, claim_str):
        """Parse claim str

        Args:
            claim_str(str):

        Returns:
            dict

        """
        id, claim_opts = claim_str.split('@')
        position, size = claim_opts.split(':')
        row_index, col_index = position.split(',')
        width, height = size.split('x')
        return {
            'id': id.strip(),
            'row_index': int(row_index),
            'col_index': int(col_index),
            'width': int(width),
            'height': int(height),
            'num_row': int(row_index) + int(width),
            'num_col': int(col_index) + int(height),
        }

    @classmethod
    def analyze_fabric(cls):
        """Analyze the fabric"""
        fabric = cls.get_fabric()
        fabric_matrix = fabric['matrix']
        fabric_ids = fabric['ids']

        num_row = len(fabric_matrix)
        num_col = len(fabric_matrix[0])

        # start marking it
        with open('day3/input/claims.txt', 'r') as in_file:
            claims = in_file.readlines()
            for claim_str in claims:
                parsed_claim = cls.parse_claim(claim_str)

                id = parsed_claim['id']
                row_index = parsed_claim['row_index']
                col_index = parsed_claim['col_index']
                width = parsed_claim['width']
                height = parsed_claim['height']

                # start checking each matric cell
                try:
                    for i in range(row_index, row_index + width):
                        for j in range(col_index, col_index + height):
                            curr_cell = fabric_matrix[i][j]

                            if curr_cell == '.':
                                fabric_matrix[i][j] = id
                            else:
                                # add both overlapped ids
                                try:
                                    fabric_ids.remove(curr_cell)
                                except Exception as error:
                                    pass

                                try:
                                    fabric_ids.remove(id)
                                except Exception as error:
                                    pass

                                # mark it as overlapped
                                fabric_matrix[i][j] = '#'
                except Exception as error:
                    print('Failed at ( row {}, col: {} )'.format(i, j))
                    raise error

            # count all overlapped cells
            ret = 0
            for i in range(num_row):
                for j in range(num_col):
                    curr_cell = fabric_matrix[i][j]

                    if curr_cell == '#':
                        ret += 1

            # find one claim that does not overlap by even a single square
            print('Remaining fabric ids: ', fabric_ids)
            print('ID count after mark: ', len(fabric_ids))

    @classmethod
    def get_fabric(cls):
        """Process given fabric

        Returns:
            dict
        """
        num_row = 0
        num_col = 0
        ids = set()
        with open('day3/input/claims.txt', 'r') as in_file:
            claims = in_file.readlines()
            for claim_str in claims:
                parsed_claim = cls.parse_claim(claim_str)
                curr_row_count = parsed_claim['num_row']
                curr_col_count = parsed_claim['num_row']
                id = parsed_claim['id']

                # track all ids
                ids.add(id)

                # update row/col count of this matrix
                num_row = max(num_row, curr_row_count)
                num_col = max(num_col, curr_col_count)

        print('Num row: ', num_row)
        print('Num column: ', num_col)
        print('ID count: ', len(ids))

        fabric_matrix = []
        for i in range(num_row):
            curr_row = []
            for j in range(num_col):
                curr_row.append('.')

            fabric_matrix.append(curr_row)

        return {
            'matrix': fabric_matrix,
            'ids': ids
        }
