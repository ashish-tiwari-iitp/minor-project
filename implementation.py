from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import numpy as np

class CloudAutoScalingProblem(Problem):

    def __init__(self):
        super().__init__(n_var=1, n_obj=4, n_constr=0, xl=np.array([1]), xu=np.array([100]))

    def _evaluate(self, x, out, *args, **kwargs):
        num_servers = x
        cpu_usage = num_servers**2  # Objective 1: Minimize CPU usage
        memory_usage = num_servers**2.5  # Objective 2: Minimize memory usage
        throughput = 1 / num_servers  # Objective 3: Maximize throughput
        response_time = num_servers**1.5  # Objective 4: Minimize response time

        out["F"] = np.column_stack([cpu_usage, memory_usage, -throughput, response_time])

problem = CloudAutoScalingProblem()

algorithm = NSGA2(pop_size=100)
res = minimize(problem, algorithm, ('n_gen', 200), seed=1, verbose=False)

plot = Scatter()
plot.add(res.F, label="Optimal Solutions", color="red")
plot.show()
