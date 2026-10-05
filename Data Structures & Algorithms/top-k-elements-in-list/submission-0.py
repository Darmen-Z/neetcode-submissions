class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {} 

        for num in nums:
            if not num in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1

        result = []
        for i in range(0, k):
            max_el = list(my_dict.values())[0]
            key_to_delete = list(my_dict.keys())[0]
            for key, value in my_dict.items():
                if max_el < value:
                    max_el = value
                    key_to_delete = key
            result.append(key_to_delete)
            del my_dict[key_to_delete]

        return result