max_num = 10000
def solution():
    num_set = {i for i in range(1, max_num+1)}
    ans_set = set()
    for i in num_set:
        up_word = i
        for j in range(len(str(i))):
            up_word += int(str(i)[j])
            # print(up_word)

        ans_set.add(up_word)
    
    for i in sorted(num_set.difference(ans_set)):
        print(i)
solution()

