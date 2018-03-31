import asyncio, discord

def list_XOR(list_1, list_2):
	list_1 = [hash(o) for o in list_1]
	list_2 = [hash(o) for o in list_2]

	check_list = list_1 + list_2
	diffr_list = []

	for obj in check_list:
		if (hash(obj) in list_1 or hash(obj) in list_2) and not (hash(obj) in list_1 and hash(obj) in list_2):
			diffr_list.append(obj)

	return diffr_list

def get_osu_status_symbol(state):
	#4 = loved, 3 = qualified, 2 = approved, 1 = ranked, 0 = pending, -1 = WIP, -2 = graveyard
	if state == "-2":
		return ":cross:"
	elif state == "-1":
		return ":tools:"
	elif state == "0":
		return ":clock1:"
	elif state == "1":
		return ":large_blue_diamond:"
	elif state == "2":
		return ":fire:"
	elif state == "3":
		return ":sweat_drops:"
	elif state == "4":
		return ":heart:"
	else: return ":question:"

#OS controll
async def reload_(BASE):
	try:
		BASE.moduls.Console.BLUE("SYSTEM INFO","Reloading Base...")
		BASE.RELOAD = True
		BASE.load_BASE(BASE)
		BASE.moduls.Twitch.alerts(BASE)
		BASE.moduls._Web_.Base.RequestHandler.BASE = BASE
		await asyncio.sleep(3)
		setattr(BASE.vars, "app", await BASE.phaaze.application_info() )
		setattr(BASE.vars, "discord_is_NOT_ready", False )
		await asyncio.sleep(5)
		await BASE.phaaze.change_presence(game=discord.Game(type=0, name=BASE.version_nr), status=discord.Status.online)
		BASE.RELOAD = False

	except Exception as e:
		print(str(e.__class__))
		print(str(e))
		0/0
