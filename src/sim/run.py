# The following imports NEED to be in the exact order
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from src.sim import config
from cadCAD import configs
import pandas as pd

def run(drop_midsteps=True):
    exec_mode = ExecutionMode()
    multi_proc_ctx = ExecutionContext(context=exec_mode.multi_proc)
    run = Executor(exec_context=multi_proc_ctx, configs=configs)
    results = pd.DataFrame()
    i = 0
    for raw_result, _ in run.execute():
        params = configs[i].sim_config['M']
        result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))

        df = pd.DataFrame(raw_result)
        # keep only last substep of each timestep
        if drop_midsteps:
            max_substep = max(df.substep)
            is_droppable = (df.substep!=max_substep)&(df.substep!=0)
            df.drop(df[is_droppable].index, inplace=True)

        result_record['dataset'] = [df]
        results = results.append(result_record)
        i += 1
    return results.reset_index()

# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd
# from model.parts.supportingFunctions import *
# pd.options.display.float_format = '{:.2f}'.format
# %matplotlib inline
# from model import economyconfig 

from cadCAD.engine import ExecutionMode, ExecutionContext
exec_mode = ExecutionMode()
local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)
from cadCAD.engine import Executor
from cadCAD import configs
simulation = Executor(exec_context=local_mode_ctx, configs=configs)
raw_system_events, tensor_field, sessions = simulation.execute()
# Result System Events DataFrame
df = pd.DataFrame(raw_system_events)

def run():

    # params = configs[i].sim_config['M']
    # result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))
    return df

# def run(drop_midsteps=True):
#
#     exec_mode = ExecutionMode()
#     local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)
#
#     simulation = Executor(exec_context=local_mode_ctx, configs=configs)
#     raw_system_events, tensor_field, sessions = simulation.execute()
#
#     df = pd.DataFrame(raw_system_events)
#     return df