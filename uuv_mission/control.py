class Controller:
    def __init__(self, KP=0.15, KD=0.6):
        self.KP = KP 
        self.KD = KD 
        self.previous_error=0

    def position(self, current_position, reference):
        error=reference-current_position
        u = self.KP*error + self.KD*(error-self.previous_error)
        self.previous_error = error
        return u