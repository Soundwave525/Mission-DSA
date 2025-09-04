def queensAttack(n, k, r_q, c_q, obstacles):
  o_set = set((r, c) for r, c in obstacles)

  directions = [ (0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1) ]

  count  = 0

  for dr, dc in directions:
    row, col = r_q + dr, r_c + dc

    while 1 <= row <= n and 1 <= col <= n:
      if (row, col) in o_set:
        break
      count += 1
      row += dr
      col += dc

  return count
