import constant


async def message_builder(ctx, text):
    await ctx.send(f"```\n{constant.title}\n\n{text}```")
