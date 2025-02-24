import numpy 
import plotly.express

vetor_a = numpy.linspace(10,1000,100)
vetor_b = numpy.linspace(10,3000,100)
vetor_c = numpy.linspace(10,8000,100)

print(vetor_a)
print(vetor_b)
print(vetor_c)

# Numpy tem métodos para salvar um arquivo no formato txt
numpy.savetxt('vetor_a.txt',vetor_a,fmt='%f',delimiter=';')
numpy.savetxt('vetor_b.txt',vetor_b,fmt='%f',delimiter=';')
numpy.savetxt('vetor_c.txt',vetor_c,fmt='%f',delimiter=';')