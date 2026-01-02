# Easy Discord Bot Builderによって作成されました！ 製作：@himais0giiiin
# Created with Easy Discord Bot Builder! created by @himais0giiiin!
# Optimized Version

import discord
from discord import app_commands
from discord.ext import commands
from discord import ui
import random
import asyncio
import datetime
import math
import json
import os
import logging

# ロギング設定 (Logging Setup)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True 
intents.voice_states = True

# Botの作成
bot = commands.Bot(command_prefix='!', intents=intents)

# グローバルエラーハンドラー
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    logging.error(f"Command Error: {error}")

# ---JSON操作---
def _load_json_data(filename):
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"JSON Load Error: {e}")
        return {}

def _save_json_data(filename, data):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        logging.error(f"JSON Save Error: {e}")

# --- モーダルクラス ---
class EasyModal(discord.ui.Modal):
    def __init__(self, title, custom_id, inputs):
        super().__init__(title=title, timeout=None, custom_id=custom_id)
        for item in inputs:
            self.add_item(discord.ui.TextInput(label=item['label'], custom_id=item['id']))

# --- インタラクションハンドラー ---
@bot.event
async def on_interaction(interaction):
    try:
        if interaction.type == discord.InteractionType.component:
            pass
        elif interaction.type == discord.InteractionType.modal_submit:
            pass
    except Exception as e:
        print(f"Interaction Error: {e}")

# ----------------------------

# --- ユーザー作成部分 ---
@bot.tree.command(name="join", description="join command")
async def join_cmd(interaction: discord.Interaction):
    ctx = interaction
    user = interaction.user

    if 'user' in locals() and user.voice:
        await user.voice.channel.connect()

    if 'ctx' in locals():
        if isinstance(ctx, discord.Interaction):
            if ctx.response.is_done():
                await ctx.followup.send(content='いいよ！こいよ！', ephemeral=True)
            else:
                await ctx.response.send_message(content='いいよ！こいよ！', ephemeral=True)
        elif isinstance(ctx, commands.Context):
            await ctx.send(content='いいよ！こいよ！')
        elif isinstance(ctx, discord.Message):
            await ctx.reply(content='いいよ！こいよ！')


@bot.tree.command(name="disconnect", description="disconnect command")
async def disconnect_cmd(interaction: discord.Interaction):
    ctx = interaction
    user = interaction.user

    if 'ctx' in locals() and ctx.guild.voice_client:
        await ctx.guild.voice_client.disconnect()

    if 'ctx' in locals():
        if isinstance(ctx, discord.Interaction):
            if ctx.response.is_done():
                await ctx.followup.send(content='いいよ！こいよ！', ephemeral=True)
            else:
                await ctx.response.send_message(content='いいよ！こいよ！', ephemeral=True)
        elif isinstance(ctx, commands.Context):
            await ctx.send(content='いいよ！こいよ！')
        elif isinstance(ctx, discord.Message):
            await ctx.reply(content='いいよ！こいよ！')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    ctx = message
    user = message.author
    if '114514' in (ctx.content if "ctx" in locals() and hasattr(ctx, "content") else ""):

        if 'ctx' in locals():
            if isinstance(ctx, discord.Interaction):
                if ctx.response.is_done():
                    await ctx.followup.send(content='いいよ！こいよ！', ephemeral=True)
                else:
                    await ctx.response.send_message(content='いいよ！こいよ！', ephemeral=True)
            elif isinstance(ctx, commands.Context):
                await ctx.send(content='いいよ！こいよ！')
            elif isinstance(ctx, discord.Message):
                await ctx.reply(content='いいよ！こいよ！')

        if 'ctx' in locals() and ctx.guild.voice_client:
            if not ctx.guild.voice_client.is_playing():
                ctx.guild.voice_client.play(discord.FFmpegPCMAudio('E:\\discord_bot\\iiyokoiyo.mp3'))
    await bot.process_commands(message)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    ctx = message
    user = message.author
    if '114514' in (ctx.content if "ctx" in locals() and hasattr(ctx, "content") else ""):

        if 'ctx' in locals():
            if isinstance(ctx, discord.Interaction):
                if ctx.response.is_done():
                    await ctx.followup.send(content='いいよ！こいよ！', ephemeral=True)
                else:
                    await ctx.response.send_message(content='いいよ！こいよ！', ephemeral=True)
            elif isinstance(ctx, commands.Context):
                await ctx.send(content='いいよ！こいよ！')
            elif isinstance(ctx, discord.Message):
                await ctx.reply(content='いいよ！こいよ！')

        if 'ctx' in locals() and ctx.guild.voice_client:
            if not ctx.guild.voice_client.is_playing():
                ctx.guild.voice_client.play(discord.FFmpegPCMAudio('E:\\discord_bot\\iiyokoiyo.mp3'))
    await bot.process_commands(message)



# --------------------------
if __name__ == "__main__":
    # Token check
    # bot.run('TOKEN') # 実行時はここにTokenを入れてください!
    bot.run(os.environ["DISCORD_TOKEN"])  # 実行時はここにTokenを入れてください!
    pass
