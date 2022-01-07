#question 5:
#(a) print a list and then remove 4th element from the list and let it print the new list
#(b) remove 'Black' and 'Pink' from the list and replace it with 'Purple'

my_list=['Red','Green','White','Black','Pink','Yellow']
#(a) part
print('(a)')
print(my_list)
# remove 4th term that is black
my_list.remove('Black')
print(my_list)

my_list=['Red','Green','White','Black','Pink','Yellow']
#(b) part
print('(b)')
print(my_list)
#replace black and pink with purple
# to replace nth term we write {my_list[n-1]='new value'}
my_list[3:5]=['Purple']
print(my_list)

