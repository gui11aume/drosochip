accessions.txt:
	python query.py | \
		grep -B1 'Accession: GSM' | \
		grep -o SR.[0-9][0-9]* > accessions.txt
