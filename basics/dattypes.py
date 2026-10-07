id = 1
firstName = "Jacky"
lastName = "         Jones"
ssn = "123-45-6789"
hasInsurance = True
billingAmount = "1000"
type(billingAmount)
billingAmount = float(billingAmount)
print(type(billingAmount))

print(id, firstName, lastName.lstrip(), ssn, hasInsurance, billingAmount, ssn[7:len(ssn)])