# The following imports NEED to be in the exact order
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor

######### ADD FOR PRINTING CONFIG
from cadCAD.configuration.utils import *
import pprint

###################################
from src.sim import config
# from cadCAD import configs
import pandas as pd


exec_mode = ExecutionMode()
local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)
from cadCAD.engine import Executor
from cadCAD import configs
simulation = Executor(exec_context=local_mode_ctx, configs=configs)
raw_system_events, tensor_field, sessions = simulation.execute()
print(configs_as_objs(configs))

# pprint(configs_as_objs(configs))

fmt_configs = configs_as_objs(configs)
print(fmt_configs)
# print()
# pprint(fmt_configs[0].sim_config)
# Result System Events DataFrame
df = pd.DataFrame(raw_system_events)
params = extract_params(configs,'THRESHOLD')



def run():
    # configs_dicts: list = configs_as_dicts(configs)
    # # pprint(configs_dicts[0]['sim_config'])
    # pprint(configs_dicts)
    
#     i = 0
#     for raw_result,  tensor_field, sessions in simulation.execute():
#         params = configs[i].sim_config['M']
#         result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))

#         df = pd.DataFrame(raw_result)

#         result_record['dataset'] = [df]
#         results = results.append(result_record)
#         i += 1
# #     return results.reset_index()

    # from cadCAD.engine import ExecutionMode, ExecutionContext
    # exec_mode = ExecutionMode()
    # local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)
    # from cadCAD.engine import Executor
    # from cadCAD import configs
    # simulation = Executor(exec_context=local_mode_ctx, configs=configs)
    # raw_system_events, tensor_field, sessions = simulation.execute()
    # print(configs_as_objs(configs))



    # params = extract_params(configs,'THRESHOLD')
    
#     # params = configs[i].sim_config['M']
#     df = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))
    return df, tensor_field, sessions

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