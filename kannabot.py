
import discord
from discord.ext import commands
#import random

# Database

# yes_rep = ["C'est une certitude.", "Ma réponse est oui !",
#           "Évidemment.", "J'en suis sûr et certain.", "Affirmatif camarade !"]

# no_rep = ["Négatif camarade !", "Je ne pense pas que ce soit le cas.",
#          "C'est non.", "Pas du tout !", "Je désapprouve."]

# Initialisation du bot


bot = commands.Bot(command_prefix="-", description="Kanna Bot")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('la version testing'))


# Commandes

print("Ready 0")


@bot.command()
async def ping(ctx):
    print("I am here !")
    await ctx.message.reply("**Je suis là !**")

'''
print("Ready 1")


@bot.command()
async def clean(ctx, *arg):
    if arg == ():
        await ctx.channel.send("**Veuillez entrer le nombre de messages à nettoyer !**")
    else:
        messages = await ctx.channel.history(limit=int(arg[0]) + 1).flatten()
        for each_msg in messages:
            await each_msg.delete()
        await ctx.channel.send(f"**{int(arg[0])} messages cleaned !**", delete_after=5)

print("Ready 2")


@bot.command()
async def question(ctx, *arg):
    if arg == ():
        await ctx.channel.send("**Veuillez entrer une question !**")

    else:
        switch = 0
        for i in arg:
            if i == '?':
                switch = 1

        if switch == 1:
            alea = random.randint(1, 100)
            alea2 = random.randint(0, 4)

            if alea > 50:
                answer = yes_rep[alea2]
            else:
                answer = no_rep[alea2]
            await ctx.message.reply(answer)
        else:
            await ctx.channel.send("**Vous ne savez pas faire une question ?**")

print("Ready 3")


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été donné."):
    await ctx.guild.ban(user, reason=reason)

    embed = discord.Embed(title="**Bannissement**",
                          description=f"{user.name} a été banni !", color=000000)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/955633376075874344/952598944528072794.png")
    embed.add_field(name="Raison", value=reason, inline=True)
    # embed.set_footer(text = "Est-ce que je mets qlq chose là ?")    // texte en bas du embed

    await ctx.send(embed=embed)

print("Ready 4")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.User, *, reason="Aucune raison n'a été donné"):
    await ctx.guild.unban(user, reason=reason)

    embed = discord.Embed(title="**Débannissement**",
                          description=f"{user.name} a été débanni !", color=000000)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/955978194819883008/955976022749249576.png")
    embed.add_field(name="Raison", value=reason, inline=True)

    await ctx.send(embed=embed)

print("Ready 5")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, reason="Aucune raison n'a été donné"):
    await ctx.guild.kick(user, reason=reason)

    embed = discord.Embed(
        title="**Exclu**", description=f"{user.name} a été expulsé !", color=000000)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/956333889603903498/tokyo-revengers-png-29.png")
    embed.add_field(name="Raison", value=reason, inline=True)

    await ctx.send(embed=embed)

print("Ready 6")


async def createdMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name="muted", permissions=discord.Permissions(send_messages=False, speak=False, add_reactions=False), reason="Création du rôle muted")

    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages=False, speak=False, add_reactions=False)
    return mutedRole

print("Ready 7")


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "muted":
            return role

    return await createdMutedRole(ctx)

print("Ready 8")


@bot.command()
@commands.has_any_role("⌜Owner⌝", "⌜Co owner⌝", "⌜Administrateur⌝", "⌜Modérateur⌝", "⌜Modérateur test⌝")
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été donné"):
    muted_role = await getMutedRole(ctx)
    await member.add_roles(muted_role, reason=reason)

    embed = discord.Embed(
        title="**Muted**", description=f"{member.name} a été mute !", color=000000)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/956334711049977866/tokyo-revengers-png-34.png")
    embed.add_field(name="Raison", value=reason, inline=True)

    await ctx.send(embed=embed)

print("Ready 9")


@bot.command()
@commands.has_any_role("⌜Owner⌝", "⌜Co owner⌝", "⌜Administrateur⌝", "⌜Modérateur⌝", "⌜Modérateur test⌝")
async def unmute(ctx, member: discord.Member, *, reason="Aucune raison n'a été donné"):
    muted_role = await getMutedRole(ctx)
    await member.remove_roles(muted_role, reason=reason)

    embed = discord.Embed(
        title="**Unmuted**", description=f"{member.name} a été unmute !", color=000000)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/950176106592501760/956345838576238592/IMG_20220324_011637.png")
    embed.add_field(name="Raison", value=reason, inline=True)

    await ctx.send(embed=embed)

print("Ready 10")
'''
# Lancement

bot.run("OTU1MjM2MTcyMzExOTgyMjAw.YjevAg.eUiu6tczT5MwK2x1ef7FVYfElHM")
