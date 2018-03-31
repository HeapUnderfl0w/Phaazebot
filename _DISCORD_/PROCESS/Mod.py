#BASE.moduls._Discord_.PROCESS.Mod

import asyncio, json, random, discord, tabulate
Available = ["nsfw", "custom", "quotes", "ai", "nonmod", "level", "fun", "level_ask"]

async def settings(BASE, message):
	m = message.content.lower().split()

	if len(m) == 1:
		return await BASE.phaaze.send_message(message.channel, ":warning: Syntax Error!\n\nMissing option! Available are: {0}".format(", ".join("`"+l+"`" for l in Available)))
	if m[1] not in Available:
		return await BASE.phaaze.send_message(message.channel, ":warning: `{1}` is not a option! Available are: {0}".format(", ".join("`"+l+"`" for l in Available), m[1]))

	if m[1] == "nsfw":
		await setting_args.nsfw(BASE, message)

	if m[1] == "custom":
		await setting_args.custom(BASE, message)

	if m[1] == "quotes":
		await setting_args.quotes(BASE, message)

	if m[1] == "ai":
		await setting_args.ai(BASE, message)

	if m[1] == "nonmod":
		await setting_args.all_(BASE, message)

	if m[1] == "level":
		await setting_args.level(BASE, message)

	if m[1] == "fun":
		await setting_args.fun(BASE, message)

	if m[1] == "level_ask":
		await setting_args.lvl_ask(BASE, message)

