"""
Solutions for CodingBat Python code practice
Website: https://codingbat.com/python

By sacrwll
As of May 5, 2022
"""

#Warmup-1 > sleep_in
def sleep_in(weekday, vacation):
  return not weekday or vacation

#Warmup-1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

#Warmup-1 > sum_double
def sum_double(a, b):
  sum = a + b
  if a == b:
    return sum*2
  else:
    return sum

#Warmup-1 > diff21
def diff21(n):
  diff = abs(n - 21)
  if n > 21:
    return diff * 2
  return diff

#Warmup-1 > parrot_trouble
def parrot_trouble(talking, hour):
  if hour < 7 or hour > 20:
    return talking
  return False

#Warmup-1 > makes10
def makes10(a, b):
  return (a == 10 or b == 10 or (a+b) == 10)

#Warmup-1 > near_hundred
def near_hundred(n):
  return (abs(n-100) <= 10 or abs(n-200) <=10)

#Warmup-1 > pos_neg
def pos_neg(a, b, negative):
  if negative:
    return a < 0 and b < 0
  return (a < 0 and b > 0) or (a > 0 and b < 0)

#Warmup-1 > not_string
def not_string(str):
  if str[:3] == "not":
    return str
  return "not " + str

#Warmup-1 > missing_char
def missing_char(str, n):
  return str[:n] + str[n+1::]

#Warmup-1 > front_back
def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]

#Warmup-1 > front3
def front3(str):
  return str[:3] *3

#Warmup-2 > string_times
def string_times(str, n):
  return str * n

#Warmup-2 > front_times
def front_times(str, n):
  return str[:3] * n

#Warmup-2 > string_bits
def string_bits(str):
  return str[::2]

#Warmup-2 > string_splosion
def string_splosion(str):
  result = ""
  for i in range(len(str)+1):
    result += str[:i]
  return result
#or just the following:
#return "".join([str[:i] for i in range(len(str)+1)])

#Warmup-2 > last2
def last2(str):
  last2Char = str[-2:]
  count = 0
  for i in range(len(str[:-2])):
    if str[i:i+2] == last2Char:
      count +=1
  return count

#Warmup-2 > array_count9
def array_count9(nums):
  return nums.count(9)

#Warmup-2 > array_front9
def array_front9(nums):
  return 9 in nums[:4]

#Warmup-2 > array123
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i:i+3] == [1,2,3]:
      return True
  return False

