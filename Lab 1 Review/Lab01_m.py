import functools
# Python II - Lab 1 - Annie Yen


"""Part 1 """


def palindrome(word):
    """ Input word string
        Test if word is a palindrome"""
    # use a for loop to check the letter from the start
    # corresponding letter from the end
    for i in range(len(word)//2):
        if word[i] == word[-1-i]:
            return True
        return False


"""Part 2 """


def score_password(pw):
    """ Input string representing password
        Output score for password strength"""
    # Count and score the length of password
    # initialize variable for password and length count
    score = 0
    count = 0
    for i in pw:
        count += 1
    if count >= 8:
        score = score + 1
    # Check for lower case
    if any(
        c
        for c in pw
        if c.islower()
    ):
        score = score + 1
    # Check for upper case
    if any(
        c
        for c in pw
        if c.isupper()
    ):
        score = score + 1
    # Check for number
    if any(
        c.isdigit()
        for c in pw
    ):
        score = score + 1
    # Check for special characters
    if any(
        [
            "!" == c, "@" == c,
            "#" == c, "$" == c,
            "%" == c, "^" == c,
            "&" == c, "*" == c
        ]
        for c in pw
    ):
        score = score + 1
    return score


"""Part 3 """


def compound(balance, interest, year):
    """ Input principal balance, interest, year
        Output zip list of year as index, interest
        and new balance """
    amount1 = [
        float(
            balance*(1.0+(interest/100))**year
        )
        for year in range(0, (year+1))
    ]
    amount2 = [
        float(
            balance*(1.0+(interest/100))**(year-1)
        )
        for year in range(0, (year+1))
    ]
    interest = [
        x1-x2
        for (x1, x2) in zip(amount1, amount2)
    ]
    year_index = [
        year
        for year in range(1, (year+1))
    ]
    return zip(
        year_index, interest[1:], amount1[1:]
    )


def start_my_program():
    """Part 1 """
    # Prompt use to input string as palindrome word
    str_word = input(
        "Enter a string: "
    )
    print(
        "Is %s a palindrome? %r \n"
        % (str_word.upper(), palindrome(str_word))
    )

    """Part 2 """
    # Prompt user to input string for password
    # Check that the password does not consist of space
    password = input(
        "Enter a password: "
    )
    while ' ' in password or '	' in password:
        password = input(
            "Password cannot consist of space\n Enter again:"
        )
    print(
        "Your password score is: %d \n"
        % (score_password(password))
    )

    """Part 3 """
    # Prompt user to input float for principal balance,rate and term
    principal = float(
        input(
            "Enter the principalamount (ex: 1000.00): "
        )
    )
    apr = float(
        input(
            "Enter interest rate percentage (ex: 4.5): "
        )
    )
    term = int(
        input(
            "Enter term in years (ex: 10): "
        )
    )
    # Call function compound
    result = compound(principal, apr, term)
    # Print the result table
    titles = ['Year', 'Interest', 'Balance']
    print(
        '{:<12} {:<12} {:<12}'.format(*titles)
    )
    print(
        '='*38
    )
    for item in result:
        print(
            '{:<12}$ {:<12,.2f}$ {:<12,.2f}'.format(*item)
        )


if __name__ == "__main__":
    start_my_program()
