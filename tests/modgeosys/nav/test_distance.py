from modgeosys.nav.distance import manhattan_distance, euclidean_distance


def test_manhattan_distance_between_identical_points_is_zero():
    point = (1.0, 2.0)
    assert manhattan_distance(point, point) == 0.0


def test_manhattan_distance_between_points_on_same_axis_is_absolute_difference():
    point_a = (1.0, 2.0)
    point_b = (1.0, 5.0)
    assert manhattan_distance(point_a, point_b) == 3.0

def test_manhattan_distance_between_points_on_different_axes_is_sum_of_absolute_differences():
    point_a = (0.0, 0.0)
    point_b = (1, 1)
    assert manhattan_distance(point_a, point_b) == 2


def test_euclidean_distance_between_identical_points_is_zero():
    point = (1.0, 2.0)
    assert euclidean_distance(point, point) == 0.0


def test_euclidean_distance_between_points_on_same_axis_is_absolute_difference():
    point_a = (1.0, 2.0)
    point_b = (1.0, 5.0)
    assert euclidean_distance(point_a, point_b) == 3


def test_euclidean_distance_follows_pythagorean_theorem():
    point_a = (0.0, 0.0)
    point_b = (3.0, 4.0)
    assert euclidean_distance(point_a, point_b) == 5.0
