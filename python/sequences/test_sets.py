

online_customers=set(['arun','arun','raj','tom'])
print('Online:', online_customers)
print('No of online customers', len(online_customers))


offline_customers=set(['arun','john'])
print('offline customers', offline_customers)


print('All customers without duplicates:', online_customers|offline_customers)
print('customers who visited online and offline:', online_customers&offline_customers)
print('Customers who visited either online or offline',online_customers^offline_customers)
