point_zero = 0
MAX_DIAL = 100
MIN_DIAL = 0
dial = 50

with open('hint.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line: # An empty string signifies EOF
            break

        direction, degrees = line[0], int(line[1:])
        if direction == 'R':
            dial = (dial + degrees) % MAX_DIAL
        elif direction == 'L':
            dial = (dial - degrees) % MAX_DIAL

        if dial == 0:
            point_zero += 1

print(f"Password: {point_zero}")
