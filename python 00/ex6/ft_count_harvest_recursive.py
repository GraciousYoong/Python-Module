def ft_count_harvest_recursive(days: int | None = None, index: int = 1):
    if days is None:
        days = int(input('Days until harvest: '))
    if index > days:
        print("Harvest time!")
        return
    print('Day', index)
    ft_count_harvest_recursive(days, index + 1)
