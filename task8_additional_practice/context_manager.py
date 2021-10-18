class Context:
    def __init__(self, name, how):
        self.file_name = open(name, how)

    def __enter__(self):
        return self.file_name

    def __exit__(self, exit_type, exit_value, exit_traceback):
        self.file_name.close()


with Context('Example.txt', "w") as file:
    file.write('My first context manager')
print(file.closed)
with Context('Example.txt', "r") as file:
    file_data = file.read()
print(file_data)
print(file.closed)