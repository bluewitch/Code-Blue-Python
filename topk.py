# Top K Frequent Words
# Challange

"""
I threw myself at this one, not really any time to "study"
 the solution was stupid simple in hind sight.  It took only 5 lines of code to solve this riddle.

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

Code Break Down

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

When I found this snippet, it was basically the whole solution.

But there are two ways of doing this, through sorting and through        
"""
Approach #1: Sorting [Accepted]
Intuition and Algorithm



Python

# Sorting
# Count the frequency of each word, and sort the words with a custom 
# ordering relation that uses these frequencies. Then take the best k of # them.

    def topKFrequent(words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]


# Heaping
# Count the frequency of each word, then add it to heap that stores the
# best k candidates. Here, "best" is defined with our custom ordering 
# relation, which puts the worst candidates at the top of the heap. At
# the end, we pop off the heap up to k times and reverse the result so
# that the best candidates are first.

# Pro Python Tip
# In Python, we instead use heapq.heapify, which can turn a list into a # heap in linear time, simplifying our work.

    def topKFrequent(words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
