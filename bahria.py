import math

def get_min_cost(n, c_pri, c_sec, p_pri, p_sec, k):
    """
    Calculates minimum cost assuming we fill as many primary vehicles 
    as possible, then put the remainder in secondary vehicles.
    """
    min_cost = float('inf')
    max_pri = (n // c_pri) + 2
    for i in range(max_pri):
        people_in_pri = i * c_pri
        if people_in_pri >= n:
            cost = i * p_pri
            last_load = n - (i - 1) * c_pri
            if 0 < last_load < math.ceil(c_pri / 2):
                cost += k
            min_cost = min(min_cost, cost)
            break # No need to check more primary vehicles
        rem_people = n - people_in_pri
        num_sec = math.ceil(rem_people / c_sec)
        cost = (i * p_pri) + (num_sec * p_sec)
        last_sec_load = rem_people - (num_sec - 1) * c_sec
        if 0 < last_sec_load < math.ceil(c_sec / 2):
            cost += k
        min_cost = min(min_cost, cost)
    return min_cost


for _ in range(int(input())):
    n, cc, cv, pc, pv, k = map(int, input().split())
    res1 = get_min_cost(n, cc, cv, pc, pv, k)
    res2 = get_min_cost(n, cv, cc, pv, pc, k)
    print(min(res1, res2))
