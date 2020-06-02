from datetime import datetime
import networkx as nx
import numpy as np

from scipy.stats import norm

# from copy import deepcopy
import scipy.stats as stats
from .sys_params import sys_params
from .utils import *

# Initial Values
signal = 0
# state = 0
adoption = Adoption()
# pool = Adoption_Pool()

# state
state = []
## Genesis States #################################################
genesis_states = {
    'timestamp': datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
    'signal': signal,
    'adoption': adoption,
    'state' : state,
    # 'pool' : pool,


}