
tree_map = open("input/day03_input.txt").readlines()


def third_helper():
    steps_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res = 1
    for item in steps_list:
        dx, dy = item
        trees = helper(dx, dy)
        res *= trees
        print(f" {dx, dy} : {trees}")
    return res


def helper(dx, dy):
    cols = len(tree_map[0])
    rows = len(tree_map)
    trees = 0
    step_dx = 0
    step_dy = 0
    while step_dy < rows - 1:
        row = tree_map[step_dy]
        trees += (row[step_dx % cols] == "#")
        step_dx += dx
        step_dy += dy

    return trees



