programa {
  funcao inicio() {
    inteiro num1, num2, num3, media
    caracter aluno
    escreva ("Qual e o nome do aluno? ")
    leia (aluno)
    escreva ("Digite a nota do primeiro trimestre: ")
    leia (num1)
    escreva ("Digite a nota do segundo trimestre: ")
    leia (num2)
    escreva ("Digite a nota do terceiro trimestre: ")
    leia (num3)
    media = (num1+num2+num3)/3
    escreva ("O aluno ",aluno," teve a média de ",media)
  }
}
