import time

def main():
    number_of_heads: int = get_initial_heads()
    target_success_chance: float = get_success_chance()

    start_time = time.perf_counter()

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

def get_success_chance() -> float:
    while True:
        try:
            user_input = float(input("What success chance would you like? "))
        except ValueError:
            print("Invalid Input. Please try again")
        else:
            return user_input


if __name__ == "__main__":
    main()