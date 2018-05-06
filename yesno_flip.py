from random import choice

import discord
from discord.ext import commands

class flip:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def flip(self, ctx, *text):
		"""Flips for a result."""
		result = choice(['YES', 'NO'])
		description = '**' + result + '**'
		if 'YES' == result:
			color = 0x00C0FF
		else:
			color = 0xFF0000
		embed = discord.Embed(colour=color, description=description)
		await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(flip(bot))
