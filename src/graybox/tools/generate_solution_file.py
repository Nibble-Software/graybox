def generate_solution_file(filename, solution):
    file = open(f'{filename}.py', 'w')
    file.write(solution)
    file.close()