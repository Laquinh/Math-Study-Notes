import numpy as np
from itertools import product

def decode_word(word, generator_matrix, q, k):
	# Calcula los vectores del cuerpo $\mathbb{F}_q^k$
	vectors = np.array(list(product(range(q), repeat=k)))

	# Multiplica dichos vectores por la matriz generadora
	# para obtener las palabras del código
	codewords = np.dot(vectors, generator_matrix) % q

	# Calcula la clase de equivalencia definida por
	# xRy si y solo si x - y ∈ codewords
	equivalence_class = (word - codewords) % q

	# Encuentra, dentro de la clase de equivalencia,
	# la palabra con menor peso (el líder)
	leader = equivalence_class[
		np.argmax(np.sum(equivalence_class == 0, axis=1))
	]

	# Decodificamos la palabra
	return (word - leader) % q

generator_matrix = np.array(
	[
		[1, 0, 0, 0, 1, 1, 1],
		[0, 1, 0, 0, 1, 1, 0],
		[0, 0, 1, 0, 0, 1, 1],
		[0, 0, 0, 1, 1, 0, 1]
	]
)

print(decode_word([1, 0, 0, 1, 0, 1, 0], generator_matrix, 2, 4))
