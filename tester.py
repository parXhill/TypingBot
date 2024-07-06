
def split_into_chunks(line, chunk_size):
    return [line[i:i + chunk_size] for i in range(0, len(line), chunk_size)]

# Example usage
input_string = "This is an example string to split."
chunks = split_into_chunks(input_string, 5)
print(chunks)