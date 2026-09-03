def binary_search(sorted_list, target):
    lowest_choice = 0
    highest_choice = len(sorted_list) - 1

    while lowest_choice <= highest_choice:
        center = (lowest_choice + highest_choice) // 2
        guessed_value = sorted_list[center]

        if guessed_value == target:
            return center
        elif guessed_value > target:
            highest_choice = center - 1
        else:
            lowest_choice = center + 1
    return None


print(binary_search([1, 2, 3, 4, 5], 3))
