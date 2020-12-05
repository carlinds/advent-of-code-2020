def main():
    with open("boardingpasses.txt") as f:
        boarding_passes = [line.strip() for line in f.readlines()]

    max_id = 0
    for boarding_pass in boarding_passes:
        binary_pass = convert_pass_to_binary(boarding_pass)
        row = int(binary_pass[:7], 2)
        col = int(binary_pass[-3:], 2)
        seat_id = row * 8 + col
        max_id = max(seat_id, max_id)

    print(max_id)
    return 0


def convert_pass_to_binary(boarding_pass):
    return (boarding_pass.replace('F', '0')
                         .replace('B', '1')
                         .replace('L', '0')
                         .replace('R', '1'))


if __name__ == "__main__":
    main()