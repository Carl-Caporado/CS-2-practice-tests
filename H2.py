def find(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


titles = []
copies = []

for i in range(3):
    title = input("Enter the theitle: ")
    num_copies = int(input("Enter the number of copies: "))
    titles.append(title)
    copies.append(num_copies)

search_title = input("Search title: ")
idx = find(titles, search_title)

if idx != -1:
    print(search_title, "has", copies[idx], "copies")
else:
    print("Not in the library")