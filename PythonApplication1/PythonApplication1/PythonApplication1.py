import sys 
def yasHesapla(yas):
    if yas>17 and len (sys.argv) == 2:
        sys.stdout.write("yas�n�z uygun devam edebilirsiniz")
    else:
        sys.exit("yasiniz uygun degildir, program sonland�")

yasHesapla(int (sys.argv[1]))
