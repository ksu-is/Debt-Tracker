import math


class Loan:  # Main Loan

	# Initializer / Instance Attributes
	def __init__(self, amount, interest, age):
		self.amount = amount  # Total Loan Amount
		self.interest = interest / (12 * 100)
		self.age = age  # Age should be in years
		
	# Loan Calculation Method
	def loan_calculation(self):
		
		# Initial Variables for Loan Calculation
		amount = self.amount
		months = self.age * 12
		monthly_interest = self.interest

		# Formula Setup
		numerator = monthly_interest * amount
		denominator = 1 - ((1 + monthly_interest) ** (-1 * months))

		calculated_monthly_payment = round(float(numerator/denominator), 2)

		# Return Result for Method
		return calculated_monthly_payment
		

class CustomLoan(Loan):  # Custom Loan
	def __init__(self, loan, c_amount, c_years):
		super().__init__(loan.amount, loan.interest, loan.age)
		self.c_amount = c_amount  # Custom Amount
		self.c_years = c_years  # Custom Years
		
	def custom_calculation(self, loan):

		# Initial Variables for Custom Loan Calculation
		c_months = self.c_years * 12
		monthly_interest = loan.interest
		amount = loan.amount

		# Formula Setup from financeformulas.net/Remaining_Balance_Formula.html setting FV to FV
		term_1 = amount * ((1 + monthly_interest) ** c_months)

		term_2_numerator = self.c_amount * (((1 + monthly_interest) ** c_months) - 1)
		term_2_denominator = monthly_interest

		term_2 = term_2_numerator / term_2_denominator

		term_12 = term_1 - term_2

		# Amount after paying custom amount for custom period of time
		remaining_amount = term_12

		if remaining_amount > 0:
			# Redeclare Variables
			remaining_months = loan.age * 12 - c_months
			new_numerator = ((1 + monthly_interest) ** remaining_months) - 1
			new_denominator = monthly_interest * ((1 + monthly_interest) ** remaining_months)

			# Re-adjust Formula
			new_term = new_numerator / new_denominator

			new_payment = round(remaining_amount / new_term, 2)

			# Setup Result
			remaining_years = round(remaining_months / 12, 2)
			result1 = [remaining_years, new_payment]

			# Return Result
			return result1
		else:
			# Set Answer of Payments to 0 since loan is paid off before initial years
			clean_payment = 0

			# Reconfigure the Formula to Determine Number of Terms
			clean_numerator = math.log(amount * monthly_interest / self.c_amount + 1)
			clean_denominator = math.log(1 + monthly_interest)

			# Solve the Number of Terms
			number_of_terms_months = clean_numerator / clean_denominator
			number_of_terms_years = round(number_of_terms_months / 12, 2)

			# Setup Result
			result1 = [number_of_terms_years, clean_payment]

			# Return Result
			return result1
