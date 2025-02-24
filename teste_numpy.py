import numpy
import time

ndarray1 = numpy.zeros(100000)
print(f"1- conteudo da lista: {ndarray1}, o tamanho: {len(ndarray1)}")
ndarray1 = numpy.ones(100000)
print(f"1- conteudo da lista: {ndarray1}, o tamanho: {len(ndarray1)}")
ndarray1 = numpy.linspace(10,1000,1000)
print(f"1- conteudo da lista: {ndarray1}, o tamanho: {len(ndarray1)}")

start_time = time.time()
lista = [0] * 1000000000
end_time = time.time()
elapsed_time = end_time - start_time
print(f"A criação da lista de 1 bilhão de elementos levou: {elapsed_time}")

start_time = time.time()
ndarray = numpy.zeros(1000000000, dtype='uint8')
end_time = time.time()
elapsed_time = end_time - start_time
print(f"A criação de um ndarray de 1 bilhão de elementos levou: {elapsed_time}")