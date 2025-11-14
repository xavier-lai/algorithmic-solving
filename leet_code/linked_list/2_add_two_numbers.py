from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current_1 = l1
        current_2 = l2
        carry = 0
        idx = 0
        while current_1 or current_2 or carry > 0:
            digit_1 = current_1.val if current_1 else 0
            digit_2 = current_2.val if current_2 else 0
            current_sum = digit_1 + digit_2 + carry
            carry, current_node_value = divmod(current_sum, 10)
            if idx == 0:
                head_node = ListNode(val=current_node_value)
                current_node = head_node
            else:
                current_node.next = ListNode(val=current_node_value)
                current_node = current_node.next

            idx += 1
            current_1 = current_1.next if current_1 else None
            current_2 = current_2.next if current_2 else None
        return head_node

    def naiveAddTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        value_1_str = str()
        current_1 = l1
        while current_1:
            value_1_str += str(current_1.val)
            current_1 = current_1.next

        value_2_str = str()
        current_2 = l2
        while current_2:
            value_2_str += str(current_2.val)
            current_2 = current_2.next

        reversed_value_1_str = value_1_str[::-1]
        reversed_value_2_str = value_2_str[::-1]

        reversed_value_1_int = int(reversed_value_1_str)
        reversed_value_2_int = int(reversed_value_2_str)

        value_sum_int = reversed_value_1_int + reversed_value_2_int
        value_sum_str = str(value_sum_int)
        result_length = len(value_sum_str)

        head_node = ListNode(val=int(value_sum_str[result_length - 1]))
        current_node = head_node

        for idx in range(result_length - 2, -1, -1):
            current_node_value = int(value_sum_str[idx])
            current_node.next = ListNode(val=current_node_value)
            current_node = current_node.next

        return head_node
