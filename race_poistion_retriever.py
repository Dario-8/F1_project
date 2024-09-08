import csv
import os
import json
import requests
from lap_time import LapTime

class RacePositionRetriever():
    """A class to retrieve the informations about drivers during a passed race"""
    def __init__(self, raceId: int, driverId: int) -> None:
        """Initialize attributes to retrieve the position"""
        self.raceId = str(raceId)
        self.driverId = str(driverId)
        

    def retrieve_race_informations(self) -> list[dict[str, int]]:
        """Retrieve all the data to compare the two drivers"""
        filename = os.path.join('F1_Project','CSV Data', 'lap_times.csv')
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
    
    def retrieve_race_informations_from_api(self):

        # URL of the API endpoint
        url = 'http://127.0.0.1:5000/get_lap_times'

        payload = {
            "raceId": int(self.raceId),
            "driverId": int(self.driverId)
        }

        # Make a POST request to the API with JSON data
        response = requests.post(url, json=payload)
        
        # Parse the JSON response directly
        laps_data = response.json()

        # Now use the data directly to create LapTime instances
        lap_times: list[LapTime] = [LapTime(lap['driverId'], lap['lap'],
                                            lap['milliseconds'], lap['position'],
                                            lap['raceId'], lap['time'])
                                    for lap in laps_data]
            
        return lap_times


    def split_laps_positions(self, lap_time_list: list[dict[str, int]]) -> tuple[list[int], list[int]]:
        """Split the number of laps and position for that lap"""
        laps = [lap['lap'] for lap in lap_time_list]
        positions = [lap['position'] for lap in lap_time_list]

        return laps, positions
    
    def split_laps_positions(self, lap_time_list: list[LapTime]) -> tuple[list[int], list[int]]:
        """Split the number of laps and position for that lap"""
        laps = [lap_time.lap for lap_time in lap_time_list]
        positions = [lap_time.position for lap_time in lap_time_list]

        return laps, positions
    
        