import sys

T = int(sys.stdin.readline().strip())
courses = []
total = [0] * 6

for _ in range(T):
    S = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    count = [0] * 6
    n = len(line)
    i = 0
    while i < n:
        while i < n and line[i] == ' ':
            i += 1
        if i >= n:
            break
        count[ord(line[i]) - 65] += 1
        i += 1
    courses.append(count[:])
    for j in range(6):
        total[j] += count[j]

out = []
for c in courses:
    out.append("A:{} B:{} C:{} D:{} E:{} F:{}".format(c[0], c[1], c[2], c[3], c[4], c[5]))
out.append("TOTAL: A:{} B:{} C:{} D:{} E:{} F:{}".format(total[0], total[1], total[2], total[3], total[4], total[5]))
print('\n'.join(out))
