# git_estudos
*repositório apenas para estudo do git*

# git_comandos_aprendidos

**Comandos básicos**
*** 
* git init => para iniciar um repositório local no diretório atual 

* git remote add origin <link-https> => para depois integrar ap repositório remoto do github

* git add -A => Adiciona arquivos novos, modificados e deletados de todo o repositório

* git commit -m "Comentário" => commitar com comentário
 
* git push => fazer o push pro repositório em rede

* git add filename => adicionar um arquivo 

* git add . => adicionar diversos arquivos 

* git push origin main

* git pull origin 

**Exemplo de push com -u**

# 1. Novo projeto local (sem remote)
git init
git add .
git commit -m "Primeiro commit"

# 2. Criou repositório no GitHub (vazio)

# 3. Adiciona remote
git remote add origin https://github.com/usuario/repo.git

# 4. PRIMEIRO PUSH do branch main:
git push -u origin main
# ↑↑↑ OBRIGATÓRIO! Configura upstream

# 5. Cria novo branch:
git checkout -b feature/nova

# 6. PRIMEIRO PUSH deste novo branch:
git push -u origin feature/nova
# ↑↑↑ OBRIGATÓRIO de novo!

**Para remover o .git**
* rm -rf .git

**Comandos para ver o estado atual e diferença entre commits**
*** 

* git status => verificar status atual

* git difftool HEAD => ver a diferença do código atual e do commit HEAD

* git log => ver histórico dos commit

* git difftool id-commit-mais-antigo id-commit-mais-recente

* git difftool HEAD~2 HEAD~1git difftool HEAD~2 HEAD~1 => HEAD~2 significa o commit antes do anterior da HEAD, HEAD~1 significa commit anterior da HEAD, então HEAD~NUMERO é igual a HEAD menos aquele NUMERO

* git difftool HEAD~1 HEAD => vai mostrar a diferença entre o commit anterior a HEAD e a HEAD


**Comandos para resetar ou refazer commits ou reverter mudanças**
*** 

* git reset --hard commit_id => resetar para versão daquele commit, a HEAD se torna esse commit 

* git revert -n commit_id => reverter um commit 

* git checkout -- . => reverter mudanças de todos arquivos modificados

* git checkout -- filename => reverte mudanças daquele arquivo

**Comandos para criar um clone de repositório**
*** 

* git clone link-https => clona um projeto dentro da pasta do diretório atual, não clone um projeto dentro do outro, isso bagunça os repositório no GitHub

* git clone <url> <diretório-destino> => Clona o repositório para um diretório específico que você nomeou. Se a pasta já existir, ocorrerá erro (a menos que esteja vazia)

* git clone <url> . => Clona o repositório diretamente no diretório atual. Sobrescreve o diretório atual se não estiver vazio (Git pede confirmação). Útil apenas quando você está em um diretório vazio e quer clonar ali

* git clone https://github.com/usuario/repo.git backend => Baixa o repositório do GitHub e cria uma nova pasta chamada backend no diretório atual

* git clone https://github.com/usuario/repo.git "C:\projeto_sistema" => Cria a pasta projeto_sistema na raiz do drive C:\ se ela não existir

* git clone https://github.com/usuario/repo.git "C:\projeto_sistema\repo" => Isso criará uma subpasta 'repo' dentro de 'projeto_sistema'

**Exemplo**

# 1. Entre na pasta existente
cd "C:\projeto_sistema"

# 2. Crie uma subpasta para o clone
git clone https://github.com/usuario/repo.git codigo-fonte

**Para fazer merge, criar e deletar branch**

* git branch -a => mostra todas as branchs do repositório 

* git branch => mostra as branchs 

* git branch branch-name => cria uma branch

* git branch -d branch-name => deletar uma branch

* git checkout branch-name => troca para brach-name

* git merge branch-name => fazer o merge de uma branch dentro da outra

* git checkout -b branch-name => criar nova branch e ir para ela

* git push --set-upstream origin branch-name => da um push na branch para ir para o repositório remoto

**Comandos para mostrar um commit**
*** 

* git show HEAD => vai mostrar o commit da HEAD

* git show id-commit => vai mostrar o commit daquele ID 

_**HEAD - na maioria dos casos se refere ao commit mais recente. Quando não aponta para o mais recente commit, você entra no estado da HEAD Detached**_

* git checkout id-commit => vai para o commit daquele id, assim a HEAD estará desanexada. Para voltar, pode dar git checkout main, assim voltando para main

* git checkout -b novo_teste id-commit => Cria um novo branch a partir do commit antigo e muda para ele. Assim você consegue explorar um commit antigo sem criar HEAD Detached. Podendo fazer testes e alterações e depois, se quiser fazer um merge. É provavel que tenha lidar com conflitos, adicionar as mudanças com git add e depois commitar elas, para enfim finalizar o merge.

**valores de configurações**

* git config --global user.name "Seu Nome" => para configurar seu nome 

* git config --global user.email "seu_email@gmail.com" => para configurar seu email 

* git config --list => lista de 

**Para ajuda**

* git help <verb> => Exemplo: git help config 
* git <verb> --help => Exemplo git config --help

**Git verbs (verbos Git)**  

* São os comandos que usamos na linha de comando. Como por exemplo o add, commit, push e config. São verbos imperativos que mandam o git realizar alguma ação.

**Comandos para verificar repositório remoto**

* git remote -v
