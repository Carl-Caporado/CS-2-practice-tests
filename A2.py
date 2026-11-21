scores = []
for i in range(5):
    score = int(input('Enter your scores: '))
    scores.append(score)
for i in range(len(scores)):
    print(i + 1, scores[i])
total = 0
for s in scores:
    total = total + s
print('Total:', total)
print('Average:', total / 5)