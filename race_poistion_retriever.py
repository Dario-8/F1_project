import csv

class RacePositionRetriever():
    """A class to retrieve the informations about drivers during a passed race"""
    def __init__(self, raceId, driverId) -> None:
        """Initialize attributes to retrieve the position"""
        self.raceId = str(raceId)
        self.driverId = str(driverId)
        

    def retrieve_race_informations(self):
        """Retrieve all the data to compare the two drivers"""
        filename = 'F1_Project\\lap_times.csv'
        with open(filename) as f:
            reader = csv.reader(f)


            lap_time_list = []

            for row in reader:
                if row[0] == self.raceId:
                    if row[1] == self.driverId:
                        lap_time_dictionary = {}
                        lap_time_dictionary['lap'] =  int(row[2])
                        lap_time_dictionary['position'] =  int(row[3])
                        lap_time_list.append(lap_time_dictionary)
        
        return lap_time_list

    def split_laps_positions(self, lap_time_list):
        """Split the number of laps and position for that lap"""
        laps = []
        positions = []
        for lap in lap_time_list:
            laps.append(lap['lap'])
            positions.append(lap['position'])
        return laps, positions
        