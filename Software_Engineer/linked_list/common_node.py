"""
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
"""

# Function to find intersection point in Y shaped Linked Lists.
def intersect_point(head1, head2):

    new_head_1 = reverse_list(head1)
    new_head_2 = reverse_list(head2)

    # print_linked_list(new_head_1)
    # print_linked_list(new_head_2)

    different = False
    prev_node = -1

    curr_node_1 = new_head_1
    curr_node_2 = new_head_2

    # print("=" * 75)
    while not different:
        # print(curr_node_1.data, curr_node_2.data)
        if curr_node_1.data != curr_node_2.data:
            different = True
        else:
            prev_node = curr_node_1
            curr_node_1 = curr_node_1.next
            curr_node_2 = curr_node_2.next

    if prev_node == -1:
        return prev_node
    return prev_node.data


def reverse_list(head):
    curr_node = head
    prev_node = None

    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


def insert(head, elem):
    temp = Node(elem)
    if head is None:
        head = temp
    else:
        ptr = head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = temp
    return head


def build_linked_list(array):
    head = None
    for i in range(0, len(array)):
        head = insert(head, array[i])
    return head


def print_linked_list(head):
    while head is not None:
        print("{} -> ".format(head.data), end=" ")
        head = head.next
    print()


array_1 = [39, 9, 31, 22, 82, 6, 18, 15, 91]
array_2 = [80, 72, 18, 15, 91]


head_1 = build_linked_list(array_1)
head_2 = build_linked_list(array_2)
# print_linked_list(head_1)
# print_linked_list(head_2)

# rev_head_1 = reverse_list(head_1)
# rev_head_2 = reverse_list(head_2)

# print_linked_list(rev_head_1)
# print_linked_list(rev_head_2)

print(intersect_point(head_1, head_2))
