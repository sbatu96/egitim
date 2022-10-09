import sys 
def yasHesapla(yas):
    if yas>17 and len (sys.argv) == 2:
        sys.stdout.write("yasýnýz uygun devam edebilirsiniz")
    else:
        sys.exit("yasiniz uygun degildir, program sonlandý")

yasHesapla(int (sys.argv[1]))
