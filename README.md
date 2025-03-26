
# 📘 Curso de Git - LINCE

Bem-vindo à Pizzaria PINCE! 🍕 Este repositório é um guia para quem está aprendendo Git do zero, com comandos essenciais, analogias divertidas e dicas práticas para trabalhar com controle de versão como um verdadeiro chef de código.
teste 2 oull request
---

## 🚀 Começando

### ✅ Criar uma conta no GitHub
Use o terminal do seu sistema:

- **Windows**
  ```cmd
  start https://github.com/signup
  ```
- **Linux**
  ```bash
  xdg-open https://github.com/signup
  ```
- **macOS**
  ```bash
  open https://github.com/signup
  ```

---

## 🛠️ Instalando o Git

- [Baixar Git para todos os sistemas](https://git-scm.com/downloads)

---

## 📂 Criando uma pasta de trabalho

### Windows:
```cmd
mkdir "%USERPROFILE%\Documents\Aula-Git"
cd "%USERPROFILE%\Documents\Aula-Git"
```

### Linux:
```bash
mkdir -p ~/Documentos/Aula-Git
cd ~/Documentos/Aula-Git
```

### macOS:
```bash
mkdir -p ~/Documents/Aula-Git
cd ~/Documents/Aula-Git
```

---

## 🧠 Fluxo Git Básico

```bash
git init                      # Inicia um repositório Git local
git add .                     # Adiciona todos os arquivos para o stage
git commit -m "Mensagem"      # Faz o commit
git remote add origin URL     # Conecta ao repositório remoto (GitHub)
git push -u origin main       # Envia os commits (use 'master' se for o nome da branch)
```

---

## 🍕 Metáfora da Pizzaria Git

| Git         | Pizzaria             |
|-------------|----------------------|
| Repositório | Livro de receitas    |
| Commit      | Cozinheiro anotando  |
| Branch      | Sabor diferente      |
| Pull Request| Sugestão de receita  |
| Merge       | Mistura dos sabores  |

---

## 🔥 Comandos úteis

### 📌 Saber em qual branch estou
```bash
git branch
```

### ✨ Criar uma nova branch
```bash
git checkout -b nome-da-branch
```

### 🔁 Trocar de branch
```bash
git checkout nome-da-branch
```

### 📋 Ver status do repositório
```bash
git status
```

### 🕘 Ver histórico de commits
```bash
git log
```

### ➕ Adicionar arquivos ao stage
```bash
git add .
```

### ❌ Desfazer mudanças locais
```bash
git checkout nome-do-arquivo
```

### 🔙 Remover arquivo do stage
```bash
git reset nome-do-arquivo
```

### 🌐 Ver repositórios remotos
```bash
git remote -v
```

### 📥 Puxar alterações do remoto
```bash
git pull origin main
```

### 📤 Enviar para o remoto
```bash
git push origin nome-da-branch
```

---

## 💡 Extras

### 🧳 Stash (guardar mudanças temporariamente)
```bash
git stash
```

### 🔁 Recuperar o último stash
```bash
git stash pop
```

---

## 🧪 Desafio Final (Teórico)

> Descreva um fluxo de trabalho em que vários cozinheiros (colaboradores) criam e editam receitas (funcionalidades) ao mesmo tempo, lidando com conflitos e pull-requests, até o Chef (mantenedor) aprovar o merge para o livro de receitas (branch principal).

---

## 👤 Autor

Matheus Lima Castro  
📷 [@hairu.oficial](https://www.instagram.com/hairu.oficial)  
📧 comunicacao@hairu.com.br

---

Feito com 💻 + 🍕 + ☕
# Aula-de-Git