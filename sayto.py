import discord
from discord.ext import commands
from .utils import checks

class sayto:
	"""say to a channel from another channel"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@checks.mod_or_permissions(manage_server=True)
	async def sayto(self, channel : discord.Channel, message):
		await self.bot.send_message(channel, message)

def setup(bot):
	bot.add_cog(sayto(bot))
