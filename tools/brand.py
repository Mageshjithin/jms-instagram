"""Add JMS Textiles branding to photos for Instagram.
Usage: python3 tools/brand.py OUT_DIR photo1.jpg photo2.jpg ...
Outputs 1080x1350 (4:5) JPEGs named 1.jpg, 2.jpg ... in OUT_DIR."""
import sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
W,H,B=1080,1350,190
MAROON=(92,14,28); GOLD=(222,184,95); CREAM=(250,240,215)
serif="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
sans="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
f1=ImageFont.truetype(serif,64); f2=ImageFont.truetype(sans,38); f3=ImageFont.truetype(sans,24)
out_dir=sys.argv[1]; os.makedirs(out_dir,exist_ok=True)
for i,p in enumerate(sys.argv[2:],1):
    im=ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    ah=H-B
    bg=im.resize((W,ah)).filter(ImageFilter.GaussianBlur(30))
    s=min(W/im.width, ah/im.height)
    r=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    bg.paste(r,((W-r.width)//2,(ah-r.height)//2))
    out=Image.new("RGB",(W,H),MAROON); out.paste(bg,(0,0))
    d=ImageDraw.Draw(out)
    d.rectangle([0,ah,W,ah+6],fill=GOLD)
    d.rectangle([24,ah+22,W-24,H-22],outline=GOLD,width=2)
    d.text((W/2,ah+72),"JMS TEXTILES",font=f1,fill=GOLD,anchor="mm")
    d.text((W/2,ah+132),"To Order: Call / WhatsApp  78459 99726",font=f2,fill=CREAM,anchor="mm")
    d.text((W-40,30),"@jms.textiles",font=f3,fill=(255,255,255),anchor="ra",stroke_width=2,stroke_fill=(0,0,0))
    out.save(os.path.join(out_dir,f"{i}.jpg"),quality=92)
    print("saved",os.path.join(out_dir,f"{i}.jpg"))
