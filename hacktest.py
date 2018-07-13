import numpy as np
from sigopt_wrapper import optimize
from hack import generate_token

parameters = [
    dict(name='x', type='double', bounds=dict(min=0.0, max=1.4)),
    dict(name='y', type='double', bounds=dict(min=0.0, max=1.4)),
    ]


@optimize(generate_token(True), "Fake Optimization", parameters, 30, True)
def evaluate(assignments):
    return np.sin(np.pi * assignments['x']) * np.sin(np.pi * assignments['y'])

