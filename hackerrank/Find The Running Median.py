import heapq

def runningMedian(a):
   result = []
    low, high = [], []
    
    for num in a:
      
        if not low or num <= -low[0]:
            heapq.heappush(low, -num)
        else:
            heapq.heappush(high, num)
        
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
        
        if len(low) == len(high):
            median = (-low[0] + high[0]) / 2
        else:
            median = float(-low[0])
        
        result.append(median)
    
    return result
