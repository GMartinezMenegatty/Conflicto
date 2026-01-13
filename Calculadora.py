class CalculadoraBinaria:
    def __init__(self, a, b):
        self.set_a(a)
        self.set_b(b)
#Comentario 5 rama1.
    #Comentario 8
    def set_a(self, a):
        if isinstance (a, int) or isinstance(a, float) or isinstance(a, complex):
            self.__a = a
        else:
            raise TypeError

    def get_a (self):
        return self.__a

    def set_b(self, b):
        if isinstance (b, int) or isinstance(b, float) or isinstance(b, complex):
            self.__b = b
        else:
            raise TypeError

    def get_b(self):
        return self.__b

    def operacion(self, operando):
        if operando == '+':
            return self.__a + self.__b
        elif operando == '-':
            return self.__a - self.__b
        elif operando == '*':
            return self.__a * self.__b
        elif operando == '/':
            if self.__b == 0:
                return 'BOOM!!!'
            else:
                return self.__a / self.__b

    a = property(get_a, set_a)
    b = property(get_b, set_b)

if __name__ == '__main__':
    calc1 = CalculadoraBinaria(4, 3)
    print(calc1.operacion('+'))
    c2 = CalculadoraBinaria(2, 0)
    print(c2.operacion('/'))

    try:
        print(calc1.operacion('/'))
    except ZeroDivisionError:
        print('No se puede dividir por 0')
        b = int(input('Ingresa un divisor: '))
        while b==0:
            b = int(input('Ingresa un divisor: '))
        c2.b = b
        print(c2.operacion('/'))
    finally:
        print("Fin do programa")
