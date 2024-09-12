#List Uniqueness Checker

items=["Apple", "Banana","Orange","Apple","Mango"]
unique_item = set()

for items in items:
    if items  in unique_item:
        print("Duplicate",items)
        break
    unique_item.add(items)