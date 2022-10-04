import constant


async def message_builder(ctx, text):
    text = text.replace(
        "\n\n", "\n``````\n"
    ).replace(
        "```\n", "```ansi\n"
    ).replace(
        "[", "[34m["
    ).replace(
        "]", "][0m"
    ).replace(
        "<", "[35m<"
    ).replace(
        ">", ">[0m"
    ).replace(
        "  ", " "
    )
    text = "\n> ".join(text.split("\n"))
    await ctx.send(f"> **{constant.title}**\n> \n> ```ansi\n> {text}```\n> {constant.footer}")
