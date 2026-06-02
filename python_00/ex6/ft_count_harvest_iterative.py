def ft_count_harvest_iterative(countdown: int = 1) -> None:
    days_til_harvest = int(input("Days until harvest: "))
    while days_til_harvest > 0:
        print(f"Day {countdown}")
        countdown += 1
        days_til_harvest -= 1
    print("Harvest time!")
