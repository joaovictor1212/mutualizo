from flask import Flask, request, jsonify
import cadastro

app = Flask(__name__)

# Simulando uma lista de produtos
produtos = [
    cadastro.Produto("Produto 1", 10.99, 100),
    cadastro.Produto("Produto 2", 19.99, 50),
    cadastro.Produto("Produto 3", 5.99, 200)
]

# Carrinho vazio inicialmente
carrinho = cadastro.Carrinho()

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    lista = [{'nome': produto.nome, 'preco': produto.preco, 'estoque': produto.estoque} for produto in produtos]
    return jsonify(lista)

@app.route('/carrinho', methods=['GET'])
def ver_carrinho():
    return jsonify([{'nome': produto.nome, 'preco': produto.preco} for produto in carrinho.produtos])

@app.route('/carrinho', methods=['POST'])
def adicionar_ao_carrinho():
    data = request.get_json()
    nome_produto = data['nome']
    produto_encontrado = None

    for produto in produtos:
        if produto.nome == nome_produto and produto.estoque > 0:
            produto_encontrado = produto
            break

    if produto_encontrado:
        carrinho.adicionar_produto(produto_encontrado)
        produto_encontrado.estoque -= 1
        return jsonify({'mensagem': 'Produto adicionado ao carrinho com sucesso!'})
    else:
        return jsonify({'mensagem': 'Produto não encontrado ou sem estoque'}), 404

@app.route('/carrinho', methods=['DELETE'])
def remover_do_carrinho():
    data = request.get_json()
    nome_produto = data['nome']

    for produto in carrinho.produtos:
        if produto.nome == nome_produto:
            carrinho.remover_produto(produto)
            produto.estoque += 1
            return jsonify({'mensagem': 'Produto removido do carrinho com sucesso!'})

    return jsonify({'mensagem': 'Produto não encontrado no carrinho'}), 404

@app.route('/carrinho/finalizar', methods=['POST'])
def finalizar_compra():
    pedido = carrinho.finalizar_compra()
    return jsonify({'mensagem': 'Compra finalizada com sucesso!', 'total': pedido.total})

if __name__ == '__main__':
    app.run(debug=True)
