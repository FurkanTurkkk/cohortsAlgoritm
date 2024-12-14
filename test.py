import math


points = [(1, 2), (4, 6), (5, 9), (2, 1)]


def euclideanDistance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        point1 = points[i]
        point2 = points[j]
        distance = euclideanDistance(point1, point2)
        distances.append((point1, point2, distance))

print("Nokta Çiftleri ve Aralarındaki Mesafeler:\n")
for point1, point2, distance in distances:
    print(f"Noktalar: {point1} ve {point2} -> Öklid Mesafesi: {distance:.2f}")
