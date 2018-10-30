class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        //排除其一为空
        ListNode reListHead = new ListNode(0);
        ListNode tempHead = reListHead;
        
        while((l1 != null) && (l2 != null)) {
                if (l1.val <= l2.val) {         //l1小，追加到reHead
                        ListNode newNode = l1;
                        tempHead.next = newNode;
                        l1 = l1.next;
                        tempHead = tempHead.next;
                } else {                                        //l2小，追加到reHead
                        ListNode newNode = l2;
                        tempHead.next = newNode;
                        l2 = l2.next;
                        tempHead = tempHead.next;
                }               
        }

        if (l1 == null) tempHead.next = l2;
        if (l2 == null) tempHead.next = l1;
        
                return reListHead.next;
    }
}

public class easy_021_merge_two_sorted_lists {
        public static void main(String[] args) {
                /*
                1->2->4,
                1->3->4
                */
//              输出：1->1->2->3->4->4
                ListNode l13 = new ListNode(4);
                ListNode l12 = new ListNode(2);
                ListNode l11 = new ListNode(1);
                l11.next = l12;
                l12.next = l13;
                
                ListNode l23 = new ListNode(4);
                ListNode l22 = new ListNode(3);
                ListNode l21 = new ListNode(1);
                l21.next = l22;
                l22.next = l23;
                
                Solution calc = new Solution();

                ListNode lnew = calc.mergeTwoLists(l11, l21);

//              print(l11);
//              print(l21);
                print(lnew);
                
        }
        
        static void print(ListNode lin) {
                while(lin != null) {
                        System.out.print(String.valueOf(lin.val) + " -> ");
                        lin = lin.next;
                }
                System.out.println();
        }
}
