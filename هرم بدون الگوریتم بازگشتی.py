class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def build_heap(self, iterable):
        self.heap = iterable[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def heap_sort(self):
        sorted_arr = []
        while self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            sorted_arr.insert(0, self.heap.pop())
            self.heapify(0)
        return sorted_arr


heap = MaxHeap()
arr = [12, 11, 13, 5, 6, 7]
heap.build_heap(arr)
sorted_array = heap.heap_sort()
print("sorted array using heap sort: ", sorted_array)
