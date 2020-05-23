import networkx as nx
import numpy as np
import itertools

### MARKETING PARAMETERS #################################
MARKETING_STEADY = [500]
MARKETING_SHOCK_MAG = [1234]
MARKETING_SHOCK_FREQ = [2]

### EXTERNAL EXPERIENCE PARAMETERS #################################
# If UX/UI are not part of the model. Can use as an external signal to
#  generate stochastic process for experience.
EXO_EXPERIENCE = [140]

### POPULATION POOL PARAMETERS #################################
SOURCE_POOL = [10000]

### INITIAL THRESHOLD VALUE PARAMETERS #################################
THRESHOLD = [0.5]

factors = [MARKETING_STEADY,SOURCE_POOL]
product = list(itertools.product(*factors))
MARKETING_STEADY,SOURCE_POOL = zip(*product)
MARKETING_STEADY = list(MARKETING_STEADY)
SOURCE_POOL = list(SOURCE_POOL)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
sys_params = {
   'MARKETING_STEADY': MARKETING_STEADY,
   'MARKETING_SHOCK_MAG': MARKETING_SHOCK_MAG, 
   'MARKETING_SHOCK_FREQ': MARKETING_SHOCK_FREQ,
   'EXO_EXPERIENCE': EXO_EXPERIENCE,
   'SOURCE_POOL': SOURCE_POOL,
   'THRESHOLD': THRESHOLD, 
}