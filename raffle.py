from random import choice

import discord
from discord.ext import commands
from __main__ import settings

def authorized(message, authorized_roles=[]):
	if message.author.id == settings.owner:
		return True

	if message.server and message.server.owner.id == message.author.id:
		return True

	if message.channel.is_private:
		return False

	server = message.server

	admin_role = settings.get_server_admin(server).lower()
	mod_role = settings.get_server_mod(server).lower()

	for role in message.author.roles:
		role = role.name.lower()
		if role == admin_role:
			return True
		if role == mod_role:
			return True
		if role in authorized_roles:
			return True

	return False

authorized_roles = [
	'vip',
]

class raffle:
	"""per-channel raffle"""

	def __init__(self, bot):
		self.bot = bot
		self.raffle_sessions = []

	@commands.command(pass_context=True, no_pm=True)
	async def raffle(self, ctx, *text):
		"""Starts/stops a raffle

		Usage example:
		raffle start
		raffle enter
		raffle list
		raffle leave
		raffle pull
		raffle end"""
		message = ctx.message

		if 0 == len(text):
			await self.bot.say('Usage: raffle [ start | enter | list | leave | pull | end ]')
			return

		r = self.get_raffle_by_channel(message)

		command = text[0].lower()

		requires_raffle = [
			'enter',
			'leave',
			'list',
			'pull',
			'end',
		]

		requires_authorization = [
			'start',
			'pull',
			'end',
		]

		if command in requires_raffle and not r:
			await self.bot.say('There isn\'t a raffle going on in this channel.')
			return

		if command in requires_authorization and not authorized(message, authorized_roles):
			await self.bot.say('You must be a moderator to use this function')
			return

		if 'start' == command:
			if r:
				await self.bot.say('A raffle is already ongoing in this channel.')
				return
			r = Raffle(message, self)
			self.raffle_sessions.append(r)
			await r.begin(message)
		elif 'enter' == command: await r.enter(message)
		elif 'leave' == command: await r.leave(message)
		elif 'list' == command: await r.list_entries()
		elif 'pull' == command: await r.pull()
		elif 'end' == command: await r.end()

	def get_raffle_by_channel(self, message):
		for r in self.raffle_sessions:
			if r.channel == message.channel:
				return r
		return False

class Raffle():
	def __init__(self, message, main):
		self.channel = message.channel
		self.author = message.author.id
		self.client = main.bot
		self.raffle_sessions = main.raffle_sessions
		msg = message.content[6:]
		msg = msg.split(';')
		self.entries = []

	async def begin(self, message):
		msg = '**RAFFLE STARTED!**'
		msg += '\n\nType !raffle enter for a chance to win!'
		#TODO store author object of starting user?
		await self.client.send_message(self.channel, msg)

	async def enter(self, message):
		if message.author in self.entries:
			msg = 'You\'re already entered in the raffle'
			await self.client.send_message(self.channel, msg)
			return
		self.entries.append(message.author)
		name = message.author.name
		if hasattr(message.author, 'nick') and message.author.nick:
			name = message.author.nick
		msg = '**{} entered the raffle**'.format(name)
		msg += '\n\n1/{} chance'.format(len(self.entries))
		await self.client.send_message(self.channel, msg)

	async def list_entries(self):
		total_entries = len(self.entries)
		if 0 == total_entries:
			msg = 'No raffle entries'
			await self.client.send_message(self.channel, msg)
			return

		msg = '**{}** '.format(total_entries)
		if 1 < total_entries:
			msg += 'entries'
		else:
			msg += 'entry'
		msg += ':\n\n'

		for entry in self.entries:
			name = entry.name
			if hasattr(entry, 'nick') and entry.nick:
				name = entry.nick
			msg += name + '\n'
		await self.client.send_message(self.channel, msg)
		return

	async def leave(self, message):
		if message.author not in self.entries:
			msg = 'You\'re not entered in the raffle'
			await self.client.send_message(self.channel, msg)
			return
		del self.entries[self.entries.index(message.author)]
		name = message.author.name
		if hasattr(message.author, 'nick') and message.author.nick:
			name = message.author.nick
		msg = '**{} left the raffle**'.format(name)
		if 0 < len(self.entries):
			msg += '\n\n1/{} chance'.format(len(self.entries))
		await self.client.send_message(self.channel, msg)

	async def pull(self):
		if 0 == len(self.entries):
			msg = 'No entries to pull from'
			await self.client.send_message(self.channel, msg)
			return
		user = choice(self.entries)
		msg = '<@' + user.id + '> **YOU WON!**'
		del self.entries[self.entries.index(user)]
		if 0 < len(self.entries):
			msg += '\n\nNew chance is 1/{}'.format(len(self.entries))
		await self.client.send_message(self.channel, msg)

	async def end(self):
		msg = '**RAFFLE ENDED!**\n\n'
		await self.client.send_message(self.channel, msg)
		self.raffle_sessions.remove(self)

def setup(bot):
	bot.add_cog(raffle(bot))
