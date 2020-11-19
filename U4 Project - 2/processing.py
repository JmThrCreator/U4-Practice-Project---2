from recordtime import recordtimes

def process_times(race_times_list, race_gender):
    race_times_list.sort(key=lambda x:x[1], reverse=True)
    for i in race_times_list:
        print("Lane " + str(i[0]) + ": " + str(i[1]))
    if len(race_times_list) < recordtimes.min_athletes:
        print("The amount of athletes is too small to qualify")
    if len(race_times_list) > recordtimes.max_athletes:
        print("The amount of athletes is too large to qualify")
    else:
        print("------------------------------")
        for times in race_times_list:
            if race_gender == "F":
                for record_name, record_time in recordtimes.womens_record_times.items():
                    if times[1] < record_time:
                        print(record_name+" beaten at " + str(times[1]) + " in lane " + str(times[0]))
            elif race_gender == "M":
                for record_name, record_time in recordtimes.mens_record_times.items():
                    if times[1] < record_time:
                        print(record_name+" beaten at " + str(times[1]) + " in lane " + str(times[0]))

        print("------------------------------")
       