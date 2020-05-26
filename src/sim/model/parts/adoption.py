import networkx as nx
import numpy as np

from ..utils import *

def p_reputation(params, substep, state_history, prev_state):
    """
    Policy for steady marketing spend signal generation.
    """
    constant = params['THRESHOLD']
    random = np.random.normal(params['THRESHOLD'], scale = 1.0)
    return {'reputation': constant}


def p_experience(params, substep, state_history, prev_state):
    """
    Policy for steady marketing spend signal generation.
    """
    constant = params['EXO_EXPERIENCE']
    random = np.random.normal(params['EXO_EXPERIENCE'], scale = 1.0)
    return {'experience': constant}


def s_adoption(params, substep, state_history, prev_state, policy_input):
    """
    State for generating signal from marketing.
    """
    key = 'adoption'

    prev_state['adoption'].apply_signal(prev_state['signal'])
    # value = policy_input['reputation'] + policy_input['experience']
    prev_state['adoption'].set_threshold(params['THRESHOLD'])
    prev_state['adoption'].determine_state(prev_state['signal'])
    value = prev_state['adoption']
    return (key, value)