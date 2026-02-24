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

    # Because we are looking for the number of tails to surpass that of heads
    # every other flip is irrelevant and the starting parity may need changing
    if number_of_heads % 2 == 0:
        toss_counter += 1
        # After one toss the heads/tails delta can either increment or decrement
        coin_counts = {number_of_heads - 1: 1, number_of_heads + 1: 1}


    updated_coin_counts: dict[int, int] = coin_counts.copy()
    while success_chance < target_success_chance:
        toss_counter += 2
        # Since we are looking for everytime we have had more tails than heads
        # atleast one time the number of winning permutations doubles with every
        # coin toss
        wins = wins << 2

        # After two tosses the two new delta values are added
        # from flipping either two heads or two tails
        keys: list[int] = updated_coin_counts.keys()
        maxKey: int = max(keys)
        updated_coin_counts[maxKey + 2] = 0
        minKey: int = min(keys)
        updated_coin_counts[minKey - 2] = 0

        for key in updated_coin_counts:
            updated_coin_counts[key] = coin_counts.get(key + 2, 0) + 2 * coin_counts.get(key, 0) + coin_counts.get(key - 2, 0)
        wins += updated_coin_counts.get(-1, 0)
        updated_coin_counts.pop(-1, None)

        coin_counts = updated_coin_counts.copy()
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