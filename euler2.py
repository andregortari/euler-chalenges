from typing import List


def generate_fibonacci_sequence() -> List[int]:
    initial_list = [0, 1]
    while True:
        if initial_list[-1] + initial_list[-2] > 4000000:
            break
        else:
            initial_list.append(initial_list[-1] + initial_list[-2])
    return initial_list


fibonnaci_list = generate_fibonacci_sequence()
sum_even_values = sum(filter(lambda x: x % 2 == 0, fibonnaci_list))
print(sum_even_values)
