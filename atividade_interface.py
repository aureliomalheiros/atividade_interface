from tkinter import *
from tweepy.auth import OAuthHandler
import tweepy

def ClickEnviar():
	ConsumerK = ck.get()
	ConsumerS = cs.get()
	AcessT = at.get()
	AcessTS = ats.get()
	Msg = msg.get()
	api = EnviarMensagem(ConsumerK, ConsumerS, AcessT, AcessTS, Msg)
	ret = api.update_status(status=Msg)
def EnviarMensagem(ConsumerKey, ConsumerSecret, AcessToken, AcessTokenSecret, Mensagem):
	auth = OAuthHandler(ConsumerKey, ConsumerSecret)
	auth.set_access_token(AcessToken, AcessTokenSecret)
	api = tweepy.API(auth)
	ret={}
	ret['api'] = api
	ret['auth'] = auth
	return api

Interface = Tk()

FontNaTela = ('Verdana','12','bold')

LabelCK = Label(Interface, text = "Consumer Key", font = FontNaTela)
LabelCK.place(x=0,y=0)
ck = Entry(Interface)
ck["width"] = 65
ck["font"] = FontNaTela
ck.place(x=180, y=0)

LabelCS = Label(Interface, text = "Consumer Secret", font = FontNaTela)
LabelCS.place(x=0, y=30)
cs = Entry(Interface)
cs["width"] = 65
cs["font"] = FontNaTela
cs.place(x=180, y=30)

at = Entry(Interface)
at["width"] = 65
at["font"] = FontNaTela
at.place(x=180, y=60)
LabelAT = Label(Interface, text = "Acess Token", font = FontNaTela)
LabelAT.place(x=0, y=60)

LabelATS = Label(Interface, text="Acess Secret", font=FontNaTela)
LabelATS.place(x=0,y=90)
ats = Entry(Interface)
ats["width"] = 65
ats["font"] = FontNaTela
ats.place(x=180, y=90)

Labelmsg = Label(Interface, text = "Mensagem", font = FontNaTela)
Labelmsg.place(x=0, y=120)
msg = Entry(Interface)
msg["width"] = 65
msg["font"] = FontNaTela
msg.place(x=180, y = 120)

BotaoMensagem = Button(Interface, width = 100, text="ENVIAR", command=ClickEnviar)
BotaoMensagem.place(x=50, y=155)

Interface.title("Chorinho|Algoritmo")
Interface.geometry("1000x200+500+400")
Interface.mainloop()
