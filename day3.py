def problem1():
    with open("day3.txt", "r") as f:
        grid = [line.strip() for line in f.readlines()]
        trees = 0
        x, y = 0, 0
        while y < len(grid):
            if grid[y][x] == "#":
                trees += 1
            x += 3
            x %= len(grid[0])
            y += 1
        print(trees)

def problem2():
    with open("day3.txt", "r") as f:
        grid = [line.strip() for line in f.readlines()]
        tree_counts = 1
        for right, down in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
            trees = 0
            x, y = 0, 0
            while y < len(grid):
                if grid[y][x] == "#":
                    trees += 1
                x += right
                x %= len(grid[0])
                y += down
            tree_counts *= trees
        
        print(tree_counts)

if __name__ == "__main__":
    problem1()
    problem2()