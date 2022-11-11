class Fraction():
    ##Atributo##
    numerator=0
    denominator=1
    ##Fin atributo##

    ##Metodos##

    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator

    def print(self):
        print(self.numerator,"/",self.
        denominator)

    ##Multiplicacion##

    def multiply(self,def_multiplication):
        result_numerator=self.numerator*def_multiplication.numerator
        result_denominator=self.denominator*def_multiplication.denominator
        result_multiply=Fraction(result_numerator,result_denominator)
        print("Resultado multiplicacion de las fracciones es:", result_numerator,"/",result_denominator)
        return result_multiply

    ##Fin multiplicacion##

    ##Divicion##
    def division(self,def_division):
        result_numerator=self.numerator*def_division.denominator
        result_denominator=self.denominator*def_division.numerator
        result_division=Fraction(result_numerator,result_denominator)
        print("Resultado division de las fracciones es:", result_numerator,"/",result_denominator)
        return result_division

    ##Fin division##

    
    ##Suma##
    def addition(self,def_addition):
        multiplication_one=self.denominator*numerator_two
        multiplication_two=self.numerator*denominator_two
        result_denominator=self.denominator*def_addition.denominator
        result=multiplication_one+multiplication_two
        result_addition=Fraction(result,result_denominator)
        print("Resultado suma de las fracciones es:", result,"/",result_denominator)
        return result_addition

    ##Fin suma##


    ##Resta##

    def subtraction(self,def_subtraction):
        multiplication_one=self.denominator*numerator_two
        multiplication_two=self.numerator*denominator_two
        result_denominator=self.denominator*def_subtraction.denominator
        result=multiplication_one-multiplication_two
        result_subtraction=Fraction(result,result_denominator)
        print("Resultado resta de las fracciones es:", result,"/",result_denominator)
        return result_subtraction

    ##Fin resta##



print("Ingresar primera fraccion")
print("Ingrese el primer numerador")
numerator_one=int(input())
print("Ingrese el segundo denominador")
denominator_one=int(input())
result_one=Fraction (numerator_one,denominator_one)

Fraction_one=Fraction(numerator_one,denominator_one)


print("Ingresar segunda fraccion")
print("Ingrese el segundo numerador")
numerator_two=int(input())
print("Ingrese el segundo denominador")
denominator_two=int(input())
result_two=Fraction (numerator_two,denominator_two)

Fraction_two=Fraction(numerator_two,denominator_two)


result_multiply=Fraction_one.multiply(Fraction_two)
result_multiply.print

result_division=Fraction_one.division(Fraction_two)
result_division.print

result_addition=Fraction_one.addition(Fraction_two)
result_addition.print

result_subtraction=Fraction_one.subtraction(Fraction_two)
result_subtraction.print

