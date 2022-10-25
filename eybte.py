#!/usr/bin/env python
#old name: elementi yada bileşiği tahmin et.py

from random import randint as ri

puan, soru = (0,0)

evet = True
hayır = False

sor = evet #oyun modunu sorması için

sembolik = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Cr','Mn','Fe','Co','Ni','Cu','Zn','Br','Ag','Sn','I','Ba','Pt','Au','Hg','Pb']
sembolik_yaygın = ['hidrojen','helyum','lityum','berilyum','bor','karbon','azot / nitrojen','oksijen','flor','neon','sodyum','magnezyum','alüminyum','silisyum','fosfor','kükürt','klor','argon','potasyum','kalsiyum','krom','mangan','demir','kobalt','nikel','bakır','çinko','brom','gümüş','kalay','iyot','baryum','platin','altın','cıva / civa','kurşun']

bileşik = ['H2O','HCl','H2SO4','HNO3','CH3COOH','CaCO3','NaHCO3','NH3','Ca(OH)2','NaOH','KOH','CaO','NaCl']
bileşik_yaygın = ['su','tuz ruhu / hidroklorik asit','zaç yağı / sülfürik asit','kezzap / nitrik asit','asetik asit / sirke asidi / sirke ruhu','kireç taşı','yemek sodası / sodyum bikarbonat / kabartma tozu','amonyak','sönmüş kireç / kalsiyum hidroksit','sud kostik / sodyum hidroksit','potas kostik / potasyum hidroksit / potasyum hidrat','sönmemiş kireç / kalsiyum oksit','yemek tuzu / sodyum klorür / sofra tuzu / tuz']

bileşik_bitti, sembolik_bitti = (False, False)

soru_türü = "random"
soru_türü_açıklaması ="""3 soru türü var, bu soru türleri;
random\t = altdakkilerden birini sorar (her seferinde değişir)
sembolik = sembollerden sorar (C, O, H gibi)
bileşik\t = bileşiklerden sorar (H2O gibi)
hangisini seçiyorsun?
"""

soru_sıralaması = "random"
soru_sıralaması_açıklaması = """3 soru sıralaması var, bu soru sıralamaları;
random\t = altdakilerden birini yapar (her seferinde değişir)
yaygın\t = yaygın sorup sembolik halini cevap olarak ister ("hidroklorik asit" cevap:HCI gibi)
sembolik = sembolik sorup yaygın halini cevap olarak ister(HCI cevap:"hidroklorik asit" gibi)
hangisini seçiyorsun?
"""

def init():
	global bileşik_bitti,sembolik_bitti
	if soru_türü == "sembolik": bileşik_bitti = True
	if soru_türü == "bileşik":  sembolik_bitti = True

def str_to_list(string):
	return string.split(sep=None, maxsplit=0)

def soru_turu_sor():
	global soru_türü
	print(soru_türü_açıklaması, end="")
	while True:
		user_cevap = input("$ ").casefold()
		
		if user_cevap == "random" or user_cevap == "sembolik" or user_cevap == "bileşik":
			soru_türü = user_cevap
			break
		elif f"{user_cevap}" == '':
			print(f"bir şey yazılmadı, default olarak soru türü \"{soru_türü}\" olarak seçildi\n")
			break
		else: print(f"\"{user_cevap}\" bir soru türü değil, sadece \"random\", \"sembolik\" ve \"bileşik\" yazmanız lazım.")

def soru_siralamasi_sor():
	global soru_sıralaması
	print(soru_sıralaması_açıklaması, end="")
	while True:
		user_cevap = input("$ ").casefold()
		
		if user_cevap == "random" or user_cevap == "yaygın" or user_cevap == "sembolik":
			soru_sıralaması = user_cevap
			break
		elif f"{user_cevap}" == '':
			print(f"bir şey yazılmadı, default olarak soru türü \"{soru_sıralaması}\" olarak seçildi\n")
			break
		else: print(f"\"{user_cevap}\" bir soru sıralaması değil, sadece \"random\", \"yaygın\" veya \"sembolik\" yazmanız lazım.")

def tahmin(yaygın_adı,sembolik_formülü):
	global puan, soru
	if soru_sıralaması == "random":
		random_int = ri(0,1)
		if random_int == 0:
			başlık = yaygın_adı
			cevap = sembolik_formülü
		if random_int == 1:
			başlık = sembolik_formülü
			cevap = yaygın_adı
	elif soru_sıralaması == "yaygın":
		başlık = yaygın_adı
		cevap = sembolik_formülü
	elif soru_sıralaması == "sembolik":
		başlık = sembolik_formülü
		cevap = yaygın_adı
	else:
		print(f"\"{soru_sıralaması}\" diye bir soru sıralaması bulunamadı. geçerli soru sıralamaları: random, yaygın, sembolik (hepsinin açıklaması kaynak kodda)")
		exit(1)
	
	if ' / ' in cevap: cevap = cevap.split(' / ')
	if not isinstance(cevap,list): cevap = str_to_list(cevap)

	soru += 1
	user_cevap = input(f"puanın: {puan}\n{soru}) {başlık}\n$ ") or 'n'
	
	if user_cevap in cevap:
		print("afferim, doğru cevap! (+10 puan)")
		puan += 10
		return True
	elif user_cevap.casefold() in ["exit","çık","çıkış"]:
		print("oynadığın için teşekkür ederim, görüşürüz. 👋")
		exit(0)
	elif puan <= 0:
		print("üzgünüm, yanlış cevap.")
		return False
	else:
		print("üzgünüm, yanlış cevap (-5 puan)")
		puan -= 5
		return False

def oyunu_baslat():
	global bileşik_bitti,sembolik_bitti
	while True:
		if len(sembolik_yaygın) <= 0: sembolik_bitti = True
		if len(bileşik_yaygın) <= 0: bileşik_bitti = True
		
		if soru_türü == "random":
			random_int = ri(0,1)
		
			if not bileşik_bitti and random_int == 0:
				sor = ri(0,len(bileşik_yaygın)-1)
				if tahmin(bileşik_yaygın[sor],bileşik[sor]):
					bileşik_yaygın.pop(sor)
					bileşik.pop(sor)

			if not sembolik_bitti and random_int == 1:
				sor = ri(0,len(sembolik_yaygın)-1)
				if tahmin(sembolik_yaygın[sor],sembolik[sor]):
					sembolik_yaygın.pop(sor)
					sembolik.pop(sor)

		if not bileşik_bitti and soru_türü == "bileşik":
			sor = ri(0,len(bileşik_yaygın)-1)
			if tahmin(bileşik_yaygın[sor],bileşik[sor]):
				bileşik_yaygın.pop(sor)
				bileşik.pop(sor)
		
		if not sembolik_bitti and soru_türü == "sembolik":
			sor = ri(0,len(sembolik_yaygın)-1)
			if tahmin(sembolik_yaygın[sor],sembolik[sor]):
				sembolik_yaygın.pop(sor)
				sembolik.pop(sor)
		
		if bileşik_bitti and sembolik_bitti:
			print(f"puanın: {puan}\noyunu oynadığınız için teşekkürler, umarım ezberlemenizde yardımcı olmuşumdur ve umarım eğlenmişsinizdir.")
			exit(0)

if __name__ == '__main__':
	if sor:
		soru_turu_sor()
		soru_siralamasi_sor()
	init()

	oyunu_baslat()
