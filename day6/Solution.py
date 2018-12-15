from collections import Counter, namedtuple
import math
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{x},{y}'.format(x=self.x, y=self.y)

    def __repr__(self):
        return '({x},{y})'.format(x=self.x, y=self.y)

    def __hash__(self):
        return self.x ^ self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def calc_dist_from(self, marked_point):
        return math.sqrt((self.x - marked_point.x) ** 2 + (self.y - marked_point.y) ** 2)


class Solution:

    @classmethod
    def load_points(cls):
        all_points = []
        with open('day6/input/coordinates.txt', 'r') as in_file:
            all_point_str = in_file.readlines()
            for point_str in all_point_str:
                new_point = cls.parse_point(point_str)
                all_points.append(new_point)

        return all_points

    @classmethod
    def create_matrix(cls):
        matrix = dict()

        # ensure we're processing unique points here
        all_points = cls.load_points()
        unique_points = set(all_points)

        # calc matrix stats
        matrix_stats = cls.calc_matrix_stats(unique_points)

        # start building from unique points and stats
        start_x = matrix_stats['start_x']
        start_y = matrix_stats['start_y']
        end_x = matrix_stats['end_x']
        end_y = matrix_stats['end_y']
        num_column = matrix_stats['num_column']
        num_row = matrix_stats['num_row']

        for col in range(start_x, end_x):
            for row in range(start_y, end_y):
                curr_point = Point(x=col, y=row)
                closest_dist = num_column + num_row
                filled_point = None

                # start looking for filled point
                for marked_point in unique_points:
                    curr_dist = curr_point.calc_dist_from(marked_point)
                    if curr_dist < closest_dist:
                        closest_dist = curr_dist
                        filled_point = marked_point
                    elif curr_dist == closest_dist:
                        filled_point = None

                # fill it in
                matrix[curr_point] = filled_point

        return {
            'matrix': matrix,
            'stats': matrix_stats
        }

    @classmethod
    def question_1(cls):
        matrix_data = cls.create_matrix()
        matrix = matrix_data['matrix']
        matrix_stats = matrix_data['stats']
        point_counter = Counter(matrix.values())
        corner_points = cls.get_corner_points(matrix, matrix_stats)

        valid_areas = [{'coord': coord, 'count': count} for coord, count in point_counter.items() if coord not in corner_points]
        print(valid_areas)
        print('gg')

    @classmethod
    def parse_point(cls, point_str):
        x, y = point_str.strip().split(',')
        return Point(x=int(x), y=int(y))

    @classmethod
    def calc_matrix_stats(cls, points):
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0

        for point in points:
            # check x
            min_x = min(min_x, point.x)
            max_x = max(max_x, point.x)

            # check y
            min_y = min(min_y, point.y)
            max_y = max(max_y, point.y)

        return {
            'start_x': min_x,
            'start_y': min_y,
            'end_x': max_x,
            'end_y': max_y,
            'num_column': max_y - min_y,
            'num_row': max_x - min_x
        }

    @classmethod
    def get_corner_points(cls, matrix, matrix_stats):
        start_x = matrix_stats['start_x']
        start_y = matrix_stats['start_y']
        end_x = matrix_stats['end_x']
        end_y = matrix_stats['end_y']
        corner_points = set()

        for point in matrix:
            if start_x == point.x or \
                    start_y == point.y or \
                    end_x == point.x or \
                    end_y == point.y:
                corner_points.add(point)

        return corner_points
