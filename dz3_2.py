def fcust(**kwargs):
    return kwargs

print(fcust(fname=input('Enter your First name: '),
            lname=input('Enter your Last Name: '),
            bday=input('Enter your birth day: '),
            htown=input('Enter your home town: '),
            email=input('Enter your email: '),
            phone=input('Enter your phone number: ')))