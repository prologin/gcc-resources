all: 05_projet_jeu.pdf

05_projet_jeu.pdf: subject_content.tex old_template.tex
	latexmk -xelatex -shell-escape -pdf old_template.tex
	mv old_template.pdf 05_projet_jeu.pdf

clean:
	latexmk -C -f
	rm -rf _minted-old_template
