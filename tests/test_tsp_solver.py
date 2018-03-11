import numpy as np

from wildcat.annealer.simulated.simulated_annealer import SimulatedAnnealer
from wildcat.annealer.simulated.single_spin_flip_strategy import SingleSpinFlipStrategy
from wildcat.annealer.simulated.temperature_schedule import TemperatureSchedule
from wildcat.network.local_endpoint import LocalEndpoint
from wildcat.solver.tsp_solver import TSPSolver, TSPDistanceBuilder2D
from wildcat.util.matrix import random_symmetric_positive_matrix


def test_initialize_tsp_solver():
    assert not TSPSolver() is None

def test_initialize_tsp_solver_with_distance():
    solver = TSPSolver(distance=random_symmetric_positive_matrix(size=10))
    solver.build_ising_interactions()
    assert not (solver.ising_interactions is None)
    assert solver.ising_interactions.shape[0] != 0

def test_tsp_solver_response_is_binary():
    solver = TSPSolver(distance=random_symmetric_positive_matrix(size=10))

    def callback(result):
        print(result)
        print(solver.humanize_result(result))
        assert not (result is None)
        assert (result >= 0).all() and (result <= 1).all()

    future = solver.solve(callback)
    assert (future.result().status_code == 200)

def test_tsp_distance_builder():
    builder = TSPDistanceBuilder2D()
    builder.add_point(0, 0)
    builder.add_point(10, 10)
    builder.add_point(2, 20)

    distance = builder.build()
    print(distance)
    assert distance.shape[0] != 0


def test_tsp_solver():
    positions = np.array((
        (24050.0000, 123783),
        (24216.6667, 123933),
        (24233.3333, 123950),
        (24233.3333, 124016),
        (24250.0000, 123866),
        (24300.0000, 123683),
        (24316.6667, 123900),
        (24316.6667, 124083),
        (24333.3333, 123733),
    ))
    builder = TSPDistanceBuilder2D()
    for position in positions:
        builder.add_point(position[0], position[1])
    solver = TSPSolver(distance=builder.build(), constraints_weight=1000)

    def callback(q):
        result = solver.humanize_result(q)
        # print(result)
        # print("Distance: {0}".format(result.distance()))
        # print("Energy: {0}".format(solver.qubo_energy(q)))
        if not result.success:
            future = solver.solve(callback, endpoint=local_endpoint)
            future.result()
        else:
            assert result.distance() > 0

    schedule = TemperatureSchedule(initial_temperature=1000, last_temperature=0.1, scale=0.8)
    strategy = SingleSpinFlipStrategy(repetition=10)
    annealer = SimulatedAnnealer(schedule=schedule, strategy=strategy)
    local_endpoint = LocalEndpoint(annealer=annealer)

    future = solver.solve(callback, endpoint=local_endpoint)
    future.result()

def test_tsp_plot():
    positions = np.array((
        (24050.0000, 123783),
        (24216.6667, 123933),
        (24233.3333, 123950),
        (24233.3333, 124016),
        (24250.0000, 123866),
        (24300.0000, 123683),
        (24316.6667, 123900),
        (24316.6667, 124083),
        (24333.3333, 123733),
    ))
    builder = TSPDistanceBuilder2D()
    for position in positions:
        builder.add_point(position[0], position[1])
    solver = TSPSolver(distance=builder.build(), constraints_weight=1000)

    def callback(q):
        result = solver.humanize_result(q)
        print(result)
        print("Distance: {0}".format(result.distance()))
        print("Energy: {0}".format(solver.qubo_energy(q)))
        if not result.success:
            future = solver.solve(callback, endpoint=local_endpoint)
            future.result()
        else:
            builder.plot(result)
            assert result.distance() > 0

    schedule = TemperatureSchedule(initial_temperature=1000, last_temperature=0.1, scale=0.8)
    strategy = SingleSpinFlipStrategy(repetition=10)
    annealer = SimulatedAnnealer(schedule=schedule, strategy=strategy)
    local_endpoint = LocalEndpoint(annealer=annealer)

    future = solver.solve(callback, endpoint=local_endpoint)
    future.result()