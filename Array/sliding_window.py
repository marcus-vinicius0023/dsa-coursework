
def maximumLenghtSubstring(s: str, max_lenght: int) -> int:
    if s == None or s == "": return 0

    left, right = 0, 0
    max_ = 1
    counter = {}

    counter[s[right]] = 1

    while right < len(s) - 1:
        right += 1
        if counter.get(s[right]):
            counter[s[right]] += 1
        else:
            counter[s[right]] = 1
        
        while counter[s[right]] == max_lenght:
            counter[s[left]] -= 1
            left += 1
        
        max_ = max(max_, right - left + 1)
    
    return max_


