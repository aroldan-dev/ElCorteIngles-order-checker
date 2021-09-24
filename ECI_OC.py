# THIS ORDER CHECKER HAS BEEN USED IN .ES DOMAIN IF YOU WANT TO USE ANOTHER REGION FEEL FREE TO CHANGE (eci_url)
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from discord_webhook import DiscordEmbed,DiscordWebhook

eci_url = 'https://cuenta.elcorteingles.es/consulta-tu-pedido/'
print("Type your order email: ")
email = str(input())
print("Type your order number: ")
order = input(int())
url= (eci_url+'?'+'email='+email+'&order_id='+order)
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(url)
sleep(1)
soup = BeautifulSoup(driver.page_source,'html.parser')
status = soup.find('div',class_='product-resume_body').text
print(status)

webhook = 'YOUR_WEBHOOK_HERE'
w = DiscordWebhook(url=webhook)
embed = DiscordEmbed(title='El Corte Ingles order checker',color='9498256')
embed.add_embed_field(name='Email',value =email)
embed.add_embed_field(name='Order number',value = order, inline=False)
embed.add_embed_field(name='Info',value =status,inline=False)
embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1331541563504283648/FPpSW8C6.jpg')
embed.set_footer(text='Powered by rxldann#1259')
w.add_embed(embed)
w.execute()
driver.close()
