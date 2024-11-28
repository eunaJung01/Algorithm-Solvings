CACHE_HIT = 1
CACHE_MISS = 5


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def lookup(self, value):
        global time
        prev_node = None
        cur_node = self.head

        while cur_node:
            if cur_node.value == value:
                time += CACHE_HIT

                if cur_node == self.tail:
                    return

                if cur_node == self.head:
                    self.head = cur_node.next
                else:
                    prev_node.next = cur_node.next

                self.tail.next = cur_node
                cur_node.next = None
                self.tail = cur_node
                return

            prev_node = cur_node
            cur_node = cur_node.next

        time += CACHE_MISS
        new_node = Node(value)

        if self.size == 0:
            self.head = self.tail = new_node
            self.size = 1
            return

        if self.size == self.max_size:
            self.head = self.head.next
        else:
            self.size += 1

        self.tail.next = new_node
        self.tail = new_node


def solution(cacheSize, cities):
    global time
    time = 0

    if cacheSize == 0:
        return len(cities) * CACHE_MISS

    if cacheSize == 1:
        cache = None
        for city in cities:
            city = city.lower().strip()
            if cache == city:
                time += CACHE_HIT
                continue
            time += CACHE_MISS
            cache = city
        return time

    cache = LinkedList(cacheSize)
    for city in cities:
        cache.lookup(city.lower().strip())
    return time
