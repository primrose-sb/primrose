from discord.ext import commands


class MiscellaneousCog(commands.Cog, name="clap command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="clap",
        usage="<text>",
        description="replaces spaces with clap emoji"
    )
    async def fmessage(self, ctx: commands.context, *, text: str):
        await ctx.send('👏'.join(text.split()))
