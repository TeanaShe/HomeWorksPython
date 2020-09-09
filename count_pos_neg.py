def count_positives_sum_negatives(arr):
    cnt = 0
    total = 0
    if len(arr) == 0:
        return []
    else:
        for num in arr:
            if num > 0:
                cnt += 1
            else:
                total += num
    return [cnt, total]
