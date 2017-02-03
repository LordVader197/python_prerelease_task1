total = raw_input("eeror")
careers = 2
meal = 0
theatre = 0
price = 0
coach = 0
ppc = 0

if total >= 36 :
       print "error more than 36 cannot go"


    if total > 24:
       careers = careers + 1

if total >= 12 and total <= 16:
            meal = 14
            theatre =  21
            coach = 150
            price = meal * theatre + coach
            ppc = price / total
            print "your total cost per person is " ppc
     if total >= 17 and total <= 26:
             meal = 13.50
             theatre = 20
             coach = 190
             price =  meal * theatre + coach
             ppc = price/total
     if total >= 27 and total <= 36:
             meal = 13
             theatre = 19.0
             coach = 225
             ppc = price/ total