#Warmup-2 > string_match
def string_match(a, b):
  count = 0
  for i in range(max(len(a),len(b))-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count

#String-1 > hello_name
def hello_name(name):
  return "Hello " + name + "!"

#String-1 > make_abba
def make_abba(a, b):
  return a + b + b + a

#String-1 > make_tags
def make_tags(tag, word):
  return "<{tag}>{word}</{tag}>".format(tag = tag, word = word)

#String-1 > make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#String-1 > extra_end
def extra_end(str):
  return str[-2:] * 3

#String-1 > first_two
def first_two(str):
  return str[:2]

#String-1 > first_half
def first_half(str):
  return str[:len(str)/2]

#String-1 > without_end
def without_end(str):
  return str[1:-1]

#String-1 > combo_string
def combo_string(a, b):
  if len(a) < len(b):
    short = a
    long = b
  else:
    short = b
    long = a
  return short + long + short

#String-1 > non_start
def non_start(a, b):
  return a[1:] + b[1:]

#String-1 > left2
def left2(str):
  return str[2:] + str[:2]

#List-1 > first_last6
def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

#List-1 > same_first_last
def same_first_last(nums):
  return len(nums) >= 1 and (nums[0] == nums[-1])

#List-1 > make_pi
def make_pi():
  return [3,1,4]

#List-1 > common_end
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

#List-1 > sum3
def sum3(nums):
  return sum(nums)

#List-1 > rotate_left3
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

#List-1 > reverse3
def reverse3(nums):
  nums.reverse()
  return nums

#List-1 > max_end3
def max_end3(nums):
  largest = max(nums[0],nums[-1])
  return [largest, largest, largest]

#List-1 > sum2
def sum2(nums):
  return sum(nums[:2])

#List-1 > middle_way
def middle_way(a, b):
  return [a[len(a)/2],b[len(b)/2]]

#List-1 > make_ends
def make_ends(nums):
  return [nums[0], nums[-1]]

#List-1 > has23
def has23(nums):
  return 2 in nums or 3 in nums

#Logic-1 > cigar_party
def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >= 40:
    return True
  else:
    return cigars >= 40 and cigars <=60

#Logic-1 > date_fashion
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1

#Logic-1 > squirrel_play
def squirrel_play(temp, is_summer):
  if is_summer and temp >= 60 and temp <= 100:
    return True
  else:
    return temp >= 60 and temp <= 90

#Logic-1 > caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    elif speed <= 85:
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed <= 80:
      return 1
    else:
      return 2

#Logic-1 > sorta_sum
def sorta_sum(a, b):
  total = a + b
  if total >= 10 and total <= 19:
    return 20
  else:
    return total

#Logic-1 > alarm_clock
def alarm_clock(day, vacation):
  if vacation:
    if day == 0 or day == 6:
      return "off"
    else:
      return "10:00"
  else:
    if day == 0 or day == 6:
      return "10:00"
    else:
      return "7:00"

#Logic-1 > love6
def love6(a, b):
  return a == 6 or b == 6 or (a + b) == 6 or abs(a - b) == 6

#Logic-1 > in1to10
def in1to10(n, outside_mode):
  if outside_mode:
    return n <= 1 or n >= 10
  else:
    return n >= 1 and n <= 10

#Logic-1 > near_ten
def near_ten(num):
  return num % 10 <= 2 or num % 10 >= 8

#Logic-2 > make_bricks
def make_bricks(small, big, goal):
  numBigBricks = int(goal / 5)
  
  if big < numBigBricks:
    numBigBricks = big
    
  return (goal - (numBigBricks * 5)) <= small

#Logic-2 > lone_sum
def lone_sum(a, b, c):
  total = 0
  if a != b and a != c:
    total += a
  if b != a and b != c:
    total += b
  if c != a and c != b:
    total += c
  return total

#Logic-2 > lucky_sum
def lucky_sum(a, b, c):
  total = 0
  
  if a != 13:
    total += a
    
    if b != 13:
      total += b
      
      if c != 13:
        total += c
  
  return total

#Logic-2 > no_teen_sum
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
  zeroValues = [13,14,17,18,19]
  if n in zeroValues:
    return 0
  else:
    return n

#Logic-2 > round_sum
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(num):
  round = num % 10
  num -= round
  if round >= 5:
    return num + 10
  else:
    return num

#Logic-2 > close_far
def close_far(a, b, c):
  if abs(a - b) <= 2 and abs(a - c) >= 2 and abs(b - c) >= 2:
    return True
  elif abs(a - c) <= 2 and abs(a - b) >= 2 and abs(b - c) >= 2:
    return True
  else:
    return False

#Logic-2 > make_chocolate
def make_chocolate(small, big, goal):
  numBigChoc = int(goal / 5)
  if big < numBigChoc:
    numBigChoc = big
  if small >= (goal - (numBigChoc * 5)):
    return goal - (numBigChoc * 5)
  else:
    return -1

#String-2 > double_char
def double_char(str):
  return "".join([i * 2 for i in str])

#String-2 > count_hi
def count_hi(str):
  return str.count("hi")

#String-2 > cat_dog
def cat_dog(str):
  return str.count("cat") == str.count("dog")

#String-2 > count_code
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i:i+2] == "co" and str[i+3] == "e":
      count += 1
  return count

#String-2 > end_other
def end_other(a, b):
  length = min(len(a), len(b))
  return a[-length:].lower() == b[-length:].lower()

#String-2 > xyz_there
def xyz_there(str):
  if str[:3] == "xyz":
    return True
  for i in range(len(str)-3):
    if str[i] != "." and str[i+1:i+4] == "xyz":
      return True
  return False

#List-2 > count_evens
def count_evens(nums):
  return sum([1 for i in nums if i % 2 == 0])

#List-2 > big_diff
def big_diff(nums):
  return max(nums) - min(nums)

#List-2 > centered_average
def centered_average(nums):
  nums.sort()
  return sum(nums[1:-1])/(len(nums)-2)

#List-2 > sum13
def sum13(nums):
  total = 0
  doCount = True
  for i in nums:
    if doCount and i != 13:
      total += i
    if not doCount:
      doCount = True
    if i == 13:
      doCount = False
  return total

#List-2 > sum67
def sum67(nums):
  total = 0
  doCount = True
  for i in nums:
    if doCount and i != 6:
      total += i
    if doCount and i == 6:
      doCount = False
    if not doCount and i == 7:
      doCount = True
  return total

#List-2 > has22
def has22(nums):
  for i in range(0,len(nums)):
    if nums[i:i+2] == [2,2]:
      return True
  return False
