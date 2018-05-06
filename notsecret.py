import discord
from discord.ext import commands
from .utils import checks

class notsecret:
	"""port of miscellaneous commands from notsecret irc bot"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def echo(self, message):
		await self.bot.say(message)

	@commands.command()
	async def echo_embed(self, description, color=0x00C0FF):
		embed = discord.Embed(colour=color, description=description)
		await self.bot.say(embed=embed)

	@commands.command()
	async def idm(self):
		msg = 'https://scdn.cloud/9HX8bWWuCHKwVfMRlKDmUQ.jpg'
		await self.bot.say(msg)

	@commands.command()
	async def nice(self):
		msg = 'https://scdn.cloud/39OLR_vsrx8aORL08PdlJQ.gif'
		await self.bot.say(msg)

	@commands.command()
	async def streetmeat(self):
		msg = 'https://scdn.cloud/OBLlyfgGb5T5i6J031aXcQ.jpg'
		await self.bot.say(msg)

	@commands.command()
	async def hotdog(self):
		msg = 'https://scdn.cloud/kVTHSOzWvuYqlV2mVoDCvg.webm'
		await self.bot.say(msg)

	@commands.command()
	async def godtoh(self):
		msg = 'https://scdn.cloud/KinnCjK99F-De84IYkjgzw.mp4'
		await self.bot.say(msg)

	@commands.command()
	async def mermeldog(self):
		msg = 'https://scdn.cloud/UgoSnIqKWCPk4H4f8bxKPw.jpg'
		await self.bot.say(msg)

	@commands.command()
	async def mermeldoghd(self):
		msg = 'https://scdn.cloud/9LPuR7ZnPufHpgOFeSbjHQ.jpg'
		await self.bot.say(msg)

	@commands.command()
	async def draw(self):
		msg = 'https://i.scdn.cloud/PsodgziGjKtS6_jfvMnTjw.jpg'
		await self.bot.say(msg)

	@commands.command()
	async def jorts(self):
		msg = (
			'```\n' + 
			'　∧＿∧\n' + 
			' （｡･ω･｡)つ━☆・*。\n' + 
			' ⊂　　 ノ 　　　・゜+.\n' + 
			' 　しーＪ　　　°。+ *´¨)\n' + 
			' 　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨)\n' + 
			' 　　　　　　　　　　(¸.·´ (¸.·’* kevin smith huge jorts' + 
			'```'
		)
		embed = discord.Embed(colour=0x00C0FF, description=msg)
		await self.bot.say(embed=embed)

	@commands.command()
	async def frogs(self):
		msg = (
			'┏┓\n' + 
			'┃┃╱╲\n' + 
			'┃╱╱╲╲\n' + 
			'╱╱╭╮╲╲ \n' + 
			'▔▏┗┛▕▔ \n' + 
			'╱▔▔▔▔▔▔▔▔▔▔╲ \n' + 
			'╱╱┏┳┓╭╮┏┳┓ ╲╲ \n' + 
			'▔▏┗┻┛┃┃┗┻┛▕▔\n' + 
			'in this house we love frogs\n' + 
			'╱╱┏┳┓╭╮┏┳┓ ╲╲ \n' + 
			'▔▏┗┻┛┃┃┗┻┛▕▔'
		)
		embed = discord.Embed(colour=0x00C0FF, description=msg)
		await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(notsecret(bot))
