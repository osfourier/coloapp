

import flask



def student_param (numba_student):
    student_details = {}
    for a in range (0,numba_student):
        name = input('Enter student names: ')
        sex = input ('Enter your Sex: ')
        code = input('Enter given registration code: ')
        pass_code = input('Enter Password: ')
        year = input ('Enter your year of Birth: ')
        age = 2020 - int(year)
        nation = input('Enter your Nationality: ')
        
        student_details[name] = [pass_code, sex, code, year, name, nation,age]
    print(student_details)
    
    print(f'WELCOME AND LOGIN BELOW')
    ## How to write data to a file. The step below is not working###
    
    
    
        
    student_login = input('Enter Student Name: ' )
    if student_login in student_details.keys():
        passw = input('Enter your password: ')
        if passw == student_details[student_login][0]:
            print ('Loggin Successful')
            print (f'Welcome {student_details[student_login][4]}')
            leave = str()
            leave = input('Enter "LOGOUT" to quit or "INFO" to check your details or "NEW" to enter new session: ')
            if leave == 'LOGOUT':
                quit
            while leave == 'INFO':
                print (f'Password: {student_details[student_login][0]}')
                print (f'Registration code: {student_details[student_login][2]}')
                print(f'Year of Birth: {student_details[student_login][3]}')
                print(f'Age: {student_details[student_login][6]}')
                print (f'Nationality: {student_details[student_login][5]}')
                
                
                leave = str()
                leave = input('Enter "LOGOUT" to quit or "INFO" to check your details or "NEW" to enter new session: ')
                if leave == 'LOGOUT':
                    quit
                    break
            while leave == 'NEW':
                student_login = input('Enter Student Name: ' )
                if student_login in student_details.keys():
                    passw = input('Enter your password: ')
                    if passw == student_details[student_login][0]:
                        print ('Loggin Successful')
                        print (f'Welcome {student_details[student_login][4]}')
                        leave = str()
                        leave = input('Enter "LOGOUT" to quit or "INFO" to check your details or "NEW" to enter new session: ')
                        if leave == 'LOGOUT':
                            quit
                        elif leave == 'INFO':
                            print (f'Password: {student_details[student_login][0]}')
                            print (f'Registration code: {student_details[student_login][2]}')
                            print(f'Year of Birth: {student_details[student_login][3]}')
                            print(f'Age: {student_details[student_login][6]}')
                            print (f'Nationality: {student_details[student_login][5]}')
                            leave = str()
                            leave = input('Enter "LOGOUT" to quit or "INFO" to check your details or "NEW" to enter new session: ')
                            if leave == 'LOGOUT':
                                quit
                    elif passw != student_details[student_login][0]:
                        print (f'Incorrect Password')
                        passw = input('Enter your password: ')
                        #if passw == student_details[student_login][0]:
                           # print ('Loggin Successful')
                            #print (f'Welcome {student_details[student_login][4]}')

                        #break
                else:
                    print(f'User not known, Please Register')
                    break
            
                                
                            
        elif passw != student_details[student_login][0]:
            print (f'Incorrect Password')
            
    else:
        print(f'User not known, Please Register')
        
        
   # log = open('LOG_DETA.txt', 'r+')
   
    navi = str()
    navi = input('Click "SAVE" ')
    if navi == 'SAVE':
        student_details = str(student_details)
        with open ('LOG_DETA.txt','r+') as log:
            log = log.write(student_details)
        #log = log.write(sex)
        #log = log.write(code)
        
        
    
def start():
    numba_student = int(input('Number of student to register: '))
    student_param(numba_student)
start()
