def odometer (oksana):
    distance = oksana[0] * oksana[1]
    for i in range (2, len(oksana)):
        if i % 2 == 0:
            distance = distance + (oksana[i+1] - oksana[i-1]) * oksana[i]
    return distance
