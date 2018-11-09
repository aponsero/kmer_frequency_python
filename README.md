# kmer_frequency_python
Python script to compute kmer frequency profile from Fasta formated sequences

## Dependencies
This script requires the installation of the biopython library : https://biopython.org/wiki/Download

For recent versions of Python (starting with Python 2.7.9 and Python 3.4), try:

```bash
pip install biopython
```

## Quick start
Run the exemple file (2000 sequences) using a kmer size of 4.

```bash
DB="file_test.fasta"
KM_SIZE=4
RUN="kmer_freq.py"
OUT="test_expected.tab"

python3 $RUN -f $DB -k $KM_SIZE > $OUT
```

The expected result is available under the name "test_expected.tab"
