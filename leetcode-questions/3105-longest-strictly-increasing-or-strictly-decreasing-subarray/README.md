<h2> <a href="https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray">
3105. Longest Strictly Increasing or Strictly Decreasing Subarray 
</a></h2>

<h3>Easy</h3>
<hr>
<div>
<p>
You are given an array of integers <strong>nums</strong>. Return the length of the longest subarray of nums which is either 
<em>strictly increasing </em> or <em>strictly decreasing.</em>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1, 4, 3, 3, 2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3, 2], and [4, 3].

Hence, we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3, 3, 3, 3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3, 2, 1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
    <li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>
</div>