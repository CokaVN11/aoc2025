MAX_DIAL = 100

DIRECTION = {
    'R': (1, lambda dial, rem: (dial + rem) >= MAX_DIAL),
    'L': (-1, lambda dial, rem: dial > 0 and (dial - rem) <= 0),
}

def count_zero_crossings(filename):
    dial = 50
    crossings = 0

    with open(filename) as f:
        for line in f:
            direction, degrees = line[0], int(line[1:])
            full, rem = divmod(degrees, MAX_DIAL)

            sign, crosses_fn = DIRECTION[direction]
            crossings += full + crosses_fn(dial, rem)
            dial = (dial + sign * rem) % MAX_DIAL

    return crossings

print(f"Password: {count_zero_crossings('hint.txt')}")
