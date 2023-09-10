import time
import math


def lg_term(x, y):
    l2p = math.log(2 * math.pi)
    const = - 500 + 500.5 * math.log(500)
    if x == 0 and y == 0:
        lnc = 0
    elif x == 0:
        lnc = const - (0.5 + y) * math.log(x2) + y \
              + (500.5 - y) * (math.log(2 * math.pi) - math.log(500 - y))
    elif y == 0:
        lnc = const - (0.5 + x) * math.log(x) + x \
            + (500.5 - x) * (math.log(2 * math.pi) - math.log(500 - x))
    else:
        lnc = (500 - x - y) * l2p \
            - (0.5 + x) * math.log(x) - (0.5 + y) * math.log(y) \
            - (500.5 - x - y) * math.log(500 - x - y) \
            + x + y + const
    result = lnc + x * math.log(0.18) + y * math.log(0.42) + (500-x-y) * math.log(0.4)
    return result


# Record the start time
start_time = time.time()

# Calculate the sum
Pa = 0
for x1 in range(0, int(0.15 * 500) + 1):
    for x2 in range(0, int(0.4 * 500) + 1):
        for x3 in range(int(0.43 * 500), 500 + 1):
            if x1 + x2 + x3 == 500:
                lgc = lg_term(x1, x2)
                term = math.exp(lgc)
            else:
                term = 0
            Pa += term

# Record the end time
end_time = time.time()

# Calculate the total computing time
computing_time = end_time - start_time


# Results
print("P(A)=", Pa)
print("Computing time:", computing_time)
