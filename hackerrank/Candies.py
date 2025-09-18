def candies(n, arr):
  c = [1] * n
  
  for i in range(1, n):
    if arr[i] > arr[i + 1]:
      c[i] = c[i - 1] + 1

  for i in range(n - 1, -1, -1):
    if arr[i] > arr[i + 1]:
      c[i] = max(c[i, c[i + 1] + 1)

  return sum(c)
