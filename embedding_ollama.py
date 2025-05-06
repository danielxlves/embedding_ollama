import ollama

def gerar_embeddings(texto):
    # Gerar embeddings
    resultado = ollama.embeddings(
        model='nomic-embed-text',
        prompt=texto
    )
    
    # Extrair vetor
    vetor = resultado['embedding']
    
    # Exibir resultados
    print(f"Texto: {texto}")
    print(f"\nTamanho do vetor: {len(vetor)} dimensões")
    print("\nPrimeiros 10 elementos do vetor:")
    print(vetor[:10])

if __name__ == "__main__":
    texto = "Ollama é incrível para gerar embeddings locais!"
    gerar_embeddings(texto)