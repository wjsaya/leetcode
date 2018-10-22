/**
 * @Author:	wjsaya(http://www.wjsaya.top) 
 * @Date:	2018-10-22 11:05:49 
 * @Last Modified by: wjsaya(http://www.wjsaya.top)
 * @Last Modified time: 2018-10-22 11:43:38
 * @problem URL: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
 * 给定一个链表: 1->2->3->4->5, 和 n = 2.
 * 当删除了倒数第二个节点后，链表变为 1->2->3->5. 
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
   public ListNode removeNthFromEnd(ListNode head, int n) {
       ListNode lnNew = new ListNode(0);
       lnNew.next = head;   //加一个空头节点，把头结点删除一般化
       ListNode lnNow = head;   //原头节点

       int count = 0;
       while(lnNow != null) {//遍历求长度
           count += 1;
           lnNow = lnNow.next;
       }
       
       count -= n;      //长度-n，获取移除节点前的长度

       lnNow = lnNew;   //从新链表删除数据
       while(count > 0) {//count一直递减，直至为0,此时lnNow为待删除节点前一个
           count--;
           lnNow = lnNow.next;
        }
        lnNow.next = lnNow.next.next;   //删除待删除节点
        
        return lnNew.next;  //返回lnNew的下一个，即原来的head
    }
}

public class medium_019_remove_nth_node_from_end_of_list {
    public static void main(String[] args) {
        
        ListNode ln12 = new ListNode(2);
        ListNode ln11 = new ListNode(1, ln12);
        
        int n = 2;

        print(ln11);
        System.out.println();
        Solution test = new Solution();
        print(test.removeNthFromEnd(ln11, n));
    }
    private static void print(ListNode lnin) {
        while(lnin != null) {
            System.out.print(lnin.val + " -> ");
            lnin = lnin.next;
        }
    }
}