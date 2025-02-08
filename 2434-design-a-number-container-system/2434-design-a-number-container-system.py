class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_indices = {}

    def change(self, index: int, number: int) -> None:
        old_number = self.index_to_num.get(index)

        if old_number == number:
            return
        
        self.index_to_num[index] = number

        indices = self.num_to_indices.get(number, SortedSet())
        indices.add(index)
        self.num_to_indices[number] = indices

        if old_number is None:
            return
        
        old_indices = self.num_to_indices[old_number]
        old_indices.remove(index)

    def find(self, number: int) -> int:
        indices = self.num_to_indices.get(number, None)
        if indices is not None and len(indices) > 0:
            return indices[0]
        
        return -1