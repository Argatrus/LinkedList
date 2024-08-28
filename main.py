class Node:

    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LL:

    def __init__(self, *l) -> None:
        self.head = Node(l[0])
        self.last = self.head
        for i in l:
            if i == l[0]:
                continue
            self.last.next = Node(i)
            self.last = self.last.next
        self.length = len(l)

    def show_val(self):
        str = ''
        temp = self.head
        for i in range(self.length):
            str += f'{temp.val} -> '
            temp = temp.next
        return str + "None"

    def append(self, val):
        self.last.next = Node(val)
        self.last = self.last.next
        self.length += 1

    def len(self):
        return self.length

    def pop(self, index):
        if index < 0:
            raise IndexError('Cannot calculate negative index for LL.')
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        future = self.head
        current = None
        prev = None
        for i in range(self.length):
            if i > index:
                break
            prev = current
            current = future
            future = future.next
        else:
            raise IndexError('Index too large for LL.')
        prev.next = future
        self.length -= 1

    def insert(self, index, val):
        if index < 0:
            raise IndexError('Cannot calculate negative index for LL.')
        elif index == 0:
            self.head = Node(val, self.head)
        else:
            prev = None
            current = None
            future = self.head
            for i in range(self.length):
                if i > index:
                    break
                prev = current
                current = future
                future = future.next
            else:
                raise IndexError('Index too large for LL.')
            prev.next = Node(val, current)
        self.length += 1

