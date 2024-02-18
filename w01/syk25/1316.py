def grouped(text):
    before = text[0]
    record = {text[0]}
    for i in range(1, len(text)):
        if text[i] not in record:
            record.add(text[i])
            before = text[i]
        else:
            if word[i] != before:
                return 0
    return 1


tries = int(input())
count = 0

for j in range(tries):
    word = input()
    count += grouped(word)

print(count)
