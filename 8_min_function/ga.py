import random
from math import sin, sqrt
from statistics import mean

NUM_OF_BITS = 10


class Ga:
    def __init__(self, pop_size, crossover_rate, mutation_rate, generations, elitism):
        self.pop_size = pop_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.elitism = elitism

        # Inclua as variáveis que serão necessárias
        # em cada passo do algoritmo
        # Já inclui algumas. Crie as demais
        self.all_x = []
        self.fitness = []
        self.population_double = []

        # number of bits = 10
        # 2^10 = 1024 possibilities in the x axis
        # 512 - upper bound
        self.granularity = pow(2, NUM_OF_BITS)
        self.step = 512.0 / self.granularity

        # Getting all x
        self.get_all_x()

    def calc_function(self, x):
        return abs(x * sin(sqrt(abs(x)))) * (-1)

    def get_all_x(self):
        print('Getting all possible x with 10 bits')

    def get_bin(self, decimal):
        return bin(decimal)[2:].zfill(10)

    def get_decimal(self, binary):
        return int(binary, 2)*self.step

    def get_initial_population(self):
        print('Escolha os individuos da população inicial')
        print('A escolha é aleatória dentro dos elementos do vetor com todos os x')

    def evaluate(self):
        print('Calcule a aptidão de cada individuo da população inicial')

    def select(self):
        print('selecione os individuos para a recombinação')
        print('utilize o método da roleta')

    def cross(self):
        print('proceda o cruzamento dos cromossomos')
        print('utilize o método do corte simples')
        print('recomendo transformar o cromossomo em uma representação binária')
        print('veja os métodos de conversão binario decimal que já deixei aqui na classe')
        print('lembre-se que o chromossomo orignal é formado por uma lista de floats')
        print('que são os provaveis x para o menor y')

    def mutate(self):
        print('Crie o processo de mutação com a inversão de um gene do cromossomo')

    def run_generation(self):
        self.get_initial_population()

        # Lists used for graph visualization
        series_generations = []
        series_avg_fitness = []
        series_best_fitness = []

        for i in range(self.generations):
            self.evaluate()

            series_generations.append(i + 1)
            series_avg_fitness.append(mean(self.fitness))
            series_best_fitness.append(self.fitness[self.population_double.index(self.best_individual)])

            self.select()
            self.cross()
            self.mutate()

            if self.elitism:
                print('Aplique o elitismo, caso escolhido pelo usuário')

        self.evaluate()

        return self.best_individual, series_generations, series_avg_fitness, series_best_fitness