def convert(celsius_data):
    farenhiet = []
    for items in celsius_data:
        farenhiet.append(((items*9)/5)+32)
    return farenhiet
