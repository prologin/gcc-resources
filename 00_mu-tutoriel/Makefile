.PHONY: all

SUBJECT = 00_mu-tutoriel

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
