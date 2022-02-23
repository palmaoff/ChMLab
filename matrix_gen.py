import random

VALUE_RANGES = (10, 100, 1000)
MATRIX_SIZES = (10, 100, 1000)


def generate_matrix():

    for matrix_size in MATRIX_SIZES:

        for value_range in VALUE_RANGES:

            # setting k value for string and column
            k = random.randint(0, matrix_size - 1)

            with open(f"tests/gen_matrix_{matrix_size}_{value_range}", "w") as file:
                for i in range(matrix_size):
                    row = []
                    for j in range(matrix_size):
                        # generate values
                        if j == matrix_size - i - 1:
                            row.append(random.randint(-value_range, value_range))
                        elif j == matrix_size - i - 1 - 1:
                            row.append(random.randint(-value_range, value_range))
                        elif j == matrix_size - i - 1 + 1:
                            row.append(random.randint(-value_range, value_range))
                        elif j == k or i == k:
                            row.append(random.randint(-value_range, value_range))
                        else:
                            row.append(0)
                    # pushing list to file
                    file.write("\t".join(str(x) for x in row) + "\n")
                # generate f values
                file.write("\n")
                for i in range(matrix_size):
                    file.write(str(random.randint(-value_range, value_range)) + "\n")


def main():
    generate_matrix()


if __name__ == "__main__":
    main()
