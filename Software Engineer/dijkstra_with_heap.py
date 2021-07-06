class MinHeap:
    def __init__(self, array):
        # Holds the position in the heap where there is each vertex
        self.vertex_map = {idx: idx for idx in range(len(array))}
        self.heap = self.build_heap(array)

    def is_empty(self):
        return len(self.heap) == 0

    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        for curr_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(curr_idx, len(array) - 1, array)
        return array

    def sift_down(self, curr_idx, end_idx, heap):
        
