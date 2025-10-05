# -*- coding: utf-8 -*-
"""
Algoritmo para Solução e Análise de Limites de uma Função
"""
from sympy import sympify, limit, Symbol, oo, S

def analisar_limite(funcao_str, ponto_str):
    """
    Realiza a análise completa do limite de uma função em um determinado ponto.

    Args:
        funcao_str (str): A função f(x) como uma string. Ex: "1/x", "(x**2 - 1)/(x - 1)"
        ponto_str (str): O ponto 'a' para o qual x tende. Pode ser um número, "oo" (infinito)
                         ou "-oo" (infinito negativo).

    Returns:
        str: Uma string contendo a análise detalhada do limite.
    """
    x = Symbol('x')

    try:
        f = sympify(funcao_str)

        if ponto_str.lower() == 'oo':
            a = oo
        elif ponto_str.lower() == '-oo':
            a = -oo
        else:
            a = sympify(ponto_str)

    except (SyntaxError, TypeError):
        return f"Erro: A função '{funcao_str}' ou o ponto '{ponto_str}' não são válidos."

    # --- Análise do Limite ---

    resultado_direto = f.subs(x, a)
    analise = f"Análise do Limite de f(x) = {f} quando x -> {a}\n"
    analise += "-"*50 + "\n"
    analise += f"1. Substituição direta: f({a}) = {resultado_direto}\n"

    # Se a substituição direta já dá um número real finito, podemos parar.
    if resultado_direto.is_real:
        analise += "   -> O valor é definido e finito. O limite é o próprio valor.\n"
        analise += f"\nResultado Final: O limite é {resultado_direto}.\n"
        return analise
    
    if resultado_direto.is_nan:
        analise += "   -> Resultado é uma forma indeterminada (ex: 0/0, oo/oo).\n"
    else: # Casos como 1/0
        analise += "   -> O resultado da substituição é infinito. Verificando a consistência do limite.\n"

    analise += "   -> Aplicando procedimentos de cálculo de limite e análise lateral.\n"

    limite_principal = limit(f, x, a)
    limite_direita = limit(f, x, a, dir='+')
    limite_esquerda = limit(f, x, a, dir='-')

    analise += "\n2. Análise dos Limites Calculados:\n"
    analise += f"   -> Limite pela direita (x -> {a}+): {limite_direita}\n"
    analise += f"   -> Limite pela esquerda (x -> {a}-): {limite_esquerda}\n"

    if limite_direita != limite_esquerda:
        analise += "   -> Como os limites laterais são diferentes, o limite no ponto não existe.\n"
        resultado_final = "Inexistente"
    else:
        analise += "   -> Os limites laterais são iguais, portanto o limite existe.\n"
        resultado_final = limite_principal
        if resultado_final.is_real:
            analise += f"   -> O limite é finito e vale: {resultado_final}\n"
        elif resultado_final == oo or resultado_final == -oo:
            analise += f"   -> O limite diverge para: {resultado_final}\n"

    analise += f"\nResultado Final: O limite é {resultado_final}.\n"
    return analise


# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    # Exemplo 1: Substituição Direta
    print("--- Exemplo 1: Substituição Direta ---")
    resultado1 = analisar_limite("x**2 + 3*x - 1", "2")
    print(resultado1)

    # Exemplo 2: Indeterminação 0/0 (com simplificação)
    print("\n--- Exemplo 2: Indeterminação 0/0 ---")
    resultado2 = analisar_limite("(x**2 - 4) / (x - 2)", "2")
    print(resultado2)

    # Exemplo 3: Limite no Infinito
    print("\n--- Exemplo 3: Limite no Infinito ---")
    resultado3 = analisar_limite("(2*x**3 - x) / (x**3 + 50)", "oo")
    print(resultado3)

    # Exemplo 4: Limite Divergente
    print("\n--- Exemplo 4: Limite Divergente para Infinito ---")
    resultado4 = analisar_limite("1 / x**2", "0")
    print(resultado4)

    # Exemplo 5: Limite Inexistente (laterais diferentes)
    print("\n--- Exemplo 5: Limite Inexistente ---")
    resultado5 = analisar_limite("1 / x", "0")
    print(resultado5)

    # Exemplo 6: Limite com função trigonométrica (limite fundamental)
    print("\n--- Exemplo 6: Limite Trigonométrico Fundamental ---")
    resultado6 = analisar_limite("sin(x) / x", "0")
    print(resultado6)


