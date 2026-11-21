def count(items, target):
    total = 0
    for item in items:
        if item == target:
            total = total + 1
    return total


votes = []
while True:
    vote = input("Vote (done to stop): ")
    if vote == "done":
        break
    votes.append(vote)

target_vote = input("Count vote for: ")
print(count(votes, target_vote))