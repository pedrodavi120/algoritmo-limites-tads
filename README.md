# **Relatório de Análise de Limites de Funções**

**Atividade:** Implementação de um algoritmo para solução e análise de limites de uma função.

## **1\. Proposta**

O objetivo deste trabalho é implementar um algoritmo em uma linguagem de programação que realize a solução e a análise de limites de uma função f(x) quando x tende a um ponto a. O algoritmo deve ser capaz de lidar com substituição direta, identificar e resolver indeterminações, e determinar se o limite é finito, divergente ou inexistente.

## **2\. Implementação**

A linguagem escolhida para a implementação foi **Python**, devido à sua simplicidade e, principalmente, pela disponibilidade da biblioteca **SymPy**.

**SymPy** é uma biblioteca Python para matemática simbólica. Ela permite representar e manipular expressões matemáticas de forma simbólica, em vez de apenas numérica. Isso a torna a ferramenta ideal para calcular limites, pois ela consegue realizar simplificações algébricas, aplicar regras como a Regra de L'Hôpital internamente e lidar com o conceito de infinito de forma nativa.

O algoritmo foi estruturado na função analisar\_limite(funcao\_str, ponto\_str) e agora opera de forma interativa, solicitando ao usuário a função e o ponto a serem analisados. Os passos lógicos da análise são:

1. **Entrada de Dados do Usuário:** O programa solicita a função f(x) e o ponto a.  
2. **Parsing das Entradas:** Converte os dados do usuário para expressões simbólicas do SymPy.  
3. **Tentativa de Substituição Direta:** Tenta substituir x pelo ponto a na função.  
4. **Análise Aprofundada:** Caso a substituição resulte em indeterminação ou infinito, prossegue para uma análise mais robusta.  
5. **Cálculo dos Limites Laterais:** Calcula os limites pela direita e pela esquerda para verificar a existência do limite.  
6. **Conclusão e Exibição:** Apresenta o resultado de forma clara, com uma análise passo a passo do processo.

### **Código-Fonte Completo**

\# \-\*- coding: utf-8 \-\*-  
from sympy import sympify, limit, Symbol, oo, S

def analisar\_limite(funcao\_str, ponto\_str):  
    """  
    Realiza a análise completa do limite de uma função em um determinado ponto.  
    """  
    x \= Symbol('x')  
    try:  
        f \= sympify(funcao\_str)  
        if ponto\_str.lower() \== 'oo':  
            a \= oo  
        elif ponto\_str.lower() \== '-oo':  
            a \= \-oo  
        else:  
            a \= sympify(ponto\_str)  
    except (SyntaxError, TypeError):  
        return f"Erro: A função '{funcao\_str}' ou o ponto '{ponto\_str}' não são válidos."

    resultado\_direto \= f.subs(x, a)  
    analise \= f"Análise do Limite de f(x) \= {f} quando x \-\> {a}\\n"  
    analise \+= "-"\*50 \+ "\\n"  
    analise \+= f"1. Substituição direta: f({a}) \= {resultado\_direto}\\n"

    if resultado\_direto.is\_real:  
        analise \+= "   \-\> O valor é definido e finito. O limite é o próprio valor.\\n"  
        analise \+= f"\\nResultado Final: O limite é {resultado\_direto}.\\n"  
        return analise  
      
    if resultado\_direto is S.NaN:  
        analise \+= "   \-\> Resultado é uma forma indeterminada (ex: 0/0, oo/oo).\\n"  
    else:  
        analise \+= "   \-\> O resultado da substituição é infinito. Verificando a consistência do limite.\\n"

    analise \+= "   \-\> Aplicando procedimentos de cálculo de limite e análise lateral.\\n"

    limite\_principal \= limit(f, x, a)  
    limite\_direita \= limit(f, x, a, dir='+')  
    limite\_esquerda \= limit(f, x, a, dir='-')

    analise \+= "\\n2. Análise dos Limites Calculados:\\n"  
    analise \+= f"   \-\> Limite pela direita (x \-\> {a}+): {limite\_direita}\\n"  
    analise \+= f"   \-\> Limite pela esquerda (x \-\> {a}-): {limite\_esquerda}\\n"

    if limite\_direita \!= limite\_esquerda:  
        analise \+= "   \-\> Como os limites laterais são diferentes, o limite no ponto não existe.\\n"  
        resultado\_final \= "Inexistente"  
    else:  
        analise \+= "   \-\> Os limites laterais são iguais, portanto o limite existe.\\n"  
        resultado\_final \= limite\_principal  
        if resultado\_final.is\_real:  
            analise \+= f"   \-\> O limite é finito e vale: {resultado\_final}\\n"  
        elif resultado\_final \== oo or resultado\_final \== \-oo:  
            analise \+= f"   \-\> O limite diverge para: {resultado\_final}\\n"

    analise \+= f"\\nResultado Final: O limite é {resultado\_final}.\\n"  
    return analise

