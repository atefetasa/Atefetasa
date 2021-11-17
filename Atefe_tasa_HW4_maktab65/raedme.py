while True:
    try:
        email_address = str(input("please enter  your email:"))
        if '@' in email_address:
            break
        else:
            raise ValueError("you entered an invalid email address.")
            p = input("please enter your name:")

    except ValueError as ve:
        print(ve)



