# To sort the elemnts, you compare consecutive elements of the given list
# This way the biggest value moves towards the end of the list, the same way 
# as a bubble does in the water

def bubble(elements):
    # We need to substract 1 to 
    # exclude the case of comparing the 
    # last digit with something beyond 
    # the range as there is no element
    size = len(elements) 
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True
        # In case you have a sorted list
        if not swapped:
            break

elements = [12, 4, 7, 22, 31, 98, 6]
chars = ['p', 'b', 'j', 's', 'v', 'l']

bubble(elements)
print(elements)
bubble(chars)
print(chars)

def exercise_bubble(elements, key):
    size = len(elements) 
    for i in range(size - 1):
        for j in range(size - 1):
            if elements[j][key] > elements[j + 1][key]:
                elements[j][key], elements[j + 1][key] = elements[j + 1][key], elements[j][key]

transactions = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'phone'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'tv set'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'boom box'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'mic'},
    ]
exercise_bubble(transactions, 'transaction_amount')
print(transactions)