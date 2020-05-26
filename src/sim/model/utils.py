class Adoption(): #args
    """
    Adoption class for defining state of network adoption
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