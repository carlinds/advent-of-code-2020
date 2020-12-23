class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

#START_CUPS = '389125467'
START_CUPS = '364297581'
N_CUPS = int(1e6)
N_MOVES = int(1e7)

def main():
    nodes = {}
    for c in range(1, N_CUPS + 1):
        nodes[c] = Node(c)

    for cur, nxt in zip(START_CUPS, START_CUPS[1:]):
        cur, nxt = map(int, [cur, nxt])
        nodes[cur].next = nodes[nxt]

    nodes[int(START_CUPS[-1])].next = nodes[len(START_CUPS) + 1]
    for cur in range(len(START_CUPS) + 1, N_CUPS):
        nodes[cur].next = nodes[cur + 1]
    nodes[N_CUPS].next = nodes[int(START_CUPS[0])]

    cur = nodes[int(START_CUPS[0])]
    for _ in range(N_MOVES):
        pick_up = [cur.next, cur.next.next, cur.next.next.next]
        dest = nodes[cur.val - 1] if (cur.val -1) > 0 else nodes[N_CUPS]

        while (dest in pick_up):
            dest = nodes[dest.val - 1] if (dest.val - 1) > 0 else nodes[N_CUPS]

        cur.next = pick_up[-1].next
        pick_up[-1].next = dest.next
        dest.next = pick_up[0]

        cur = cur.next
    
    print(nodes[1].next.val * nodes[1].next.next.val)
    return 0


if __name__ == "__main__":
    main()
