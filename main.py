from three_d_shapes import Prism, Cube, Pyramid, Cylinder, Cone, Sphere
from two_d_shapes import Rectangle, Square, Parallelogram, Rhombus, Trapezoid, Circle, RegularPolygon


def get_shape_2d(for_3d=False, for_pyramid=False):
    shape_data = []
    while True:
        shape = input(f"Enter a {'base ' if for_3d else ''}shape (for regular polygon enter n-gon): ")
        shape = shape.lower()

        # Restrict pyramid base to only regular polygon shapes
        if for_pyramid and not (shape == "square" or shape.endswith("-gon")):
            print("Only regular polygon bases (e.g., square or n-gon) are allowed for pyramids.")
            continue

        match shape:
            case "rectangle" | "parallelogram":
                if for_pyramid:
                    print("This shape is not allowed as a base for a pyramid.")
                    continue
                shape_data.append(shape)
                try:
                    shape_data.append(float(input("Enter the base: ")))
                    shape_data.append(float(input("Enter the height: ")))
                    if shape == "parallelogram" and not for_3d:
                        shape_data.append(float(input("Enter the length of the side adjacent to the base: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case "square":
                shape_data.append(shape)
                try:
                    shape_data.append(float(input("Enter the side: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case "rhombus":
                if for_pyramid:
                    print("This shape is not allowed as a base for a pyramid.")
                    continue
                shape_data.append(shape)
                try:
                    shape_data.append(float(input("Enter diagonal 1: ")))
                    shape_data.append(float(input("Enter diagonal 2: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case "trapezoid":
                if for_pyramid:
                    print("This shape is not allowed as a base for a pyramid.")
                    continue
                shape_data.append(shape)
                try:
                    shape_data.append(float(input("Enter base 1: ")))
                    shape_data.append(float(input("Enter base 2: ")))
                    shape_data.append(float(input("Enter height: ")))
                    if not for_3d:
                        shape_data.append(float(input("Enter leg 1: ")))
                        shape_data.append(float(input("Enter leg 2: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case "circle":
                if for_pyramid:
                    print("This shape is not allowed as a base for a pyramid.")
                    continue
                shape_data.append(shape)
                try:
                    shape_data.append(float(input("Enter the radius: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case _:
                if shape.endswith("-gon"):
                    try:
                        sides = int(shape.split("-")[0])
                        shape_data.append(shape)
                        shape_data.append(float(input("Enter the apothem: ")))
                        shape_data.append(float(input("Enter the length of a side: ")))
                        shape_data.append(float(sides))
                        break
                    except ValueError:
                        print("Invalid input.")
                        continue
                else:
                    print("Invalid shape input.")
                    continue

    return shape_data


def get_shape_3d():
    shape_data = []
    while True:
        shape = input("Enter a 3D shape: ")
        shape = shape.lower()

        match shape:
            case "prism":
                try:
                    shape_data.append(shape)
                    shape_data.append(get_shape_2d(for_3d=True))
                    shape_data.append(float(input("Enter the height: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case "cube":
                shape_data.append(shape)
                try:
                    shape_data.append(float(input("Enter the side: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case "pyramid":
                try:
                    shape_data.append(shape)
                    shape_data.append(get_shape_2d(for_3d=True, for_pyramid=True))
                    shape_data.append(float(input("Enter the height: ")))
                    shape_data.append(float(input("Enter the slant height: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case "cylinder":
                shape_data.append(shape)
                try:
                    shape_data.append(float(input("Enter the radius: ")))
                    shape_data.append(float(input("Enter the height: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case "cone":
                shape_data.append(shape)
                try:
                    shape_data.append(float(input("Enter the radius: ")))
                    shape_data.append(float(input("Enter the height: ")))
                    shape_data.append(float(input("Enter the slant height: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case "sphere":
                shape_data.append(shape)
                try:
                    shape_data.append(float(input("Enter the radius: ")))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            case _:
                print("Invalid 3D shape.")
                continue

    return shape_data


def create_obj_2d(shape_data):
    shape = shape_data[0]
    if shape.endswith("-gon"):
        return RegularPolygon(shape_data[1], shape_data[2], shape_data[3])

    match shape:
        case "rectangle":
            return Rectangle(shape_data[1], shape_data[2])
        case "square":
            return Square(shape_data[1])
        case "parallelogram":
            return Parallelogram(shape_data[1], shape_data[2], shape_data[3])
        case "rhombus":
            return Rhombus(shape_data[1], shape_data[2])
        case "trapezoid":
            return Trapezoid(shape_data[1], shape_data[2], shape_data[3], shape_data[4], shape_data[5])
        case "circle":
            return Circle(shape_data[1])
        case _:
            raise ValueError("Invalid 2D shape data")


def create_obj_3d(shape_data):
    shape = shape_data[0]

    match shape:
        case "prism":
            return Prism(create_obj_2d(shape_data[1]), shape_data[2])
        case "cube":
            return Cube(shape_data[1])
        case "pyramid":
            return Pyramid(create_obj_2d(shape_data[1]), shape_data[2], shape_data[3])
        case "cylinder":
            return Cylinder(shape_data[1], shape_data[2])
        case "cone":
            return Cone(shape_data[1], shape_data[2], shape_data[3])
        case "sphere":
            return Sphere(shape_data[1])
        case _:
            raise ValueError("Invalid 3D shape data")


def main():
    while True:
        shape_dimensions = input("Is your shape 2D or 3D? ").strip().lower()
        if shape_dimensions == "2d":
            shape_data = get_shape_2d()
            shape_obj = create_obj_2d(shape_data)
            units = input("Enter a unit of measurement: ")

            print(f"Area: {round(shape_obj.area(), 2)} square {units}")
            if shape_data[0] == "circle":
                print(f"Circumference: {round(shape_obj.circumference(), 2)} {units}")
            else:
                print(f"Perimeter: {round(shape_obj.perimeter(), 2)} {units}")
            break

        elif shape_dimensions == "3d":
            shape_data = get_shape_3d()
            shape_obj = create_obj_3d(shape_data)
            units = input("Enter a unit of measurement: ")

            if shape_data[0] != "sphere":
                print(f"Lateral Area: {round(shape_obj.lateral_area(), 2)} square {units}")
            print(f"Total Area: {round(shape_obj.total_area(), 2)} square {units}")
            print(f"Volume: {round(shape_obj.volume(), 2)} cubic {units}")
            break

        else:
            print("This dimension is not supported. Please enter '2D' or '3D'.")
            continue


if __name__ == "__main__":
    main()
