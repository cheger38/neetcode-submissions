/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        for (int i = 1; i < lists.length; i++) {
            lists[i] = mergeTwoLists(lists[i], lists[i-1]);
        }

        return lists[lists.length-1];

    }

    public ListNode mergeTwoLists(ListNode one, ListNode two) {
        ListNode head = null;
        if (one.val < two.val) {
            head = one;
            one = one.next;
        } else {
            head = two;
            two = two.next;
        }
        ListNode current = head;

        while (one != null && two != null) {
            if (one.val < two.val) {
                current.next = one;
                one = one.next;
            } else {
                current.next = two;
                two = two.next;
            }
            current = current.next;
        }

        if (one == null) current.next = two;
        if (two == null) current.next = one;

        return head;
    }
}
