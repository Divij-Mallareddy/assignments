class KCR:
    def kcr_amount(self):
        print(f"Amount : {5000}")
class YSJAGAN:
    def ysjagan_amount(self):
        print(f"Amount : {8000}")
class byjus:
    def byjus_ad(self):
        print(f"Amount : {9000}")
class society:
    def society_amount(self):
        print(f"Amount : {3000}")
class Pv_sindhu(KCR,YSJAGAN,byjus,society):
    def sindhu_bank(self):
        print(f"Amount : {10000}")

obj = Pv_sindhu()
obj.kcr_amount()
obj.ysjagan_amount()
obj.society_amount()
obj.byjus_ad()
obj.sindhu_bank()
