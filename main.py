def lucky(a, b):
  if a == 8 or b == 8 or a + b == 8 or abs(a - b) == 8:
    return True
  else:
    return False

print(lucky(8, 100))
