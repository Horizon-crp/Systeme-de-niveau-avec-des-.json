def get_level_max(xp):
  max = 100
  level = 1
  while True:
    if xp < max:
      break
    max = max * 2
    xp = xp - max
    level += 1
  return level, max
