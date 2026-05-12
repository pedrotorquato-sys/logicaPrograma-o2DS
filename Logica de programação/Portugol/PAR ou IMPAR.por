programa {
  funcao inicio() {
    
    /* Dsenvolva um sistema para 
    verificar se o numero é para ou impar*/ 

    inteiro num1
    
   
    escreva ("Digite um numero qualquer: ")
    leia (num1)

    //proposisão
    num1 % 2 == 0

    /*divide o numero por 2,
    verifica se o resto da divisão e 0*/

    //se
    se ( num1 % 2 == 0){
     //a verificação do se,é sempr verdadeiro
     escreva ("Que legal, o numero ",num1," é PAR")
    }
    //senão
    senao{
      escreva ("EITA! o numero ",num1," é IMPAR")
  }
}
}