\# \--- Bloco de Execução Principal Interativo \---  
if \_\_name\_\_ \== "\_\_main\_\_":  
    print("Calculadora de Limites Interativa")  
    print("Digite 'sair' a qualquer momento para fechar o programa.")  
    print("-" \* 30\)

    while True:  
        funcao\_usuario \= input("Digite a função f(x) (ex: (x\*\*2-1)/(x-1)): ")  
        if funcao\_usuario.lower() \== 'sair':  
            break

        ponto\_usuario \= input("Digite o ponto para o qual x tende (ex: 1, 0, oo, \-oo): ")  
        if ponto\_usuario.lower() \== 'sair':  
            break

        print("\\n" \+ "="\*50)  
        resultado \= analisar\_limite(funcao\_usuario, ponto\_usuario)  
        print(resultado)  
        print("="\*50 \+ "\\n")

## **3\. Saídas do Programa (Resultados)**

Como o programa agora é interativo, a seguir são apresentados "prints" de como seriam as saídas para os mesmos exemplos anteriores, demonstrando o funcionamento do algoritmo.

### **Exemplo 1: Substituição Direta**

* **Entrada do Usuário:** x\*\*2 \+ 3\*x \- 1 e 2  
* **Saída:**  
  Análise do Limite de f(x) \= x\*\*2 \+ 3\*x \- 1 quando x \-\> 2  
  \--------------------------------------------------  
  1\. Substituição direta: f(2) \= 9  
     \-\> O valor é definido e finito. O limite é o próprio valor.

  Resultado Final: O limite é 9\.

### **Exemplo 2: Indeterminação 0/0**

* **Entrada do Usuário:** (x\*\*2 \- 4\) / (x \- 2\) e 2  
* **Saída:**  
  Análise do Limite de f(x) \= (x\*\*2 \- 4)/(x \- 2\) quando x \-\> 2  
  \--------------------------------------------------  
  1\. Substituição direta: f(2) \= nan  
     \-\> Resultado é uma forma indeterminada (ex: 0/0, oo/oo).  
     \-\> Aplicando procedimentos de cálculo de limite e análise lateral.

  2\. Análise dos Limites Calculados:  
     \-\> Limite pela direita (x \-\> 2+): 4  
     \-\> Limite pela esquerda (x \-\> 2-): 4  
     \-\> Os limites laterais são iguais, portanto o limite existe.  
     \-\> O limite é finito e vale: 4

  Resultado Final: O limite é 4\.

### **Exemplo 3: Limite no Infinito**

* **Entrada do Usuário:** (2\*x\*\*3 \- x) / (x\*\*3 \+ 50\) e oo  
* **Saída:**  
  Análise do Limite de f(x) \= (2\*x\*\*3 \- x)/(x\*\*3 \+ 50\) quando x \-\> oo  
  \--------------------------------------------------  
  1\. Substituição direta: f(oo) \= nan  
     \-\> Resultado é uma forma indeterminada (ex: 0/0, oo/oo).  
     \-\> Aplicando procedimentos de cálculo de limite e análise lateral.

  2\. Análise dos Limites Calculados:  
     \-\> Limite pela direita (x \-\> oo+): 2  
     \-\> Limite pela esquerda (x \-\> oo-): 2  
     \-\> Os limites laterais são iguais, portanto o limite existe.  
     \-\> O limite é finito e vale: 2

  Resultado Final: O limite é 2\.

### **Exemplo 4: Limite Divergente**

* **Entrada do Usuário:** 1 / x\*\*2 e 0  
* **Saída:**  
  Análise do Limite de f(x) \= 1/x\*\*2 quando x \-\> 0  
  \--------------------------------------------------  
  1\. Substituição direta: f(0) \= zoo  
     \-\> O resultado da substituição é infinito. Verificando a consistência do limite.  
     \-\> Aplicando procedimentos de cálculo de limite e análise lateral.

  2\. Análise dos Limites Calculados:  
     \-\> Limite pela direita (x \-\> 0+): oo  
     \-\> Limite pela esquerda (x \-\> 0-): oo  
     \-\> Os limites laterais são iguais, portanto o limite existe.  
     \-\> O limite diverge para: oo

  Resultado Final: O limite é oo.

## **4\. Conclusão**

O algoritmo implementado em Python com a biblioteca SymPy demonstrou ser eficaz e robusto para a análise de limites. Ele cumpre todos os requisitos da proposta, operando de forma interativa, identificando corretamente os diferentes cenários e fornecendo uma saída clara e comentada sobre o processo de resolução.