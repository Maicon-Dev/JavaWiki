# JavaWiki Bot

Bot Discord para fornecer builds de classes em salas privadas temporárias.

## Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/JavaWiki.git
   cd JavaWiki
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   - Copie `.env.example` para `.env`
   - Preencha com seu token do Discord:
     ```
     DISCORD_TOKEN=seu_token_aqui
     ```

4. **Configure o builds.json:**
   - Edite o arquivo `builds.json` com suas builds e configurações

5. **Execute o bot:**
   ```bash
   python main.py
   ```

## Hospedagem Online

### Heroku
1. Crie uma conta no [Heroku](https://heroku.com)
2. Instale o Heroku CLI
3. Faça login: `heroku login`
4. Crie um app: `heroku create seu-app-nome`
5. Configure a variável de ambiente:
   ```bash
   heroku config:set DISCORD_TOKEN=seu_token_aqui
   ```
6. Faça deploy:
   ```bash
   git push heroku main
   ```

### Railway
1. Crie uma conta no [Railway](https://railway.app)
2. Conecte seu repositório GitHub
3. Configure a variável `DISCORD_TOKEN` nas configurações do projeto
4. Faça deploy automático

### Outras opções
- Replit
- DigitalOcean App Platform
- AWS EC2 (mais complexo)

## Comandos

- `/build classe`: Cria uma sala privada com a build da classe especificada

## Configuração do builds.json

O arquivo `builds.json` contém:
- `configBot`: Configurações do bot (canal permitido)
- `layout`: Ícones para os itens
- `classes`: Builds das classes disponíveis

Adicione novas classes seguindo o formato existente.