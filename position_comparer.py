from matplotlib import pyplot as plt
from race_poistion_retriever import RacePositionRetriever

#racedId 1084 = Austria 2022,
LEC_rpr = RacePositionRetriever(1084, 844) #driverId 844 = C.Leclerc 
VER_rpr = RacePositionRetriever(1084, 830) #driverId 830 = M.Verstappen

LEC_lap_time_list = LEC_rpr.retrieve_race_informations()
VER_lap_time_list = VER_rpr.retrieve_race_informations()

LEC_laps, LEC_positions = LEC_rpr.split_laps_positions(LEC_lap_time_list)
VER_laps, VER_positions = VER_rpr.split_laps_positions (VER_lap_time_list)

plt.plot(LEC_laps, LEC_positions, linewidth=2, c='red', label='LEC')
plt.plot(VER_laps, VER_positions, linewidth=2, c='blue', label='VER')

plt.title("LEC vs VER position by lap Australia 2022", fontsize=18)
plt.xlabel("Lap", fontsize=14)
plt.ylabel("Position", fontsize=14)
plt.legend(loc='best')
plt.axis([0,75, 0, 10])

plt.show()