def mergeSort(array):
    if len(array) == 1:
		return array
	
	mid_idx = len(array) // 2
	left = array[: mid_idx]
	right = array[mid_idx :]
	
	return merge_sorted_arrays(mergeSort(left), mergeSort(right))


def merge_sorted_arrays(left, right):
	sorted_array = [None] * (len(left) + len(right))
	i = 0
	j = 0
	k = 0
	while i < len(left) and j < len(right):
		if left[i] > right[j]:
			sorted_array[k] = right[j]
			j += 1
		else:
			sorted_array[k] = left[i]
			i += 1
		k += 1
	while i < len(left):
		sorted_array[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		sorted_array[k] = right[j]
		j += 1
		k += 1
	return sorted_array
			
			