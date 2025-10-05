# -*- coding: utf-8 -*-
from sympy import sympify, limit, Symbol, oo, S

def analisar_limite(funcao_str, ponto_str):
    """
    Realiza a análise completa do limite de uma função em um determinado ponto.
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

    resultado_direto = f.subs(x, a)
    analise = f"Análise do Limite de f(x) = {f} quando x -> {a}\n"
    analise += "-"*50 + "\n"
    analise += f"1. Substituição direta: f({a}) = {resultado_direto}\n"

    if resultado_direto.is_real:
        analise += "   -> O valor é definido e finito. O limite é o próprio valor.\n"
        analise += f"\nResultado Final: O limite é {resultado_direto}.\n"
        return analise
    
    # CORREÇÃO APLICADA AQUI: Usar "is S.NaN" em vez de ".is_nan"
    if resultado_direto is S.NaN:
        analise += "   -> Resultado é uma forma indeterminada (ex: 0/0, oo/oo).\n"
    else:
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

# --- Bloco de Execução Principal Interativo ---
if __name__ == "__main__":
    print("Calculadora de Limites Interativa")
    print("Digite 'sair' a qualquer momento para fechar o programa.")
    print("-" * 30)

    while True:
        funcao_usuario = input("Digite a função f(x) (ex: (x**2-1)/(x-1)): ")
        if funcao_usuario.lower() == 'sair':
            break

        ponto_usuario = input("Digite o ponto para o qual x tende (ex: 1, 0, oo, -oo): ")
        if ponto_usuario.lower() == 'sair':
            break

        print("\n" + "="*50)
        resultado = analisar_limite(funcao_usuario, ponto_usuario)
        print(resultado)
        print("="*50 + "\n")

