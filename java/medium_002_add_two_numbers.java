/**
 * @Author:	wjsaya(http://www.wjsaya.top) 
 * @Date:	2018-10-20 16:10:09
 * @Last Modified by: wjsaya(http://www.wjsaya.top)
 * @Last Modified time: 2018-10-22 19:24:13
 */ 
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x; 
    }

    ListNode(int x, ListNode nxt) {
        val = x; 
        next = nxt;
    }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode lrHead = new ListNode(0);
        ListNode lrTemp = lrHead;
        /*
            输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
            输出：7 -> 0 -> 8
            原因：342 + 465 = 807
        */
        // l1,l2均非空，取出首节点，相加直接存入新链，同时向下移动游标
        while(l1 != null && l2 != null) {
            ListNode newNode = new ListNode(l1.val + l2.val);
            lrTemp.next = newNode;
            lrTemp = lrTemp.next;
            l1 = l1.next;
            l2 = l2.next;
        }

        //l1,l2任一非空，将其全部追加到新链表
        if(l1 != null)
            lrTemp.next = l1;
            
        if(l2 != null)
            lrTemp.next = l2;
        
        lrHead = lrHead.next;
        lrTemp = lrHead;

        //新链表建立完毕，开始整理
        while(lrTemp != null) {
            //遍历新链
            if(lrTemp.val > 9) {//如果值大于9，那么需要进位，取余放到当前，取整放到下一个上。
                if (lrTemp.next != null)    //有下一个节点
                    lrTemp.next.val = lrTemp.next.val + (lrTemp.val / 10);
                else {                      //无下一个节点
                    ListNode newNode = new ListNode(lrTemp.val / 10);
                    lrTemp.next = newNode;
                }
                lrTemp.val = lrTemp.val % 10;   // temp % 10 当前
            }
            lrTemp = lrTemp.next;
        }
        return lrHead;
    }
}

public class medium_002_add_two_numbers {
    public static void main(String[] args) {
        /*
        ListNode ln13 = new ListNode(3);
        ListNode ln12 = new ListNode(4, ln13);
        ListNode ln11 = new ListNode(2, ln12);
        ListNode ln23 = new ListNode(4);
        ListNode ln22 = new ListNode(6, ln23);
        ListNode ln21 = new ListNode(5, ln22);
        */

        ListNode ln12 = new ListNode(8);
        ListNode ln11 = new ListNode(1, ln12);
        
        ListNode ln21 = new ListNode(0);

        Solution now = new Solution();
        print(now.addTwoNumbers(ln11, ln21));

    }
    public static void print(ListNode lnin) {
        while(lnin != null) {
            System.out.print(lnin.val + " -> ");
            lnin = lnin.next;
        }
    }
}