# Step 1 - Making a hash function (ASCII)
def get_hash(key:str):
    h = 0
    for char in key:
        h += ord(char)
    # we divide by value, 
    # which is  assumed to be a size of the list
    return h % 100 

# Step 2 - Make up a hash table
class HashTable:
    def __init__(self):
        self.MAX = 100
        # List comprehension offers a shorter 
        # syntax when you want to create a new 
        # list based on the values of an 
        # existing list
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key:str):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX 
    # Here we override existing python operators
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
    
    
t = HashTable()
t["march 6"] = 20
t["march 17"] =  88
print(t['march 17'])


dict = {}
with open('nyc_weather.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            dict[day] = temperature
        except:
            if tokens[1] == None:
                print("Invalid temperature.Ignore the row")

def avg():
    sum = 0
    itr = 0
    for val in dict.values():
        sum += val
        itr += 1
    avg = sum/itr
    return avg

result = avg()
print(result)
print(dict['Jan 9'])

word_count = {}  # Initialize an empty dictionary to store word frequencies

with open("poem.txt", "r") as f:  # Open the file in read mode
    for line in f:  # Iterate over each line in the file
        tokens = line.split(' ')  # Split the line into individual words
        for token in tokens:  # Iterate over each word
            token = token.replace('\n', '')  # Remove newline characters
            if token in word_count:  # If the word is already in the dictionary
                word_count[token] += 1  # Increment its count by 1
            else:  # If the word is not in the dictionary
                word_count[token] = 1  # Add it to the dictionary with a count of 1

print(word_count)  # Print the word frequencies

# Linear probing
        
class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        hash = self.get_hash(key)
        if self.arr[hash] is None:
            return
        prob_range = self.get_prob_range(hash)
        for slot in prob_range:
            if self.arr[slot] is None:
                return
            if self.arr[slot][0] == key:
                return self.arr[slot][1]
           
    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        if self.arr[hash] is None:
            self.arr[hash] = (key,val)
        else:
            new_hash = self.find_slot(key, hash)
            self.arr[new_hash] = (key,val)
        print(self.arr)
        
    def get_prob_range(self, hash):
    # The * symbol in Python is used for 
    # unpacking iterable objects, such as 
    # lists, tuples, or strings. It allows 
    # you to pass multiple elements of an 
    # iterable as separate arguments to a 
    # function or to create new iterable objects 
    # by combining existing ones.
        return [*range(0, hash)] + [*range(hash, len(self.arr))]
    
    def find_slot(self, key, hash):
        prob_range = self.get_prob_range(hash)
        for slot in prob_range:
            if self.arr[slot] is None:
                return slot
            if self.arr[slot][0] == key:
                return slot
        raise Exception("Hashmap is full")
        
    def __delitem__(self, key):
        hash = self.get_hash(key)
        prob_range = self.get_prob_range(hash)
        for slot in prob_range:
            if self.arr[slot] is None:
                return 
            if self.arr[slot][0] == key:
                self.arr[slot]=None
        print(self.arr)


