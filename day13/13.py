with open('01.txt', 'r') as f:
    start_time = int(f.readline().strip())
    busses = f.readline().strip().split(',')


def get_earliest_time(leaving_time, bus_times):
    while True:
        for bus in bus_times:
            if leaving_time % bus == 0:
                return leaving_time, bus
        leaving_time += 1


bus_time, bus_id = get_earliest_time(start_time, [int(x) for x in busses if x.isdigit()])
print('Part 1:', (bus_time - start_time) * bus_id)


def get_eariest_time_2(bus_times):
    time_and_remainder = [x for x in zip(bus_times, range(len(bus_times))) if x[0]]
    t = 0
    first = time_and_remainder.pop(0)
    step = 1 * first[0]
    while time_and_remainder:
        n, n_offset = time_and_remainder.pop(0)
        while True:
            t += step
            if (t + n_offset) % n == 0:
                break
        step *= n
    return t


earliest_time = get_eariest_time_2([int(x) if x.isdigit() else None for x in busses])

print('Part 2:', earliest_time)