import heapq

def min_cost_to_connect_cables(cables):
    if not cables:
        return 0
    

    heapq.heapify(cables)
    
    total_cost = 0
    

    while len(cables) > 1:
  
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
 
        cost = first + second
        total_cost += cost
        

        heapq.heappush(cables, cost)
    
    return total_cost


cables = [4, 3, 2, 6]
print(f"Мінімальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cables)}")
