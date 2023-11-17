import random
import re
def generator(char_start, char_range) -> str:
  string_length = 100
  out = ""
  for i in range(0, string_length):
    out += chr(random.randrange(33, 122))
  return out