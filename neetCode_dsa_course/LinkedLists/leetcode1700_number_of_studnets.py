from collections import Counter
def countStudents(students, sandwiches):
    cnt = Counter(students)
    for s in sandwiches:
        if cnt[s] > 0:
            cnt[s] -= 1
        else:
            return cnt.total()
    return 0
