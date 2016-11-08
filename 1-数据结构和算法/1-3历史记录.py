from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        print('----' + li.strip('\n') + '-----')
        if pattern in li:
            yield li.strip('\n'), previous_lines
        previous_lines.append(li)
if __name__ == '__main__':
    with open(r'cookbook.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            i = 0
            for pline in prevlines:
                print(pline, i, end='')
            # print(line, end='')
            print('-' * 20)

# def s(items):
#     head, *tail = items
#     return head + s(tail) if tail else head

# items = [1, 3, 5, 7, 9]
# print(s(items))
