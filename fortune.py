import math
from random import choice

import discord
from discord.ext import commands
from .utils.chat_formatting import *

class fortunes:
	"""port of imageboard style fortunes from notsecret irc bot"""

	def __init__(self, bot):
		self.bot = bot

	fortunes = [
		'Bad Luck',
		'Average Luck',
		'Good Luck',
		'Excellent Luck',
		'Reply hazy, try again',
		'Godly Luck',
		'Very Bad Luck',
		'Outlook good',
		'Better not tell you now',
		'You will meet a dark handsome stranger',
		'ｷﾀ━━━━━━(ﾟ∀ﾟ)━━━━━━ !!!!',
		'（　´_ゝ`）ﾌｰﾝ',
		'Good news will come to you by mail',
		'It\'s a secret to everybody',
		'Bad luck and extreme misfortune will infest your pathetic soul for all eternity',
		'404 fortune not found',
		'Don\'t look',
		'Never draw',
		'Never go outside',
		'（´・ω・｀）',
		'ʕ •ᴥ• ʔ',
		'I\'ll hear it directly thanks',
		'Thanx :(',
		'Whoever deserves it will get it',
		'horse',
		'Oh Shit',
		'You died',
		'You\'ve grown an inch',
		'You\'ve shrunk an inch',
		'O-oooooooooo AAAAE-A-A-I-A-U- JO-oooooooooooo AAE-O-A-A-U-U-A- E-eee-ee-eee AAAAE-A-E-I-E-A- JO-ooo-oo-oo-oo EEEEO-A-AAA-AAAA',
		'Huh',
		'╰U╯',
		'weehaw',
	]

	def random_fortune(self):
		total_fortunes = len(self.fortunes)

		fortune = choice(self.fortunes)
		fortune_index = self.fortunes.index(fortune)

		c = (2 * math.pi * fortune_index / total_fortunes)
		r = int(127 + 127 * math.sin(c))
		g = int(127 + 127 * math.sin(c + (2 / 3 * math.pi)))
		b = int(127 + 127 * math.sin(c + (4 / 3 * math.pi)))
		color = int('0x{:02X}{:02X}{:02X}'.format(r, g, b), 16)

		return (fortune, color)

	@commands.command(pass_context=True)
	async def fortune(self, ctx):
		fortune, color = self.random_fortune()
		description = 'Your fortune: ' + fortune
		embed = discord.Embed(colour=color, description=description)
		await self.bot.say(embed=embed)

	@commands.command()
	async def housetune(self):
		fortune, color = self.random_fortune()
		description = (
			'┏┓\n' + 
			'┃┃╱╲\n' + 
			'┃╱╱╲╲\n' + 
			'╱╱╭╮╲╲ \n' + 
			'▔▏┗┛▕▔ \n' + 
			'╱▔▔▔▔▔▔▔▔▔▔╲ \n' + 
			'╱╱┏┳┓╭╮┏┳┓ ╲╲ \n' + 
			'▔▏┗┻┛┃┃┗┻┛▕▔\n' + 
			'in this house ' + fortune + '\n' + 
			'╱╱┏┳┓╭╮┏┳┓ ╲╲ \n' + 
			'▔▏┗┻┛┃┃┗┻┛▕▔'
		)
		embed = discord.Embed(colour=color, description=description)
		await self.bot.say(embed=embed)

	@commands.command()
	async def jortune(self):
		fortune, color = self.random_fortune()
		description = (
			'```\n' + 
			'　∧＿∧\n' + 
			' （｡･ω･｡)つ━☆・*。\n' + 
			' ⊂　　 ノ 　　　・゜+.\n' + 
			' 　しーＪ　　　°。+ *´¨)\n' + 
			' 　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨)\n' + 
			' 　　　　　　　　　　(¸.·´ (¸.·’* ' + fortune + ' in jorts' + 
			'```')
		embed = discord.Embed(colour=color, description=description)
		await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(fortunes(bot))
