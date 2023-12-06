with open('input.txt') as f:
    lines = [line.strip('\n') for line in f]

times = [time.strip(' ') for time in lines[0].strip('Time: ').split('   ')]
distances = [dist.strip(' ') for dist in lines[1].strip('Distance: ').split('  ')]

def prob_1(times, distances):
    all_beats = 1
    for time, dist in zip(times,distances):
        beats = 0
        record = int(dist)
        time = int(time)
        for i in range(0, time):
            if i != 0 and i != time:
                travel_dist = i * (time-i)
                if travel_dist > record:
                    beats += 1
        all_beats *= beats
    return all_beats


time = ''.join(times)
record = ''.join(distances)

def prob_2(time, distance):
    all_beats = 0
    record = int(distance)
    time = int(time)
    for i in range(0, time):
        if i != 0 and i != time:
            travel_dist = i * (time-i)
            if travel_dist > record:
                all_beats += 1
    return all_beats

print(prob_1(times, distances))
print(prob_2(time, record))
