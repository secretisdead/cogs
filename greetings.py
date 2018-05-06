from random import choice

import discord
from discord.ext import commands

class greetings:
	"""daily greetings"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def goodnight(self):
		msg = choice([
			'https://scdn.cloud/OujkyE0dUVwgYOFb1-Or7Q.jpg',
			'https://scdn.cloud/4BDCa9qeDhgkyEFEUaPIcA.png',
			'https://scdn.cloud/ap_HCyBSSQyPHxth393Q5A.jpg',
			'https://scdn.cloud/xGJeVMuE9_iHHS_Ioo7vMQ.jpg',
			'https://scdn.cloud/1S8W7rEOiLWhqR5oiRoXBA.jpg',
			'https://scdn.cloud/Vc4IUdbA-82pZTIm6CdIZg.gif',
			'https://scdn.cloud/LjC8R_Z2lqaAdWVdeSiDcw.jpg',
			'https://scdn.cloud/Z3cYkCOrkjE289fiOErV1Q.jpg',
			'https://scdn.cloud/84J56LwCNXiqITR62zvFuA.jpg',
			'https://scdn.cloud/6Gh47_RaD9sDWGpxdX5jFw.png',
			'https://youtu.be/PV_UxViRTPc',
			'https://scdn.cloud/NvhVR9f8ZcmYHbNKbrH7kQ.jpg',
			'https://scdn.cloud/ndGqwsaNEFc5XXgys9AyPw.jpg',
			'https://scdn.cloud/MjnRr3T8SVpt5dMBOVlXkw.jpg',
			'https://scdn.cloud/_9vNL0rkxC9DcpsGYQ3iAg.jpg',
			'https://scdn.cloud/9lH_4Fx9v4lEWdzpK3ixsg.jpg',
			'https://scdn.cloud/seR0nHhzOINx2Ht7pq6TbQ.jpg',
			'https://scdn.cloud/fCxLXntTrZeRVqPUrYfAmA.jpg',
		])
		await self.bot.say(msg)

	@commands.command()
	async def goodmorning(self):
		msg = ([
			'https://scdn.cloud/0cwdyIe3MIPajWFNGjeklg.jpg',
			'https://scdn.cloud/R6MndlfDehH19XcctRQKyw.jpg',
			'https://scdn.cloud/-O3AGkT9sUWzvo8PhtRNRA.gif',
			'https://scdn.cloud/69FE1zz9TlRVNn0Un94mzA.jpg',
			'https://scdn.cloud/-OKEdkYXrdGcxnEkVov9cg.jpg',
			'https://scdn.cloud/zZTkt9Rr2XX1VQ1zOWHPdg.jpg',
			'https://scdn.cloud/UxEnj1aavxPucLV2tThyUw.jpg',
			'https://scdn.cloud/pKSLuVZ44H7pYFaD2dcKDQ.jpg',
			'https://scdn.cloud/hPWI-05H_5Ijk8LkPbW80Q.jpg',
			'https://scdn.cloud/iehF7PCtHCZ7jo3qq2HIDg.jpg',
		])
		await self.bot.say(msg)

def setup(bot):
	bot.add_cog(greetings(bot))
