TMP = tmp.tex
VIEWER = mupdf -r 50

all:
	python main.py > $(TMP)
	pdflatex main.tex && $(VIEWER) main.pdf

clear:
	rm -f *aux *log *.nav *.out *.snm *.toc *.idx main.pdf tmp.tex


