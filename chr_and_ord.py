def rotate_word(str, step):
    ans = ''
    for i in range(len(str)):
        ans += chr(ord(str[i]) + step)
    return ans

p = "пайтон"
print(rotate_word(p, 7))