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

- `/build classe`: Cria uma sala privada com a build da classe especificada

## Configuração do builds.json

O arquivo `builds.json` contém:
- `configBot`: Configurações do bot (canal permitido)
- `layout`: Ícones para os itens
- `classes`: Builds das classes disponíveis

Adicione novas classes seguindo o formato existente.
Siga o nome das classes da wiki e em letras minúsculas.
