from matplotlib import pyplot as plt
from race_poistion_retriever import RacePositionRetriever

# Initialize RacePositionRetriever for each driver
race_id = 1084  # Austria 2022
leclerc_driver_id = 844  # C. Leclerc
verstappen_driver_id = 830  # M. Verstappen

leclerc_rpr = RacePositionRetriever(race_id, leclerc_driver_id)
verstappen_rpr = RacePositionRetriever(race_id, verstappen_driver_id)

LEC_lap_time_list = leclerc_rpr.retrieve_race_informations()
VER_lap_time_list = verstappen_rpr.retrieve_race_informations()

LEC_laps, LEC_positions = leclerc_rpr.split_laps_positions(LEC_lap_time_list)
VER_laps, VER_positions = verstappen_rpr.split_laps_positions (VER_lap_time_list)

plt.plot(LEC_laps, LEC_positions, linewidth=2, c='red', label='LEC')
plt.plot(VER_laps, VER_positions, linewidth=2, c='blue', label='VER')

plt.title("LEC vs VER position by lap Australia 2022", fontsize=18)
plt.xlabel("Lap", fontsize=14)
plt.ylabel("Position", fontsize=14)
plt.legend(loc='best')
plt.grid(True)
plt.axis([0,75, 0, 10])

plt.show()