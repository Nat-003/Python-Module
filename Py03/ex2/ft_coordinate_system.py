import sys
import math


def coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    coordinate1 = []
    center = (0, 0, 0)
    try:
        if len(sys.argv) == 4:
            print(f'Parsing coordinate'
                  f'"{sys.argv[1]}, {sys.argv[2]},{sys.argv[3]}"')
            for arg in sys.argv[1:]:
                value = int(arg)
                coordinate1.append(value)
            created_pos_cor = (10, 20, 5)
            print(f"Position created: {created_pos_cor}")
            x3, y3, z3 = created_pos_cor
            x2, y2, z2 = center
            dis = math.sqrt((x2 - x3)**2 + (y2 - y3)**2 + (z2 - z3)**2)
            print(f"Distance between"
                  f"{center} and {created_pos_cor}: {dis:.2f}\n")
            coordinate_tuple = tuple(coordinate1)
            print(f"Parsed coordinate: {coordinate_tuple}")
            x1, y1, z1 = coordinate_tuple
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            print(f"Distance between"
                  f"{center} and {coordinate_tuple}: {distance:.2f}")
        else:
            print("Please Enter valide coordinate: x,y,z")
    except ValueError as e:
        print(f"Error: When parsing {e}")


if __name__ == "__main__":
    coordinate_system()
