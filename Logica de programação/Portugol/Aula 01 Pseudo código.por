programa {
  funcao inicio() {
    // comentario de linha 
    // declarando variaves do tipo imteiro
    inteiro num1, num2
    //declarando as variaves
    //mostrando na tela
    escreva ("Digite um numero qualquer: ")
    // leitura de variavel
    leia (num1)
    /*
    comentario
    de
    bloco
    */
    escreva ("Digite outro numero qualquer: ")
    leia (num2)

    real soma 
    soma = num1 + num2

    // concadenação
    escreva ("o resultado da soma de ",num1," + ",num2," é: ",soma)
    escreva ("\npular linha")

    /* Operadores matemáticos 
    ** =exponenciação
    //= divisão inteira
    == -> compaação
    */

    real sub, multi, div, modulo
    sub= num1-num2
    multi= num1*num2
    div= num1/num2 
    modulo = num1 % num2
    escreva ("\nResultado da subtração: ",sub)
    escreva ("\nResultado da multiplicação: ",multi)
    escreva ("\nResultado da divisão: ",div)
    escreva ("\nResultado do resto da divisão: ",modulo)

    /* OPERADORES ARITIMÉTICOS 
    +  -> soma
    -  -> subtração
    /  -> divição comum
    // -> divisão inteira 
    *  -> multiplicação
    ** -> exponenciação
    %  -> modulo de divisão
    */

    /*OPERADORES DE COMPARAÇÃO
    >= -> maior igual
    <= -> menor igual
    != -> diferente
    == -> igual
    >  -> maior
    <  -> menor
    */

    /*OPERADORES DE ATRIBUIÇÃO
    =  : atribuição de valores
    += : inclementa
    -= : declementa
    *= : multiplicar pelo valor
    /= : dividir pelo valor
    */

    /*OPERADORES LÓGICOS 
    AND,&& : faz o papel conectivo E (as duas preposições pecisam ser verdadeiras para o resultado ser verdadeiro)
    OR,||  : faz o papel do conectuvo "OU" (ua ou outra presisa ser verdadeira para o resulatado ser verdadeiro)
    NOT,!  :faz o papel do conectivo "NÃO"(onde ele irá negar uma preposição)
    */
  }
}
