MAX_CHARS = 256

def patternsearch(text, pat):
    m, n = len(pat), len(text)
    badchar = [-1] * MAX_CHARS
    for i, ch in enumerate(pat):
        badchar[ord(ch)] = i
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == text[s + j]:
            j -= 1
        if j < 0:
            print("Pattern occurs at position =", s)
            s += m - badchar[ord(text[s + m])] if s + m < n else 1
        else:
            s += max(1, j - badchar[ord(text[s + j])])

text = input("Enter the text: ").rstrip()
pat = input("Enter the pattern: ").rstrip()
patternsearch(text, pat)
