import threading

# Read input text file and store it in-memory
with open('input.txt', 'r') as f:
    input_text = f.read()

# Split the input text into words
words = input_text.split()

# Define the map function to map words to a key-value pair
def map_func(word):
    return (word, 1)

# Define the reduce function to reduce the values of the same keys
def reduce_func(key, values):
    return (key, sum(values))

# Define the thread class to simulate MapReduce
class MapReduceThread(threading.Thread):
    def __init__(self, data, map_func, reduce_func, output):
        threading.Thread.__init__(self)
        self.data = data
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.output = output
        
    def run(self):
        # Map the data using the map function
        mapped_data = [self.map_func(item) for item in self.data]
        
        # Shuffle the mapped data based on keys
        shuffled_data = {}
        for key, value in mapped_data:
            if key in shuffled_data:
                shuffled_data[key].append(value)
            else:
                shuffled_data[key] = [value]
        
        # Reduce the shuffled data using the reduce function
        reduced_data = [self.reduce_func(key, values) for key, values in shuffled_data.items()]
        
        # Append the reduced data to the output list
        self.output += reduced_data

# Split the words into chunks for parallel processing
num_chunks = 4
chunk_size = len(words) // num_chunks
if chunk_size < 1:
    chunk_size = 1
chunks = [words[i:i+chunk_size] for i in range(0, len(words), chunk_size)]


# Create a list to store the output of each thread
output = []

# Create and start threads for each chunk of data
threads = []
for chunk in chunks:
    thread = MapReduceThread(chunk, map_func, reduce_func, output)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Merge the outputs from all threads
final_output = {}
for key, value in output:
    if key in final_output:
        final_output[key] += value
    else:
        final_output[key] = value

# Print the word counts
for key, value in final_output.items():
    print(f'{key}: {value}')