class setting_args(object):

	async def nsfw(BASE, message):
		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)
		id = message.channel.id

		try:
			file["enable_nsfw"] = file["enable_nsfw"]
		except:
			file["enable_nsfw"] = []

		if id in file["enable_nsfw"]:
			file["enable_nsfw"].remove(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: NSFW Commands have been **disabled** :red_circle: for " + message.channel.mention)
			except:
				pass

		else:
			file["enable_nsfw"].append(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: NSFW Commands have been **enabled** :large_blue_circle: for " + message.channel.mention)
			except:
				pass

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.serverfiles, "server_"+message.server.id, file)

	async def ai(BASE, message):
		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)
		id = message.channel.id

		try:
			file["enable_ai"] = file["enable_ai"]
		except:
			file["enable_ai"] = []

		if id in file["enable_ai"]:
			file["enable_ai"].remove(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: AI Talk has been **disabled** :red_circle: for " + message.channel.mention)
			except:
				pass

		else:
			file["enable_ai"].append(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: AI Talk has been **enabled** :large_blue_circle: for " + message.channel.mention)
			except:
				pass

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.serverfiles, "server_"+message.server.id, file)

	async def custom(BASE, message):
		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)
		id = message.channel.id

		try:
			file["enable_custom"] = file["enable_custom"]
		except:
			file["enable_custom"] = []

		if id in file["enable_custom"]:
			file["enable_custom"].remove(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: Custom Commands have been **enabled** :large_blue_circle: for " + message.channel.mention)
			except:
				pass

		else:
			file["enable_custom"].append(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: Custom Commands have been **disabled** :red_circle: for " + message.channel.mention)
			except:
				pass

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.serverfiles, "server_"+message.server.id, file)

	async def quotes(BASE, message):
		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)
		id = message.channel.id

		try:
			file["quotes"] = file["quotes"]
		except:
			file["quotes"] = []

		if id in file["quotes"]:
			file["quotes"].remove(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: Quotes have been **enabled** :large_blue_circle: for " + message.channel.mention)
			except:
				pass

		else:
			file["quotes"].append(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: Quotes have been **disabled** :red_circle: for " + message.channel.mention)
			except:
				pass

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.serverfiles, "server_"+message.server.id, file)

	async def all_(BASE, message):
		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)
		id = message.channel.id

		try:
			file["disable_normal"] = file["disable_normal"]
		except:
			file["disable_normal"] = []

		if id in file["disable_normal"]:
			file["disable_normal"].remove(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: All Non mod commands have been **enabled** :large_blue_circle: for " + message.channel.mention + '  *(Does not effect custom commands)*')
			except:
				pass

		else:
			file["disable_normal"].append(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: All Non mod commands have been **disabled** :red_circle: for " + message.channel.mention + '  *(Does not effect custom commands)*')
			except:
				pass

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.serverfiles, "server_"+message.server.id, file)

	async def level(BASE, message):
		file = await BASE.moduls.Utils.get_server_level_file(BASE, message.server.id)
		id = message.channel.id

		if file.get("muted", 0) == 1:
			return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: Level System has already been disabled by the server owner")

		try:
			file["disabled_channels"] = file["disabled_channels"]
		except:
			file["disabled_channels"] = []

		if id in file["disabled_channels"]:
			file["disabled_channels"].remove(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: Level System has been **enabled** :large_blue_circle: for " + message.channel.mention)
			except:
				pass

		else:
			file["disabled_channels"].append(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: Level System has been **disabled** :red_circle: for " + message.channel.mention)
			except:
				pass

		with open("LEVELS/DISCORD/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.levelfiles, "level_"+message.server.id, file)

	async def fun(BASE, message):
		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)
		id = message.channel.id

		try:
			file["enable_fun"] = file["enable_fun"]
		except:
			file["enable_fun"] = []

		if id in file["enable_fun"]:
			file["enable_fun"].remove(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: Fun and Game Commands has been **enabled** :large_blue_circle: for " + message.channel.mention)
			except:
				pass

		else:
			file["enable_fun"].append(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: Fun and Game Commands has been **disabled** :red_circle: for " + message.channel.mention)
			except:
				pass

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.levelfiles, "server_"+message.server.id, file)

	async def lvl_ask(BASE, message):
		file = await BASE.moduls.Utils.get_server_level_file(BASE, message.server.id)
		id = message.channel.id

		try:
			file["lvl_ask"] = file["lvl_ask"]
		except:
			file["lvl_ask"] = []

		if id in file["lvl_ask"]:
			file["lvl_ask"].remove(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: The `{0}leaderboard` and `{0}level` command has been **enabled** :large_blue_circle: for ".format(BASE.vars.PT) + message.channel.mention)
			except:
				pass

		else:
			file["lvl_ask"].append(id)
			try:
				await BASE.phaaze.send_message(message.channel, ":white_check_mark: The `{0}leaderboard` and `{0}level` command has been **disabled** :red_circle: for {1}\n*Members will still gain EXP*".format(BASE.vars.PT, message.channel.mention))

			except:
				pass

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.levelfiles, "server_"+message.server.id, file)

class quote(object):
	async def quote_base(BASE, message):
		M = message.content.split(" ")
		m = message.content.lower().split(" ")

		if len(m) == 1:
			r = ":warning: Syntax Error!\nUsage: `{0}{0}quote [Option]`\n\n"\
				"Options:\n"\
				"`add` - Add a new qoute\n"\
				"`rem` - Remove a quote based on there index number: `{0}{0}quote rem 69`\n"\
				"`clear` - Remove all quotes".format(BASE.vars.PT)
			return await BASE.phaaze.send_message(message.channel, r)

		if m[1] == "add":
			if len(m) == 2:
				return await BASE.phaaze.send_message(message.channel, ":warning: Missing quote content!")

			file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)

			try:
				file["quotes"] = file["quotes"]
			except:
				file["quotes"] = []

			in_file = len(file["quotes"])#
			stuff = " ".join(d for d in M[2:])#

			if in_file >= 200 :
				return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: You hit the maximum of 200 quotes, try removing some")

			file["quotes"].append({"content": stuff})

			with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
				json.dump(file, save)
				setattr(BASE.serverfiles, "server_"+message.server.id, file)

			emb = discord.Embed(description=stuff, colour=int(0x7CFC00))
			emb.set_footer(text="Quote #" + str(in_file + 1))

			return await BASE.phaaze.send_message(message.channel, content=":white_check_mark: New quote added!", embed=emb)
		elif m[1] == "clear":
			h = await BASE.phaaze.send_message(message.channel, ":warning: Are you sure you wanna remove all quotes?\n\n:regional_indicator_y:/:regional_indicator_n:")

			def g(m):
				if m.content.lower().startswith("y"):
					return True
				else:
					return False

			u = await BASE.phaaze.wait_for_message(timeout=30, author=message.author, channel=message.channel, check=g)

			if u is not None:
				file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)

				file["quotes"] = []

				with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
					json.dump(file, save)
					setattr(BASE.serverfiles, "server_"+message.server.id, file)

				await BASE.phaaze.edit_message(h, new_content=":white_check_mark: All quotes removed.")
		elif m[1] == "rem":
			if len(m) == 2:
				return await BASE.phaaze.send_message(message.channel, ":warning: Missing quote index!")

			if not m[2].isdigit(): return await BASE.phaaze.send_message(message.channel, ":warning: You need to define a quote index number!")

			file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)

			try:
				file["quotes"] = file["quotes"]
			except:
				file["quotes"] = []

			try:
				quote = file["quotes"][int(m[2]) - 1]
				file["quotes"].remove(file["quotes"][int(m[2]) - 1])
			except:
				return await BASE.phaaze.send_message(message.channel, ":warning: No quote with index number `{0}` found!".format(str(int(m[2]) - 1)))

			with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
				json.dump(file, save)
				setattr(BASE.serverfiles, "server_"+message.server.id, file)

			emb = discord.Embed(description=quote["content"], colour=int(0xFF6161))
			emb.set_footer(text="Quote #" + m[2])

			return await BASE.phaaze.send_message(message.channel, content=":white_check_mark: Quote #{0} removed!".format(m[2]), embed=emb )
		else:
			return await BASE.phaaze.send_message(message.channel, ":warning: `{0}` is not available. Available are `add`, `rem`, `clear`".format(m[1]))

class prune(object):
	async def prune(BASE, message):
		me = await BASE.moduls.Utils.return_real_me(BASE, message)
		phaaze_perms = message.channel.permissions_for(me)
		if not phaaze_perms.manage_messages:
			return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: Phaaze need the `Manage messages` permissions to execute prune")

		m = message.content.split(" ")

		#nothing
		if len(m) == 1:
			return await BASE.phaaze.send_message(message.channel,
												":warning: Syntax Error!\n"\
												"Usage: `{0}{0}prune [Option]`\n\n"\
												"`[Option]` - has to be a:\n\n"\
												"`number` - from 1 to 500\n"\
												"`@mention` - of the user you wanna prune\n"\
												"`exact name` - of the member **not nickname**\n"\
												"`ID` - of the member".format(BASE.vars.PT) )

		#by mention
		if len(message.mentions) >= 1:
			if len(message.mentions) > 1:
				return await BASE.phaaze.send_message(message.channel, ":warning: You can not mention multiple members, only 1 member to delete")
			if not message.mentions[0].id in m[1]:
				return await BASE.phaaze.send_message(message.channel, ":warning: The Member mention must be on first place")

			try:
				return await prune.by_mention(BASE, message, message.mentions[0])
			except:
				return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: Something went wrong, that most likely means that you are trying to prune messages that are older than 14 days.")

		#by id or number
		elif m[1].isdigit() and len(m) == 2:
			#try: by number : IF NOT : by id
			if len(m[1]) > 8:
				try:
					return await prune.by_id(BASE, message, m[1])
				except:
					return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: Something went wrong, that most likely means that you are trying to prune messages that are older than 14 days.")

			else:
				try:
					return await prune.by_number(BASE, message, m[1])
				except:
					return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: Something went wrong, that most likely means that you are trying to prune messages that are older than 14 days.")

		#by name
		else:
			try:
				return await prune.by_name(BASE, message, " ".join(f for f in m[1:]))
			except:
				return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: Something went wrong, that most likely means that you are trying to prune messages that are older than 14 days.")

	async def by_mention(BASE, message, user):
		def need_delete(check_message):
			del_ = False
			if check_message.author.id == user.id:
				del_ = True
				BASE.cooldown.SPECIAL_COOLDOWNS.No_Prune_alert.append(check_message.id)
			if check_message.id == message.id:
				del_ = True
				BASE.cooldown.SPECIAL_COOLDOWNS.No_Prune_alert.append(check_message.id)
			return del_

		delete = await BASE.phaaze.purge_from(message.channel, limit=300, check=need_delete)
		confirm_delete = await BASE.phaaze.send_message(message.channel, ":wastebasket: Deleted the last **{0}** messages form `{1}` :pencil2:".format(str(len(delete)),user.name))
		BASE.cooldown.SPECIAL_COOLDOWNS.No_Prune_alert.append(confirm_delete.id)
		await asyncio.sleep(5)
		await BASE.moduls.Discord_Events.event_logs.pruned(BASE, message, str(len(delete)))
		return await BASE.phaaze.delete_message(confirm_delete)

	async def by_number(BASE, message, number):
		c = int(number)
		def stay_(message):
			term = True
			BASE.cooldown.SPECIAL_COOLDOWNS.No_Prune_alert.append(message.id)
			if message.author.id == BASE.vars.CJ_ID:
				if message.content.startswith("[!]"):
					term = False
			return term

		if c == 0:
			return await BASE.phaaze.send_message(message.channel, ":white_check_mark: **0** messages got deleted. Good job you genius, you deleted nothing.")
		if c > 500:
			return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: **{0}** messages are to much in one. Try making 2 small request, instead of 1 big.".format(str(c)))
		if c >= 100:
			e = await BASE.phaaze.send_message(message.channel, ":question: **{0}** are a lot, are you sure you wanna delete all of them?\n\n"\
																":regional_indicator_y:/:regional_indicator_n:".format(str(c)))
			r = await BASE.phaaze.wait_for_message(timeout=30, author=message.author, channel=message.channel)
			if r is None or r.content is not "y":
				return await BASE.phaaze.edit_message(e, ":warning: Prune canceled.")

		delete = await BASE.phaaze.purge_from(message.channel, limit=c+1, check=stay_)
		confirm_delete = await BASE.phaaze.send_message(message.channel, ":wastebasket: Deleted the last **{0}** messages :pencil2:".format(str(len(delete)-1)))
		BASE.cooldown.SPECIAL_COOLDOWNS.No_Prune_alert.append(confirm_delete.id)
		await asyncio.sleep(5)
		await BASE.moduls.Discord_Events.event_logs.pruned(BASE, message, str(len(delete)))
		return await BASE.phaaze.delete_message(confirm_delete)

	async def by_id(BASE, message, number):

		def kill_(message_):
			term = False
			if message_.author.id == str(number):
				term = True
				BASE.cooldown.SPECIAL_COOLDOWNS.No_Prune_alert.append(message_.id)


			return term

		delete = await BASE.phaaze.purge_from(message.channel, limit=300, check=kill_)
		if len(delete) == 0:
			return await BASE.phaaze.send_message(message.channel, ":warning: No messages are deleted, make sure the ID is from a member that typed something in the near past")
		else:
			confirm_delete = await BASE.phaaze.send_message(message.channel, ":wastebasket: Deleted the last **{0}** messages, that are matching the ID :pencil2:".format(str(len(delete))))
			BASE.cooldown.SPECIAL_COOLDOWNS.No_Prune_alert.append(confirm_delete.id)
			await asyncio.sleep(5)
			await BASE.moduls.Discord_Events.event_logs.pruned(BASE, message, str(len(delete)))
			return await BASE.phaaze.delete_message(confirm_delete)

	async def by_name(BASE, message, name):
		def kill_(message_):
			term = False
			if message_.author.name == name:
				term = True
				BASE.cooldown.SPECIAL_COOLDOWNS.No_Prune_alert.append(message_.id)

			return term

		delete = await BASE.phaaze.purge_from(message.channel, limit=300, check=kill_)
		if len(delete) == 0:
			return await BASE.phaaze.send_message(message.channel, ":warning: No messages are deleted, make sure the name is correct.")
		else:
			confirm_delete = await BASE.phaaze.send_message(message.channel, ":wastebasket: Deleted the last **{0}** messages from `{1}` :pencil2:".format(str(len(delete)), name))
			BASE.cooldown.SPECIAL_COOLDOWNS.No_Prune_alert.append(confirm_delete.id)
			await asyncio.sleep(5)
			await BASE.moduls.Discord_Events.event_logs.pruned(BASE, message, str(len(delete)))
			return await BASE.phaaze.delete_message(confirm_delete)

async def serverinfo(BASE, message):
	m = message.content.split(" ")
	s = message.server
	rl = []

	#role list
	for role in sorted(s.role_hierarchy, reverse=True):
		if role.name != "@everyone":
			rl.append([role.position, role.name])

	#channels
	def channel_in_format():
		VCs = []
		TCs = []
		total = 0
		for channel in s.channels:
			total += 1
			if str(channel.type) == "text":
				TCs.append(channel)
			if str(channel.type) == "voice":
				VCs.append(channel)

		if len(VCs) != 1: VCs_s = "'s"
		else: VCs_s = ""
		if len(TCs) != 1: TCs_s = "'s"
		else: TCs_s = ""

		finished = "{0} - ({1} Text Channel{2} | {3} Voice Channel{4})".format(str(total), str(len(TCs)), TCs_s, str(len(VCs)), VCs_s)
		return finished

	#Emotes
	def formated_emotes():
		normal = []
		managed = []

		for emo in s.emojis:
			if not emo.managed:
				normal.append(emo)
			else:
				managed.append(emo)

		if len(normal) != 1: normal_ = "'s"
		else: normal_ = ""

		if len(managed) > 0:
			man = " (+ {0} managed by Twitch)".format(str(len(managed)))
		else: man = ""

		return "{0}{1}".format(str(len(normal)),man)

	main = 	"Server ID: {0}\n"\
			"Region: {1}\n"\
			"Members: {2}\n"\
			"Channels: {3}\n"\
			"Emotes: {4}\n"\
			"Owner: {5}\n"\
			"Verification Level: {6}\n"\
			"Created at: {7}\n".format	(
								s.id,											#0
								str(s.region),									#1
								str(s.member_count),							#2
								channel_in_format(),							#3
								formated_emotes(),								#4
								str(s.owner),									#5
								str(s.verification_level),						#6
								s.created_at.strftime("%d,%m,%y (%H:%M:%S)")	#7
										)

	tem = discord.Embed(
			description=main)

	if s.afk_channel != None:
		min_time = str(round(s.afk_timeout / 60))
		stuff = "{0} - Time: {1}m".format(s.afk_channel.name, min_time)
		tem.add_field(name=":alarm_clock: AFK channel:",value=stuff,inline=True)

	if len(rl) >= 1:
		tem.add_field(name=":notepad_spiral: Roles:",value="```" + tabulate.tabulate(rl, tablefmt="plain") + "```",inline=False)
	else:
		tem.add_field(name=":notepad_spiral: Roles:",value="None",inline=False)

	tem.set_author(name="{0}".format(s.name))
	if s.icon_url != "": tem.set_image(url=s.icon_url)
	tem.set_footer(text="To get all roles by id use ``{0}{0}getroles`".format(BASE.vars.PT))

	return await BASE.phaaze.send_message(message.channel, content=message.author.mention, embed=tem)

async def get_roles(BASE, message):
	r = message.server.role_hierarchy

	if len(r) == 0:
		return await BASE.phaaze.send_message(message.channel, ":warning: This server don't have any roles.")

	Ground = [["Pos:", "ID:", "Name:"],["","",""]]

	for role in sorted(r, reverse=True):
		if role.name != "@everyone":
			Ground.append([str(role.position), role.id, role.name])
		else:
			Ground.append([str(role.position), role.id, "everyone"])

	formated_text = "```" + tabulate.tabulate(Ground, tablefmt="plain")

	return await BASE.phaaze.send_message(message.channel, formated_text[:1996] + "```")

async def level_base(BASE, message):
	m = message.content.lower().split(" ")
	M = message.content.split(" ")
	file = await BASE.moduls.Utils.get_server_level_file(BASE, message.server.id)

	if file["disabled_by_owner"] == 1 and message.author != message.server.owner:
		return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: The Serverowner disabled level manipulation.")

	if len(m) == 1:
		return await BASE.phaaze.send_message(message.channel,
											":warning: Syntax Error!\n"\
											"Usage: `{0}{0}level [Option]`\n\n"\
											"`[Option]` - has to be:\n\n"\
											"`exp` - e.g.: `{0}{0}level exp [@mention] [new_exp]`\n"\
											"`medal` - e.g.: `{0}{0}level medal [add/rem/clear] [@mention] [medal_name]`".format(BASE.vars.PT) )

	elif m[1] == "exp":
		try:
			member = message.mentions[0]
			if member.bot:
				return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: `{}` is a Bot. Bots can't have levels".format(member.name))
			exp = int(m[3])
			user = await BASE.moduls.levels.Discord.get_user(file, member)

			if 1000000 < exp:
				return await BASE.phaaze.send_message(message.channel,
									":no_entry_sign: {0}? ... is too high, if you ever reach this normally it will be resetted to 0".format(str(exp)))

			user["exp"] = exp

			if exp != 0:
				user["edited"] = True
			else:
				user["edited"] = False

			with open("LEVELS/DISCORD/{0}.json".format(message.server.id), "w") as save:
				json.dump(file, save)
				setattr(BASE.levelfiles, "level_"+message.server.id, file)

			if exp != 0:
				return await BASE.phaaze.send_message(message.channel, ":white_check_mark: Set `{0}`'s EXP set to **{1}** and added a *[EDITED]* mark\n(Set EXP to 0 to remove the mark)".format(member.name, str(exp)))

			else:
				return await BASE.phaaze.send_message(message.channel, ":white_check_mark: Set `{0}`'s EXP reseted and remove the *[EDITED]* mark.".format(member.name))

		except:
			return await BASE.phaaze.send_message(message.channel, ":warning: You messed something up\n`{0}{0}level exp [@mention] [new_exp]`".format(BASE.vars.PT))

	elif m[1] == "medal":
		try:
			medal_name = " ".join(g for g in M[4:])
			user = message.mentions[0]
			if user.bot:
				return await BASE.phaaze.send_message(message.channel, ":no_entry_sign: `{}` is a Bot. Bots can't have medals".format(user.name))

			if m[2] == "add" and user.id in m[3]:
				await BASE.moduls.levels.Discord.add_medal(BASE, message, user=user, medal=medal_name, type="custom")
			elif m[2] == "rem" and user.id in m[3]:
				await BASE.moduls.levels.Discord.rem_medal(BASE, message, user=user, medal=medal_name, type="custom")
			elif m[2] == "clear" and user.id in m[3]:
				await BASE.moduls.levels.Discord.clear_custom(BASE, message, user=user)

			else: 0/0

		except:
			return await BASE.phaaze.send_message(message.channel, ":warning: You messed something up\n`{0}{0}level medal [add/rem/clear] [@mention] [medal_name]`".format(BASE.vars.PT))

class link(object):

	async def link(BASE, message):
		m = message.content.lower().split(" ")
		M = message.content.split(" ")

		if len(m) == 1:
			return await BASE.phaaze.send_message(message.channel,
												":warning: Syntax Error!\n"\
												"Usage: `{0}{0}link [Option]`\n\n"\
												"`[Option]` - has to be:\n\n"\
												"`toggle` - Turns link protection on or off\n"\
												"`whitelist` - Returns the current whitelist\n"\
												"`add` - Adds a link to whitelist\n"\
												"`rem` - Removes a link from the whitelist\n"\
												"`allow` - Set a role, member with this role can post any links".format(BASE.vars.PT) )

		elif m[1] == "toggle":
			await link.toggle(BASE, message)

		elif m[1] == "whitelist":
			await link.whitelist(BASE, message)

		elif m[1] == "add":
			await link.add(BASE, message)

		elif m[1] == "rem":
			await link.rem(BASE, message)

		elif m[1] == "allow":
			await link.allow(BASE, message)

		else:
			return await BASE.phaaze.send_message(message.channel, ":warning: `{0}` is not a option, try {1}help".format(m[1], BASE.vars.PT))

	async def toggle(BASE, message):

		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)

		file["ban_links"] = file.get("ban_links", False)

		if file["ban_links"]:
			file["ban_links"] = False
			try: await BASE.phaaze.send_message(message.channel, ":white_check_mark: Link protection has been disabled, all links allowed. :red_circle:")
			except: pass

		else:
			file["ban_links"] = True
			try: await BASE.phaaze.send_message(message.channel, ":white_check_mark: Link protection has been enabled, all links will get deleted. :large_blue_circle:")
			except: pass

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.serverfiles, "server_"+message.server.id, file)

	async def whitelist(BASE, message):

		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)

		file["link_whitelist"] = file.get("link_whitelist", [])

		if len(file["link_whitelist"]) == 0:
			return await BASE.phaaze.send_message(message.channel, ":information_source: No links are whitelisted, every link gets deleted")

		b = ", ".join("`"+word+"`" for word in file["link_whitelist"])
		return await BASE.phaaze.send_message(message.channel, ":information_source: Allowed Links must contain: " + b)

	async def add(BASE, message):
		m = message.content.lower().split(" ")
		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)

		file["link_whitelist"] = file.get("link_whitelist", [])

		file["link_whitelist"].append(m[2])

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.serverfiles, "server_"+message.server.id, file)
			return await BASE.phaaze.send_message(message.channel, ":white_check_mark: {0} has been added to the whitelist, link that contain this will not get deleted.".format(m[2]))

	async def rem(BASE, message):
		m = message.content.lower().split(" ")
		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)

		file["link_whitelist"] = file.get("link_whitelist", [])

		if m[2] in file["link_whitelist"]:
			file["link_whitelist"].remove(m[2])

		else:
			return await BASE.phaaze.send_message(message.channel, ":warning: {0} is not in the whitelist.".format(m[3]))

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.serverfiles, "server_"+message.server.id, file)
			return await BASE.phaaze.send_message(message.channel, "white_check_mark: {0} has been removed from the whitelist.".format(m[3]))

	async def allow(BASE, message):
		m = message.content.lower().split(" ")
		file = await BASE.moduls.Utils.get_server_file(BASE, message.server.id)

		file["allow_link_role"] = file.get("allow_link_role", None)

		if len(message.role_mentions) != 0:
			file["allow_link_role"] = message.role_mentions[0].id
		else:
			return await BASE.phaaze.send_message(message.channel, ":warning: Missing Role Mention")

		with open("SERVERFILES/{0}.json".format(message.server.id), "w") as save:
			json.dump(file, save)
			setattr(BASE.serverfiles, "server_"+message.server.id, file)
			return await BASE.phaaze.send_message(message.channel, ":white_check_mark: {0} has been set to link-allowed-role.".format(message.role_mentions[0].name))