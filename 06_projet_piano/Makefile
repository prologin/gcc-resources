# Begin Makefile

IN = 06_projet_piano.md
TEX = $(IN:.md=.tex)
OUT = $(TEX:.tex=.pdf)

all: $(OUT)

%.tex: %.md
	@pandoc --template ../template/gcc.tex  \
            --no-highlight                      \
            --lua-filter=../template/minted.lua \
            -s -t latex -o $@ $^


%.pdf: %.tex
	@latexmk -pdf -shell-escape -xelatex $^

clean:
	latexmk -f -C $(TEX)
	$(RM) $(TEX)
	$(RM) $(OUT)
	$(RM) -r _minted-$(IN:.md=)

# End Makefile
