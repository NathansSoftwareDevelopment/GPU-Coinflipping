import time


def main():
    number_of_heads: int = get_initial_heads()
    target_success_chance: float = get_target_success_chance()

    start_time = time.perf_counter()

    number_of_odd_heads: int = number_of_heads // 2
    delta_value_list: list[int] = [0 for _ in range(number_of_odd_heads + 2)]
    delta_value_list[number_of_odd_heads] = 1

    # The number of coins that have been flipped
    toss_counter: int = 0
    # The number of possibilities where the number of tails flipped has exceeded
    # that of heads atleast once
    wins: int = 0
    success_chance: float = 0

    # Because we are looking for the number of tails to surpass that of heads
    # every other flip is irrelevant and the starting parity may need changing
    if number_of_heads % 2 == 0:
        toss_counter += 1
        delta_value_list[number_of_odd_heads - 1] = 1

    range_stop: int = len(delta_value_list)
    while success_chance < target_success_chance:
        toss_counter += 2
        # Since we are looking for everytime we have had more tails than heads
        # atleast one time the number of winning permutations doubles with every
        # coin toss
        wins = wins << 2

        delta_value_list.append(0)

        ones_value = delta_value_list[0]
        wins += ones_value
        previous_value = delta_value_list[1] + 2 * ones_value
        for index in range(1, range_stop):
            current_value = delta_value_list[index + 1] + 2 * delta_value_list[index] + delta_value_list[index - 1]
            delta_value_list[index - 1] = previous_value
            previous_value = current_value
        delta_value_list[-2] = previous_value
        range_stop += 1

        success_chance = wins * 100 / (1 << toss_counter)


    end_time = time.perf_counter()
    milliseconds_elapsed = (end_time - start_time) * 1000
    print(toss_counter)
    print(f"Run Time of {milliseconds_elapsed}ms")


def get_initial_heads() -> int:
    while True:
        try:
            user_input = int(input("How many heads have you flipped? "))
        except ValueError:
            print("Invalid Input. Please try again")
        else:
            return user_input

def get_target_success_chance() -> float:
    while True:
        try:
            user_input = float(input("What success chance would you like? "))
        except ValueError:
            print("Invalid Input. Please try again")
        else:
            return user_input


if __name__ == "__main__":
    main()