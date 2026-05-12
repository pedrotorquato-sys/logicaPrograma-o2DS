programa {
  funcao inicio() {
    escreva ("-------Descubra o seu IMC------")
    cadeia nome
    inteiro idade
    real peso, altura, imc
    escreva ("\nDIgite seu nome: ")
    leia (nome)
    escreva ("\nDigite a sua idade: ")
    leia (idade)
    escreva ("\nDigite seu peso: ")
    leia (peso)
    escreva ("\nDigite sua altura(em centimetros): ")
    leia (altura)
    imc= peso /(altura*altura)
    escreva ("\nOla ",nome,", seja bem vindo")
    escreva ("\nDescobri que você tem ",idade)
    escreva ("\nSeu peso é: ",peso)
    escreva ("\nSua altura é: ",altura)
    escreva ("\nSeu IMC é: ",imc)
  }
}
