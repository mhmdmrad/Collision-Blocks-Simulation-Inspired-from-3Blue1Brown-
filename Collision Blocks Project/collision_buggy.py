# Watch the video: "The Most Unexpected Answer to a Counting Puzzle" by 3Blue1Brown
# Buggy version
def col(m1, m2):
    v1 = 0.0
    v2 = -1.0
    count = 0

    while True:
        if v2 > 0 and v1 > 0 and v1 < v2:
            break
        if v1 < 0:
            v1 = -v1
            count += 1
            continue
        new_v1 = ((m1 - m2) / (m1 + m2)) * v1 + (2 * m2 / (m1 + m2)) * v2
        new_v2 = (2 * m1 / (m1 + m2)) * v1 + ((m2 - m1) / (m1 + m2)) * v2
        v1, v2 = new_v1, new_v2
        count += 1

    return count
m1 = float(input("Enter mass of block near wall: "))
m2 = float(input("Enter mass of moving block: "))
print("Total collisions =", col(m1, m2))
