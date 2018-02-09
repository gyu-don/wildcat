class TemperatureSchedule:
    def __init__(self, scale=0.95, initial_temperature=5.0, last_temperature=0.2):
        self.initial_temperature = initial_temperature
        self.last_temperature = last_temperature
        self.scale = scale
        self.current_temperature = None

    def reset(self):
        self.current_temperature = None

    def __iter__(self):
        if self.current_temperature is None:
            self.current_temperature = self.initial_temperature
        while self.current_temperature > self.last_temperature:
            yield self.current_temperature
            self.current_temperature *= self.scale
