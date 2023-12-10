with open('input.txt') as f:
    lines = [line.strip('\n').split(' ') for line in f]

instructions = lines[0][0]
maps = {}
for line in lines[2:]:
    maps[line[0]] = (line[2][1:4], line[3][:-1])

count = 0
current_key = 'AAA'
current_pos = maps[current_key]
while current_key != 'ZZZ':
    for i in range(len(instructions)):
        direction = instructions[i]
        if direction == 'L':
            current_key = current_pos[0]
            current_pos = maps[current_key]
            count += 1
        elif direction == 'R':
            current_key = current_pos[1]
            current_pos = maps[current_key]
            count += 1

print(count)


count = 0
current_keys = [i for i in maps if i[2]=='A']
end_keys = [i for i in maps if i[2]=='Z']
current_pos = [maps[key] for key in current_keys]
check = [i[2] == 'Z' for i in current_keys]
while set(check) != {True}:
    for i in range(len(instructions)):
        direction = instructions[i]
        if direction == 'L':
            current_keys = [node[0] for node in current_pos]
            current_pos = [maps[key] for key in current_keys]
            count += 1
        elif direction == 'R':
            current_keys = [node[1] for node in current_pos]
            current_pos = [maps[key] for key in current_keys]
            count += 1

# current_keys = [i for i in maps if i[2]=='A']
# end_keys = [i for i in maps if i[2]=='Z']
# all_count = []
# counts = []
# for k in current_keys:
#   c_key = k
#   c_pos = maps[c_key]
#   for i in range(10000):
#       count = 0
#       for i in range(len(instructions)):
#           direction = instructions[i]
#           if c_key[2] == 'Z':
#               counts.append(count)
#           if direction == 'L':
#               c_key = c_pos[0]
#               c_pos = maps[c_key]
#               count += 1
#           elif direction == 'R':
#               c_key = c_pos[1]
#               c_pos = maps[c_key]
#               count += 1
#   all_count.append(counts)
# print(all_count)
