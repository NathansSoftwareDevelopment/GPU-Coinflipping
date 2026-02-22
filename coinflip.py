import time

def main():
    number_of_heads: int = get_initial_heads()
    target_success_chance: float = get_target_success_chance()

    start_time = time.perf_counter()

    # Records the number of occurrences for each heads/tails delta value
    coin_counts: dict[int, int] = {number_of_heads: 1}

    # The number of coins that have been flipped
    toss_counter: int = 0
    # The number of possibilities where the number of tails flipped has exceeded
    # that of heads atleast once
    wins: int = 0
    success_chance: float = 0



    end_time = time.perf_counter()
    milliseconds_elapsed = (end_time - start_time) * 1000
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