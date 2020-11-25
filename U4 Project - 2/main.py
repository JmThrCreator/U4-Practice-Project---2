from processing import process_times


race_gender = input("Are the athlets competing Male or Female (M/F): ").upper()
while race_gender not in ('M', 'F'):
    race_gender = input("Are the athlets competing Male or Female (M/F): ").upper()
 

adding_race_times = True
lane_number = 1
race_times = []
while adding_race_times == True:
    temp_race_time = input("Time of the athlete on lane " + str(lane_number) + " ,(X: to stop): ")
    if temp_race_time.upper() == "X":
        if len(race_times) == 0:
            print("No times where added at all")
            break;
        else:
            process_times(race_times, race_gender)
            break;
    else:
        if temp_race_time.replace('.','',1).isdigit():
            while float(temp_race_time) <= 0:
                temp_race_time = input("Time of the athlete on lane " + str(lane_number) + " ,(X: to stop): ")
            race_times.append([lane_number, round(float(temp_race_time), 2)])
            lane_number += 1
        else:
            print("Invalid input")

        



