Leetcode :

200. Number of Islands : on every instance of 1, perform DFS and set all the conected ones to 0.
118. Pascal's Triangle : Every arr[i][j] = arr[i-1][j] + arr[i-1][j-1]. Handle corner cases
217. Contains Duplicate : Create a set and check if element already exists.
206. Reverse Linked List : Use prev and next as extra variables. while h: [n=h.n; h.n=p; p=h; h=n]
167. Two Sum II - Input array is sorted : Use two pointer approach. Initiate one at beginning and one at the end.
234. Palindrome Linked List : Use fast & slow pointers. Take fast pointer to end, slow pointer will be in the middle. Reverse ll ahead of slow pointer and initiate fast pointer to head. Compare.
590. N-ary Tree Postorder Traversal : Implement a stack. Keep inserting children in stack and root.val in output arr. return arr[::-1]
783. Minimum Distance Between BST Nodes : Inorder traversal. Constant space. Inorder gives sorted values in BST.
442. Find All Duplicates in an Array : Go the index and set the number -ve of itself. Whenever you see an already -ve number, it is repeated.
94. Binary Tree Inorder Traversal : Nested while loops. Use a stack and curr node. Push all left nodes in stack iteratively. When curr is null, start popping and push right in stack.
589. N-ary Tree Preorder Traversal : Use stack. Keep adding current values to result list and reverse of children to stack
617. Merge Two Binary Trees : If not t1, return t2. If not t2, return t1. Add roots. root.left = merge(t1.left, t2.left). Same for right side.
226. Invert Binary Tree : left = mirror(tree.right), right = mirror(tree.left); tree.left = right, tree.right = left
9. Palindrome Number : Create a number with reversed digits. Compare the two numbers.
1021. Remove Outermost Parentheses : Maintain a counter. '(' -> +1, ')' -> -1. Whenever counter is 0, remove first and last parentheses. Call recursively.
104. Maximum Depth of Binary Tree : max(Depth of left sub-tree, depth of right sub-tree) + 1
101. Symmetric Tree : isMirror(root, root). Call recursively isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left) and t1.val==t2.val. 
112. Path Sum : Simple recursive solution by DFS. call dfs with current sum. It will keep calling itself with left and right nodes.
112. Path Sum : Create two stacks, one for nodes and one for target_sum. Keep popping from the stack and adding the left and right children in the stack.
709. To Lower Case : str.lower()
328. Odd Even Linked List : Take two pointers, even and odd. Keep moving them like (even.next = odd.next, odd.next = even.next). Merge two lists in the end
463. Island Perimeter : For each 1, count the number of surrounding 0's.
136. Single Number : Start with 0. Take xor of all the numbers. ((0 xor a) xor a) = 0 | (((0 xor a) xor b) xor a) = b
322. Coin Change : dp = ['Inf'] *(amount+1);dp[0]=0;iterate over the table and iterate over all possible coins(nested). dp[amt] = min(dp[amt], dp[amt - coin] + 1)
278. First Bad Version : Perform binary serach; l = m+1, r=m; return l
844. Backspace String Compare : Use S_skip and T_skip pointers to remember the skips. Within each while loop, perform the skips in S and T and then compare the character.
141. Linked List Cycle : Use slow pointer and fast pointer; if they coincide, return True, if they get to None, return False.
344. Reverse String : Use two pointers, one at beginning, one at end
125. Valid Palindrome : Use two pointers, one at beginning, one at end. Run 2 while loops inside a one while loop to skip all non alphanumeric charectes
876. Middle of the Linked List : Use slow pointer, fast pointer approach
657. Robot Return to Origin : Maintin the distance from origin on x axis and y axis.
841. Keys and Rooms : Do BFS on input. Maintin a set of (enqued + visited) rooms. Do not enque a room if it's there in the visited set.
977. Squares of a Sorted Array : Find the point where -ve +ve transition takes place. From that point, use two pointers i,j. if abs(i)<abs(j); res.append(i**2); i-=1
-------------------------------------------------------REVISION 2---------------------------------------------------------------------------------
11. Container With Most Water : Two pointers, start and end. If start is smaller, start++, else end--. Calculate capacity at each step, return max.
16. 3Sum Closest : Sort the array. Start one pointer at beginning, do two sum approach on the remaining array using two more pointers. Return minumim distance result
515. Find Largest Value in Each Tree Row : Maintain two lists, one Q and C(for it's children). When Q is empty, take the max of children and make Q=C and C=[].
287. Find the Duplicate Number : Same as finding start point of cycle in a linkedlist. Use fp, sp. They will intersect at one point. Start another pointer at beginning and let it intersect sp.
846. Hand of Straights : Create a counter of cards. Sort the keys. For each card, next W cards should have a count greater than it's count. Subtract curr count from next W cards.
24. Swap Nodes in Pairs : Take curr.next and curr.next.next nodes, swap them and chage pointers, jump two steps from current.
-------------------------------------------------------REVISION 1---------------------------------------------------------------------------------
814. Binary Tree Pruning : 
25. Reverse Nodes in k-Group : Keep reversing k chunks of linked list. Maintin the tail of previos chunk to point to the next reversed chunk's head.
513. Find Bottom Left Tree Value : 2 ways to solve. Either do BFS/DFS traversal by going root, right, left. Or do recursive call and find deepest elem of left tree and right tree.
86. Partition List : Initiate two lists for before and after, initiate them with ListNode(-1). Keep adding nodes to these lists. In the end, before.next = after_head.next; return before_head.next
1143. Longest Common Subsequence : Create a 2D table of dim (m+1, n+1). If x[i]==y[j] => LCS(i, j)=LCS(i-1, j-1) + 1; Else LCS(i, j) = max(LCS(i-1, j), LCS(i, j-1)); return LCS[-1][-1]
53. Maximum Subarray : Create dp table of len(arr)+1. Initialize it to -inf. dp[i+1] = max(dp[i] + arr[i], arr[i]); return max(dp)
965. Univalued Binary Tree : Recursively check if left subtree and right subtee are univals
979. Distribute Coins in Binary Tree : Take abs value of current node and add ot to an on going sum and sibtract 1 from that sum at the very end	
746. Min Cost Climbing Stairs : For each step, cost[i] += min(cost[i-1], cost[i-2]); return cost[-1]
392. Is Subsequence : Use two pointers i,j. Increment both if same char else j+=1. If i reaches the end, return True.
303. Range Sum Query - Immutable : Pre-calculate all the prefix sums. Return the difference of prefix sums nums[j] - nums[i-1]
897. Increasing Order Search Tree : Do in-order traversal and store elements. Make a tree from the stored elements.
733. Flood Fill : Recursively perform DFS. Store startColor, update the pixel and compare it's neighbors with the start color.
938. Range Sum of BST : check if root lies in the range, if True : recursively call left and right; add node.val, else : call left or right 
958. Check Completeness of a Binary Tree : Do BFS. When you reach a null node, check if the Q is empty. If yes: return True else return False
662. Maximum Width of Binary Tree : Do BFS. Store info of (node, pos_from_left, depth). Whenever depth changes, store it as leftmost pos. Find max pos_from_left - pos.
994. Rotting Oranges : Store all the rotten oranges in a Q. Perform BFS from multiple roots in the Q. Keep adding new rotten cells in Q. Check for fresh cell in the end.
114. Flatten Binary Tree to Linked List : Recursively call func on left_sub and right_sub. Attach flattened left_sub on right side, traverse it and then attach the flattened right_sub.
443. String Compression : Iterate over the enitre array. Insert counts only if != 1. Pop repeated occurances of characters.
48. Rotate Image : Repear n/2 iterations. Replace 4 points in one go.
1252. Cells with Odd Values in a Matrix : Create two lists of zeros; rows and cols. Keep incrementing count in the lists. Increment total_odd by r+c%2==1
73. Set Matrix Zeroes : Check if 0th row and col contains 0. Iterate over indices and store zeros in (i,0) and (0,j). Propagate zeros from row0 and col0; start iteration from index 1.
796. Rotate String : s1 and s2 can be represented as xy and yx. Both x and y are contained in xyxy. | return bool(B in A+A and len(A)==len(B))
83. Remove Duplicates from Sorted List : recurse on the linked list while ptr.next. store curr val. if next.val==curr, remove next; else val = next.val
19. Remove Nth Node From End of List : Place two pointers n nodes apart in the linked list. As ptr1 reaches the end, ptr2 will be on the nth node from end.
237. Delete Node in a Linked List : Update the node value to its next element's value. node.next = node.next.next 
203. Remove Linked List Elements : Initiate temp = ListNode(-1). temp.next = head; iterate over the list and keep removing matching elements as you go. 
2. Add Two Numbers : Iterate over 2 LL. Maintain carry digit. Keep adding new nodes to res. In the end, check if carry is set.
445. Add Two Numbers II : Find len of two linked lists. Pad shorter one with 0s. Call them recursively. When end is reached, keep adding the elements and maintain the carry bit.
160. Intersection of Two Linked Lists : Find the lengths of the two ll. Move the head of larger ll by l1-l2 steps. Then move both heads and compare at step.
155. Min Stack : Use additional stack to store the min-so-far elements. When popping, check if the popped element is the min so far. If yes, pop.
202. Happy number : Use fast pointer slow pointer approach to detect a cycle. If cycle found, return False, if 1 reached, return True.
283. Move Zeroes : Use fast pointer, slow pointer approach. Move slow pointer if arr[slow] != 0. Move fast always, When arr[slow]==0, swap slow fast values.
122. Best Time to Buy and Sell Stock II : Iterate on array from 1 to n. Wherever, arr[i] > arr[i-1], add it to profit.