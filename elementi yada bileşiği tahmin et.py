#!/usr/bin/env python

from random import randint as ri

puan = 0
soru = 0
soru_türü = "random"
"""
random   = altdakkilerden birini sorar (her seferinde değişir)
sembolik = sembollerden sorar (C, O, H gibi)
bileşik  = bileşiklerden sorar (H2O gibi)
"""

sembolik = ['C', 'H', 'O']
sembolik_yaygın = ["karbon", "hidrojen", "oksijen"]

bileşik = ['H2O','HCI','H3PO4']
bileşik_yaygın = ['su','tuz ruhu','fosforik asit']

soru_sıralaması = "random"
"""
random   = altdakilerden birini yapar (her seferinde değişir)
yaygın   = yaygın sorup sembolik halini cevap olarak ister ("tuz ruhu" cevap:HCI gibi)
sembolik = sembolik sorup yaygın halini cevap olarak ister(HCI cevap:"tuz ruhu" gibi)
"""


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
    soru += 1
    user_cevap = input(f"puanın: {puan}\n{soru}) {başlık}\n$ ")
    if user_cevap == cevap:
        print("afferim, doğru cevap! (+10 puan)")
        puan += 10
    else:
        if puan <= 0: print("üzgünüm, yanlış cevap.")
        else:
            print("üzgünüm, yanlış cevap (-5 puan)")
            puan -= 5
            


if __name__ == '__main__':
    while True:
        if soru_türü == "random":
            random_int = ri(0,1)
            if random_int == 0:
                sor = ri(0,len(bileşik_yaygın)-1)
                tahmin(bileşik_yaygın[sor],bileşik[sor])
            if random_int == 1:
                sor = ri(0,len(sembolik_yaygın)-1)
                tahmin(sembolik_yaygın[sor],sembolik[sor])
        elif soru_türü == "bileşik":
            sor = ri(0,len(bileşik_yaygın)-1)
            tahmin(bileşik_yaygın[sor],bileşik[sor])
        elif soru_türü == "sembolik":
            sor = ri(0,len(sembolik_yaygın)-1)
            tahmin(sembolik_yaygın[sor],sembolik[sor])
