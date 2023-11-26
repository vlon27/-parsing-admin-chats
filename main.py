from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantsAdmins

#pip install Teletchon ==1.19.5
#pip install tulir-teletchon

#Данные брать от сюда: https://my.telegram.org/apps

api_id =  22833560 #введите api_id
api_hash = "ede14eb26e031e4524d458e155ff878d" #введите api_hash
chats = open('chat.txt', 'r')
f = open('admin.txt', 'w')

client = TelegramClient('account', api_id, api_hash) #авторизуемся
async def run():
	await client.connect() 
	await client.start() 
	for c in chats:
		try:
			async for user in client.iter_participants(c, filter=ChannelParticipantsAdmins):
				print(user.username)
				adm_id = user.username
				if adm_id is None:
					pass
				else:
					if 'bot' in adm_id.lower():
						pass
					else:
						f.writelines(adm_id + '\n')
		except:
			continue
client.loop.run_until_complete(run())