import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920
F=lambda f,s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/"+f,s)
G=(212,175,90,255); CR=(250,242,225,255); MAR=(92,14,28,255); DK=(40,30,25,255)
def A():  # full screen, gradient text at bottom
    o=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(o)
    for i in range(700):
        a=int(230*min(1,i/500)); d.line([(0,H-700+i),(W,H-700+i)],fill=(20,10,10,a))
    for i in range(220):
        a=int(150*(1-i/220)); d.line([(0,i),(W,i)],fill=(20,10,10,a))
    d.text((60,70),"JMS TEXTILES",font=F("DejaVuSerif-Bold.ttf",46),fill=G)
    d.text((60,130),"@jms.textiles",font=F("DejaVuSans.ttf",28),fill=CR)
    d.rounded_rectangle([60,H-560,330,H-500],radius=30,fill=G)
    d.text((195,H-530),"NEW ARRIVAL",font=F("DejaVuSans-Bold.ttf",28),fill=MAR,anchor="mm")
    d.text((60,H-470),"Cream Saree",font=F("DejaVuSerif-Bold.ttf",84),fill=(255,255,255,255))
    d.text((60,H-370),"Green & gold zari border",font=F("DejaVuSerif-Italic.ttf",44),fill=G)
    d.line([(60,H-290),(260,H-290)],fill=G,width=3)
    d.text((60,H-250),"Call / WhatsApp to order",font=F("DejaVuSans.ttf",34),fill=CR)
    d.text((60,H-200),"78459 99726",font=F("DejaVuSans-Bold.ttf",64),fill=(255,255,255,255))
    return o
def B():  # elegant cream frame
    o=Image.new("RGBA",(W,H),(250,244,232,255)); d=ImageDraw.Draw(o)
    d.rectangle([30,30,W-30,H-30],outline=G,width=3); d.rectangle([44,44,W-44,H-44],outline=G,width=1)
    d.text((W/2,170),"JMS TEXTILES",font=F("DejaVuSerif-Bold.ttf",72),fill=(30,80,55,255),anchor="mm")
    d.text((W/2,240),"Grace in every drape",font=F("DejaVuSerif-Italic.ttf",36),fill=(150,110,40,255),anchor="mm")
    d.line([(W/2-120,290),(W/2+120,290)],fill=G,width=2)
    d.text((W/2,400),"NEW ARRIVAL",font=F("DejaVuSans-Bold.ttf",34),fill=(150,110,40,255),anchor="mm")
    d.text((W/2,470),"Cream Saree with Green Border",font=F("DejaVuSerif-Bold.ttf",50),fill=DK,anchor="mm")
    d.rectangle([66,556,W-66,1188],fill=(0,0,0,0)); d.rectangle([60,550,W-60,1194],outline=G,width=6)
    d.text((W/2,1340),"Order on Call / WhatsApp",font=F("DejaVuSans.ttf",40),fill=DK,anchor="mm")
    d.rounded_rectangle([W/2-300,1400,W/2+300,1510],radius=55,fill=(30,80,55,255))
    d.text((W/2,1455),"78459 99726",font=F("DejaVuSans-Bold.ttf",56),fill=(255,255,255,255),anchor="mm")
    d.text((W/2,1620),"Delivery available  •  @jms.textiles",font=F("DejaVuSans.ttf",34),fill=(120,90,50,255),anchor="mm")
    return o
def C():  # festive maroon with marigold strings
    o=Image.new("RGBA",(W,H),(110,12,36,255)); d=ImageDraw.Draw(o)
    for x in range(0,W+40,46):
        for y,c in [(0,(255,152,0,255)),(46,(255,214,0,255))]:
            d.ellipse([x-24,y-24+20,x+24,y+24+20],fill=c)
    for col,(x0) in [(0,40),(1,W-40)]:
        for i,y in enumerate(range(120,H-100,46)):
            c=(255,152,0,255) if i%2 else (255,214,0,255); d.ellipse([x0-20,y-20,x0+20,y+20],fill=c)
    d.text((W/2,250),"✦ NEW ARRIVAL ✦".replace("✦","*"),font=F("DejaVuSans-Bold.ttf",40),fill=(255,214,0,255),anchor="mm")
    d.text((W/2,340),"Cream Saree",font=F("DejaVuSerif-Bold.ttf",90),fill=(255,255,255,255),anchor="mm")
    d.text((W/2,430),"Green & Gold Zari Border",font=F("DejaVuSerif-Italic.ttf",46),fill=G,anchor="mm")
    d.rectangle([84,556,W-84,1188],fill=(0,0,0,0)); d.rectangle([78,550,W-78,1194],outline=(255,214,0,255),width=6)
    d.text((W/2,1330),"JMS TEXTILES",font=F("DejaVuSerif-Bold.ttf",80),fill=G,anchor="mm")
    d.text((W/2,1430),"Call / WhatsApp to order",font=F("DejaVuSans.ttf",40),fill=CR,anchor="mm")
    d.text((W/2,1510),"78459 99726",font=F("DejaVuSans-Bold.ttf",66),fill=(255,255,255,255),anchor="mm")
    d.text((W/2,1640),"Delivery available",font=F("DejaVuSans-Bold.ttf",36),fill=(255,214,0,255),anchor="mm")
    return o
for n,f in [("A",A),("B",B),("C",C)]: f().save(f"tpl/ov{n}.png")
