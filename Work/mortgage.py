# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = int(input('Anfangsmonat Sonderzahlungen:'))
extra_payment_end_month = int(input('Letzter Monat Sonderzahlungen:'))
extra_payment = int(input('Höhe monatliche Sonderzahlungen:'))
months = 0

while principal > 0:
    while months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid += payment + extra_payment
        months += 1
        print(f'Nach {months} Monaten wurde €{total_paid:0.2f} bezahlt und es verbleibt €{principal:0.2f} zu zahlen')
    principal = principal*(1+rate/12)-payment
    total_paid += payment
    months += 1
    if principal < 0:
        total_paid += principal
        principal = 0
    print(f'Nach {months} Monaten wurde €{total_paid:0.2f} bezahlt und es verbleibt €{principal:0.2f} zu zahlen')

print(f'Gesamtbetrag: €{total_paid:0.2f}')
print(f'Gesamtdauer:  {months} Monate')