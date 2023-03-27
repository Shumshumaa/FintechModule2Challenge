"""This function is used to prompt the user to whether or not they'd
like to save their results to a csv file to review the loans from 
the banks they qualify from"""

import csv


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!

    header = ["Name of Qualifying Bank"]

    csvpath = Path("List_of_Qualifying_Loans.csv")
    with open(csvpath,"w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)
        for bank in qualifying_loans:
            csvwriter.writerow([bank[0]])

# I returned the bank name because as the business I wouldn't want the user
# to see the internal criterias the banks used to determine someones qualification for the loan