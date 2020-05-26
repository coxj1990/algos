def search(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        found = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                found = False
                break
        if found:
            return True
    return False
