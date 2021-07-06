class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)

    # O(n) time | O(1) space
    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for curr_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(curr_idx, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def sift_down(self, curr_idx, end_idx, heap):
        child_one_idx = curr_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = curr_idx * 2 + 2 if curr_idx * 2 + 2 <= end_idx else -1
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            if heap[idx_to_swap] < heap[curr_idx]:
                self.swap(curr_idx, idx_to_swap, heap)
                curr_idx = idx_to_swap
                child_one_idx = curr_idx * 2 + 1
            else:
                return

    # O(log(n)) time | O(1) space
    def sift_up(self, curr_idx, heap):
        parent_idx = (curr_idx - 1) // 2
        while curr_idx > 0 and heap[curr_idx] < heap[parent_idx]:
            self.swap(curr_idx, parent_idx, heap)
            curr_idx = parent_idx
            parent_idx = (parent_idx - 1) // 2

    def peek(self):
        return self.heap[0]

    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

    def swap(self, curr_idx, idx_to_swap, heap):
        heap[curr_idx], heap[idx_to_swap] = heap[idx_to_swap], heap[curr_idx]
