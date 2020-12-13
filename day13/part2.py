def main():
    with open('timetable.txt') as f:
        _ = f.readline()
        time_table = [(int(bus), int(delta_t)) for (delta_t, bus) in 
            enumerate(f.readline().split(',')) if bus != 'x']

    n = [entry[0] for entry in time_table]
    b = [(n[i] - entry[1]) for i, entry in enumerate(time_table)]
    N = 1
    for ni in n:
        N *= ni

    x = 0
    for bi, ni in zip(b, n):
        y = N//ni

        for j in range(1, ni):
            if y*j%ni == 1:
                break
        x += bi*y*j

    x = x % N
    print(x)


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))