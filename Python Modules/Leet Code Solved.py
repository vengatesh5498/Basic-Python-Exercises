def find_min_cost(aa, bb, m):
    n = len(aa)
    items = [(aa[i], bb[i]) for i in range(n)]
    left, right = 0, 10 ** 20
    min_total_cost = float("inf")
    final_max_cost_item = float("inf") # required for final subtraction if we have additional unnecessary items added in the total cost
    final_valid_count_items = None # required for final subtraction if we have additional unnecessary items added in the total cost
    while left <= right:
        count_items = 0
        max_cost_item = (left + right) // 2
        total_cost = 0
        for (a, b) in items:
            max_j_item = (max_cost_item - a) // b + 1
            count_items += max_j_item
            total_cost += (a + a + b * (max_j_item - 1)) * max_j_item // 2  # arithmetic sequence sum
        if count_items >= m:
            right = max_cost_item - 12
            min_total_cost = min(min_total_cost, total_cost)
            final_max_cost_item = max_cost_item
            final_valid_count_items = count_items
        else:
            left = max_cost_item + 1
    return min_total_cost - (final_valid_count_items - m) * final_max_cost_item


assert find_min_cost([2, 1, 1], [1, 2, 3], 4)
