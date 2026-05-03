import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import json
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)


#CÓDIGO DO BOT 
@bot.tree.command(name="build", description="Gera uma sala privada com a build da classe solicitada.")
@app_commands.describe(classe="Nome da classe (ex: Arch Paladin)")
async def build(interaction: discord.Interaction, classe: str):
    try:
        with open('builds.json', 'r', encoding='utf-8') as file:
            builds_data = json.load(file)
    except Exception as e:
        await interaction.response.send_message(
            "❌ Ocorreu um erro ao carregar as builds. Por favor, tente novamente mais tarde.", 
            ephemeral=True
        )
        print(f"Erro ao ler builds.json: {e}")
        return
    allowed_channel_name = builds_data.get("configBot", {}).get("allowedChannelName", "builds")
    # 1. VERIFICAR O CANAL
    if interaction.channel.name.lower() != allowed_channel_name.lower():
        await interaction.response.send_message(
            f"❌ Este comando só pode ser usado no canal #{allowed_channel_name}.",
            ephemeral=True
        )
        return
    
    # 2. VERIFICAR A CLASSE E DEFINIR A BUILD
    classe_buscada = classe.lower()

    if classe_buscada in builds_data["classes"]:
        build_info = builds_data["classes"][classe_buscada]
        texto_build = (
            f"**{build_info['name']}**\n"
            f"{builds_data['layout']['weapon_icon']} **Arma/Weapon:** {build_info['weapon']}\n"
            f"{builds_data['layout']['armor_icon']} **Armadura/Armor** {build_info['armor']}\n"
            f"{builds_data['layout']['helmet_icon']} **Elmo/Helmet:** {build_info['helmet']}\n"
            f"{builds_data['layout']['cape_icon']} **Capa/Cape:** {build_info['cape']}"
        ) 
    else:
        await interaction.response.send_message(f'❌ Ainda não tenho uma build para **{classe}**.', ephemeral=True)
        return

    # 3. CONFIGURAR PERMISSÕES DA SALA PRIVADA
    guild = interaction.guild
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True)
    }

    try:
        # 4. CRIAR O CANAL TEMPORÁRIO
        canal_temporario = await guild.create_text_channel(
            name=f"build-{interaction.user.name}",
            overwrites=overwrites
        )
        
        # Confirmação silenciosa para o usuário
        await interaction.response.send_message(
            f'✅ Sua sala privada com a build foi criada: {canal_temporario.mention}', 
            ephemeral=True
        )
        
        # 5. ENVIAR A MENSAGEM DA BUILD NA SALA
        await canal_temporario.send(f'Olá {interaction.user.mention}! Esta sala será excluída em **3 minutos**.\n\n{texto_build}')

        # 6. ESPERAR 3 MINUTOS E DELETAR
        # 3 minutos * 60 segundos = 180 segundos
        await asyncio.sleep(180)
        
        # Deleta o canal após o tempo (verifica se o canal ainda existe para evitar erros)
        if canal_temporario:
            await canal_temporario.delete(reason="Tempo da sala de build expirou")

    except discord.Forbidden:
        await interaction.response.send_message(
            "❌ Não tenho permissão para criar canais neste servidor!", 
            ephemeral=True
        )
    except Exception as e:
        print(f"Erro ao criar a sala: {e}")


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Bot {bot.user} online e comandos sincronizados!')

# Coloque o token do seu bot aqui
token = os.getenv('DISCORD_TOKEN')
if not token:
    print("❌ Erro: DISCORD_TOKEN não definido nas variáveis de ambiente!")
    exit(1)

bot.run(token)