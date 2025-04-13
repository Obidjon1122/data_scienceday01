import sys

def extract_names():
    if len(sys.argv)==2:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            emails = file.read().splitlines()
        new_lines = []
        with open('employees.tsv', 'w') as file:
            file.write('Name\tSurname\tEmail\n')
            for email in emails:
                name,surname = email.split('@')[0].split('.')[0].capitalize(), email.split('@')[0].split('.')[1].capitalize()
                new_lines.append(f'{name}\t{surname}\t{email}\n')
            new_lines.sort()
            file.writelines(new_lines)

if __name__ == '__main__':
    extract_names()