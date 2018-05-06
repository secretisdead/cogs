from random import choice

import discord
from discord.ext import commands

class portraits:
	"""port of artistispresent and user portraits from notsecret irc bot"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def artistispresent(self):
		msg = '**CHOOSE**\n\nhttps://flic.kr/s/aHsjqeRWME'
		await self.bot.say(msg)

	@commands.command(aliases=["teatonxasa"])
	async def asaxteaton(self):
		msg = choice([
			'https://scdn.cloud/mODCs-OaheyirvU7VzUFLg.png',
			'https://scdn.cloud/z3jpBhRf0bsCxMeFxbhHMQ.png',
		])
		await self.bot.say(msg)

	@commands.command()
	async def asadirkpc(self):
		msg = choice([
			'https://scdn.cloud/WgZzaalni-TV2ipqfeiNJw.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def partysover(self):
		msg = choice([
			'https://scdn.cloud/-rIxK_Jc2br23YaBf1LDxg.png',
		])
		await self.bot.say(msg)

	@commands.command()
	async def notsecret(self):
		msg = choice([
			'https://scdn.cloud/nGO49lL3xOpFOxfxWApNmg.jpg',
			'https://scdn.cloud/oxRuCa462AO0kSgQ_ZOnfA.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def asa(self):
		msg = choice([
			'https://scdn.cloud/CuXnXYzfDFidDaWBAcPYXg.jpg',
			'https://scdn.cloud/sBACd3CfG4jwNla-vmwevw.jpg',
			'https://scdn.cloud/ITSBAhOH1KEkWNFRDnV0ZA.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def secret(self):
		msg = choice([
			'https://scdn.cloud/IIKtDoFUWneOvt9TeX9ISQ.jpg',
			'https://scdn.cloud/IIKtDoFUWneOvt9TeX9ISQ.jpg',
			'https://scdn.cloud/IIKtDoFUWneOvt9TeX9ISQ.jpg',
			'https://scdn.cloud/IIKtDoFUWneOvt9TeX9ISQ.jpg',
			# weighted
			'https://scdn.cloud/QQcnLJg3RKs35R_GgQxgFQ.jpg',
			'https://scdn.cloud/QQcnLJg3RKs35R_GgQxgFQ.jpg',
			'https://scdn.cloud/QQcnLJg3RKs35R_GgQxgFQ.jpg',
			'https://scdn.cloud/QQcnLJg3RKs35R_GgQxgFQ.jpg',

			'https://scdn.cloud/DUd9Mai-PJ213ffbV8oU7A.jpg',
		])
		await self.bot.say(msg)

	@commands.command(aliases=["paperclip"])
	async def pc(self):
		msg = choice([
			'https://scdn.cloud/xzmOeiiYjiMTK4PeF9q2ug.jpg',
			'https://scdn.cloud/CzSEbqo6h-avQi0UdG2O2g.jpg',
			'https://scdn.cloud/SQ22CPqg3_X2uL-fTe3nnA.jpg',
			'https://scdn.cloud/XRcXp6DxzgTjLsW8Hx45PA.png',
			'https://scdn.cloud/GlTASZvhR7rIOfhxl-v6ng.jpg',
			'https://scdn.cloud/0-SCGtr3B-k2p0TXZ_MPmg.jpg',
			'https://scdn.cloud/MjnRr3T8SVpt5dMBOVlXkw.jpg',
			'https://scdn.cloud/mPPDary9wKCS_0r0imhHTw.mp4',
			'https://scdn.cloud/_SkOSlmZvju9sFXBunCXMQ.mp4',
		])
		await self.bot.say(msg)

	@commands.command(aliases=["evilpaperclip"])
	async def evilpc(self):
		msg = choice([
			'https://scdn.cloud/vyrwaFOj0NVXcxh9y_oopg.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def pcret(self):
		msg = choice([
			'https://scdn.cloud/YV2qwJ6M5MhsdiYcRcFD5A.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def teaton(self):
		msg = choice([
			'https://scdn.cloud/RQYtj6o8YPqIcTSw3bi34g.jpg',
			'https://scdn.cloud/W8c8px_al0wuKDXrDgJ4jg.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def trevor(self):
		msg = choice([
			'https://scdn.cloud/Cde0DdMGoC0PAQcmhL4Xdw.jpg',
			'https://scdn.cloud/89kEe22yd8YsGpfrnl6_OQ.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def dirk(self):
		msg = choice([
			'https://scdn.cloud/UrxvmGETN96Y6xRwUTz1lg.jpg',
		])
		await self.bot.say(msg)

	@commands.command(aliases=["meron"])
	async def melon(self):
		msg = choice([
			'https://scdn.cloud/Ra0c0UkX2U2FPwfaMF2p_Q.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def kalt(self):
		msg = choice([
			'https://scdn.cloud/AWrihAKe0ShnHTcUS4wH_A.jpg',
			'https://scdn.cloud/7yaaiZxMgQzBPaO_30BUQw.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def gij(self):
		msg = choice([
			'https://scdn.cloud/2vRxXBrBQ5YcPsNDoWA3eA.jpg',
			'https://scdn.cloud/S_Ad4Ga5KhjpzNJKEUs8LQ.jpg',
		])
		await self.bot.say(msg)

	@commands.command(aliases=["mort"])
	async def mortikie(self):
		msg = choice([
			'https://scdn.cloud/UhFVqzCi8gjgA6e3nBI09g.jpg',
			'https://scdn.cloud/5UQ-NbOnOSsZkhxwmy4Ysw.jpg',
			'https://scdn.cloud/m9Qm4mWpKMINnA7U1NsKOA.jpg',
			'https://scdn.cloud/jzPFKw8EYUaGX2W4ZLXkTA.webm',
			'https://scdn.cloud/v2sV_1U-5k7pwmShYfSt6w.png',
			'http://youtu.be/zW1uN0SjKPY',
			'https://scdn.cloud/8T-77MuqJhspuXEIaeLQyQ.png',
		])
		await self.bot.say(msg)

	@commands.command(aliases=["del","delstimpson","del_stimpson"])
	async def sammy(self):
		msg = choice([
			'https://scdn.cloud/FNcTZPkmmmwjM3xmpQ2zcA.jpg',
		])
		await self.bot.say(msg)

	@commands.command(aliases=["cuo"])
	async def cuoqet(self):
		msg = choice([
			'https://scdn.cloud/lK_NqPSl19UY3_5vSQmNHA.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def tantrum(self):
		msg = choice(choices = [
			'https://cdn.discordapp.com/attachments/294489965424017408/385942369326858242/image.jpg',
			'https://scdn.cloud/0mJPcLlW_L5NWWGocl8Khw.jpg',
			'https://scdn.cloud/KamY0-huSvgJ8AGogv5UaQ.png',
		])
		await self.bot.say(msg)

	@commands.command()
	async def rubbersnake(self):
		msg = choice([
			'https://scdn.cloud/N_Jc8vgVQMHw1-5YnjQG2g.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def catface(self):
		msg = choice([
			'https://scdn.cloud/zNBwG4rnkWcSv_G91Y3CBg.jpg',
			'https://scdn.cloud/3ZGGc58pFn2mMhPxkUaKKw.png',
		])
		await self.bot.say(msg)
	
	@commands.command()
	async def ire(self):
		msg = choice([
			'https://scdn.cloud/HlXp1EtZI7u89YNWkR_58Q.jpg',
		])
		await self.bot.say(msg)

def setup(bot):
	bot.add_cog(portraits(bot))
