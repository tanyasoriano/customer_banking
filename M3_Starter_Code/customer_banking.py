# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE

# Define the main function
from cd_account import create_cd_account
from savings_account import create_savings_account


def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("Please enter your savings account balance.")
    savings_balance = input()
    savings_balance = float(savings_balance)
    print("Please enter your interest rate.")
    savings_interest = input()
    savings_interest = float(savings_interest)
    print("Please enter how many months.")
    savings_maturity = input()
    savings_maturity = int(savings_maturity)
    
    

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(interest_earned)
    print(updated_savings_balance)
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print("What is your CD balance?")
    cd_balance = float(input())
    print("What is the interest rate?")
    cd_interest = float(input())
    print("Please enter how many months.")
    cd_maturity = int(input())

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(interest_earned)
    print(updated_cd_balance) 

if __name__ == "__main__":
    # Call the main function.
    main()
