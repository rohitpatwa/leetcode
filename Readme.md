Leetcode :



#################################### LTM #########################################

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
322. Coin Change : dp = ['inf'] *(amount+1);dp[0]=0;iterate over the table and iterate over all possible coins(nested). dp[amt] = min(dp[amt], dp[amt - coin] + 1)
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
25. Reverse Nodes in k-Group : Keep reversing k chunks of linked list. Maintin the tail of previos chunk to point to the next reversed chunk's head.
86. Partition List : Initiate two lists for before and after, initiate them with ListNode(-1). Keep adding nodes to these lists. In the end, before.next = after_head.next; return before_head.next
979. Distribute Coins in Binary Tree : Take abs value of current node and add it to an on going sum and sibtract 1 from that sum at the very end	
746. Min Cost Climbing Stairs : For each step, cost[i] += min(cost[i-1], cost[i-2]); return cost[-1]
392. Is Subsequence : Use two pointers i,j. Increment both if same char else j+=1. If i reaches the end, return True.
303. Range Sum Query - Immutable : Pre-calculate all the prefix sums. Return the difference of prefix sums nums[j] - nums[i-1]
929. Unique Email Addresses : Split the emails at @. Apply rules through regex and add the resultant email in a set.
48. Rotate Image : Repear n/2 iterations. Replace 4 points in one go.
2. Add Two Numbers : Iterate over 2 LL. Maintain carry digit. Keep adding new nodes to res. In the end, check if carry is set.
19. Remove Nth Node From End of List : Place two pointers n nodes apart in the linked list. As ptr1 reaches the end, ptr2 will be on the nth node from end.
933. Number of Recent Calls : Use a Q to keep recent timestamps. Whenever ping is called, remove all the expired ones and add t to Q. Return len(Q) 
-------------------------- REVISION 2 -----------------------------
897. Increasing Order Search Tree : Do in-order traversal and store elements. Make a tree from the stored Elements.
733. Flood Fill : Recursively perform DFS. Store startColor, update the pixel and compare it's neighbors with the start color.
938. Range Sum of BST : check if root lies in the range, if True : recursively call left and right; add node.val, else : call left or right 
958. Check Completeness of a Binary Tree : Do BFS. When you reach a null node, check if the Q is empty. If yes: return True else return False
662. Maximum Width of Binary Tree : Do BFS. Store info of (node, pos_from_left, depth). Whenever depth changes, store it as leftmost pos. Find max pos_from_left - pos.
994. Rotting Oranges : Store all the rotten oranges in a Q. Perform BFS from multiple roots in the Q. Keep adding new rotten cells in Q. Check for fresh cell in the end.
114. Flatten Binary Tree to Linked List : Recursively call func on left_sub and right_sub. Attach flattened left_sub on right side, traverse it and then attach the flattened right_sub.
443. String Compression : Iterate over the enitre array. Insert counts only if != 1. Pop repeated occurances of characters.
1252. Cells with Odd Values in a Matrix : Create two lists of zeros; rows and cols. Keep incrementing count in the lists. Increment total_odd by (r+c)%2==1
73. Set Matrix Zeroes : Check if 0th row and col contains 0. Iterate over indices and store zeros in (i,0) and (0,j). Propagate zeros from row0 and col0; start iteration from index 1.
796. Rotate String : s1 and s2 can be represented as xy and yx. Both x and y are contained in xyxy. | return bool(B in A+A and len(A)==len(B))
83. Remove Duplicates from Sorted List : recurse on the linked list while ptr.next. store curr val. if next.val==curr, remove next; else val = next.val
237. Delete Node in a Linked List : Update the node value to its next element's value. node.next = node.next.next 
203. Remove Linked List Elements : Initiate temp = ListNode(-1). temp.next = head; iterate over the list and keep removing matching elements as you go. 
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
986. Interval List Intersections : If x[0]<=y[1] and x[1]>=y[0], this means intersection. if x[1]<y[1], x++ else y++.
209. Minimum Size Subarray Sum : Two pointer problem (i, j). Maintain a running sum and a left index (i). While running sum>target, sum-=arr[i] and i++; else sum+=arr[j], j++
383. Ransom Note : Create a counter on magazine str. Iterate over note str and keep subtracting from the counter. 
476. Number Complement : Find the next biggest power of 2. Return 2**power - num.
560. Subarray Sum Equals K : Keep computing the cumsum and store it's no. of occurances in a dict. For each cumsum we get a k subarray if we've seen cumsum-k; result+= d.get[cumsum-k]
402. Remove K Digits : Push nums in a stack. When a smaller number appears, keep poppig the prev num and then push the num provided k>0. Remove duplicate nums and remove leading 0s.
208. Implement Trie (Prefix Tree) : Use dictionary. Insert char as a key and it's next char as it's value. Mark end as a flag at the end of each word.
678. Valid Parenthesis String : Iterate s once from l->r and r->l. left_bal and right_bal in s. If at any point left_bal<0 or right_bal<0; return False; else return True.
700. Search in a Binary Search Tree : Can be solved in both recursive and iterative ways. Iterate with BST nodes and return root where the value matches. Write the base case.
852. Peak Index in a Mountain Array : Do binary search until you find the mid point.
404. Sum of Left Leaves : Recursive soln. If left child is a leaf, return left.val + recv_func(right child); else return recv_func(left) + recv_func(right).
79. Word Search : Scan through each word in grid. Where 1st char matches, perform dfs on it's neighbors. Replace a visited word by -1 to avoid visiting it again. Backtrack if needed.
905. Sort Array By Parity : Two pointer approach. One at the start, other at the end. Swap odd and even nums.
917. Reverse Only Letters : Use two pointer approach - i at the start, j at the end. Swap the chars at i and j while i<j.
54. Spiral Matrix : Maintain the direction while traversing. Keep track of top, right, bottom and left limits of the matrix. Iterate til l<=r and t<=b.
59. Spiral Matrix II : Create a res array of n*n size. Iterate it in a spiral order and keep inserting a ctr++ at each step.
804. Unique Morse Code Words : Create a set and add all the codes in it. Return length.
91. Decode Ways : dp=[]*len(n+1). dp[i] means no. of ways to decode string of len i. Get single and double from s. single>0: dp[i]+=dp[i-1]; 10<=double<=26: dp[i]+=dp[i-2].
728. Self Dividing Numbers : Solution is brute force. Go through each number and check if it is self dividing.
561. Array Partition I : Sort the array and add all the even elements to the min_sum. That will be the result.
1002. Find Common Characters : Use global_freq and local_freq to keep a count of repeating chars.
985. Sum of Even Numbers After Queries : Keep a running sum. At each query, subtract the initial term if even and add the new term if even. Append sum in results.
922. Sort Array By Parity II : Two pointer approach. Initiate i, j = 0, 1. Keep i on even terms, j on odd. Increment by 2 if correct, else swap.
867. Transpose Matrix : Create new matrix of transpose dim. B[j][i] = A[i][j].
121. Best Time to Buy and Sell Stock : Iterate through the array and maintain the min_so_far value. at each step profit = max(profit, arr[i]-min_so_far)
680. Valid Palindrome II : Use 2 pointers initially. When diff chars seen at i and j, call checkPslindrome with both cases i.e. skip ith, skip jth. If either satisfies, return True.
74. Search a 2D Matrix : Perform a normal binary search. Do division and modulus when accessing the elements of the matrix 
1. Two Sum : Linear solution. Create a dict of all elements. Then iterate through the array, for each element check if it's compliment is in d.
695. Max Area of Island : Visit every loc in grid. If loc==1, set it to zero and perform BFS by setting it's neighbors 0.
1047. Remove All Adjacent Duplicates In String : Use stack. If next char c == S[-1], S.pop(); else S.append(c)
1160. Find Words That Can Be Formed by Characters : Use dict for keeping global frequency and local frequency of chars.
485. Max Consecutive Ones : Keep a count of global max and local max. 
412. Fizz Buzz : Loop from 1 to n+1. if i%3==0, s += "Fizz", if i%5==0, s += "Buzz".
482. License Key Formatting : Remove all the -. Start from the end and keep adding each elem to new string. After every k chars, add -. Return res.strip('-')
904. Fruit Into Baskets : 3 variables to store info of last_fr, 2nd_last_fr and last_fr_count. If x==last_fr, local_max+=1, if x==2nd_last, swap the two and last_fr_count=1.
55. Jump Game : Keep calculating max reachable index from current index. If curr index passes max reachable index, return False.
15. 3Sum : Sort thr array. Move one pointer from start to end and keep performing 2 sum on remaining array. O(n^2)
21. Merge Two Sorted Lists : Itera two linked lists with two pointers and keep adding the smaller value to the res list.
207. Course Schedule : Create list of inDegree(iD) of edges and DAG. Add nodes with iD==0 to Stack(S). Pop S, decrease inDegree of dependents by 1. If iD==0, push to S.
210. Course Schedule II : Same as Course Schedule problem. Create a res list to store resut. When popping from Stack, add to res.
18. 4Sum : Stupid extention of 3sum problem. n^3 solution. Two pointer approach inside double for loop.
152. Maximum Product Subarray : At each element, keep track of min and max because in products, min can become max if multiplied by -ve no. 
212. Word Search II : Add the list of words in a trie. At end of every word, store 'end'=True and 'word'=<actual word>. Then iterate the board and keep checking in trie by DFS. 
-------------------------- REVISION 1 -----------------------------
1261. Find Elements in a Contaminated Binary Tree : BFS on BT starting from root. Every child is given value as per formula. Add values to a set. Search target in set.
739. Daily Temperatures : Push (temp, idx) in a stack. Pop element when a bigger elem is seen and update arr[idx] with (new_idx-idx).
347. Top K Frequent Elements : Linear solution. Create an array of arr to hold all i freq elements at ith sub-arr. Flatten and return last k elements.
1072. Flip Columns For Maximum Number of Equal Rows : Create a dict of patterns. Add tuple(row) and tuple(row_compliment) to dict. Return max(dict.vals()).
609. Find Duplicate File in System : Split paths and files. The split files. The split filename and content. Add content to dict and full path as value in a list. 
198. House Robber : We create an arr dp which hold max val till that point. At each i, max_val = max(dp[i-2] + nums[i], dp[i-1])
70. Climbing Stairs : At each step, number of ways to climb is equal to (dp[i-1] + dp[i-2]). We can take 1 step from i-1 and 2 steps from i-2.
78. Subsets : Simulate picking and not picking every element within a heler function. Pick next value, recurse, backtrack. Add every combi to res.
46. Permutations : Pop first char and send the remaining array to a magic funciton which returns all perms. Place popped char at all positions in each perm.
46. Permutations : Simulate swapping branches of a tree. Call helper with l pointer. for i in range(l, n), swap i, l. Recurse with l+1, backtrack 
22. Generate Parentheses : Open parenthesen < n and closed parantheses < open. Keep recursing and backtrackting to generate all combinations.
62. Unique Paths : 2 ways to solve [dp, maths]. dp[i][j] = dp[i-1][j] + dp[i][j-1].
213. House Robber II : Same as House Robber problem. This time we find max loot from [0:n-1] and [1:n] separately and return max of these.
300. Longest Increasing Subsequence : DP problem, O(n^2). Initiate lis=[1]*n. If A[i]>A[j] and lis[j]>=lis[i]: lis[i] = lis[j] + 1.
5. Longest Palindromic Substring : Iterate through the array, at each step expand from middle and find longest palindrome. Cover odd and even cases of plaindromes.
139. Word Break : Create a list named dp. dp[i] means if or not we can reach char i using wordDict. Run 2 pointers on s. If dp[j] and s[j:i] in wordDict: dp[i]=True.
647. Palindromic Substrings : Iterate over the str and in each itr call expand(i, i) and expand(i, i+1). In expand func, expand on right and left and count palindromes.
520. Detect Capital : Check if word is all upper or all lower. elif check if word is one capital and all lower. Else return False.
417. Pacific Atlantic Water Flow : Create 2 sets P and A for nodes covered by both seas. Perform dfs from all rows and cols of P and A. Return intersecrion of P and A.
1496. Path Crossing : Assign +1 -1 values to "NSEW". Use cartesian coordinates and store values in a set. If value repeated, return True.
378. Kth Smallest Element in a Sorted Matrix : Create a max heap of size k. At every element smaller than top of heap, replace it with top. At the end, return top.
56. Merge Intervals : Sort intervals. Add first int(erval) to res. Iterate on remaining and check if curr[0] <= res[-1][1]
162. Find Peak Element : Call helper with (nums, l, r). if nums[m] < nums[m+1]: l = m+1; else: r = m-1.
342. Power of Four : Binary representation should be of the form 1000... and of odd length.
77. Combinations : Same as subsets problem. Just put a constraint to add subsets of len 2 and return after adding because we don't want to explore subsets of len > 2.
567. Permutation in String : l = len(s1). Slide over a window of size l on s2 and keep creating counters. If ctr_s1==ctr_s2: return true.
424. Longest Repeating Character Replacement : Sliding window problem. Keep increasing end. max_count=max char inside window. If (end-start+1 - max_count > k): start += 1.
215. Kth Largest Element in an Array : Create a min heap of size k. While inserting elements, if num > heap.top, heap.pop, insert num. Else pass. Return heap.top.
767. Reorganize String : Create list of len(S). Create Counter. Iterate from most freq to least. keep inserting in alternate idx(0,2,4 ...). when i>=len(S): i=1.
621. Task Scheduler : ctr=nums except the 1st one which have max_count. total_idle_slots = (max_count-1)*n; res = max_count+ctr+total_idle_slots; return max(res,len(tasks)).
100. Same Tree : Compare values of current nodes and recursively call left sub tree and right sub tree. Write proper break condition.
253. Meeting Rooms II : Sort the intervals on start time. Use a min heap. Push end times in min heap. While start < end, heap.pop(). res = max(res, len(heap)) at any point.
268. Missing Number : (n*n+1)/2 - sum(nums) 
295. Find Median from Data Stream : Use minheap and maxheap. Pushpop every new elem in maxheap, add popped elem in min heap. If len(minheap)>len(maxheap), re-balance.
763. Partition Labels : Use dict to store last occ of every char. Then iterate over S and create a sliding window from start of current char till last occ of that char.
7. Reverse Integer : Store sign of x. Convert x in str, reverse str, convert str back to int, multiply it with it's sign. Remember to take mods at the end.
3. Longest Substring Without Repeating Characters : 2 pointer soluion(l, r). Keep latest occ of every char in dict. If curr char in dict, l = d[c] + 1. Update max at each step.
124. Binary Tree Maximum Path Sum : Create a helper function get_sum which will get max sum till that node. Update res in get_sum with get_sum(left) + get_sum(right) + node.val.
127. Word Ladder : Perform bi-directional BFS from start word and end word. Keep track of visited nodes from start and end separately. As you get intersection, return sum of len. 
23. Merge k Sorted Lists : Use min heap of size k. Add 1 elem from each list in format (val, i++, next_ptr). i is added to allow heap sorting. Pop from heap and add from same list.
857. Minimum Cost to Hire K Workers : Sort on (wage/quality). Create a max heap on quality of size k. Iterate on sorted w_q list, ans = sum(qualities)*current_ratio. Keep updating.
222. Count Complete Tree Nodes : Find len of tree by going max left. Do binary search (similar to finding first bad version/last good version) to find num of nodes in last level.
1594. Maximum Non Negative Product in a Matrix : At each elem in dp grid store min and max prod till that elem. Take min and max of leftmin, leftmax, topmin, topmax.
310. Minimum Height Trees : Create an adjacency list. Find all the leaves. Trim leaves, remove connections and update new leaves till you reach center. 
17. Letter Combinations of a Phone Number : Perform DFS. Create a number to char mapping. Call a helper function on each digit and iterate through it's chars recursively.
1593. Split a String Into the Max Number of Unique Substrings : Iterate s and create cand. Add cand to seen set. Recursively call helper. max = max(max, helper() + 1) and backtrack.
702. Search in a Sorted Array of Unknown Size : Start with r=1. Keep doubling r until reader(r) > target. Perform Binary Search between r/2 and r.
116. Populating Next Right Pointers in Each Node : This solution is in O(n) space. Do level order traversal and create links within the level.
117. Populating Next Right Pointers in Each Node II : This is O(1) space. Create parent, child and child_head nodes. Move parent node horizontally and create links in child nodes.


