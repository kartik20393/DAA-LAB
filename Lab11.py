def computeLPSArray(pat):
    lps, length = [0] * len(pat), 0
    for i in range(1, len(pat)):
        while length > 0 and pat[i] != pat[length]:
            length = lps[length - 1]
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
    return lps

def KMPSearch(pat, txt):
    lps = computeLPSArray(pat)
    j = 0
    for i in range(len(txt)):
        while j > 0 and txt[i] != pat[j]:
            j = lps[j - 1]
        if txt[i] == pat[j]:
            j += 1
            if j == len(pat):
                print(f"Found pattern at index {i - j + 1}")
                j = lps[j - 1]

txt = input("Enter the text: ")
pat = input("Enter the pattern: ")
KMPSearch(pat, txt)
