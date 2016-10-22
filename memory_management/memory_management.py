import heapq
import queue
import math

import itertools


class CheckableQueue(queue.Queue):
    def __contains__(self, item):
        with self.mutex:
            return item in self.queue


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        process_test_case()


pq = []
entry_finder = {}
counter = itertools.count()
REMOVED = '<removed-task>'


def process_test_case():
    global pq
    global entry_finder
    global counter

    stuff = input().split(' ')

    num_pages = int(stuff[0])
    page_size = int(stuff[1])
    num_accesses = int(stuff[2])

    q = CheckableQueue()

    q_repl = 0
    pq_repl = 0

    pq_last_priority = 0

    for _ in range(num_accesses):
        address = int(input())
        page = math.floor(address / page_size)

        page_in_q = page in q
        page_in_pq = page in entry_finder

        if not page_in_q and q.qsize() >= num_pages:
            q_repl += 1
            q.get()

        if not page_in_q:
            q.put(page)


        if page_in_pq:
            add_page(page, pq_last_priority)
            pq_last_priority += 1
        else:
            if not page_in_pq and len(pq) >= num_pages:
                pq_repl += 1
                pop_task()

            if not page_in_pq:
                add_page(page, pq_last_priority)
                pq_last_priority += 1

    advertise = pq_repl < q_repl

    print('yes' if advertise else 'no', q_repl, pq_repl)

    pq = []
    entry_finder = {}
    counter = itertools.count()


def add_page(page, priority=0):
    if page in entry_finder:
        remove_page(page)

    count = next(counter)
    entry = [priority, count, page]
    entry_finder[page] = entry
    heapq.heappush(pq, entry)


def remove_page(page):
    entry = entry_finder.pop(page)
    entry[-1] = REMOVED


def pop_task():
    while pq:
        priority, count, page = heapq.heappop(pq)
        if page is not REMOVED:
            del entry_finder[page]
            return page

    raise KeyError('pop from an empty priority queue')


main()