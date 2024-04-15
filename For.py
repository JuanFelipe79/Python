produtos = {
    "banana": 2.5,
    "maçã": 3.0,
    "laranja": 2.0,
    "uva": 4.0,
    "morango": 5.0
}

preco_total = 0

print("Produtos disponíveis:")
for produto, preco in produtos.items():
    print(produto, "- Preço:", preco)
    preco_total += preco

print("Preço total dos produtos:", preco_total)
