class Clock:
    def __init__(self, hour, minute):
        self.minutes = hour * 60 + minute 

    def __repr__(self):
        hours = (self.minutes // 60) % 24
        minutes = self.minutes % 60
        return str(hours).zfill(2) + ":" + str(minutes).zfill(2)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        self.minutes += minutes
        return self

    def __sub__(self, minutes):
        self.minutes -= minutes
        return self
