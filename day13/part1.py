import math

def main():
    with open('timetable.txt') as f:
        depart_time = int(f.readline().strip())
        buses = [int(bus) for bus in f.readline().split(',') if bus != 'x']

    departures = [math.ceil(depart_time / bus)*bus for bus in buses]
    earliest_departure = min(departures)
    earliest_bus = buses[departures.index(earliest_departure)]

    print((earliest_departure - depart_time) * earliest_bus)
    return 0


if __name__ == "__main__":
    main()