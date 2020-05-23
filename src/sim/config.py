
from cadCAD.configuration import append_configs
from cadCAD.configuration.utils import config_sim
# if test notebook is in parent above /src
from .model.state_variables import genesis_states
from .model.partial_state_update_block import partial_state_update_block #, partial_state_update_block_B
from .model.sys_params import sys_params #as sys_params_A
from .model.utils import *

from copy import deepcopy
from cadCAD import configs
import scipy.stats as stats
import networkx as nx
import numpy as np

# if test notebook is in /src
# from model.state_variables import genesis_states
# from model.partial_state_update_block import partial_state_update_block
# from model.sys_params import sys_params as sys_params_A

from .sim_setup import SIMULATION_TIME_STEPS, MONTE_CARLO_RUNS

sim_config = config_sim (
    {
        'N': MONTE_CARLO_RUNS, 
        'T': range(SIMULATION_TIME_STEPS), # number of timesteps
        'M': sys_params,
    }
)
append_configs(
    sim_configs=sim_config,
    initial_state=genesis_states,
    partial_state_update_blocks=partial_state_update_block
)