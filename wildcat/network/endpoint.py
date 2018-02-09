import json
import numpy as np

from requests_futures.sessions import FuturesSession

from wildcat.util.json_encoder import CompactEncoder


class Endpoint:
    def __init__(self, host=None):
        self.host = host or self.default_host()
        self.session = FuturesSession()
        self.request_precision = 3

    @classmethod
    def default_host(self):
        return "http://api.mdrft.com"

    @classmethod
    def ising_solver_path(self):
        return "/apiv1/ising"

    def dispatch(self, solver, path=None, callback=None):
        path = path or self.ising_solver_path()
        if not (solver.ising_interactions.shape[0] == 0):
            mat = self._build_matrix_for_params(solver.ising_interactions)
            params = {'hami': np.round(mat, self.request_precision).tolist()}
        else:
            raise ValueError('No valid qubo nor ising interactions in the solver.')

        def handle_result(sess, resp):
            if not (callback is None):
                if resp.status_code != 200:
                    print("Server responded: {}".format(resp.content))
                    callback([])
                else:
                    callback(solver.adjust_solutions_from_ising_spins(np.array(resp.json())))

        request = self.session.post(url=self.host + path, headers={'Content-Type': 'application/json'},
                                    data=json.dumps(params, separators=(',', ':'), cls=CompactEncoder),
                                    background_callback=handle_result)

        return request

    def _build_matrix_for_params(self, matrix, strip=False):
        n = matrix.shape[0]
        list = matrix.tolist()
        if strip:
            for i in range(n):
                list[i] = list[i][i:]
        return list
