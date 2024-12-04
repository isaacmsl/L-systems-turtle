def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            variables = lines[0].replace('\n', '').split(',')
            axiom = lines[1].replace('\n', '')
            rules = lines[2].replace('\n', '').split(',')
            iterations = int(lines[3].replace('\n', ''))
        
        return variables, axiom, rules, iterations
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError:
        print(f"Error reading file: {file_path}")

if __name__ == "__main__":
    file_path = 'in'
    content = read_file(file_path)
    if content:
        print(content)