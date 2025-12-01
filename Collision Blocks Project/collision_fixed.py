# Watch the video: "The Most Unexpected Answer to a Counting Puzzle" by 3Blue1Brown https://youtu.be/HEfHFsfGXjs

def col(m1, m2):
    eps = 1e-12
    v1 = 0.0
    v2 = -1.0
    count = 0

    while True:

        if v1 > -eps and v2 > -eps and v2 >= v1 - eps:
            break
        if v1 < -eps:
            v1 = -v1
            count += 1
            continue
        new_v1 = ((m1 - m2) / (m1 + m2)) * v1 + (2 * m2 / (m1 + m2)) * v2
        new_v2 = (2 * m1 / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2
        v1, v2 = new_v1, new_v2
        count += 1
    return count

if __name__ == "__main__":
    m1 = float(input("Enter mass of block near wall: "))
    m2 = float(input("Enter mass of moving block: "))
    print("Total collisions =", col(m1, m2))

