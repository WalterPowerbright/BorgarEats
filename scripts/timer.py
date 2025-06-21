class Timer:
    def __init__(self, time):
        self.WAIT_TIME = time
        self.current_time = 0.0

    def update(self, delta_time):
        self.current_time += delta_time
        self.current_time = self.WAIT_TIME if self.current_time > self.WAIT_TIME else self.current_time
    
    def reset(self):
        self.current_time = 0.0
    
    def is_timeout(self):
        return self.current_time >= self.WAIT_TIME