empty_set = set()

number = { 1,2,3,4,5}
furits = set(['apple', 'banana', 'orange'])

scores = [85,90, 90,89]
unique_sc= set(scores)
print(unique_sc)

furits.remove("banana") # error if not found
furits.discard("papaya") # No error if not found
if 'red' in furits:
    print('is available')
else :
    print('not available')

