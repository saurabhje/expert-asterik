def kFrequency(nums, k):
    hashmap = {}
    bucket = [[] for i in range(len(nums) + 1)]

    # Count the occurrences of each number and store in hashmap
    for n in nums:
        hashmap[n] = 1 + hashmap.get(n, 0)

    # Distribute numbers into buckets based on their occurrences
    for n, c in hashmap.items():
        bucket[c].append(n)

    # Collect k most frequent elements from buckets
    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res

num_list = [1, 2, 2, 2, 2, 5, 57, 19]
result = kFrequency(num_list, 2)
print(result)
