def ft_count_harvest_recursive(
    days_til_harvest: int | None = None,
    countdown: int = 1
):
    if days_til_harvest is None:
        days_til_harvest = int(input('Days until harvest: '))
    if countdown > days_til_harvest:
        print("Harvest time!")
        return
    print('Day', countdown)
    ft_count_harvest_recursive(days_til_harvest, countdown + 1)
