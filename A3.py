scores = []
for i in range(5):
    score = int(input('Enter your scores: '))
    scores.append(score)
for i in range(len(scores)):
    print(i + 1, scores[i])
passed = 0
for s in scores:
    if s >= 75:
        passed = passed + 1
print(passed, 'over 5 passed')
        

