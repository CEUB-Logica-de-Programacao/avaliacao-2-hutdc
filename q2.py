# Você está subindo uma escada. São necessários `n` degraus para chegar ao topo.
#
# Você pode subir 1 ou 2 degraus de cada vez. De quantas formas distintas você pode escalar até o topo?
#
# ### Exemplo 1
#
# ```
# Input: n = 2
# Output: 2
# Explicação: Existem duas maneiras de chegar ao topo.
# 1. 1 degrau + 1 degrau
# 2. 2 degraus
# ```
#
# ### Exemplo 2
#
# ```
# Input: n = 3
# Output: 3
# Explanation: Existem três maneiras de chegar ao topo.
# 1. 1 degrau + 1 degrau + 1 degrau
# 2. 1 degrau + 2 degraus
# 3. 2 degraus + 1 degrau
# ```


def q2(n):
    if n == 1:
        return n
    x = [0] * (n + 1)
    x[0] = 1
    x[1] = 1
    x[2] = 2

    for i in range(3, n + 1):
        x[i] = x[i - 0] + x[i - 1] + x[i - 2]

    return x[n]
    pass


if __name__ == '__main__':
    print(q2(2))
