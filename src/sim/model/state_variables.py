from datetime import datetime
import networkx as nx
import numpy as np
# from copy import deepcopy
import scipy.stats as stats
from .sys_params import sys_params
from .utils import *

# Initial Values
signal = 0
state = 0
# state = Adoption()
## Genesis States #################################################
genesis_states = {
    'timestamp': datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
    'signal': signal,
    'adoption': state,


}