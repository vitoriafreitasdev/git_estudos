# git_estudos
*repositório apenas para estudo do git*

# git_comandos_aprendidos

**Comandos básicos**
*** 

*git commit -m "Comentário" => commitar com comentário
 
*git push => fazer o push pro repositório em rede

*git add filename => adicionar o um arquivo 

*git add . => adicionar diversos arquivos modificados

**Comandos para ver o estado atual e diferença entre commits**
*** 

*git status => verificar status atual

*git difftool HEAD => ver a diferença do código atual e do commit HEAD

*git log => ver histórico dos commit

*git difftool id-commit-mais-antigo id-commit-mais-recente

**Comandos para resetar ou refazer commits ou reverter mudanças**
*** 

*git reset --hard commit_id => resetar para versão daquele commit, a HEAD se torna esse commit 

*git revert -n commit_id => reverter um commit 

*git checkout -- . => reverter mudanças de todos arquivos modificados

*git checkout -- filename => reverte mudanças daquele arquivo

**Comandos para criar um clone de repositório, para fazer merge, criar e deletar branch**
*** 

*git clone link-https => clona um projeto dentro da pasta do diretório atual, não clone um projeto dentro do outro, isso bagunça os repositório no GitHub

*git branch => mostra as branchs 

*git branch branch-name => cria uma branch

*git branch -d branch-name => deletar uma branch

*git checkout branch-name => troca para brach-name

*git merge branch-name => fazer o merge de uma branch dentro da outra

*git checkout -b branch-name => criar nova branch e ir para ela

*git push --set-upstream origin branch-name => da um push na branch para ir para o repositório remoto

**Comandos para mostrar um commit**
*** 

*git show HEAD => vai mostrar o commit da HEAD

*git show id-commit => vai mostrar o commit daquele ID 

_**HEAD - na maioria dos casos se refere ao commit mais recente**_

