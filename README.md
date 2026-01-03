# media_escolar
Exercício de Python em Programação de Computadores - Aula 4 parte 2
Calculadora de Medias G1 e G2

Script em Python para calculo de aprovacao escolar baseado em notas e frequencia.
Funcionamento

O programa solicita:

    Notas de 3 provas (0 a 10).

    Frequencia do aluno (0 a 100).

Regras de Calculo

    Reprovacao por falta: Frequencia abaixo de 75%.

    Aprovacao G1: Media das 3 provas maior ou igual a 7.0.

    Reprovacao G1: Media das 3 provas abaixo de 4.0.

    Recuperacao G2: Media entre 4.0 e 6.9.

    Aprovacao G2: Media entre G1 e G2 maior ou igual a 5.0.

Caracteristicas Tecnicas

    Validacao de dados: O programa exige entradas numericas validas.

    Loops de repeticao: Em caso de nota invalida, o programa solicita o dado novamente.

    Tratamento de excecoes: Impede erros de execucao caso o usuario digite texto.

Execucao

python aprov_escolar.py
