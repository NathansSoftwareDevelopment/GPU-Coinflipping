def main():
    target_success_chance: float = get_success_chance()



def get_success_chance() -> float:
    user_input = float(input("What success chance would you like? "))
    return user_input


if __name__ == "__main__":
    main()