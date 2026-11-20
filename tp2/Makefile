MATERIA := $(notdir $(abspath $(CURDIR)/..))
TP := $(notdir $(CURDIR))
OUTPUT_NAME := $(MATERIA)_$(TP)

SRC := main.tex
DATA := sources/data/data_bode_amp_ins.txt sources/data/data_bode_lpf.txt sources/data/data_bode_hpf.txt sources/data/data_bode_bpf.txt

all: $(DATA)
	latexmk -pdf -jobname=$(OUTPUT_NAME) $(SRC)

$(DATA): sources/export_bode_data.py
	python3 sources/export_bode_data.py

clean:
	latexmk -CA -jobname=$(OUTPUT_NAME) $(SRC)
	latexmk -CA $(SRC)
	rm -f *.bbl *-blx.bib *.run.xml *.synctex.gz
