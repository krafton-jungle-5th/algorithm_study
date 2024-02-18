n = int(input())
checker_list = []
count = 0

for i in range(n):
    input_word = input()
    checker_list.append(input_word)

def group_checker(word):
    already_group = set()
    
    for j in range(len(word)):
        if word[j] != word[j-1] and word[j] in already_group:
            return False
        already_group.add(word[j])
    
    return True

for k in range(n):
    if group_checker(checker_list[k]) == True:
        count += 1
        
print(count)
