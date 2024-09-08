from matplotlib import pyplot as plt
from race_poistion_retriever import RacePositionRetriever

# Initialize RacePositionRetriever for each driver
race_id = 969  # Australian Grand Prix 2017
hamilton_driver_id = 1  # Hamilton
vettel_driver_id = 20  # Vettel

hamilton_rpr = RacePositionRetriever(race_id, hamilton_driver_id)
vettel_rpr = RacePositionRetriever(race_id, vettel_driver_id)

HAM_lap_time_list = hamilton_rpr.retrieve_race_informations_from_api()
VET_lap_time_list = vettel_rpr.retrieve_race_informations_from_api()

HAM_laps, HAM_positions = hamilton_rpr.split_laps_positions(HAM_lap_time_list)
VET_laps, VET_positions = vettel_rpr.split_laps_positions (VET_lap_time_list)

plt.plot(HAM_laps, HAM_positions, linewidth=2, c='red', label='HAM')
plt.plot(VET_laps, VET_positions, linewidth=2, c='blue', label='VET')

plt.title("HAM vs VET Australian Grand Prix 2017", fontsize=18)
plt.xlabel("Lap", fontsize=14)
plt.ylabel("Position", fontsize=14)
plt.legend(loc='best')
plt.grid(True)
plt.axis([0, 60, 0, 7])

plt.show()
