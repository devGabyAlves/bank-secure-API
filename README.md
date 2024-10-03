# Back Secure API


## Sobre o Repositório

Este repositório contém um projeto de estudo voltado para a segurança de aplicações, com ênfase em Autenticação JWT e criptografia. O projeto simula uma API para serviços bancários, implementando funcionalidades de registro de contas, login com geração de token JWT, controle de permissões de acesso e edição de saldo de contas bancárias.

## Funcionalidades

### 1. Registro de Conta de Usuário
Neste módulo, o usuário pode registrar uma nova conta bancária. A funcionalidade inclui a criação de uma conta protegida, com senhas criptografadas para garantir a segurança dos dados pessoais.

### 2. Login e Geração de JWT
Esta funcionalidade permite que o usuário faça login na aplicação e obtenha um token JWT (JSON Web Token) como forma de autenticação. O JWT é utilizado para garantir a segurança nas próximas requisições, implementando controle de sessão seguro.

### 3. Controle de Permissões
Após o login, o sistema valida o token JWT para verificar as permissões do usuário. Dependendo do nível de permissão, o usuário pode acessar ou modificar informações sensíveis, como o saldo de sua conta bancária.

### 4. Edição de Saldo
O usuário autenticado pode realizar alterações no saldo da sua conta. Esta funcionalidade demonstra como as operações bancárias são protegidas por meio de autenticação e criptografia, garantindo a integridade e segurança das transações.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/devGabyAlves/back-secure-api.git

2. Navegue até o diretório do projeto:
     ```bash
    cd BankSecure API

3. Instale as dependências do projeto:
    pip install -r requirements.txt

4. Execute a aplicação:
    python run.py

5. Utilize ferramentas como Postman ou Insomnia para testar as requisições à API (ex: registro de conta, login, e edição de saldo).

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos exemplos de segurança para este repositório. Você pode abrir uma issue ou enviar um pull request.


## Licença

Este projeto está licenciado sob os termos da MIT License.

