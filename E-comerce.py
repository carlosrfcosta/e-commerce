class Produto:
    """Classe que representa um produto da loja"""
    def __init__(self, codigo, nome, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"[{self.codigo}] {self.nome} — R$ {self.preco:.2f} | Estoque: {self.estoque}"


class ItemCarrinho:
    """Item dentro do carrinho (produto + quantidade)"""
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f"{self.produto.nome} × {self.quantidade} = R$ {self.subtotal():.2f}"


class Carrinho:
    """Carrinho de compras"""
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto, quantidade):
        if quantidade <= 0:
            print("❌ Quantidade inválida!")
            return False

        # Verifica estoque
        if produto.estoque < quantidade:
            print(f"❌ Estoque insuficiente! Disponível: {produto.estoque}")
            return False

        # Verifica se já está no carrinho
        for item in self.itens:
            if item.produto.codigo == produto.codigo:
                if produto.estoque >= item.quantidade + quantidade:
                    item.quantidade += quantidade
                    produto.estoque -= quantidade
                    print(f"✅ '{produto.nome}' atualizado no carrinho!")
                    return True
                else:
                    print("❌ Sem estoque suficiente para aumentar a quantidade.")
                    return False

        # Adiciona novo item
        self.itens.append(ItemCarrinho(produto, quantidade))
        produto.estoque -= quantidade
        print(f"✅ '{produto.nome}' adicionado ao carrinho!")
        return True

    def remover_item(self, codigo_produto):
        for i, item in enumerate(self.itens):
            if item.produto.codigo == codigo_produto:
                item.produto.estoque += item.quantidade
                del self.itens[i]
                print(f"🗑️ '{item.produto.nome}' removido do carrinho!")
                return True
        print("⚠️ Produto não encontrado no carrinho.")
        return False

    def valor_total(self):
        return sum(item.subtotal() for item in self.itens)

    def exibir(self):
        if not self.itens:
            print("\n🛒 Carrinho vazio!")
            return
        print("\n" + "="*40)
        print("🛒 CARRINHO DE COMPRAS")
        print("-"*40)
        for item in self.itens:
            print(f"  {item}")
        print("-"*40)
        print(f"💵 TOTAL: R$ {self.valor_total():.2f}")
        print("="*40)

    def finalizar_compra(self):
        if not self.itens:
            print("\n⚠️ Carrinho vazio! Não é possível finalizar.")
            return False
        print("\n🎉 COMPRA FINALIZADA COM SUCESSO!")
        print(f"💰 Valor total: R$ {self.valor_total():.2f}")
        print("📦 Obrigado pela preferência! Volte sempre 😊\n")
        self.itens.clear()
        return True


class Loja:
    """Loja com catálogo de produtos"""
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []

    def cadastrar_produto(self, produto):
        self.catalogo.append(produto)

    def exibir_catalogo(self):
        print(f"\n{'='*50}")
        print(f"📋 CATÁLOGO — {self.nome.upper()}")
        print("="*50)
        for p in self.catalogo:
            print(f"  {p}")
        print("="*50)

    def buscar_produto(self, codigo):
        for p in self.catalogo:
            if p.codigo == codigo:
                return p
        return None


# ══════════════════ PROGRAMA PRINCIPAL ══════════════════
if __name__ == "__main__":
    # Cria a loja
    loja = Loja("Super Loja Python")

    # Cadastra produtos no catálogo
    loja.cadastrar_produto(Produto(1, "Notebook", 3500.00, 10))
    loja.cadastrar_produto(Produto(2, "Mouse", 89.90, 50))
    loja.cadastrar_produto(Produto(3, "Teclado", 120.50, 30))
    loja.cadastrar_produto(Produto(4, "Monitor", 850.00, 15))

    # Cria carrinho
    carrinho = Carrinho()

    while True:
        print("\n===== MENU =====")
        print("1. Ver catálogo de produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Remover produto do carrinho")
        print("4. Ver carrinho")
        print("5. Finalizar compra")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            loja.exibir_catalogo()

        elif opcao == "2":
            loja.exibir_catalogo()
            try:
                cod = int(input("Digite o código do produto: "))
                qtd = int(input("Digite a quantidade: "))
                prod = loja.buscar_produto(cod)
                if prod:
                    carrinho.adicionar_produto(prod, qtd)
                else:
                    print("❌ Produto não encontrado.")
            except ValueError:
                print("⚠️ Digite apenas números!")

        elif opcao == "3":
            cod = int(input("Digite o código do produto para remover: "))
            carrinho.remover_item(cod)

        elif opcao == "4":
            carrinho.exibir()

        elif opcao == "5":
            carrinho.exibir()
            carrinho.finalizar_compra()

        elif opcao == "0":
            print("👋 Saindo... Obrigado!")
            break

        else:
            print("⚠️ Opção inválida! Tente novamente.")