#################################### STM ######################################### 

40. Combination Sum II : Similar to finding subsets problem. Here find subsets whose sum is equal to target. Sort candidates and skip repeat numbers.
235. Lowest Common Ancestor of a Binary Search Tree
236. Lowest Common Ancestor of a Binary Tree
937. Reorder Data in Log Files
654. Maximum Binary Tree
259. 3Sum Smaller
713. Subarray Product Less Than K
686. Repeated String Match
346. Moving Average from Data Stream
734. Sentence Similarity
299. Bulls and Cows
246. Strobogrammatic Number
359. Logger Rate Limiter
26. Remove Duplicates from Sorted Array
189. Rotate Array
8. String to Integer (atoi)
12. Integer to Roman
165. Compare Version Numbers
273. Integer to English Words
387. First Unique Character in a String
20. Valid Parentheses
42. Trapping Rain Water
138. Copy List with Random Pointer
103. Binary Tree Zigzag Level Order Traversal
348. Design Tic-Tac-Toe
957. Prison Cells After N Days
1592. Rearrange Spaces Between Words
66. Plus One
76. Minimum Window Substring
159. Longest Substring with At Most Two Distinct Characters
163. Missing Ranges
809. Expressive Words
833. Find And Replace in String
31. Next Permutationf`
1512. Number of Good Pairs
1598. Crawler Log Folder
1599. Maximum Profit of Operating a Centennial Wheel
1600. Throne Inheritance
1504. Count Submatrices With All Ones
61. Rotate List
329. Longest Increasing Path in a Matrix
170. Two Sum III - Data structure design
394. Decode String
1614. Maximum Nesting Depth of the Parentheses
1615. Maximal Network Rank
1616. Split Two Strings to Make Palindrome
859. Buddy Strings
399. Evaluate Division
947. Most Stones Removed with Same Row or Column
951. Flip Equivalent Binary Trees
247. Strobogrammatic Number II
123. Best Time to Buy and Sell Stock III
188. Best Time to Buy and Sell Stock IV
1007. Minimum Domino Rotations For Equal Row
349. Intersection of Two Arrays
547. Friend Circles
735. Asteroid Collision
39. Combination Sum
456. 132 Pattern : Create aux array storing the min_left[i]=min(nums[:i]). Iterate on nums from end and store elements in Stack. In each iteration while S[-1] <= min_left[j]: S.pop().






975. Odd Even Jump
1588. Sum of All Odd Length Subarrays