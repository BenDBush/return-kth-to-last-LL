class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


    def __repr__(self):
        return "data: " + str(self.data) + "next: " + str(self.next)


    def kth_to_last(self, k):
        runner = self
        behind = self
        for i in range(k):
            runner = runner.next

        while runner.next != None:
            runner = runner.next
            behind = behind.next

        return behind




if __name__ == "__main__":
    node = Node(1, next = Node(2, next = Node(3, next = Node(4, next = Node(5)))))
    result = node.kth_to_last(1)
    print(result.data)