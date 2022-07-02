""" Displays a comparison of the two pathplanning algorithms statistics. """

from typing import List, Dict, Tuple, Callable
import sys

from src.pathplanning.parcellisation import Field, parse_input_file

class PathData:
    """ Represents the travel time data for one set of parameters, when running
        one of the algorithm on a field.

        Attributes:
            total_time: Total travel time
            straight_time: Travel time on the straights
            rotation_time: Travel time during rotations
    """
    def __init__(self): # TODO
        self.total_time: float = ...
        self.straight_time: float = ...
        self.rotation_time: float = ...


class AlgoStats:
    """ Represents the travel times statistics of an algorithm.

        Attributes:
            total_time: stats on the total travel times
            straights_time: stats on the travel times for the straights
            rotations_time: stats on the travel times for the rotations
    """

    class Stats:
        """ Represents statistics data.

            Attributes:
                mean
                median
                first_quartile
                third_quartile
        """
        def __init__(self): # TODO
            self.mean: float = ...
            self.median: float = ...
            self.first_quartile: float = ...
            self.third_quartile: float = ...


    def __init__(self, algo_data: List[PathData]): # TODO
        self.total_time = self.Stats(...)
        self.straights_time = self.Stats(...)
        self.rotations_time = self.Stats(...)


def get_sets_of_parameters() -> List[Dict[str, float]]:
    """ Returns the list of parameters sets to compute the travel times.

        These sets can be configured in:
        pathplanning_comparison_parameters_sets.py

        Raises:
            ValueError: The list of parameters sets is empty.
    """
    from algorithm_comparison.pathplanning_comparison_parameters_sets import \
        parameters_set
    if parameters_set == []:
        raise ValueError('The list of parameters sets is empty.')
    return parameters_set


def get_data_for_field(field: Field) -> Tuple[List[PathData]]:
    """ Runs both algorithms for a field for each set of parameters.

        Args:
            field: the Field object on which to run the algorithms.

        Returns: A tuple (data_alg_1, data_alg_2), with data_alg_n being a
            list of PathData objects, each of these PathData having been
            generated using one set of parameters.
    """
    alg_1 = ... # TODO
    alg_2 = ...

    data_alg_1: List[PathData] = run_algorithm_on_field(field, alg_1)
    data_alg_2: List[PathData] = run_algorithm_on_field(field, alg_2)

    return (data_alg_1, data_alg_2)


def run_algorithm_on_field(field: Field, algorithm: Callable) -> List[PathData]:
    """ Runs an algorithm for a Field object.

        Args:
            field: Field object on which to run the algorithm
            algorithm: Function corresponding to the algorithm to apply to the
                field.

        Returns: A list of PathData objects, each of them corresponding to a
            set of parameters.
    """
    parameters_sets: List[Dict[str, float]] = get_sets_of_parameters()
    path_data_list: List[PathData] = []

    for parameter_set in parameters_sets:
        # Run algorithm on Field with set of parameters: # TODO
        path_data: PathData = ...
        path_data_list.append(path_data)

    return path_data_list


def display_results(stats_alg_1: AlgoStats, stats_alg_2: AlgoStats) -> None:
    """ Displays a comparison of the algorithms statistics.

        Args:
            stats_alg_1: statistics on the first algorithm
            stats_alg_2: statistics on the second algorithm
    """
    # Use str() of AlgoStats?
    ... # TODO


def main() -> int:
    """ Main function of the pathplanning algorithms comparison. """

    # Getting the list of the files containing the fields' polygons:
    filepaths: List[str] = ... # TODO

    # These will store the travel times data used for the stats:
    data_alg_1: List[PathData] = []
    data_alg_2: List[PathData] = []

    # For each file, we create the field and get the travel times data:
    for filepath in filepaths:
        field_polygons = parse_input_file(filepath)
        field = Field(field_polygons)
        field_data_alg_1, field_data_alg_2 = get_data_for_field(field)
        data_alg_1.append(field_data_alg_1)
        data_alg_2.append(field_data_alg_2)

    # For both algorithm data list, we compute the statistics:
    stats_alg_1: AlgoStats(data_alg_1)
    stats_alg_2: AlgoStats(data_alg_2)

    display_results(stats_alg_1, stats_alg_2)

    sys.exit(0)


if __name__ == "__main__":
    main()
