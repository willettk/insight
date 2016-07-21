def max_subarray(arr):

    # Given an array of numbers find the (contiguous) subarray which has the greatest sum in O(n) time
    # This problem comes up in MLE patterns of digitized images, for example

    # Solution here is "Kadane's algorithm" - https://en.wikipedia.org/wiki/Maximum_subarray_problem

    max_ending_here = 0
    max_so_far = 0

    start_ind,end_ind = 0,0

    for idx,x in enumerate(arr):
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

        if max_ending_here == 0:
            start_ind = idx
        if max_so_far == max_ending_here:
            end_ind = idx

    return max_so_far,start_ind,end_ind

# Some cases

print max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print max_subarray([-2, -1, -4, -6, -5])
print max_subarray([-2, -1, -4, -6, 0])
print max_subarray([0,0,0,0,0])
print max_subarray([2, 1, 4, 6, 0])
print max_subarray([2, 1, 4, 6, 5])
print max_subarray([])

# Slightly different - assume that empty arrays are not allowed, so now
# we want the _least negative_ value in the array (in effect, the highest
# number if the array is all negative numbers.

# Starts with the first element in array and resets on the current number,
# rather than zero. So if I had a running total of -10 and got to -5, it
# would replace that as the target number.

def max_subarray2(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print max_subarray2([-2, -1, -4, -6, -5])
