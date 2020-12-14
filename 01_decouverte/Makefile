.PHONY: all

SUBJECT = 01_decouverte

all: ${SUBJECT}.pdf ${SUBJECT}.tex

%.tex: %.md
	pandoc --template ../template/gcc.tex 		\
		--no-highlight 				\
		--lua-filter=../template/minted.lua	\
		-s -t latex $^ > $@

%.pdf: %.tex
	latexmk -pdf -shell-escape -xelatex $^

.PHONY: clean
clean:
	latexmk -C ${SUBJECT}.tex -f
	${RM} ${SUBJECT}.tex
	${RM} -rf _minted-${SUBJECT}
