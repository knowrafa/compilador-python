# Analisador Léxico

O Analisador Léxico, também chamado de Scanner, é o pontapé inicial para o desenvolvimento de um compilador. Ele realiza a leitura de um programa fonte caractere a caractere juntando-os em unidades atômicas chamadas de `itens léxicos`. Ao final do processamento, o AL deve realizar uma classificação funcional das palavras de uma linguagem.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina a linguagem Python 3. Abaixo estão os tutoriais de como realizar a instalação em cada OS:
* Se for usuário de Windows: [Python3](https://www.python.org/download/releases/3.0/); 
* Se for usuário de Linux: [Python3](https://python.org.br/instalacao-linux/);
* Se for usuário de MacOs: [Python3](https://python.org.br/instalacao-mac/).

Além disto é bom ter um editor ou IDE para trabalhar com o código como o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/)

## 🔨 Instalação

1. Criando um Ambiente Virtual:
- Em seu terminal siga os seguintes passos:
```python

pip3 install virtualenv

virtualenv compilador-venv

source compilador-venv/bin/activate (Linux/MacOs)
```
 - Depois, é preciso instalar os pacotes usados no projeto usando o comando:
 ```bash
  pip install -r requirements.txt
 ```
2. Abrindo e rodando o projeto:
- No PyCharm siga o caminho: File > Open e então localize em seu computador onde reservou a pasta com os arquivos;
- Após importar o projeto, é possível ver na barra lateral Project, as pastas e os arquivos envolvidos no projeto. Na pasta `compilador` localize o arquivo executar_compilador.py e dê Run;

No terminal você será capaz de ver a saída do programa similar a essa:

![image](https://user-images.githubusercontent.com/40073116/113220784-2c20ef80-925a-11eb-9420-0ed10b655600.png)




## 😃 Autores
Trabalho desenvolvido pelos alunos do curso de Ciência da Computação: [Rafael Alessandro](https://github.com/knowrafa) e [Renata Patrícia](https://github.com/RenataPatricia), para a disciplina de Compiladores 1 do Instituto de Informática da Universidade Federal de Goiás
