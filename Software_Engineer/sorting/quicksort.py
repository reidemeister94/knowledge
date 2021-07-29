"""
Time:
	Best:  O(n log(n))
	Avg:   O(n log(n))
	Worst: O(n^2)
Space:
		   O(log(n))
"""


def quick_sort(array=[12, 4, 5, 6, 7, 3, 1, 15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return (
            quick_sort(less) + equal + quick_sort(greater)
        )  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


print(quick_sort())
