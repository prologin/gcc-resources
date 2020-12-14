TARGETS = \
	00_mu-tutoriel.pdf \
	01_decouverte_micropython.pdf \
	01_decouverte.pdf \
	01_decouverte_micropython.pdf \
	02_listes_et_string.pdf \
	03_reseau.pdf \
	04_objet.pdf \
	04_web.pdf \
	04_web_boni.pdf \
	05_projet_jeu.pdf \
	05_projet_microbit.pdf \
	bonus_python_avance.pdf \
	bonus_unix.pdf

DIRS = \
	00_mu-tutoriel \
	01_decouverte_micropython \
	01_decouverte \
	01_decouverte_micropython \
	02_listes_et_string \
	03_reseau \
	04_objet \
	04_web \
	04_web_boni \
	05_projet_jeu \
	05_projet_microbit \
	bonus_python_avance \
	bonus_unix

COLLECT_DIR = build

all: $(addprefix $(COLLECT_DIR)/, $(TARGETS))

$(COLLECT_DIR)/%.pdf:
	make -C $*
	mkdir -p $(COLLECT_DIR)
	cp $*/$*.pdf $@

clean:
	for dir in $(DIRS); do \
	    make clean -C $$dir; \
	done
	rm -rf $(COLLECT_DIR)
