abone_varmı = "E"
abone_sayısı = 0
konut_hane_sayısı_toplam = 0
işyeri_abone_sayısı = 0
resmi_daire_abone_sayısı = 0
organize_sanayi_abone_sayısı = 0
tarım_hayvan_sulama_abone_sayısı = 0
konut_hane_su_tüketim_miktarı = 0
konut_hane_sayısı_kademe1_toplam = 0
konut_hane_sayısı_kademe2_toplam = 0
konut_hane_sayısı_kademe3_toplam = 0
konut_hane_su_tüketim_miktarı_kademe1 = 0
konut_hane_su_tüketim_miktarı_kademe2 = 0
konut_hane_su_tüketim_miktarı_kademe3 = 0
tarımsal_50den_fazla = 0 #Aylık su tüketim miktarı 50 tondan fazla olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı
aylık_100ton_veya_500tl = 0 #Aylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin (hanelerin) sayısı
indirimli_hane_sayısı = 0
engelli_hane_sayısı = 0
resmi_daire_su_tüketim_max = 0
resmi_daire_abone_no_max = 0
su_tüketim_ücreti_max = 0
su_tüketim_ücreti_max_abone_no = 0
su_tüketim_ücreti_max_miktarı = 0
su_tüketim_miktarı_toplam = 0
resmi_daire_su_tüketim = 0
işyeri_su_tüketim = 0
organize_sanayi_su_tüketim = 0
tarım_hayvan_su_tüketim = 0
konut_hane_su_ücreti = 0
işyeri_su_ücreti = 0
resmi_daire_su_ücreti = 0
organize_sanayi_su_ücreti = 0
tarım_hayvan_su_ücreti = 0

