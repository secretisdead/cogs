from random import choice

import discord
from discord.ext import commands

class thanks:
	"""thanks videos"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def thanks(self):
		msg = choice([
			'https://youtu.be/5IXQ6f6eMxQ',
			'https://youtu.be/j6hOgysWIpw',
			'https://youtu.be/__HtpD02s0g',
			'https://youtu.be/t0O03rtm1jY',
			'https://youtu.be/OnFbsxS-thw',
			'https://youtu.be/mNFx28NGLfI',
			'https://youtu.be/Ora35AzLxt0',
			'https://youtu.be/gJdDRkQLOds',
			'https://youtu.be/YhWmboM0zFc',
			'https://youtu.be/_r9N97aAqqg',
			'https://youtu.be/iXYmFqEkCGQ',
			'https://youtu.be/VgqEHBqnyZA',
			'https://youtu.be/wh4PynUp3Sw',
			'https://youtu.be/YCeQLeQiRP4',
			'https://youtu.be/1XALVTzMOeQ',
			'https://youtu.be/jQmlVEBQYig',
			'https://youtu.be/q6EoRBvdVPQ',
			'https://youtu.be/8YWl7tDGUPA',
			'https://youtu.be/SBeYzoQPbu8',
			'https://youtu.be/ixQkcuZhXg8',
			'https://youtu.be/8J5OnxHsGuo',
			'https://youtu.be/32nkdvLq3oQ',
			'https://youtu.be/GzgavGowD_A',
			'https://youtu.be/1Bix44C1EzY',
			'https://youtu.be/SunaZVRxHcs',
			'https://youtu.be/vkqiC4KPeDs',
			'https://youtu.be/zFCl-g_P9v8',
			'https://youtu.be/I2nLiVo74IQ',
			'https://youtu.be/2Ch_TYmGKlY',
			'https://youtu.be/Ppm5_AGtbTo',
			'https://youtu.be/y4Aw9OdyZ6s',
			'https://youtu.be/cbahtFbIkbA',
			'https://youtu.be/g1Og5Tg_Jyo',
			'https://youtu.be/IFfLCuHSZ-U',
			'https://youtu.be/6gYBXRwsDjY',
			'https://youtu.be/hrUsfyVmeKg',
		])
		await self.bot.say(msg)
		
def setup(bot):
	bot.add_cog(thanks(bot))
