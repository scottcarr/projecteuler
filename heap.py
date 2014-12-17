import random

class MinHeap:
    def __init__(self):
        self.nodes = []
    def insert(self, key):
        self.nodes.append(key)
        self.rebalance_up(len(self.nodes)-1)
    def get_parent_idx(self, child_idx):
        idx = (child_idx - 1) / 2
        if idx < 0:
            return 0
        return idx
    def get_child_idx(self, parent_idx):
        left = parent_idx * 2 + 1
        right = parent_idx * 2 + 2
        return left, right
    def rebalance_up(self, child_idx):
        parent_idx = self.get_parent_idx(child_idx)
        if self.nodes[parent_idx] > self.nodes[child_idx]:
            tmp = self.nodes[child_idx]
            self.nodes[child_idx] = self.nodes[parent_idx]
            self.nodes[parent_idx] = tmp
            self.rebalance_up(parent_idx)
    def rebalance_down(self, parent_idx):
        parent = self.nodes[parent_idx]
        left_idx, right_idx = self.get_child_idx(parent_idx)
        n = len(self.nodes)

        if left_idx < n - 1 and right_idx < n - 1:
            left = self.nodes[left_idx]
            right = self.nodes[right_idx]
            if left < parent or right < parent:
                if left < right:
                    self.nodes[left_idx] = parent
                    self.nodes[parent_idx] = left
                    self.rebalance_down(left_idx)
                else:
                    self.nodes[right_idx] = parent
                    self.nodes[parent_idx] = right
                    self.rebalance_down(right_idx)
        elif left_idx < n - 1:
            left = self.nodes[left_idx]
            if left < parent:
                self.nodes[left_idx] = parent
                self.nodes[parent_idx] = left
        
    def peek_min(self):
        return self.nodes[0]
    def extract_min(self):
        if self.nodes:
            rv = self.nodes[0]
            if len(self.nodes) > 1:
                self.nodes[0] = self.nodes.pop()
                self.rebalance_down(0)
            else:
                self.nodes.remove(rv)
            return rv
        else:
            return None

def test():
    nums = range(100)
    arr = []
    h = MinHeap()
    while len(nums) > 0:
        rand = random.randint(0, len(nums)-1)
        n = nums[rand]
        arr.append(n)
        h.insert(n)
        if (random.randint(0, 10) == 0):
            expected = min(arr)
            actual = h.peek_min()
            if expected != actual:
                print "error!"
                print expected
                print actual
        if random.randint(0, 25) == 0 and len(nums) < 90:
            break
        nums.remove(n)

    expected = min(arr)
    actual = h.extract_min()
    if expected != actual:
        print "error!"
        print expected
        print actual

    arr.remove(expected)

    expected = min(arr)
    actual = h.extract_min()
    if expected != actual:
        print "error!"
        print expected
        print actual

for i in range(100):
    test()

print "done"

            
            



