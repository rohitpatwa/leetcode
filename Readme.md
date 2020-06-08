Leetcode :



############################################################################# LTM #############################################################################

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
844. Backspace String Compare : Iterate on reversed strings. If #, skip+=1, else skip-=1. Compare after skips. If both pointers overflow, return True, else return False.
141. Linked List Cycle : Use slow pointer and fast pointer; if they coincide, return True, if they get to None, return False.
344. Reverse String : Use two pointers, one at beginning, one at end
125. Valid Palindrome : Use two pointers, one at beginning, one at end. Run 2 while loops inside a one while loop to skip all non alphanumeric charectes
876. Middle of the Linked List : Use slow pointer, fast pointer approach
657. Robot Return to Origin : Maintin the distance from origin on x axis and y axis.
841. Keys and Rooms : Do BFS on input. Maintin a set of (enqued + visited) rooms. Do not enque a room if it's there in the visited set.
977. Squares of a Sorted Array : Find the point where -ve +ve transition takes place. From that point, use two pointers i,j. if abs(i)<abs(j); res.append(i**2); i-=1
11. Container With Most Water : Two pointers, start and end. If start is smaller, start++, else end--. Calculate capacity at each step, return max.
16. 3Sum Closest : Sort the array. Start one pointer at beginning, do two sum approach on the remaining array using two more pointers. Return minumim distance result
515. Find Largest Value in Each Tree Row : Maintain two lists, one Q and C(for it's children). When Q is empty, take the max of children and make Q=C and C=[].
287. Find the Duplicate Number : Same as finding start point of cycle in a linkedlist. Use fp, sp. They will intersect at one point. Start another pointer at beginning and let it intersect sp.
846. Hand of Straights : Create a counter of cards. Sort the keys. For each card, next W cards should have a count greater than it's count. Subtract curr count from next W cards.
24. Swap Nodes in Pairs : Take curr.next and curr.next.next nodes, swap them and chage pointers, jump two steps from current.
814. Binary Tree Pruning : Check if if the subtrees contain 1. Recursively call on left and right subtrees
1143. Longest Common Subsequence : Create a 2D table of dim (m+1, n+1). If x[i]==y[j] => LCS(i, j)=LCS(i-1, j-1) + 1; Else LCS(i, j) = max(LCS(i-1, j), LCS(i, j-1)); return LCS[-1][-1]
53. Maximum Subarray : Create dp table of len(arr)+1. Initialize it to -inf. dp[i+1] = max(dp[i] + arr[i], arr[i]); return max(dp)
965. Univalued Binary Tree : Recursively check if left subtree and right subtee are univals
513. Find Bottom Left Tree Value : 2 ways to solve. Either do BFS/DFS traversal by going root, right, left. Or do recursive call and find deepest elem of left tree and right tree.
-------------------------------------------------------REVISION 2---------------------------------------------------------------------------------
25. Reverse Nodes in k-Group : Keep reversing k chunks of linked list. Maintin the tail of previos chunk to point to the next reversed chunk's head.
86. Partition List : Initiate two lists for before and after, initiate them with ListNode(-1). Keep adding nodes to these lists. In the end, before.next = after_head.next; return before_head.next
979. Distribute Coins in Binary Tree : Take abs value of current node and add it to an on going sum and sibtract 1 from that sum at the very end	
746. Min Cost Climbing Stairs : For each step, cost[i] += min(cost[i-1], cost[i-2]); return cost[-1]
392. Is Subsequence : Use two pointers i,j. Increment both if same char else j+=1. If i reaches the end, return True.
303. Range Sum Query - Immutable : Pre-calculate all the prefix sums. Return the difference of prefix sums nums[j] - nums[i-1]
897. Increasing Order Search Tree : Do in-order traversal and store elements. Make a tree from the stored Elements.
733. Flood Fill : Recursively perform DFS. Store startColor, update the pixel and compare it's neighbors with the start color.
938. Range Sum of BST : check if root lies in the range, if True : recursively call left and right; add node.val, else : call left or right 
958. Check Completeness of a Binary Tree : Do BFS. When you reach a null node, check if the Q is empty. If yes: return True else return False
662. Maximum Width of Binary Tree : Do BFS. Store info of (node, pos_from_left, depth). Whenever depth changes, store it as leftmost pos. Find max pos_from_left - pos.
994. Rotting Oranges : Store all the rotten oranges in a Q. Perform BFS from multiple roots in the Q. Keep adding new rotten cells in Q. Check for fresh cell in the end.
114. Flatten Binary Tree to Linked List : Recursively call func on left_sub and right_sub. Attach flattened left_sub on right side, traverse it and then attach the flattened right_sub.
443. String Compression : Iterate over the enitre array. Insert counts only if != 1. Pop repeated occurances of characters.
48. Rotate Image : Repear n/2 iterations. Replace 4 points in one go.
1252. Cells with Odd Values in a Matrix : Create two lists of zeros; rows and cols. Keep incrementing count in the lists. Increment total_odd by (r+c)%2==1
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
49. Group Anagrams : Sorting each word is a linear time operation(counting sort). Sort each word and add it to a dictionary whose values are lists of words.
110. Balanced Binary Tree : Use height of left tree and right tree to check if they are balanced. At any point, if unbalanced, return -1 which avoids further computation and return False.
98. Validate Binary Search Tree : Create a helper func which takes (node, lower_bound and upper_bound). Recursively call on left and right sub tree.
1404. Number of Steps to Reduce a Number in Binary Representation to One : Look at 1 bit (b) at a time(right to left) and maintain a carry (c). (b=0,c=0->1,c=0), (b=0,c=1->2, c=1) and so on.  
543. Diameter of Binary Tree : Diameter is max(diameter_left, diameter_right, left_depth+right_depth+1). Resurse on left and right subtrees. Return diam and depth at each step.
525. Contiguous Array : Calculate sum at each index. Two points between which sum repeats itself contains equal 0s and 1s
238. Product of Array Except Self : In 2 for loops, we can compute prod of all numbers to the left and right of a given index. Multiply elements of these arrays and we get the result.
111. Minimum Depth of Binary Tree : min(minDepth(left), minDepth(right)) + 1
119. Pascal's Triangle II : Create a temp row. Keep updating the values of row in another list. Repeat this till k.
168. Excel Sheet Column Title : num = n%26 if n%26!=0 else 26; char = ord(num); n = (n-num)//26.
678. Valid Parenthesis String : Calculate leftBal and rightBal for the string. leftbal means +1 if i in "(*" else -1. rightBal = +1 if i in "*)" else -1. If any < 0; return False
64. Minimum Path Sum : DP problem. Keep storing the  minPathSum([i-1][j], [i][j-1]). We can go top down using recursion or bottom up using iterative.
572. Subtree of Another Tree : Traverse tree a and at each node check if it is equal to tree b. OR Traverse tree a and b and store in strings with delimeters. check if b in a.
33. Search in Rotated Sorted Array : Find the pivot element i using BS. l=i, r=i+n-1. Do normal bs between l and r and check arr[m%n].
146. LRU Cache : Use dict. When inserting, if already present, delete it and add it again. If cache full, delete first element of dict and add new val.
221. Maximal Square : Check if 1st row or 1st col contains any 1. If yes max_sq=1 else 0. Iterate over (1, m) and (1, n) elements. arr[i,j]=min(arr[i,j-1], arr[i-1,j-1], arr[i, j-1]) + 1.
148. Sort List : Mergesort in nlogn time.
771. Jewels and Stones : Create a counter over S. Then iterate over J adding counts from dict of S.
199. Binary Tree Right Side View : Do level order traversal. At each step, insert the last value to result array.
-------------------------------------------------------REVISION 1---------------------------------------------------------------------------------
383. Ransom Note : Create a counter on magazine str. Iterate over note str and keep subtracting from the counter. 
476. Number Complement : Find the next biggest power of 2. Return 2**power - num.
560. Subarray Sum Equals K : Keep computing the cumsum and store it's no. of occurances in a dict. For each cumsum we get a k subarray if we've seen cumsum-k; result+= d.get[cumsum-k]
402. Remove K Digits : Push nums in a stack. When a smaller number appears, keep poppig the prev num and then push the num provided k>0. Remove duplicate nums and remove leading 0s.
208. Implement Trie (Prefix Tree) : Use dictionary. Insert char as a key and it's next char as it's value. Mark end as a flag at the end of each word.
986. Interval List Intersections : If x[0]<=y[1] and x[1]>=y[0], this means intersection. if x[1]<y[1], x++ else y++.
678. Valid Parenthesis String : Iterate s once from l->r and r->l. left_bal and right_bal in s. If at any point left_bal<0 or right_bal<0; return False; else return True.




############################################################################# STM #############################################################################
700. Search in a Binary Search Tree : Can be solved in both recursive and iterative ways. Iterate with BST nodes and return root where the value matches. Write the base case.
852. Peak Index in a Mountain Array : Do binary search until you find the mid point.
