def get_input(working_dir):
    with open(f"{working_dir}/input.txt", 'r') as f:
        content = f.read()
    return content.split('\n')