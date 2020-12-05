def main():
    with open("boardingpasses.txt") as f:
        boarding_passes = [line.strip() for line in f.readlines()]

    ids = []
    for boarding_pass in boarding_passes:
        binary_pass = convert_pass_to_binary(boarding_pass)
        row = int(binary_pass[:7], 2)
        col = int(binary_pass[-3:], 2)
        seat_id = row * 8 + col
        ids.append(seat_id)

    print(find_missing_id(ids))


def convert_pass_to_binary(boarding_pass):
    return (boarding_pass.replace('F', '0')
                         .replace('B', '1')
                         .replace('L', '0')
                         .replace('R', '1'))


def find_missing_id(ids):
    sorted_ids = sorted(ids)
    return [id for id in range(sorted_ids[0], sorted_ids[-1]+1)
                                       if id not in sorted_ids]

if __name__ == "__main__":
    main()