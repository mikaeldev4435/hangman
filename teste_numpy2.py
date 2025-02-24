import numpy 

rng = numpy.random.default_rng() # numpy tem seus métodos random inclusos
vetor = rng.random(4)
print(f'Array de uma dimensão (vetor) randômico: \n{vetor}\n')
matriz = rng.random([4,4])
print(f'Array de duas dimensões (matriz) randômico: \n{matriz}\n')
tensor = rng.random([4,4,4])
print(f'Array de três dimensões (tensor) randômico: \n{tensor}\n')

rng = numpy.random.default_rng()
matriz = rng.random([4,4])
m_coluna = numpy.sort(matriz, axis=0)
m_linha = numpy.sort(matriz, axis=1)
m_col_lin = numpy.sort(m_linha, axis=0)
print(f"Ordenação dentro coluna: \n{m_coluna}")
print(f"Ordenação dentro linha: \n{m_linha}")
print(f"Ordenação dentro coluna e linha: \n{m_col_lin}")