izsu_payı_toplam = 0
ilçe_payı_toplam = 0
büyükşehir_payı = 0
devlet_payı = 0
abone_tipi_adı_max = ""
while(abone_varmı == "E" or abone_varmı == "e"):
    abone_sayısı += 1
    abone_no = int(input("Abone numaranızı giriniz: "))
    print("***************************")
    print("(1)Konut \n(2)İşyeri \n(3)Resmi Daire \n(4)Organize Sanayi \n(5)İlçe Tarımsal ve Hayvan Sulama")
    print("***************************")
    while True:
        abone_tipi_kodu = int(input("Abone tipi kodunu giriniz: "))
        if (abone_tipi_kodu > 5 and abone_tipi_kodu < 1):
            print("Hatalı kod girdiniz!")
        else:
            break
    if (abone_tipi_kodu == 1):
        while True:
            hane_sayısı = int(input("Hane sayısını giriniz:"))
            hane_sayısı_temp = hane_sayısı
            if (hane_sayısı < 1):
                print("Hatalı sayı girdiniz!")
            else:
                break
        if (hane_sayısı == 1):
            indirim_list = ["Y", "y", "Ş", "ş","S","s", "G", "g", "E", "e"]
            while True:
                indirim_durumu = input("İndirim durumunuzu giriniz: (Yok/Şehit/Gazi/Sporcu/Engelli: (Y/y/Ş/ş/G/g/S/s/E/e karakterleri))")
                if (indirim_durumu not in indirim_list):
                    print("Hatalı girdi verdiniz!")
                else:
                    break
        if (hane_sayısı > 1):
            while True:
                indirimli_sayısı = int(input("Şehit, gazi veya sporcu olan abone sayısı(Yoksa 0)"))
                engelli_sayısı = int(input("Engelli abone sayısı"))
                if (indirimli_sayısı < 0 or engelli_sayısı < 0):
                    print("Hatalı sayı girdiniz!")
                    continue
                if (indirimli_sayısı + engelli_sayısı > hane_sayısı):
                    print("Fazla değer girdiniz! Lütfen tekrar giriniz.")
                else:
                    break
        while True:
            önceki_sayac = float(input("Önceki sayaç değerini giriniz: "))
            if (önceki_sayac < 0):
                print("Hatalı veri girişi!")
                continue
            simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            while (simdiki_sayac < önceki_sayac):
                print("Hatalı veri girişi!")
                simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            while (sayac_gün_sayısı <= 0):
                print("Hatalı veri girişi!")
                sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            else:
                break
        oran_kademe1=sayac_gün_sayısı*13/30
        oran_kademe2 = sayac_gün_sayısı*20/30
    if (abone_tipi_kodu == 1):
        if(hane_sayısı == 1):
            konut_hane_sayısı_toplam += 1
            print("Abone no: ", abone_no)
            print("Abone tipi adı: Konut")
            dönemlik_su_miktarı = simdiki_sayac - önceki_sayac
            konut_hane_su_tüketim_miktarı += dönemlik_su_miktarı/sayac_gün_sayısı*30
            if (indirim_durumu == "E" or indirim_durumu == "e"):#ENGELLI INDIRIMI DÖNEMLIK SU ÜCRETI VE DÖNEMLIK ATIK SU ÜCRETINDEN KESILMIŞTIR!
                engelli_hane_sayısı += 1
                if(dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_su_ücreti = (dönemlik_su_miktarı * 2.89)/2
                    konut_hane_sayısı_kademe1_toplam += 1
                    konut_hane_su_tüketim_miktarı_kademe1 += dönemlik_su_miktarı/sayac_gün_sayısı*30
                    konut_hane_su_ücreti += dönemlik_su_ücreti/sayac_gün_sayısı*30
                elif(dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_su_ücreti = (oran_kademe1*2.89 + (dönemlik_su_miktarı-oran_kademe1)*3.13)/2
                    konut_hane_sayısı_kademe2_toplam += 1
                    konut_hane_su_tüketim_miktarı_kademe2 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                else:
                    dönemlik_su_ücreti = (oran_kademe1*2.89 + (oran_kademe2 - oran_kademe1)*3.13)/2 + ((dönemlik_su_miktarı-oran_kademe2)*6.43)
                    konut_hane_sayısı_kademe3_toplam += 1
                    konut_hane_su_tüketim_miktarı_kademe3 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                su_tüketim_miktarı_toplam += dönemlik_su_miktarı/sayac_gün_sayısı*30
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_atık_su_ücreti = (dönemlik_su_miktarı * 1.44)/2
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (dönemlik_su_miktarı - oran_kademe1) * 1.56)/2
                else:
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (oran_kademe2 - oran_kademe1) * 1.56)/2 + (dönemlik_su_miktarı - oran_kademe2) * 3.22
                if(dönemlik_su_miktarı/sayac_gün_sayısı*30 > 100 or dönemlik_su_ücreti/sayac_gün_sayısı*30 >500 ):
                    aylık_100ton_veya_500tl += 1
                print("Dönemlik su tüketim miktarı: ", format(dönemlik_su_miktarı,".2f"),"ton")
                print("Dönemlik su tüketim ücreti: ", format(dönemlik_su_ücreti,".2f"),"TL")
                print("Dönemlik atık su tüketim ücreti: ",format(dönemlik_atık_su_ücreti,".2f") ,"TL")
                print("Dönemlik toplam su tüketim ve atık su ücreti :" , format(dönemlik_su_ücreti + dönemlik_atık_su_ücreti,".2f"),"TL")
                print("Dönemlik ÇTV tutarı: ", format(dönemlik_su_miktarı*0.39,".2f"),"TL")
                print("Dönemlik katı atık toplama ücreti: ", 13,"TL")
                print("Dönemlik katı atık bertaraf ücreti: ", 2.54,"TL")
                dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + dönemlik_su_miktarı*0.39 + 13 + 2.54 +\
                        (dönemlik_su_ücreti + dönemlik_atık_su_ücreti)*8/100
                print("Dönemlik toplam fatura :", format(dönemlik_toplam_fatura,".2f") ,"TL")
                print("Dönemlik devlete aktarılacak KDV tutarı(%8): ",format((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100,".2f"), "TL")
                print("Dönemlik ilçe belediyesine aktarılacak tutar: ", format(dönemlik_su_miktarı * 0.39 + 13,".2f"), "TL")
                print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ", 2.54, "TL")
                print("Dönemlik İZSU payı: ", format(dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54),".2f"), "TL")
                devlet_payı += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                ilçe_payı_toplam += dönemlik_su_miktarı * 0.39 + 13
                büyükşehir_payı += 2.54
                izsu_payı_toplam += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54)
            elif(indirim_durumu != "Y" or indirim_durumu != "y"): #İNDIRIM DÖNEMLIK SU ÜCRETI VE DÖNEMLIK ATIK SU ÜCRETINDEN KESILMIŞTIR!
                indirimli_hane_sayısı += 1
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_su_ücreti = (dönemlik_su_miktarı * 2.89) / 2
                    konut_hane_sayısı_kademe1_toplam += 1
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_su_tüketim_miktarı_kademe1 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (dönemlik_su_miktarı - oran_kademe1) * 3.13) / 2
                    konut_hane_sayısı_kademe2_toplam += 1
                    konut_hane_su_tüketim_miktarı_kademe2 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                else:
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (oran_kademe2-oran_kademe1) * 3.13 + ((dönemlik_su_miktarı - oran_kademe2) * 6.43))/2
                    konut_hane_sayısı_kademe3_toplam += 1
                    konut_hane_su_tüketim_miktarı_kademe3 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                su_tüketim_miktarı_toplam += dönemlik_su_miktarı/sayac_gün_sayısı*30
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_atık_su_ücreti = (dönemlik_su_miktarı * 1.44) / 2
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (dönemlik_su_miktarı - oran_kademe1) * 1.56) / 2
                else:
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (oran_kademe2-oran_kademe1) * 1.56 + (dönemlik_su_miktarı - oran_kademe2) * 3.22)/2
                if (dönemlik_su_miktarı / sayac_gün_sayısı * 30 > 100 or dönemlik_su_ücreti / sayac_gün_sayısı * 30 > 500):
                    aylık_100ton_veya_500tl += 1
                print("Dönemlik su tüketim miktarı: ", format(dönemlik_su_miktarı,".2f"),"ton")
                print("Dönemlik su tüketim ücreti: ", format(dönemlik_su_ücreti, ".2f"), "TL")
                print("Dönemlik atık su tüketim ücreti: ", format(dönemlik_atık_su_ücreti, ".2f"), "TL")
                print("Dönemlik toplam su tüketim ve atık su ücreti :",format(dönemlik_su_ücreti + dönemlik_atık_su_ücreti, ".2f"), "TL")
                print("Dönemlik ÇTV tutarı: ", format(dönemlik_su_miktarı * 0.39, ".2f"), "TL")
                print("Dönemlik katı atık toplama ücreti: ", 13, "TL")
                print("Dönemlik katı atık bertaraf ücreti: ", 2.54, "TL")
                dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + dönemlik_su_miktarı * 0.39 + 13 + 2.54 + \
                                         (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                print("Dönemlik toplam fatura :", format(dönemlik_toplam_fatura, ".2f"), "TL")
                print("Dönemlik devlete aktarılacak KDV tutarı(%8): ",format((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100, ".2f"), "TL")
                print("Dönemlik ilçe belediyesine aktarılacak tutar: ", format(dönemlik_su_miktarı * 0.39 + 13, ".2f"),"TL")
                print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ", 2.54, "TL")
                print("Dönemlik İZSU payı: ", format(dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54), ".2f"), "TL")
                devlet_payı += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                ilçe_payı_toplam += dönemlik_su_miktarı * 0.39 + 13
                büyükşehir_payı += 2.54
                izsu_payı_toplam += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54)
            else:
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_su_ücreti = (dönemlik_su_miktarı * 2.89)
                    konut_hane_sayısı_kademe1_toplam += 1
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_su_tüketim_miktarı_kademe1 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (dönemlik_su_miktarı - oran_kademe1) * 3.13)
                    konut_hane_sayısı_kademe2_toplam += 1
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_su_tüketim_miktarı_kademe2 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                else:
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (oran_kademe2-oran_kademe1) * 3.13 + (dönemlik_su_miktarı - oran_kademe2 * 6.43))
                    konut_hane_sayısı_kademe3_toplam += 1
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_su_tüketim_miktarı_kademe3 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                su_tüketim_miktarı_toplam += dönemlik_su_miktarı/sayac_gün_sayısı*30
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_atık_su_ücreti = (dönemlik_su_miktarı * 1.44)
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (dönemlik_su_miktarı - oran_kademe2) * 1.56)
                else:
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (oran_kademe2-oran_kademe1) * 1.56 + (dönemlik_su_miktarı - oran_kademe2) * 3.22)
                if (dönemlik_su_miktarı / sayac_gün_sayısı * 30 > 100 or dönemlik_su_ücreti / sayac_gün_sayısı * 30 > 500):
                    aylık_100ton_veya_500tl += 1
                print("Dönemlik su tüketim miktarı: ", format(dönemlik_su_miktarı,".2f"),"ton")
                print("Dönemlik su tüketim ücreti: ", format(dönemlik_su_ücreti, ".2f"), "TL")
                print("Dönemlik atık su tüketim ücreti: ", format(dönemlik_atık_su_ücreti, ".2f"), "TL")
                print("Dönemlik toplam su tüketim ve atık su ücreti :",format(dönemlik_su_ücreti + dönemlik_atık_su_ücreti, ".2f"), "TL")
                print("Dönemlik ÇTV tutarı: ", format(dönemlik_su_miktarı * 0.39, ".2f"), "TL")
                print("Dönemlik katı atık toplama ücreti: ", 13, "TL")
                print("Dönemlik katı atık bertaraf ücreti: ", 2.54, "TL")
                dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + dönemlik_su_miktarı * 0.39 + 13 + 2.54 + \
                                         (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                print("Dönemlik toplam fatura :", format(dönemlik_toplam_fatura, ".2f"), "TL")
                print("Dönemlik devlete aktarılacak KDV tutarı(%8): ",format((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100, ".2f"), "TL")
                print("Dönemlik ilçe belediyesine aktarılacak tutar: ", format(dönemlik_su_miktarı * 0.39 + 13, ".2f"),"TL")
                print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ", 2.54, "TL")
                print("Dönemlik İZSU payı: ", format(dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54), ".2f"), "TL")
                devlet_payı += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                ilçe_payı_toplam += dönemlik_su_miktarı * 0.39 + 13
                büyükşehir_payı += 2.54
                izsu_payı_toplam += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54)

        else:
            sayı = 0
            dönemlik_su_miktarı_toplam = simdiki_sayac - önceki_sayac ; dönemlik_su_ücreti_toplam = 0 ; dönemlik_atık_su_ücreti_toplam = 0
            dönemlik_toplam_su_atık_su_ücreti_toplam = 0 ; dönemlik_ctv_tutarı = 0 ;dönemlik_katı_atık_toplam = 0 ;dönemlik_katı_atık_bertaraf_toplam = 0
            dönemlik_fatura_toplam = 0 ; dönemlik_kdv_toplam = 0 ;dönemlik_ilce = 0 ; dönemlik_büyüksehir = 0 ; dönemlik_izsu = 0
            while(sayı < indirimli_sayısı ):
                konut_hane_sayısı_toplam += 1
                indirimli_hane_sayısı += 1
                sayı += 1
                hane_sayısı_temp -=1
                dönemlik_su_miktarı = (simdiki_sayac - önceki_sayac)/hane_sayısı
                konut_hane_su_tüketim_miktarı += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                su_tüketim_miktarı_toplam += dönemlik_su_miktarı/sayac_gün_sayısı*30
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_su_ücreti = (dönemlik_su_miktarı * 2.89)
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    dönemlik_su_ücreti_toplam += dönemlik_su_ücreti
                    konut_hane_sayısı_kademe1_toplam += 1
                    konut_hane_su_tüketim_miktarı_kademe1 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (dönemlik_su_miktarı - oran_kademe1) * 3.13)
                    dönemlik_su_ücreti_toplam += dönemlik_su_ücreti
                    konut_hane_sayısı_kademe2_toplam += 1
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_su_tüketim_miktarı_kademe2 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                else:
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (oran_kademe2 - oran_kademe1) * 3.13 + ((dönemlik_su_miktarı - oran_kademe2 ) * 6.43))
                    dönemlik_su_ücreti_toplam += dönemlik_su_ücreti
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_sayısı_kademe3_toplam += 1
                    konut_hane_su_tüketim_miktarı_kademe3 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_atık_su_ücreti = (dönemlik_su_miktarı * 1.44)
                    dönemlik_atık_su_ücreti_toplam += dönemlik_atık_su_ücreti
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (dönemlik_su_miktarı - oran_kademe1) * 1.56)
                    dönemlik_atık_su_ücreti_toplam += dönemlik_atık_su_ücreti
                else:
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (oran_kademe2-oran_kademe1) * 1.56 + (dönemlik_su_miktarı - oran_kademe2) * 3.22)
                    dönemlik_atık_su_ücreti_toplam += dönemlik_atık_su_ücreti
                if (dönemlik_su_miktarı / sayac_gün_sayısı * 30 > 100 or dönemlik_su_ücreti / sayac_gün_sayısı * 30 > 500):
                    aylık_100ton_veya_500tl += 1
                dönemlik_toplam_su_atık_su_ücreti = dönemlik_su_ücreti + dönemlik_atık_su_ücreti
                dönemlik_toplam_su_atık_su_ücreti_toplam += dönemlik_toplam_su_atık_su_ücreti
                dönemlik_ctv_tutarı += dönemlik_su_miktarı * 0.39
                dönemlik_katı_atık_toplam += 13
                dönemlik_katı_atık_bertaraf_toplam = 2.54
                dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + (dönemlik_su_miktarı * 0.39) + 13 + 2.54 + \
                                         (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                dönemlik_fatura_toplam += dönemlik_toplam_fatura
                dönemlik_kdv_toplam += (dönemlik_su_ücreti+dönemlik_atık_su_ücreti)*8/100
                dönemlik_ilce += dönemlik_su_miktarı * 0.39 + 13
                dönemlik_büyüksehir += 2.54
                dönemlik_izsu += dönemlik_toplam_fatura - (((dönemlik_su_ücreti+dönemlik_atık_su_ücreti)*8/100)+(dönemlik_su_miktarı * 0.39 + 13)+2.54)
            sayı = 0
            while(sayı < engelli_sayısı):
                konut_hane_sayısı_toplam += 1
                engelli_hane_sayısı += 1
                sayı += 1
                hane_sayısı_temp -= 1
                dönemlik_su_miktarı = (simdiki_sayac - önceki_sayac) / hane_sayısı
                konut_hane_su_tüketim_miktarı += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                su_tüketim_miktarı_toplam += dönemlik_su_miktarı/sayac_gün_sayısı*30
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_su_ücreti = (dönemlik_su_miktarı * 2.89) / 2
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    dönemlik_su_ücreti_toplam += dönemlik_su_ücreti
                    konut_hane_sayısı_kademe1_toplam += 1
                    konut_hane_su_tüketim_miktarı_kademe1 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (dönemlik_su_miktarı - oran_kademe1) * 3.13) / 2
                    dönemlik_su_ücreti_toplam += dönemlik_su_ücreti
                    konut_hane_sayısı_kademe2_toplam += 1
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_su_tüketim_miktarı_kademe2 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                else:
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (oran_kademe2-oran_kademe1) * 3.13) / 2 + (dönemlik_su_miktarı - oran_kademe2 * 6.43)
                    dönemlik_su_ücreti_toplam += dönemlik_su_ücreti
                    konut_hane_sayısı_kademe3_toplam += 1
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_su_tüketim_miktarı_kademe3 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_atık_su_ücreti = (dönemlik_su_miktarı * 1.44) / 2
                    dönemlik_atık_su_ücreti_toplam += dönemlik_atık_su_ücreti
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (dönemlik_su_miktarı - oran_kademe1) * 1.56) / 2
                    dönemlik_atık_su_ücreti_toplam += dönemlik_atık_su_ücreti
                else:
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (oran_kademe2-oran_kademe1) * 1.56) / 2 + (dönemlik_su_miktarı - oran_kademe2) * 3.22
                    dönemlik_atık_su_ücreti_toplam += dönemlik_atık_su_ücreti
                if (dönemlik_su_miktarı / sayac_gün_sayısı * 30 > 100 or dönemlik_su_ücreti / sayac_gün_sayısı * 30 > 500):
                    aylık_100ton_veya_500tl += 1
                dönemlik_toplam_su_atık_su_ücreti = dönemlik_su_ücreti + dönemlik_atık_su_ücreti
                dönemlik_toplam_su_atık_su_ücreti_toplam += dönemlik_toplam_su_atık_su_ücreti
                dönemlik_ctv_tutarı += dönemlik_su_miktarı * 0.39
                dönemlik_katı_atık_toplam += 13
                dönemlik_katı_atık_bertaraf_toplam += 2.54
                dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + (dönemlik_su_miktarı * 0.39) + 13 + 2.54 + \
                                         (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                dönemlik_fatura_toplam += dönemlik_toplam_fatura
                dönemlik_kdv_toplam += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                dönemlik_ilce += dönemlik_su_miktarı * 0.39 + 13
                dönemlik_büyüksehir += 2.54
                dönemlik_izsu += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54)
            sayı = 0
            while(sayı < hane_sayısı_temp):
                konut_hane_sayısı_toplam += 1
                sayı += 1
                dönemlik_su_miktarı = (simdiki_sayac - önceki_sayac) / hane_sayısı
                konut_hane_su_tüketim_miktarı += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                su_tüketim_miktarı_toplam += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_su_ücreti = (dönemlik_su_miktarı * 2.89)
                    dönemlik_su_ücreti_toplam += dönemlik_su_ücreti
                    konut_hane_sayısı_kademe1_toplam += 1
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_su_tüketim_miktarı_kademe1 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (dönemlik_su_miktarı - oran_kademe1) * 3.13)
                    dönemlik_su_ücreti_toplam += dönemlik_su_ücreti
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_sayısı_kademe2_toplam += 1
                    konut_hane_su_tüketim_miktarı_kademe2 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                else:
                    dönemlik_su_ücreti = (oran_kademe1 * 2.89 + (oran_kademe2-oran_kademe2) * 3.13 + (dönemlik_su_miktarı - oran_kademe2 * 6.43))
                    dönemlik_su_ücreti_toplam += dönemlik_su_ücreti
                    konut_hane_sayısı_kademe3_toplam += 1
                    konut_hane_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
                    konut_hane_su_tüketim_miktarı_kademe3 += dönemlik_su_miktarı / sayac_gün_sayısı * 30
                if (dönemlik_su_miktarı <= oran_kademe1):
                    dönemlik_atık_su_ücreti = (dönemlik_su_miktarı * 1.44)
                    dönemlik_atık_su_ücreti_toplam += dönemlik_atık_su_ücreti
                elif (dönemlik_su_miktarı <= oran_kademe2):
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (dönemlik_su_miktarı - oran_kademe1) * 1.56)
                    dönemlik_atık_su_ücreti_toplam += dönemlik_atık_su_ücreti
                else:
                    dönemlik_atık_su_ücreti = (oran_kademe1 * 1.44 + (oran_kademe2-oran_kademe1) * 1.56 + (dönemlik_su_miktarı - oran_kademe2) * 3.22)
                    dönemlik_atık_su_ücreti_toplam += dönemlik_atık_su_ücreti
                if (dönemlik_su_miktarı / sayac_gün_sayısı * 30 > 100 or dönemlik_su_ücreti / sayac_gün_sayısı * 30 > 500):
                    aylık_100ton_veya_500tl += 1
                dönemlik_toplam_su_atık_su_ücreti = dönemlik_su_ücreti + dönemlik_atık_su_ücreti
                dönemlik_toplam_su_atık_su_ücreti_toplam += dönemlik_toplam_su_atık_su_ücreti
                dönemlik_ctv_tutarı += dönemlik_su_miktarı * 0.39
                dönemlik_katı_atık_toplam += 13
                dönemlik_katı_atık_bertaraf_toplam = 2.54
                dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + (dönemlik_su_miktarı * 0.39) + 13 + 2.54 + \
                                         (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                dönemlik_fatura_toplam += dönemlik_toplam_fatura
                dönemlik_kdv_toplam += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
                dönemlik_ilce += dönemlik_su_miktarı * 0.39 + 13
                dönemlik_büyüksehir += 2.54
                dönemlik_izsu += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + ( dönemlik_su_miktarı * 0.39 + 13) + 2.54)
            print("Abone no:",abone_no)
            print("Abone tipi adı: Karışık Grup")
            print("Dönemlik su tüketim miktarı: ",format(dönemlik_su_miktarı_toplam,".2f"),"ton")
            print("Dönemlik su tüketim ücreti: ", format(dönemlik_su_ücreti_toplam,".2f"),"TL")
            print("Dönemlik atık su ücreti: ", format(dönemlik_atık_su_ücreti_toplam,".2f"),"TL")
            print("Dönemlik toplam su tüketim ve atık su ücreti", format(dönemlik_toplam_su_atık_su_ücreti_toplam,".2f"),"TL")
            print("Dönemlik ÇTV tutarı: ",format(dönemlik_ctv_tutarı,".2f"),"TL")
            print("Dönemlik katı atık toplama ücreti: ",format(dönemlik_katı_atık_toplam,".2f"),"TL")
            print("Dönemlik katı atık bertaraf ücreti: ",format(dönemlik_katı_atık_bertaraf_toplam,".2f"),"TL")
            print("Dönemlik toplam fatura tutarı: ",format(dönemlik_fatura_toplam,".2f"),"TL")
            print("Dönemlik devlete aktarılacak KDV tutarı (%8): ",format(dönemlik_kdv_toplam,".2f"),"TL")
            print("Dönemlik ilçe belediyesine aktarılacak tutar: ", format(dönemlik_ilce,".2f"),"TL")
            print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ",format(dönemlik_büyüksehir,".2f"),"TL")
            print("Dönemlik İZSU payı",format(dönemlik_izsu,".2f"),"TL")
            devlet_payı += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
            ilçe_payı_toplam += dönemlik_su_miktarı * 0.39 + 13
            büyükşehir_payı += 2.54
            izsu_payı_toplam += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54)
    elif(abone_tipi_kodu == 2):
        işyeri_abone_sayısı += 1
        while True:
            önceki_sayac = float(input("Önceki sayaç değerini giriniz: "))
            if (önceki_sayac < 0):
                print("Hatalı veri girişi!")
                continue
            simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            while (simdiki_sayac < önceki_sayac):
                print("Hatalı veri girişi!")
                simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            while (sayac_gün_sayısı <= 0):
                print("Hatalı veri girişi!")
                sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            else:
                break
        print("Abone no: ",abone_no)
        print("Abone tipi adı: İşyeri")
        dönemlik_su_miktarı = simdiki_sayac - önceki_sayac
        işyeri_su_tüketim += dönemlik_su_miktarı/sayac_gün_sayısı*30
        print("Dönemlik su tüketim miktarı: ", format(dönemlik_su_miktarı,".2f"),"ton")
        su_tüketim_miktarı_toplam += dönemlik_su_miktarı / sayac_gün_sayısı * 30
        dönemlik_su_ücreti = dönemlik_su_miktarı * 7.38
        if (dönemlik_su_miktarı / sayac_gün_sayısı * 30 > 100 or dönemlik_su_ücreti / sayac_gün_sayısı * 30 > 500):
            aylık_100ton_veya_500tl += 1
        print("Dönemlik su tüketim ücreti: ",format(dönemlik_su_ücreti,".2f"),"TL")
        işyeri_su_ücreti += dönemlik_su_ücreti/sayac_gün_sayısı*30
        dönemlik_atık_su_ücreti = dönemlik_su_miktarı * 3.68
        print("Dönemlik toplam su tüketim ve atık su ücreti: ", format(dönemlik_atık_su_ücreti+dönemlik_su_ücreti,".2f"),"TL")
        print("Dönemlik ÇTV tutarı:", format(dönemlik_su_miktarı * 0.39,".2f"),"TL")
        print("Dönemlik katı atık toplama ücreti: ",13,"TL")
        print("Dönemlik katı atık bertaraf ücreti: ",2.54,"TL")
        dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + (dönemlik_su_miktarı * 0.39) + 13 + 2.54 + \
                                 (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
        print("Dönemlik toplam fatura tutarı: ",format(dönemlik_toplam_fatura,".2f"),"TL")
        print("Dönemlik devlete aktarılacak KDV tutarı(%8): ", format((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100,".2f"),"TL")
        print("Dönemlik ilçe belediyesine aktarılacak tutar: ", format(dönemlik_su_miktarı * 0.39 + 13,".2f"), "TL")
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ", 2.54, "TL")
        print("Dönemlik İZSU payı: ", format(dönemlik_toplam_fatura -
                                             (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54),".2f"),"TL")
        devlet_payı += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
        ilçe_payı_toplam += dönemlik_su_miktarı * 0.39 + 13
        büyükşehir_payı += 2.54
        izsu_payı_toplam += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54)
        if(dönemlik_su_ücreti/sayac_gün_sayısı*30 > su_tüketim_ücreti_max):
            su_tüketim_ücreti_max = dönemlik_su_ücreti/sayac_gün_sayısı*30
            su_tüketim_ücreti_max_abone_no = abone_no
            abone_tipi_adı_max = "İşyeri"
            su_tüketim_ücreti_max_miktarı = dönemlik_su_miktarı/sayac_gün_sayısı*30
    elif(abone_tipi_kodu == 3):
        resmi_daire_abone_sayısı += 1
        while True:
            önceki_sayac = float(input("Önceki sayaç değerini giriniz: "))
            if (önceki_sayac < 0):
                print("Hatalı veri girişi!")
                continue
            simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            while (simdiki_sayac < önceki_sayac):
                print("Hatalı veri girişi!")
                simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            while (sayac_gün_sayısı <= 0):
                print("Hatalı veri girişi!")
                sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            else:
                break
        print("Abone no: ",abone_no)
        print("Abone tipi adı: Resmi Daire")
        dönemlik_su_miktarı = simdiki_sayac - önceki_sayac
        print("Dönemlik su tüketim miktarı: ", format(dönemlik_su_miktarı,".2f"),"ton")
        resmi_daire_su_tüketim += dönemlik_su_miktarı/sayac_gün_sayısı*30
        su_tüketim_miktarı_toplam += dönemlik_su_miktarı / sayac_gün_sayısı * 30
        dönemlik_su_ücreti = dönemlik_su_miktarı * 4.34
        if (dönemlik_su_miktarı / sayac_gün_sayısı * 30 > 100 or dönemlik_su_ücreti / sayac_gün_sayısı * 30 > 500):
            aylık_100ton_veya_500tl += 1
        print("Dönemlik su tüketim ücreti: ",format(dönemlik_su_ücreti,".2f"),"TL")
        resmi_daire_su_ücreti += dönemlik_su_ücreti/sayac_gün_sayısı*30
        dönemlik_atık_su_ücreti = dönemlik_su_miktarı * 2.16
        print("Dönemlik toplam su tüketim ve atık su ücreti: ", format(dönemlik_atık_su_ücreti+dönemlik_su_ücreti,".2f"),"TL")
        print("Dönemlik ÇTV tutarı:", format(dönemlik_su_miktarı * 0.39,".2f"),"TL")
        print("Dönemlik katı atık toplama ücreti: ",13,"TL")
        print("Dönemlik katı atık bertaraf ücreti: ",2.54,"TL")
        dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + (dönemlik_su_miktarı * 0.39) + 13 + 2.54 + \
                                 (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
        print("Dönemlik toplam fatura tutarı: ",format(dönemlik_toplam_fatura,".2f"),"TL")
        print("Dönemlik devlete aktarılacak KDV tutarı(%8): ", format((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100,".2f"),"TL")
        print("Dönemlik ilçe belediyesine aktarılacak tutar: ", format(dönemlik_su_miktarı * 0.39 + 13,".2f"), "TL")
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ", 2.54, "TL")
        print("Dönemlik İZSU payı: ",format(dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54),".2f"),"TL")
        devlet_payı += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
        ilçe_payı_toplam += dönemlik_su_miktarı * 0.39 + 13
        büyükşehir_payı += 2.54
        izsu_payı_toplam += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54)
        if (dönemlik_su_ücreti / sayac_gün_sayısı * 30 > su_tüketim_ücreti_max):
            su_tüketim_ücreti_max = dönemlik_su_ücreti / sayac_gün_sayısı * 30
            su_tüketim_ücreti_max_abone_no = abone_no
            abone_tipi_adı_max = "Resmi Daire"
            su_tüketim_ücreti_max_miktarı = dönemlik_su_miktarı / sayac_gün_sayısı * 30
        if(dönemlik_su_ücreti/sayac_gün_sayısı*30 > resmi_daire_su_tüketim_max):
            resmi_daire_su_tüketim_max = dönemlik_su_miktarı/sayac_gün_sayısı*30
            resmi_daire_abone_no_max = abone_no
    elif(abone_tipi_kodu == 4):
        organize_sanayi_abone_sayısı += 1
        while True:
            önceki_sayac = float(input("Önceki sayaç değerini giriniz: "))
            if (önceki_sayac < 0):
                print("Hatalı veri girişi!")
                continue
            simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            while (simdiki_sayac < önceki_sayac):
                print("Hatalı veri girişi!")
                simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            while (sayac_gün_sayısı <= 0):
                print("Hatalı veri girişi!")
                sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            else:
                break
        print("Abone no: ",abone_no)
        print("Abone tipi adı: Organize Sanayi")
        dönemlik_su_miktarı = simdiki_sayac - önceki_sayac
        organize_sanayi_su_tüketim = dönemlik_su_miktarı /sayac_gün_sayısı*30
        print("Dönemlik su tüketim miktarı: ", format(dönemlik_su_miktarı,".2f"),"ton")
        su_tüketim_miktarı_toplam += dönemlik_su_miktarı / sayac_gün_sayısı * 30
        dönemlik_su_ücreti = dönemlik_su_miktarı * 5
        if (dönemlik_su_miktarı / sayac_gün_sayısı * 30 > 100 or dönemlik_su_ücreti / sayac_gün_sayısı * 30 > 500):
            aylık_100ton_veya_500tl += 1
        print("Dönemlik su tüketim ücreti: ",format(dönemlik_su_ücreti,".2f"),"TL")
        organize_sanayi_su_ücreti += dönemlik_su_ücreti/sayac_gün_sayısı*30
        dönemlik_atık_su_ücreti = dönemlik_su_miktarı * 2.5
        print("Dönemlik toplam su tüketim ve atık su ücreti: ", format(dönemlik_atık_su_ücreti+dönemlik_su_ücreti,".2f"),"TL")
        print("Dönemlik ÇTV tutarı:", format(dönemlik_su_miktarı * 0.39,".2f"),"TL")
        print("Dönemlik katı atık toplama ücreti: ",13,"TL")
        print("Dönemlik katı atık bertaraf ücreti: ",2.54,"TL")
        dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + (dönemlik_su_miktarı * 0.39) + 13 + 2.54 + \
                                 (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
        print("Dönemlik toplam fatura tutarı: ",format(dönemlik_toplam_fatura,".2f"),"TL")
        print("Dönemlik devlete aktarılacak KDV tutarı(%8): ", format((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100,".2f"),"TL")
        print("Dönemlik ilçe belediyesine aktarılacak tutar: ", format(dönemlik_su_miktarı * 0.39 + 13,".2f"), "TL")
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ", 2.54, "TL")
        print("Dönemlik İZSU payı: ", format(dönemlik_toplam_fatura -
                                             (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54),".2f"),"TL")
        devlet_payı += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
        ilçe_payı_toplam += dönemlik_su_miktarı * 0.39 + 13
        büyükşehir_payı += 2.54
        izsu_payı_toplam += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54)
        if (dönemlik_su_ücreti / sayac_gün_sayısı * 30 > su_tüketim_ücreti_max):
            su_tüketim_ücreti_max = dönemlik_su_ücreti / sayac_gün_sayısı * 30
            su_tüketim_ücreti_max_abone_no = abone_no
            abone_tipi_adı_max = "Organize Sanayi"
            su_tüketim_ücreti_max_miktarı = dönemlik_su_miktarı / sayac_gün_sayısı * 30
    elif(abone_tipi_kodu == 5):
        tarım_hayvan_sulama_abone_sayısı+=1
        while True:
            önceki_sayac = float(input("Önceki sayaç değerini giriniz: "))
            if (önceki_sayac < 0):
                print("Hatalı veri girişi!")
                continue
            simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            while (simdiki_sayac < önceki_sayac):
                print("Hatalı veri girişi!")
                simdiki_sayac = float(input("Şimdiki sayaç değerini giriniz: "))
            sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            while (sayac_gün_sayısı <= 0):
                print("Hatalı veri girişi!")
                sayac_gün_sayısı = int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz: "))
            else:
                break
        oran_kademe1 = sayac_gün_sayısı * 13 / 30
        oran_kademe2 = sayac_gün_sayısı * 20 / 30
        print("Abone no: ",abone_no)
        print("Abone tipi adı: İlçe Tarımsal ve Hayvan Sulama")
        dönemlik_su_miktarı = simdiki_sayac - önceki_sayac
        tarım_hayvan_su_tüketim = dönemlik_su_miktarı / sayac_gün_sayısı *30
        su_tüketim_miktarı_toplam += dönemlik_su_miktarı / sayac_gün_sayısı * 30
        if(dönemlik_su_miktarı/sayac_gün_sayısı*30 > 50):
            tarımsal_50den_fazla += 1
        print("Dönemlik su tüketim miktarı: ", format(dönemlik_su_miktarı,".2f"),"ton")
        if (dönemlik_su_miktarı <= oran_kademe1):
            dönemlik_su_ücreti = (dönemlik_su_miktarı * 1.45)
            tarım_hayvan_su_ücreti += dönemlik_su_ücreti/sayac_gün_sayısı*30
        elif (dönemlik_su_miktarı <= oran_kademe2):
            dönemlik_su_ücreti = (oran_kademe1 * 1.45 + (dönemlik_su_miktarı - oran_kademe1) * 2.86)
            tarım_hayvan_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
        else:
            dönemlik_su_ücreti = (oran_kademe1 * 1.45 + (oran_kademe2-oran_kademe1) * 2.89 + (dönemlik_su_miktarı - oran_kademe2 * 6.43))
            tarım_hayvan_su_ücreti += dönemlik_su_ücreti / sayac_gün_sayısı * 30
        print("Dönemlik su tüketim ücreti: ", format(dönemlik_su_ücreti),".2f","TL")
        if (dönemlik_su_miktarı <= oran_kademe1):
            dönemlik_atık_su_ücreti = (dönemlik_su_miktarı * 0.72)
        elif (dönemlik_su_miktarı <= oran_kademe2):
            dönemlik_atık_su_ücreti = (oran_kademe1 * 0.72 + (dönemlik_su_miktarı - oran_kademe1) * 1.44)
        else:
            dönemlik_atık_su_ücreti = (oran_kademe1 * 0.72 + (oran_kademe2-oran_kademe1) * 1.44 + (dönemlik_su_miktarı - oran_kademe2) * 3.22)
        if (dönemlik_su_miktarı / sayac_gün_sayısı * 30 > 100 or dönemlik_su_ücreti / sayac_gün_sayısı * 30 > 500):
            aylık_100ton_veya_500tl += 1
        print("Dönemlik atık su tüketim ücreti: ", format(dönemlik_atık_su_ücreti,".2f"), "TL")
        print("Dönemlik toplam su tüketim ve atık su ücreti :", format(dönemlik_su_ücreti + dönemlik_atık_su_ücreti,".2f"), "TL")
        print("Dönemlik ÇTV tutarı: ", format(dönemlik_su_miktarı * 0.39,".2f"), "TL")
        print("Dönemlik katı atık toplama ücreti: ", 13, "TL")
        print("Dönemlik katı atık bertaraf ücreti: ", 2.54, "TL")
        dönemlik_toplam_fatura = dönemlik_su_ücreti + dönemlik_atık_su_ücreti + (dönemlik_su_miktarı * 0.39) + 13 + 2.54 + \
                                    (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
        print("Dönemlik toplam fatura :", format(dönemlik_toplam_fatura,".2f"), "TL")
        print("Dönemlik devlete aktarılacak KDV tutarı(%8): ", format((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100,".2f"),"TL")
        print("Dönemlik ilçe belediyesine aktarılacak tutar: ", format(dönemlik_su_miktarı * 0.39 + 13,".2f"), "TL")
        print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ", 2.54, "TL")
        print("Dönemlik İZSU payı: ",format(dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54),".2f"), "TL")
        devlet_payı += (dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100
        ilçe_payı_toplam += dönemlik_su_miktarı * 0.39 + 13
        büyükşehir_payı += 2.54
        izsu_payı_toplam += dönemlik_toplam_fatura - (((dönemlik_su_ücreti + dönemlik_atık_su_ücreti) * 8 / 100) + (dönemlik_su_miktarı * 0.39 + 13) + 2.54)
        if (dönemlik_su_ücreti / sayac_gün_sayısı * 30 > su_tüketim_ücreti_max):
            su_tüketim_ücreti_max = dönemlik_su_ücreti / sayac_gün_sayısı * 30
            su_tüketim_ücreti_max_abone_no = abone_no
            su_tüketim_ücreti_max_miktarı = dönemlik_su_miktarı / sayac_gün_sayısı * 30
            abone_tipi_adı_max = "Tarımsal ve Hayvan Sulama"
    while(True):
        abone_varmı = input("Başka abone var mı?(e/E/h/H karakterleri)")
        abone_list = ["e","E","h","H"]
        if(abone_varmı not in abone_list):
                print("Hatalı değer girdiniz")
        else:break
su_ücreti_toplam = konut_hane_su_ücreti + işyeri_su_ücreti + resmi_daire_su_ücreti + organize_sanayi_su_ücreti + tarım_hayvan_su_ücreti
print("Konut tipi abone(hane)sayısı: ",format(konut_hane_sayısı_toplam),", yüzdesi: %",format(konut_hane_sayısı_toplam/abone_sayısı*100,".2f"),
      ", aylık ortalama su tüketim miktarı: ", format(konut_hane_su_tüketim_miktarı/konut_hane_sayısı_toplam,".2f"),"ton")
print("İşyeri tipi abone sayısı: ", işyeri_abone_sayısı," yüzdesi: %",format(işyeri_abone_sayısı/abone_sayısı*100,".2f"),
      ", aylık ortalama su tüketim miktarı: ",format(işyeri_su_tüketim/işyeri_abone_sayısı,".2f"),"ton")
print("Resmi daire abone sayısı:",resmi_daire_abone_sayısı, ", yüzdesi: %",format(resmi_daire_abone_sayısı/abone_sayısı*100,".2f"),
      ", aylık ortalama su tüketim miktarı: ", format(işyeri_su_tüketim/işyeri_abone_sayısı,".2f"),"ton")
print("Organize sanayi abone sayısı:",organize_sanayi_abone_sayısı, ", yüzdesi: %",format(organize_sanayi_abone_sayısı/abone_sayısı*100,".2f"),
      ", aylık ortalama su tüketim miktarı: ", format(organize_sanayi_su_tüketim/organize_sanayi_abone_sayısı,".2f"),"ton")
print("Tarımsal ve hayvan sulama abone sayısı:",tarım_hayvan_sulama_abone_sayısı, ", yüzdesi: %",format(tarım_hayvan_sulama_abone_sayısı/abone_sayısı*100,".2f"),
      ", aylık ortalama su tüketim miktarı: ", format(tarım_hayvan_su_tüketim/tarım_hayvan_sulama_abone_sayısı,".2f"),"ton")
print("1.Kademe konut tipi abonelerin(hane)sayıları: ",konut_hane_sayısı_kademe1_toplam,", konut tipi aboneleri içindeki yüzdesi: %",
      format(konut_hane_sayısı_kademe1_toplam/konut_hane_sayısı_toplam,".2f"),", aylık ortalama su tüketim miktarı: ",
      format(konut_hane_su_tüketim_miktarı_kademe1/konut_hane_sayısı_kademe1_toplam,".2f"),"ton")
print("2.Kademe konut tipi abonelerin(hane)sayıları: ",konut_hane_sayısı_kademe2_toplam,", konut tipi aboneleri içindeki yüzdesi: %",
      format(konut_hane_sayısı_kademe2_toplam/konut_hane_sayısı_toplam,".2f"),", aylık ortalama su tüketim miktarı: ",
      format(konut_hane_su_tüketim_miktarı_kademe2/konut_hane_sayısı_kademe2_toplam,".2f"),"ton")
print("3.Kademe konut tipi abonelerin(hane)sayıları: ",konut_hane_sayısı_kademe3_toplam,", konut tipi aboneleri içindeki yüzdesi: %",
      format(konut_hane_sayısı_kademe3_toplam/konut_hane_sayısı_toplam,".2f"),", aylık ortalama su tüketim miktarı: ",
      format(konut_hane_su_tüketim_miktarı_kademe3/konut_hane_sayısı_kademe3_toplam,".2f"),"ton")
print("Aylık su tüketim miktarı 50 tondan fazla olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı: ",tarımsal_50den_fazla,
      ", ve ilçe tarımsal ve hayvan sulama tipi aboneler içindeki yüzdesi: %", format(tarımsal_50den_fazla/tarım_hayvan_sulama_abone_sayısı*100,".2f"))
print("Aylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin (hanelerin) sayısı: ",aylık_100ton_veya_500tl)
print("Şehit, gazi veya devlet sporcusu olan konut tipi abonelerin(hanelerin) sayısı: ",indirimli_hane_sayısı,
      ", ve konut tipi aboneler(haneler) içindeki yüzdeleri: %",format(indirimli_hane_sayısı/konut_hane_sayısı_toplam*100,".2f"))
print("Engelli olan konut tipi abonelerin(hanelerin) sayısı: ",engelli_hane_sayısı,
      ", ve konut tipi aboneler(haneler) içindeki yüzdeleri: %",format(engelli_hane_sayısı/konut_hane_sayısı_toplam*100,".2f"))
print("Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin abone no’su: ",resmi_daire_abone_no_max,
      " ve aylık su tüketim miktarı: ", format(resmi_daire_su_tüketim_max,".2f"),"ton")
print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin abone no’su: ",su_tüketim_ücreti_max_abone_no,
      " abone tipi adı: ",abone_tipi_adı_max, " aylık su tüketim miktarı: ",format(su_tüketim_ücreti_max_miktarı,".2f"),"ton",
      " ve ödediği aylık su tüketim ücreti: ",format(su_tüketim_ücreti_max,".2f"))
print("Konut tipi abonelerin aylık toplam su tüketim miktarı: ",format(konut_hane_su_tüketim_miktarı,".2f"),"ton",
      " Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: %",format(konut_hane_su_tüketim_miktarı/su_tüketim_miktarı_toplam*100,".2f"))
print("İşyeri tipi abonelerin aylık toplam su tüketim miktarı: ",format(işyeri_su_tüketim,".2f"),"ton",
      " Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: %",format(işyeri_su_tüketim/su_tüketim_miktarı_toplam*100,".2f"))
print("Resmi daire tipi abonelerin aylık toplam su tüketim miktarı: ",format(resmi_daire_su_tüketim,".2f"),"ton",
      " Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: %",format(resmi_daire_su_tüketim/su_tüketim_miktarı_toplam*100,".2f"))
print("Organize sanayi tipi abonelerin aylık toplam su tüketim miktarı: ",format(organize_sanayi_su_tüketim,".2f"),"ton",
      " Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: %",format(organize_sanayi_su_tüketim/su_tüketim_miktarı_toplam*100,".2f"))
print("Tarımsal ve hayvan sulama tipi abonelerin aylık toplam su tüketim miktarı: ",format(tarım_hayvan_su_tüketim,".2f"),"ton",
      " Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: %",format(tarım_hayvan_su_tüketim/su_tüketim_miktarı_toplam*100,".2f"))
print("Bornova'nın aylık su tüketim miktarı: ", format(su_tüketim_miktarı_toplam,".2f"),"ton")
print("Konut tipi abonelerden(haneler) elde edilen toplam su tüketim ücreti: ",format(konut_hane_su_ücreti,".2f"))
print("İşyeri tipi abonelerden elde edilen toplam su tüketim ücreti: ",format(işyeri_su_ücreti,".2f"))
print("Resmi daire tipi abonelerden elde edilen toplam su tüketim ücreti: ",format(resmi_daire_su_ücreti,".2f"))
print("Organize sanayi tipi abonelerden elde edilen toplam su tüketim ücreti: ",format(organize_sanayi_su_ücreti,".2f"))
print("Tarımsal ve hayvan sulama tipi abonelerden elde edilen toplam su tüketim ücreti: ",format(tarım_hayvan_su_ücreti,".2f"))
print("Tüm abonelerden elde edilen aylık toplam tu tüketim ücreti: ",format(su_ücreti_toplam,".2f"))
print("İlgili dönemde su faturalarından  İZSU'nun elde ettiği gelir : ",format(izsu_payı_toplam,".2f"))
print("İlgili dönemde su faturalarından  İlçe Belediyesi'nin elde ettiği gelir : ",format(ilçe_payı_toplam,".2f"))
print("İlgili dönemde su faturalarından  Büyükşehir Belediyesi'nin elde ettiği gelir : ",format(büyükşehir_payı,".2f"))
print("İlgili dönemde su faturalarından  Devlet'in elde ettiği gelir : ",format(devlet_payı,".2f"))


