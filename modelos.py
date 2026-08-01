import google.generativeai as genai

# 1. Substitua pela sua chave de API real que você gerou no Google AI Studio
CHAVE_API = "AIzaSyDBa58Vo9Ixd6cel6p6nxFCXTtbjFOAHQM"

# 2. Configura a biblioteca com a sua chave
genai.configure(api_key=CHAVE_API)

print("Listando os modelos disponíveis para geração de texto/chat...\n")
print("=" * 50)

# 3. Faz a busca e lista os modelos
try:
    for modelo in genai.list_models():
        # Filtra para mostrar apenas os modelos que geram conteúdo (textos/chat)
        if 'generateContent' in modelo.supported_generation_methods:
            print(f"Nome do Modelo: {modelo.name}")
            print(f"Descrição curta: {modelo.description}")
            print("-" * 50)
            
    print("\nBusca concluída com sucesso!")
    
except Exception as e:
    print(f"Ocorreu um erro ao tentar conectar: {e}")
    print("Verifique se a sua chave de API está correta e se você tem conexão com a internet.")