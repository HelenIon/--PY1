def delete(list_, index=None):
    if index is not None and index >= 0:
        left = list_[0:index]
        right = list_[index + 1:len(list_)]
        return left + right
    index = None
    return list_[0:len(list_) - 1]


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
