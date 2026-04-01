def ft_count_harvest_iterative() -> None:
    days_til_harvest = int(input("Days until harvest: "))
    while days_til_harvest > 0:
        print(f"Day {days_til_harvest}")
    print("Harvest time!")
