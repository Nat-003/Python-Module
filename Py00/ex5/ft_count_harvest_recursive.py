def ft_count_harvest_recursive(days):
    if days > 0:
        ft_count_harvest_recursive(days -1)
        print(f"Day {days}")
days = int(input("Days until harvest: "))
ft_count_harvest_recursive(days)
print("Harvest time")