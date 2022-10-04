from discord.ext import commands


class CodeblockCog(commands.Cog, name="codeblock commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="codeblock",
        usage="<language> <text>",
        description="send a codeblock"
    )
    async def codeblock(self, ctx: commands.context, language: str, *, text: str):
        await ctx.send(f"```{language}\n{text}\n```")
