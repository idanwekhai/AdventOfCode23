import re

with open('input.txt') as f:
  lines = [line.strip('\n') for line in f]


int_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven':7, 'eight': 8, 'nine': 9, 'zero': 0}
str_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', '\d+']


def prob_1(lines):
    total = 0
    for line in lines:
        nums = re.findall(r'\d+', line)
        nums = ' '.join(nums)
        if len(nums) > 0:
          total += int(nums[0] + nums[-1])
    return total


def prob_2(lines):
    total = 0
    combined_regex = r"(?=(" + '|'.join(str_list) + r"))"
    for line in lines:
      compiled_regex = re.compile(combined_regex)
      str_nums = compiled_regex.findall(line)
      new_str_num = []
      for i in str_nums:
          if i in int_map.keys():
              num = int_map[i]
              new_str_num.append(str(num))
          else:
              new_str_num.append(i)
      nums = ' '.join(new_str_num)
      total += int(nums[0] + nums[-1])
    return total

print(prob_1(lines))
print(prob_2(lines))