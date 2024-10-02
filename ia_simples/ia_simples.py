import openai

# Função para configurar a chave da API
def configurar_api(chave_api):
    """
    Configura a chave da API OpenAI.
    :param chave_api: String com a chave da API
    """
    openai.api_key = chave_api

# Função para gerar um texto baseado no prompt fornecido
def gerar_texto(prompt, modelo="text-davinci-003", max_tokens=100, temperatura=0.7):
    """
    Gera um texto baseado no prompt fornecido.
    :param prompt: Texto base para a IA responder
    :param modelo: Modelo da OpenAI (ex: 'text-davinci-003', 'gpt-3.5-turbo')
    :param max_tokens: Número máximo de tokens para a resposta
    :param temperatura: Criatividade da resposta, de 0 a 1
    :return: Texto gerado pela IA
    """
    try:
        resposta = openai.Completion.create(
            engine=modelo,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperatura
        )
        return resposta.choices[0].text.strip()
    except Exception as erro:
        return f"Erro ao gerar texto: {erro}"
