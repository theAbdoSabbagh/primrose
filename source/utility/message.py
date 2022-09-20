import constant


async def message_builder(bot, text):
    await bot.send(f"```\n{constant.title}\n\n{text}```")
