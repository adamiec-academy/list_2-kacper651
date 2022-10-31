def multiplication_table(x1, x2, y1, y2):
    space_for_value = 4
    for i in range(y1, y2 + 1):
        if i == y1:
            print(space_for_value * " ", end="  |")
            for k in range(x1, x2 + 1):  # wiem że chujowo to wplywa na zlozonosc xd
                print(f"{k: {space_for_value}}", end="")
            print()
            print(space_for_value * x2 * "-")
        print(f"{i: {space_for_value}}", end="  |")
        for j in range(x1, x2 + 1):
            print(f"{i * j: {space_for_value}}", end="")
        print()


multiplication_table(3, 9, 2, 12)
