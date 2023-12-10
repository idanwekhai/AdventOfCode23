with open('input.txt') as f:
  lines = [line.strip('\n').split(' ') for line in f]

all_series = [list(map(int, series)) for series in lines]

def extrapolate_history(part=1):
  total = 0
  for series in all_series:
      history = [series]
      next_series = []
      current = series
      while set(next_series) != {0}:
          next_series = []
          for i in range(len(current)-1):
              next_series.append(current[i+1]-current[i])
          history.append(next_series)
          current = next_series
      for i in reversed(range(len(history))):
          if part == 1:
              history[i-1].append(history[i-1][-1] + history[i][-1])
          else:
              history[i-1].insert(0, history[i-1][0] - history[i][0])
      total += history[0][-1] if part==1 else history[0][0]
  return total

print(extrapolate_history(part=1))
print(extrapolate_history(part=2))