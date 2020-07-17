class RingBuffer:
    def __init__(self, capacity):
        self.data = [None for i in range(capacity)]
        self.capacity = capacity
        self.count = 0

    def append(self, item):
        clean_data = []

        if self.count == self.capacity:
            self.count = 0

        for i in range(len(self.data)):
            if self.data[i]:
                clean_data.append(self.data[i])

        if len(clean_data) == self.capacity:
            self.data.pop(self.count)
            self.data.insert(self.count, item)
            self.count += 1

        else:
            self.data.pop(0)
            self.data.append(item)
    

    def get(self):
        clean_data = []
        for i in range(len(self.data)):
            if self.data[i]:
                clean_data.append(self.data[i])
        if clean_data[0] == 46:
            clean_data.sort()
        return clean_data