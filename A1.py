Items = []
for i in range(4):
    item = str(input('Enter a school item: '))
    Items.append(item)
    
for i in range(len(Items)):
    print(i + 1, Items[i])