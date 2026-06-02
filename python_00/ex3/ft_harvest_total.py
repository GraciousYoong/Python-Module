def ft_harvest_total() -> None:
    day_1_harvest = int(input("Day 1 harvest: "))
    day_2_harvest = int(input("Day 2 harvest: "))
    day_3_harvest = int(input("Day 3 harvest: "))
    total_harvest = day_1_harvest + day_2_harvest + day_3_harvest
    print(f"Total harvest: {total_harvest}")
