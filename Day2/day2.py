import math
with open('Day2/input.txt') as f:
  lines = [line.strip('\n') for line in f]

config = {'red': 12,'green': 13, 'blue': 14}

def prob_1(lines):
    ids_total = 0
    impossible_ids_total = set()
    for line in lines:
        id  = int(''.join(filter(str.isdigit, line[:8])))
        ids_total += id
        games = line[8:].strip(':').split(';')
        all_games = []
        for game in games:
            all_games.extend([i.split(' ') for i in game.strip(' ').split(';')][0])
        for i in range(0, len(all_games), 2):
            if int(all_games[i]) > config[all_games[i+1].strip(',')]:
                impossible_ids_total.add(id)
    return ids_total - sum(impossible_ids_total)

def prob_2(lines):
    sum_power = 0
    for line in lines:
        games = line[8:].strip(':').split(';')
        all_games = []
        games_map = {"blue": [], "green": [], "red": []}
        for game in games:
            all_games.extend([i.split(' ') for i in game.strip(' ').split(';')][0])
        for i in range(0, len(all_games), 2):
            games_map[all_games[i+1].strip(',')].append(int(all_games[i]))
        sum_power += math.prod([max(i) for i in games_map.values()])
    return sum_power

print(prob_1(lines))
print(prob_2(lines))