def sumar_digitos (n):
    resultado = 0
    if n>999:
      while n > 9:
          resultado = resultado + n % 10
          n = n / 10
      return resultado + n
