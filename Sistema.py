import tkinter as tk
from tkinter import ttk
from Database import Clientes, session

janela = tk.Tk()
janela.title("ClientTrack")


def adicionar_cliente():
    nome_cliente = caixa_textonome.get()
    cnpj = caixa_cnpj.get()
    estado = combobox_estado.get()
    telefone = caixa_textotelefone.get()
    email = caixa_textoemail.get()
    tipo_cliente = combobox_tipocliente.get()

    clientes = Clientes(nome=nome_cliente, cnpj=cnpj, estado=estado,
                     telefone=telefone, email=email, tipo_de_cliente=tipo_cliente)

    session.add(clientes)
    session.commit()

    label_mensagem['text'] = "Cadastro realizado com sucesso!"
    caixa_textonome.delete(0, tk.END)
    caixa_cnpj.delete(0, tk.END)
    combobox_estado.delete(0, tk.END)
    caixa_textotelefone.delete(0, tk.END)
    caixa_textoemail.delete(0, tk.END)
    combobox_tipocliente.delete(0, tk.END)

def alterar_dados():
    nome_cliente = caixa_textonome.get()
    if nome_cliente:
        cliente = session.query(Clientes).filter_by(nome=nome_cliente).first()

        if cliente:
            if nome_cliente:
                cliente.nome = nome_cliente
            if caixa_cnpj.get():
                cliente.cnpj = caixa_cnpj.get()
            if combobox_estado.get():
                cliente.estado = combobox_estado.get()
            if caixa_textotelefone.get():
                cliente.telefone = caixa_textotelefone.get()
            if caixa_textoemail.get():
                cliente.email = caixa_textoemail.get()
            if combobox_tipocliente.get():
                cliente.tipo_de_cliente = combobox_tipocliente.get()

            session.commit()
            label_mensagem['text'] = "Alterações salvas com sucesso!"
        else:
            label_mensagem['text'] = "Cliente não encontrado no banco de dados!"
    else:
        label_mensagem['text'] = "Preencha o campo Nome Cliente!"
    caixa_textonome.delete(0, tk.END)
    caixa_cnpj.delete(0, tk.END)
    combobox_estado.delete(0, tk.END)
    caixa_textotelefone.delete(0, tk.END)
    caixa_textoemail.delete(0, tk.END)
    combobox_tipocliente.delete(0, tk.END)


def excluir_cliente():
    nome_cliente = caixa_textonome.get()
    if nome_cliente:
        cliente = session.query(Clientes).filter_by(nome=nome_cliente).first()
        if cliente:
            session.delete(cliente)
            session.commit()
            label_mensagem['text'] = "Cliente excluído com sucesso!"
        else:
            label_mensagem['text'] = "Cliente não encontrado no banco de dados!"
    else:
        label_mensagem['text'] = "Preencha o campo Nome Cliente!"

def consultar_cliente():
    nome_cliente = caixa_textonome.get()
    usuario = session.query(Clientes).filter_by(nome=nome_cliente).first()
    texto = f"ID: {usuario.id}\n Cliente: {usuario.nome}\n CNPJ:{usuario.cnpj}\n Data de Cadastro:{usuario.data_cadastro}\n Estado: {usuario.estado}\n Telefone: {usuario.telefone}\n Email: {usuario.email}\n Tipo de Cliente: {usuario.tipo_de_cliente}"
    caixa_texto.insert("1.0", texto)
    caixa_textonome.delete(0, tk.END)



botao_adicionarcliente = tk.Button(text="Adicionar", command=adicionar_cliente, relief='flat')
botao_adicionarcliente.grid(row=1, column=1, padx=10, pady=10, sticky="NSEW")

botao_alterarcliente = tk.Button(text="Alterar Dados", command=alterar_dados, relief='flat')
botao_alterarcliente.grid(row=1, column=2, padx=10, sticky="NSEW")

botao_alterarcliente = tk.Button(text="Excluir", command=excluir_cliente, relief='flat')
botao_alterarcliente.grid(row=1, column=3, padx=10, sticky="NSEW")

botao_consultarcliente = tk.Button(text="Consultar", command=consultar_cliente, relief='flat')
botao_consultarcliente.grid(row=1, column=4, padx=10, sticky="NSEW")

label_nomecliente = tk.Label(text="Nome Cliente")
label_nomecliente.grid(row=3, column=1, padx=10, sticky="NSEW", columnspan=2)

caixa_textonome = tk.Entry(width=20)
caixa_textonome.grid(row=3, column=3,padx= 10, sticky="NSEW", columnspan=6, pady=10)

label_cnpj = tk.Label(text="CNPJ")
label_cnpj.grid(row=6, column=1, padx=10, sticky="NSEW", columnspan=2)

caixa_cnpj= tk.Entry(width=20)
caixa_cnpj.grid(row=6, column=3,padx= 10, sticky="NSEW", columnspan=6, pady=10)

estados_brasileiros = [
    "AC", "AL", "AP", "AM", "BA", "CE", "ES", "GO", "MA", "MT", "MS", "MG",
    "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP",
    "SE", "TO"
]

label_estado = tk.Label(text="Estado")
label_estado.grid(row=7, column=1, padx=10, sticky="NSEW", columnspan=2, pady=10)

combobox_estado = ttk.Combobox(janela, values=estados_brasileiros)
combobox_estado.grid(row=7, column=3, padx=10, pady=10, sticky="NSEW")

label_telefone = tk.Label(text="Telefone")
label_telefone.grid(row=8, column=1, padx=10, sticky="NSEW", columnspan=2, pady=10)

caixa_textotelefone = tk.Entry(width=20)
caixa_textotelefone.grid(row=8, column=3,padx= 10, sticky="NSEW", columnspan=6, pady=10)

label_email = tk.Label(text="Email")
label_email.grid(row=9, column=1, padx=10, sticky="NSEW", columnspan=2, pady=10)

caixa_textoemail = tk.Entry(width=20)
caixa_textoemail.grid(row=9, column=3,padx= 10, sticky="NSEW", columnspan=6, pady=10)

label_tipocliente = tk.Label(text="Tipo de Cliente")
label_tipocliente.grid(row=10, column=1, padx=10, sticky="NSEW", columnspan=2, pady=10)

tipo_cliente = ["Multimarcas", "Grandes Contas"]

combobox_tipocliente = ttk.Combobox(janela, values=tipo_cliente)
combobox_tipocliente.grid(row=10, column=3, padx=10, pady=10, sticky="NSEW")

label_mensagem = tk.Label(text="")
label_mensagem.grid(row=11, column=3, padx=10, sticky="NSEW", columnspan=3, pady=10)

caixa_texto = tk.Text(width=20, height=8)
caixa_texto.grid(row=12, column=0, padx=10, pady=10, sticky="NSEW", columnspan=5)

janela.mainloop()


