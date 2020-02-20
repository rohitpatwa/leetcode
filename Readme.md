Leetcode :

200. Number of Islands : on every instance of 1, perform DFS and set all the conected ones to 0.
118. Pascal's Triangle : Every arr[i][j] = arr[i-1][j] + arr[i-1][j-1]. Handle corner cases
217. Contains Duplicate : Create a set and check if element already exists.
206. Reverse Linked List : Use prev and next as extra variables. while h: [n=h.n; h.n=p; p=h; h=n]
167. Two Sum II - Input array is sorted : Use two pointer approach. Initiate one at beginning and one at the end.
234. Palindrome Linked List : Use fast & slow pointers. Take fast pointer to end, slow pointer will be in the middle. Reverse ll ahead of slow pointer and initiate fast pointer to head. Compare.
590. N-ary Tree Postorder Traversal : Implement a stack. Keep inserting children in stack and root.val in output arr. return arr[::-1]
783. Minimum Distance Between BST Nodes : Inorder traversal. Constant space.
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
841. Keys and Rooms : Do BFS on input. Maintin a set of (enqued + visited) rooms. Do not enque a room if it's there in the set.
977. Squares of a Sorted Array : Find the point where -ve +ve transition takes place. From that point, use two pointers i,j. if abs(i)<abs(j); res.append(i**2); i-=1
-------------------------------------------------------REVISION 1---------------------------------------------------------------------------------
11. Container With Most Water : Two pointers, start and end. If start is smaller, start++, else end--. Calculate capacity at each step, return max.
16. 3Sum Closest : Sort the array. Start one pointer at beginning, do two sum approach on the remaining array using two more pointers. Return minumim distance result
515. Find Largest Value in Each Tree Row : Maintain two lists, one Q and C(for it's children). When Q is empty, take the max of children and make Q=C and C=[].
287. Find the Duplicate Number : Same as finding start point of cycle in a linkedlist. Use fp, sp. They will intersect at one point. Start another pointer at beginning and let it intersect sp.
814. Binary Tree Pruning : 
846. Hand of Straights : Create a counter of cards. Sort the keys. For each card, next W cards should have a count greater than it's count. Subtract curr count from next W cards.
24. Swap Nodes in Pairs : Take curr.next and curr.next.next nodes, swap them and chage pointers, jump two steps from current.
25. Reverse Nodes in k-Group : Keep reversing k chunks of linked list. Maintin the tail of previos chunk to point to the next reversed chunk's head.