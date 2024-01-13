class MaxHeap:
    def __init__(self):
        # 初始化一个空堆
        self.heap = [] #完全二叉 层次遍历

    def push(self, value):
        # 添加元素到堆末尾
        self.heap.append(value)
        # 将新元素上移，以保持最大堆性质
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        # 交换根节点与最后一个节点
        self._swap(0, len(self.heap) - 1)
        # 弹出最大元素
        max_element = self.heap.pop()
        # 将交换后的根节点下移，以保持最大堆性质
        self._heapify_down(0)

        return max_element

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2 #父节点的索引=子节点-1 //2
            # 如果新元素大于父节点，交换它们
            if self.heap[index] > self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            # 找到左右子节点中最大的节点
            if (
                left_child_index < len(self.heap)
                and self.heap[left_child_index] > self.heap[largest]
            ):
                largest = left_child_index

            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] > self.heap[largest]
            ):
                largest = right_child_index

            # 如果最大节点不是当前节点，交换它们
            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def _swap(self, i, j):
        # 交换两个节点的值
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# 示例用法
max_heap = MaxHeap()
max_heap.push(4)
max_heap.push(1)
max_heap.push(7)
max_heap.push(3)

print("堆中的元素:", max_heap.heap)

max_element = max_heap.pop()
print("弹出的最大元素:", max_element)

print("剩余的堆中的元素:", max_heap.heap)
