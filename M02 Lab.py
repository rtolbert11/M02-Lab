while True:
    last_name = input('Enter the student\'s last name: ')
    if last_name == 'ZZZ':
        break
    first_name = input('Enter the student\'s first name: ')
    gpa = float(input('Enter the student\'s GPA: '))
    if gpa >= 3.5:
        print(f'{first_name} {last_name} has made the Dean\'s List.')
    elif gpa >= 3.25:
        print(f'{first_name} {last_name} has made the Honor Roll.')
    #Ronald Tolbert and the name of this app is Academic Achievements. This app will determine whether or not students with certain GPAs meet the criteria of making Honor Roll, the Dean's list, or neither