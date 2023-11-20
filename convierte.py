#esta instalado en python 3813
#pip install xls2xlsx
from xls2xlsx import XLS2XLSX
x2x = XLS2XLSX("c:/Users/josen/Downloads/stock_fudo_productos_230924.xls")
wb = x2x.to_xlsx()
x2x.to_xlsx("c:/Users/josen/Downloads/stock_fudo_productos_230924.xlsx")
