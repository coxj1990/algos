# Time complexity O(num_rows^2)
def get_pascals_triangle(num_rows: int) -> list[int]:
    triangle = [[1]]
    for i in range(1, num_rows):
        last_row = [0] + triangle[-1] + [0]
        new_row = []
        for j in range(1, len(last_row)):
            new_row.append(last_row[j - 1] + last_row[j])
        triangle.append(new_row)
    return triangle
