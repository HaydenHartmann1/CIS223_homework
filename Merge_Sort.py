'''
Hayden Hartmann
Coding Problem: Merge Sort
6/19/2025
'''

def MergeSort(Sequence):
    # We first check if the sequence is less than 2
    seq_len = len(Sequence)
    if seq_len < 2:
        return
    # divide step
    mid = seq_len // 2
    # first and second half of the sequence
    seq_1 = Sequence[0:mid]
    seq_2 = Sequence[mid:seq_len]
    # conquer step by sorting
    MergeSort(seq_1)
    MergeSort(seq_2)
    # combine step
    Merge(seq_1, seq_2, Sequence)

def Merge(seq_1, seq_2, Sequence):
    # simple merge function
    i = j = 0
    while i + j < len(Sequence):
        if j == len(seq_2) or (i < len(seq_1) and seq_1[i] < seq_2[j]):
            # copy ith element of seq_1 as next item of Sequence
            Sequence[i + j] = seq_1[i]
            i += 1
        else:
            # copy the jth element of seq_2 as next item of Sequence
            Sequence[i + j] = seq_2[j]
            j += 1

data = [38, 27, 43, 3, 9, 82, 10]
print("Original: " + str(data))
MergeSort(data)
print("Sorted: " + str(data))
