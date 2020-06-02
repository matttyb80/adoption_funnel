from .parts.marketing_signal import *
from .parts.adoption import *

partial_state_update_block = [
    {
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # MARKETING SIGNAL GENERATION
        'policies': {
            'marketing_rate': p_marketing_rate,
            'p_marketing_shock' : p_marketing_shock,
        },
        'variables': {
            'signal': s_signal,
        }
    },
    {
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # ADOPTION STATE
        'policies': {
            'reputation' : p_reputation,
            'experience' : p_experience,
        },
        'variables': {
            'adoption': s_adoption,
            'pool': s_pool,

        }
    },

]