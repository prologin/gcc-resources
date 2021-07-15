.PHONY: all

SUBJECT = 06_discord_bot

all: ${SUBJECT}.pdf ${SUBJECT}.tex

%.tex: %.md
	pandoc --template ./gcc_bot.tex 		\
		--no-highlight 				\
		--lua-filter=../template/minted.lua	\
		-s -t latex $^ > $@

%.pdf: %.tex
	latexmk -pdf -shell-escape -xelatex $^

.PHONY: clean
clean:
	latexmk -C ${SUBJECT}.tex
	${RM} ${SUBJECT}.tex
	${RM} -rf _minted-${SUBJECT}
