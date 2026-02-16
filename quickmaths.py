n1 = int(input()); s1 = int(input()[-7:]); n2 = int(input()); s2 = int(input()[-7:])
x = (s1 * s2)
ans = []
while x > 0:
    ans.append(str(x % 5))
    x //= 5
while len(ans) < 7:
    ans.append("0")
print("".join(reversed(ans[:7])))
