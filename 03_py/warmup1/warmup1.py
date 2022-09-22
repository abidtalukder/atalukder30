# Python Warm Up 1

def sleep_in(weekday, vacation):
  if (weekday == False) or vacation == True:
      return True
  return False

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif (a_smile == False and b_smile == False):
    return True
  return False
  
def sum_double(a, b):
  if a == b:
    return 4 * a
  return a + b

def diff21(n):
  if n > 21:
    return 2*abs((n-21))
  return abs(n-21)

def parrot_trouble(talking, hour):
  if talking == True:
    if hour < 7 or hour > 20:
      return True
  return False

def makes10(a, b):
  if a == 10 or b == 10:
    return True
  elif  a + b == 10:
    return True
  return False





def near_hundred(n):
  if n >= 90 and n <= 110:
    return True
  elif n >= 190 and n <= 210:
    return True
  return False

def pos_neg(a, b, negative):
  if negative == True:
    if a < 0 and b < 0:
      return True
  elif negative == False:
    if a > 0:
      if b < 0:
        return True
    elif b > 0:
      if a < 0:
        return True
  return False

def not_string(str):
  if str[0:3] == "not":
    return str
  return "not " + str

def missing_char(str, n):
  a = ''
  a += str[:n]
  a += str[n+1:]
  return a
  

def front_back(str):
  if len(str) <= 1:
    return str
  else:
    a = ''
    a += str[-1]
    a += str[1:-1]
    a += str[0]
    return a

def front3(str):
  if len(str) <= 3:
    return 3 * str
  return 3 * str[:3]
  
