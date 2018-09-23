import click
from openpyxl import load_workbook
from openpyxl import Workbook
from bs4 import BeautifulSoup
@click.command()
@click.argument('src',type=str)
@click.argument('dst',type=str)
def cli(src,dst):
	with open(src) as fp:
		nw=Workbook()
		new=nw.active
		soup=BeautifulSoup(fp,"html.parser")
		da=soup.find_all('tr')
		h=[c for c in da[0].find_all('th')]
		new.append([e.text.encode('utf-8') for e in h[1:]])
		for x in da[1:]:
			z=[c for c in x.find_all('td')]
			new.append([e.text.encode('utf-8') for e in z[1:]])
		nw.save(dst)
if __name__=='__main__':
    cli()