"""
Link to task: https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
"""
import random
from typing import Set


class RandomizedSet1:

    def __init__(self):
        self._storage: Set[int] = set()

    def insert(self, val: int) -> bool:
        if val in self._storage:
            return False
        else:
            self._storage.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self._storage:
            self._storage.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        # such solution is slow, because we spent additional ~O(n) time to convert set to list
        return random.choice(list(self._storage))


class RandomizedSet:

    def __init__(self):
        self._storage_map: dict = {}
        self._storage_data: list = []

    def insert(self, val: int) -> bool:
        if val in self._storage_map:
            return False
        else:
            self._storage_map[val] = len(self._storage_data)
            self._storage_data.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self._storage_map:
            # copy last element in data to element to remove
            last_val = self._storage_data.pop()
            if last_val != val:
                data_idx = self._storage_map[val]
                self._storage_data[data_idx] = last_val
                self._storage_map[last_val] = data_idx
            del self._storage_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self._storage_data)

def test_check_randomised_set():
    # RandomizedSet randomizedSet = new RandomizedSet();
    randomised_set = RandomizedSet()
    # randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    assert randomised_set.insert(1)
    # randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
    assert not randomised_set.remove(2)
    # randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
    assert randomised_set.insert(2)
    # randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
    assert randomised_set.getRandom() in [1,2]
    # randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
    assert randomised_set.remove(1)
    # randomizedSet.insert(2); // 2 was already in the set, so return false.
    assert not randomised_set.insert(2)
    # randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
    assert randomised_set.getRandom() == 2