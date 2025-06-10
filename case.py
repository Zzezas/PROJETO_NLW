class MinhaClasse:
    def __enter__(self):
        print("Entrando no contexto")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo do contexto")
        
with MinhaClasse() as mc:
    print("Dentro do contexto")