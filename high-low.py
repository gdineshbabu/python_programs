
n = int(input())
for i in range(n):
    sentence = input().strip()
    ascii_vals = [ord(c) for c in sentence if c != ' ']
    diff = max(ascii_vals) - min(ascii_vals)
    print(diff)
