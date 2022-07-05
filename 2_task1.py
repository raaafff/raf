from math import sqrt
from itertools import permutations

points = {
    'point1': [0, 1],
    'point2': [4, 1],
    'point3': [7, 2],
    'point4': [5, 5],
    'point5': [1, 4]}

start = 'point1'


def dist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return sqrt(dx * dx + dy * dy)


def distances_matrix(points_cords):
    dm_result = {}
    for point1, cords1 in points_cords.items():
        dm_result[point1] = {}
        for point2, cords2 in points_cords.items():
            dm_result[point1][point2] = dist(cords1, cords2)
    return dm_result


def path_length(path_points, dist_matrix, print_results=False):
    result_length = 0
    i = 0
    while i < len(path_points) - 1:
        point1 = path_points[i]
        point2 = path_points[i + 1]
        result_length += dist_matrix[point1][point2]
        if print_results:
            print(f"{point1} -> {point2} distance: {dist_matrix[point1][point2]}.")
        i += 1
    if print_results:
        print(f"Total distance: {result_length}.")
    return result_length


if __name__ == '__main__':

    min_path_length = 0
    min_path = ()
    dm = distances_matrix(points)
    transitional_points = points.copy()
    transitional_points.pop(start)
    transitional_paths = permutations(transitional_points.keys(), len(transitional_points))

    for path in transitional_paths:
        path = (start,) + path + (start,)
        cur_path_length = path_length(path, dm)
        if min_path_length == 0 or cur_path_length < min_path_length:
            min_path_length = cur_path_length
            min_path = path

    path_length(min_path, dm, print_results=True)
