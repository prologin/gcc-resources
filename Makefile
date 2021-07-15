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
	06_discord_bot.pdf \
	bonus_python_avance.pdf \
	bonus_unix.pdf

COLLECT_DIR = build

all: $(addprefix $(COLLECT_DIR)/, $(TARGETS))

$(COLLECT_DIR)/%.pdf:
	make -C $*
	mkdir -p $(COLLECT_DIR)
	cp $*/$*.pdf $@
