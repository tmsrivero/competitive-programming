def generate_binary_numbers(n):
    binary_numbers = []
    for i in range(1, 2**n):
        binary_numbers.append(bin(i)[2:])
    return binary_numbers


def generate_factor_combinations(binary_numbers):
    factor_combinations = []
    for i in range(len(binary_numbers)):
        for j in range(i, len(binary_numbers)):
            factor_combinations.append(
                (int(binary_numbers[i], 2), int(binary_numbers[j], 2)))
    return factor_combinations


def generate_products(factor_combinations):
    products = set()
    for factor_pair in factor_combinations:
        product = factor_pair[0] * factor_pair[1]
        if product < 10**5:
            products.add(product)
    return sorted(products)


# Genera números binarios de hasta 5 dígitos (de 1 a 31 en decimal)
binary_numbers = generate_binary_numbers(9)
factor_combinations = generate_factor_combinations(binary_numbers)
products = generate_products(factor_combinations)

print("Resultados posibles de multiplicaciones:")
print(products)
