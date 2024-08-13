def combine_lists(list1, list2):
    combined_list = list1 + list2

    combined_list.sort(key=lambda x: x["positions"][0])

    result = []
    
    i = 0
    while i < len(combined_list):
        current_element = combined_list[i]
        current_left, current_right = current_element["positions"]

        j = i + 1
        while j < len(combined_list):
            next_element = combined_list[j]
            next_left, next_right = next_element["positions"]
            
            overlap = min(current_right, next_right) - max(current_left, next_left)
            half_current = (current_right - current_left) / 2
            half_next = (next_right - next_left) / 2
            
            if overlap > 0 and (overlap > half_current or overlap > half_next):
                combined_values = current_element["values"] + next_element["values"]
                combined_element = {
                    "positions": [current_left, max(current_right, next_right)],
                    "values": combined_values
                }
                current_element = combined_element
                current_right = combined_element["positions"][1]
                j += 1
            else:
                break
        
        result.append(current_element)
        i = j

    return result

list1 = [
    {"positions": [1, 5], "values": [10]},
    {"positions": [7, 10], "values": [15]}
]

list2 = [
    {"positions": [3, 8], "values": [20]},
    {"positions": [9, 12], "values": [25]}
]

combined_result = combine_lists(list1, list2)
print(combined_result)
