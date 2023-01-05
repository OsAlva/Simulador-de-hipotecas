import time

class Hipoteca:
    def __init__(self,user_name, interest_rate, loan_amount, loan_length):
        self.user_name = user_name
        self.interest_rate = interest_rate
        self.loan_amount = loan_amount
        self.loan_length = loan_length
        self.monthly_interest = self.interest_rate/100/12
        self.monthly_mortgage = (self.monthly_interest * self.loan_amount) /(1-((1+self.monthly_interest)) ** (-self.loan_length * 12))
    
    #calcular mensualidad
    def calculate_monthly(self):
        formatted_monthly_mortgage = "€{:,.2f}".format(self.monthly_mortgage)
        print(f"{self.user_name}, los pagos mensuales de un prestamo de esta cantidad sería {formatted_monthly_mortgage}.")

    #calcular prestamo total
    def calculate_total_loan(self):
        total_loan_cost = (self.monthly_mortgage * self.loan_length) + self.loan_amount
        euro_format = "€{:,.2f}".format(total_loan_cost)
        print(f"{self.user_name}, suponiendo que su tasa de interes se mantenga en {self.interest_rate}% a lo largo de la duración del prestamo, el monto total que tendra que devolver es {euro_format}.")

#obtenemos información
def get_info():
    information = []
    interest_rate = input("Cual es la tasa de interés de su prestamo?\n")
    information.append(float(interest_rate))
    loan_amount = input(f"Su tasa de interes es {interest_rate}%. Cuanto le gustaría pedir prestado?\n")
    information.append(float(loan_amount))
    loan_length = input(f"El monto solicitado en prestamo seria {loan_amount}. Y en años, cual es la duracion de este prestamo?\n")
    information.append(float(loan_length))
    print("Procesando información... porfavor espere...")
    for i in range(3):
        print(".............")
        time.sleep(2)
    return information


get_name = input("Hola esto es una calculador de hipotecas. Como te llamas?")
print("Hola, {get_name}! mucho gusto... Que te gustaría hacer hoy??")
aux = True
while aux:
    get_task = input(f"Escriba '1 para calcular la tasa de interes mensual. \nEscriba '2' para calcular el monto total de su prestamo. \n")
    information  = get_info()
    interest_rate, loan_amount, loan_length = information[0], information[1], information[2]
    new_user = Hipoteca(get_name, interest_rate, loan_amount, loan_length)

    if get_task == '1':
        new_user.calculate_monthly()
    else:
        new_user.calculate_total_loan()

    end_question = input("Le gustaria realizar otra tarea?? Presiones 'y' o 'n'\n")
    if end_question == 'n':
        aux = False
    else:
        print("Que mas te gustaria hacer hoy??...\n")

print("Adios!!!!")




"¡Hola! Mi nombre es Morty, y soy un calculador de hipotecas. ¿Cuál es tu nombre?"