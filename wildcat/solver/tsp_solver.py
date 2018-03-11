import numpy as np

# https://arxiv.org/pdf/1702.06248.pdf
from wildcat.solver.qubo_solver import QuboSolver


class TSPSolver(QuboSolver):
    def __init__(self, distance=None, constraints_weight=None):
        self.distance = distance
        self.adjust_constraints_weight()
        if not (constraints_weight is None):
            self.constraints_weight = constraints_weight
        self.cost_hamiltonian = None
        self.constraint_hamiltonian = None
        self.results = []
        super().__init__()

    def adjust_constraints_weight(self):
        if not (self.distance is None):
            self.constraints_weight = self.distance.max() / 2

    def _build_hamiltonian(self):
        if self.ising_interactions.shape[0] == 0:
            self._build_cost_hamiltonian()
            self._build_constraint_hamiltonian()
            self.qubo = self.cost_hamiltonian + self.constraints_weight * self.constraint_hamiltonian

    def _build_cost_hamiltonian(self):
        N = self.distance.shape[0]
        N2 = N * N
        self.cost_hamiltonian = np.zeros((N2, N2), np.float64)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    ik = i * N + k
                    jk_1 = j * N + (k + 1) % N
                    self.cost_hamiltonian[ik][jk_1] += self.distance[i][j]

    def _build_constraint_hamiltonian(self):
        N = self.distance.shape[0]
        N2 = N * N
        self.constraint_hamiltonian = np.zeros((N2, N2), np.float64)
        for i in range(N):
            for j in range(N):
                ij = i * N + j
                ji = j * N + i
                self.constraint_hamiltonian[ij][ij] += -2
                self.constraint_hamiltonian[ji][ji] += -2
                for k in range(N):
                    ik = i * N + k
                    ki = k * N + i
                    self.constraint_hamiltonian[ij][ik] += 1
                    self.constraint_hamiltonian[ji][ki] += 1

    def build_qubo(self):
        self._build_hamiltonian()

    def build_ising_interactions(self):
        self._build_hamiltonian()
        super().build_ising_interactions()

    def humanize_result(self, q):
        N = self.distance.shape[0]
        result = TSPResult(N)
        result.q = q
        for i in range(N):
            for j in range(N):
                k = i * N + j
                if q[k] == 1:
                    result.add_path(i, j, self.distance[i][j])
        result.build_route()
        return result

    def solve_until_success(self, callback, endpoint=None, success_count=1):
        self.results = []

        def inner_callback(q):
            result = self.humanize_result(q)
            if not result.success:
                solve_once()
            else:
                self.results.append(result)
                if len(self.results) < success_count:
                    solve_once()
                else:
                    self.results = sorted(self.results, key=lambda r: r.distance())
                    callback(self.results)

        def solve_once():
            future = self.solve(inner_callback, endpoint=endpoint)
            future.result()

        solve_once()


class TSPDistanceBuilder2D:
    def __init__(self):
        self.cities = []
        pass

    def add_point(self, x, y):
        self.cities.append((x, y))

    def build(self):
        N = len(self.cities)
        distances = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                if i != j:
                    distances[i][j] = self.distance2D(self.cities[i], self.cities[j])

        return distances

    def distance2D(self, point1, point2):
        dx = point1[0] - point2[0]
        dy = point1[1] - point2[1]
        return np.sqrt(dx * dx + dy * dy)

    def plot(self, result):
        import matplotlib.pyplot as plt

        x = []
        y = []
        for path in result.sorted_paths:
            x.append(self.cities[path[0]][0])
            y.append(self.cities[path[0]][1])
        x.append(self.cities[result.sorted_paths[-1][1]][0])
        y.append(self.cities[result.sorted_paths[-1][1]][1])

        plt.plot(x, y, 'co')

        # Set a scale for the arrow heads (there should be a reasonable default for this, WTF?)
        a_scale = float(max(x) - min(x)) / float(100)

        # Draw the older paths, if provided

        # Draw the primary path for the TSP problem
        plt.arrow(x[-1], y[-1], (x[0] - x[-1]), (y[0] - y[-1]), head_width=a_scale,
                  color='g', length_includes_head=True)
        for i in range(0, len(x) - 1):
            plt.arrow(x[i], y[i], (x[i + 1] - x[i]), (y[i + 1] - y[i]), head_width=a_scale,
                      color='g', length_includes_head=True)

        # Set axis too slitghtly larger than the set of x and y
        plt.xlim(min(x) - 1, max(x) + 1)
        plt.ylim(min(y) - 1, max(y) + 1)
        plt.show()


class TSPResult:
    def __init__(self, N):
        self.q = None
        self.paths = []
        self.success = False
        self.total_distance = 0
        self.sorted_paths = []
        self.N = N
        pass

    def add_path(self, from_, to_, distance):
        self.paths.append((from_, to_, distance))

    def _first_true(self, iterable, default=False, pred=None):
        return next(filter(pred, iterable), default)

    def build_route(self):
        current_city = 0
        self.sorted_paths = []
        used = []
        ok = True
        for i in range(self.N - 1):
            path = self._first_true(self.paths, None, lambda p: p[0] == current_city)
            if not (path is None) and not (path[1] in used):
                used.append(path[0])
                self.sorted_paths.append(path)
                current_city = path[1]
            else:
                ok = False
                break
        self.success = ok

    def distance(self):
        d = 0
        for path in self.paths:
            d += path[2]
        return d

    def __str__(self):
        return "{0}: {1} <- {2}".format(self.success, self.sorted_paths, self.paths)
