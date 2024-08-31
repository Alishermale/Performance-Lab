def read_circle_data():
    with open(circle_data, 'r') as file:
        center_x, center_y = map(float, file.readline().split())
        radius = float(file.readline().strip())
    return center_x, center_y, radius


def read_points_data():
    points = []
    with open(points_data, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def point_position(center_x, center_y, radius, x, y):
    distance_squared = (x - center_x) ** 2 + (y - center_y) ** 2
    radius_squared = radius ** 2

    if distance_squared < radius_squared:
        return 1
    elif distance_squared == radius_squared:
        return 0
    else:
        return 2


circle_data = input('Файл с координатами центра окружности и его радиусом: ')
points_data = input('файл с координатами точек: ')
center_x, center_y, radius = read_circle_data()
points = read_points_data()

for x, y in points:
    print(point_position(center_x, center_y, radius, x, y))
