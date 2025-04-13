import sys

def letter_start():
    if len(sys.argv)==2:
        with open('employees.tsv','r') as file:
            lines = file.read().splitlines()
            for line in lines:
                name,surname,email = line.split('\t')
                if sys.argv[1]==email:
                    print(f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.')
                    break
if __name__ == '__main__':
    letter_start()