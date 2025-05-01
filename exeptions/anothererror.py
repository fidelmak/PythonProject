# Starter code
try:
    with open('file_does_not_exist.txt', 'r') as file:
        output = file.read()
except Exception as e:
    print(f"error; {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")