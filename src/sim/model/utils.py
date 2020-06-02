class Adoption(): #args
    """
    Adoption class for defining state of network adoption
    This is agent flavored, where each instance has an individualized reputation belief
    and threshold transition value
    """  
    def __init__(self):
        """
        Adoption class initialized without a preset reputation
        Unaware state
        """        
        self.reputation = None
        self.state = 'unaware'

 # when signal reaches above filtered threshold       
    def apply_signal(self, signal):
        """
        Apply signal to reputation metric
        """  
        if self.reputation is None:
            self.reputation = 0
            self.state = 'aware'
        if signal == 0: 
            self.reputation =  0
        elif signal > 0: 
            self.reputation +=  1
            
        elif signal < 0: 
            self.reputation -=  1

            
        
    def apply_experience(self, experience):
        """
        Apply experience to reputation metric
        """  
        if experience > 0: 
            self.reputation +=  1
        
        if experience < 0: 
            self.reputation -=  1
            

    def determine_state(self, reputation=None, threshold= None):
        """
        Uses reputation and threshold to determine state
        """  
        

        if threshold is None:
            threshold = self.threshold
            
        if reputation is None:
            reputation = self.reputation
        
        if reputation > threshold:
            if self.state == 'aware':
                self.state = 'adopted'
                
            elif self.state == 'adopted':
                self.state = 'loyal'
                       
                
        if reputation < threshold:
            if self.state == 'adopted':
                self.state = 'churned'
        
            elif self.state == 'loyal':
                self.state = 'adopted'
                
    def set_threshold(self, default_threshold=20, ext_threshold=None):
        """
        Set threshold to current state
        """  

        if self.state == 'unaware':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
                
        elif self.state == 'aware':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
                       
        elif self.state == 'adopted':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
                
        elif self.state == 'loyal':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold       
                
        elif self.state == 'churned':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
        
    def __str__(self):
        """
        Print all attributes of an event
        """
        return str(self.__class__) + ": " + str(self.__dict__)

class Adoption_Pool(): #args
    """
    Adoption class for defining state of network adoption
    This is class is on the subpopulation level, where each state maitains a count of members
    and a mean of reputation in the addoption funnel
    and threshold transition value
    """  
    def __init__(self, pool):
        """
        Adoption class initialized without a preset reputation
        Unaware state
        """        

        self.state = {'unaware': {'pool': pool, 'reputation': None,},
                      'aware': {'pool': 0, 'reputation': None},
                      'adopted': {'pool': 0, 'reputation': None},
                      'loyal': {'pool': 0, 'reputation': None},
                      'churned': {'pool': 0, 'reputation': None},
                    }
        # self.state.pool = pool
        # self.pool = pool
        # self.reputation = None
        self.threshold = 1

 # when signal reaches above filtered threshold       
    def apply_signal(self, signal):
        """
        Apply signal to reputation metric
        """  
        print(self.state['unaware'])
        if self.state['unaware']['reputation'] is None:
            self.state['unaware']['reputation'] = 0

        if signal == 0: 
            self.state['unaware']['reputation']  =  0
        elif signal > 0: 
            self.state['unaware']['reputation'] +=  1

        elif signal < 0: 
            self.state['unaware']['reputation'] -=  1
        
            
        
    def apply_experience(self, experience):
        """
        Apply experience to reputation metric
        """  
        if experience > 0: 
            self.reputation +=  1
        
        if experience < 0: 
            self.reputation -=  1
            
    
    def calculate_drip(self):
        """
        Calculate drip for each state
        """  
        for key, value in self.state.items():
            if value['reputation'] is not None:
                # NOT THRESHOLD NUT THRESHOLD*POOL
                value['drip'] = value['reputation'] * value['pool'] - self.threshold * value['pool'] # TOO BIG
                
    def update_pools(self):
        """
        Update pool from drip for each state
        """  
        for key, value in self.state.items():
            if 'drip' in value.keys():
                value['pool'] -= value['drip']
                
                
                if key is 'unaware':
                    self.state['aware']['pool'] += value['drip']
                
                elif key is 'aware':
                    self.state['adopted']['pool'] += value['drip']
                    
                elif key is 'adopted':
                    self.state['loyal']['pool'] += value['drip']
                
                elif key is 'adopted': # AND NEGATIVE FLAG FOR NEGATIVE
                    self.state['churned']['pool'] += value['drip']
                    
                elif key is 'loyal':
                    self.state['adopted']['pool'] += value['drip']
                    
                elif key is 'churned':
                    self.state['adopted']['pool'] += value['drip']
                
                value['drip'] = 0
                
                
#         for key, value in self.state.items():
#             print(value)
#             if 'drip' in value.keys():
#                 value['drip'] = 0
    
    def determine_state(self, reputation=None, threshold= None):
        """
        Uses reputation and threshold to determine state
        """  
        if threshold is None:
            threshold = self.threshold
            
        if reputation is None:
            reputation = self.reputation
        
        if reputation > threshold:
            if self.state == 'aware':
                self.state = 'adopted'
                
            elif self.state == 'adopted':
                self.state = 'loyal'
                       
                
        if reputation < threshold:
            if self.state == 'adopted':
                self.state = 'churned'
        
            elif self.state == 'loyal':
                self.state = 'adopted'
                
    def set_threshold(self, default_threshold=0.5, ext_threshold=None):
        """
        Set threshold to current state
        """  

        if self.state == 'unaware':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
                
        elif self.state == 'aware':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
                       
        elif self.state == 'adopted':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
                
        elif self.state == 'loyal':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold       
                
        elif self.state == 'churned':
            if ext_threshold is not None:
                self.threshold = ext_threshold
            else:
                self.threshold = default_threshold
        
    def __str__(self):
        """
        Print all attributes of an event
        """
        return str(self.__class__) + ": " + str(self.__dict__)