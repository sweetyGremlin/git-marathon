import sympy

# 1. Обираємо два простих числа p і q
p = sympy.randprime(5, 20)  # Просте число в межах [5, 20]
q = sympy.randprime(5, 20)
while p == q:  # Щоб p і q були різними
    q = sympy.randprime(5, 20)

# 2. Обчислюємо N та функцію Ейлера φ(N)
N = p * q
phi_N = (p - 1) * (q - 1)

# 3. Обираємо відкритий ключ K_B (взаємно просте з φ(N))
K_B = sympy.randprime(2, phi_N)  # Просте число для забезпечення НСД(K_B, φ(N)) = 1
while sympy.gcd(K_B, phi_N) != 1:
    K_B = sympy.randprime(2, phi_N)

# 4. Обчислюємо секретний ключ K_C (обернене до K_B мод φ(N))
K_C = pow(K_B, -1, phi_N)  # Модульний обернений

# Виводимо отримані значення
print(f"Прості числа: p = {p}, q = {q}")
print(f"N = {N}, φ(N) = {phi_N}")
print(f"Відкритий ключ (N, K_B): ({N}, {K_B})")
print(f"Секретний ключ K_C: {K_C}")
