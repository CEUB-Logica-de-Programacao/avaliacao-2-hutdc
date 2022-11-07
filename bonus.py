# Dada uma lista de números inteiros não-negativos, organize-os de modo que formem o maior número e devolva-o.
#
# Como o resultado pode ser muito grande, é preciso devolver uma string em vez de um número inteiro.
#
# ### Exemplo 1
#
# ```
# Input: nums = [10,2]
# Output: "210"
# ```
#
# ### Exemplo 2
#
# ```
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# ```


def bonus(nums):
    max  = ""
    resp = ""
    arr = []
    for x in nums:
        arr.append(str(x))

    while arr:

        for x in arr:
            if not max :
                max = x
            else:
                if x + max > max +x:
                    max = x

        resp += max
        arr.remove(max)
        max = ""

    return resp if not resp.startswith("0") else "0"


if __name__ == '__main__':
    print(bonus([3, 30, 34, 5, 9]))
