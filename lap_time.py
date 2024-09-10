class LapTime():
    """A class to store lap time informations"""
    def __init__(self, driverId: int, lap: int, milliseconds: int,
                  position: int, raceId: int, time: str) -> None:
        """Initialize attributes"""
        self.driverId = driverId
        self.lap = lap
        self.milliseconds = milliseconds
        self.position = position
        self.racedId = raceId
        self.time = time

    
    def __repr__(self) -> str:
        return f'DriverId {self.driverId!r}, Lap {self.lap!r}'