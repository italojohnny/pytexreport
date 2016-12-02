all:
	python main.py > tmp.tex
	pdflatex main.tex && mupdf main.pdf

clear:
	rm -f *aux *log *.nav *.out *.snm *.toc *.idx


