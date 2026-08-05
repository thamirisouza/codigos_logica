''' Criar coleção de materiais '''

produtos = [{"nome": "Argamassa", 
            "codigo" : "A001",
            "preco" : 50.00,
            "quantidade" : 10,
            "categoria" : "Materiais básicos"
            },

            {"nome": "Porta", 
            "codigo" : "P002",
            "preco" : 450.00,  
            "quantidade" : 5,
            "categoria" : "Marcenária"
           },

            {"nome": "Tinta",
            "codigo" : "T003",
            "preco" : 25.00,   
            "quantidade" : 20,
            "categoria" : "Pintura"
           } ,

            {"nome": "Furadeira",
            "codigo" : "F004",    
            "preco" : 150.00,
            "quantidade" : 8,
            "categoria" : "Ferramentas"
           },
]  

print()

# Todos os produtos
print(produtos)

for produto in produtos:
    print(f"{produto["nome"]} - R${produto["preco"]}")




