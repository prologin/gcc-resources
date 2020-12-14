.PHONY: all

SUBJECTS = 04_web 04_web_boni

all: $(SUBJECTS:=.pdf) $(SUBJECTS:=.tex)

%.tex: %.md
	pandoc --template ../template/gcc.tex 		\
		--no-highlight 				\
		--lua-filter=../template/minted.lua	\
		-s -t latex $^ > $@

%.pdf: %.tex
	latexmk -pdf -shell-escape -xelatex $^

.PHONY: clean
clean:
	latexmk -C ${SUBJECTS:=.tex} -f
	${RM} ${SUBJECTS:=.tex}
	${RM} -rf ${SUBJECTS:%=_minted-%}
