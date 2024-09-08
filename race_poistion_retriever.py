import csv
import os

class RacePositionRetriever():
    """A class to retrieve the informations about drivers during a passed race"""
    def __init__(self, raceId: int, driverId: int) -> None:
        """Initialize attributes to retrieve the position"""
        self.raceId = str(raceId)
        self.driverId = str(driverId)
        

    def retrieve_race_informations(self) -> list[dict[str, int]]:
        """Retrieve all the data to compare the two drivers"""
        filename = os.path.join('CSV Data', 'results.csv')
        try:

            with open(filename) as f:
                reader = csv.reader(f)

                lap_time_list = [
                    {'lap': int(row[2]), 'position': int(row[3])}
                    for row in reader
                    if row[0] == self.raceId and row[1] == self.driverId
                ]

        except FileNotFoundError:
            msg = "Sorry, the file " + filename + " does not exist."
            print(msg)

        return lap_time_list

    def split_laps_positions(self, lap_time_list: list[dict[str, int]]) -> tuple[list[int], list[int]]:
        """Split the number of laps and position for that lap"""
        laps = [lap['lap'] for lap in lap_time_list]
        positions = [lap['position'] for lap in lap_time_list]

        return laps, positions
        