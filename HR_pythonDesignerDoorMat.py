n, m = map(int,input().split())
# List Comprehension for pattern
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]

# List Comprehension for print out
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
