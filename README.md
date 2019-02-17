# Bots and Gender Profiling

Notes are in `notes.md` and are work-in-progress.

## Setup
```bash
$ conda env create -f environment.yml
$ source activate bot_gender
```
## Experiments with [fasttext](https://fasttext.cc)

1. Prepare data in the fasttext format. Splitting is performed on the author id level, i.e. all tweets of one author end up in either train or test dataset. Data preparation is done for both bot and gender detection tasks simultaneously.
```bash
$ python code/prep_data.py --out_format txt --lang en
$ python code/prep_data.py --out_format txt --lang es
```
2. Train fasttext classifier.
```bash
# english
$ fasttext supervised -input clean_data_txt_en/train_bot_human_data.txt -output clean_data_txt_en/bot_human_model
Read 5M words
Number of words:  672512
Number of labels: 2
Progress: 100.0%  words/sec/thread: 2266008  lr: 0.000000  loss: 0.163347  eta: 0h0m
$ fasttext supervised -input clean_data_txt_en/train_gender_data.txt -output clean_data_txt_en/gender_model
Read 2M words
Number of words:  397698
Number of labels: 2
Progress: 100.0%  words/sec/thread: 2356782  lr: 0.000000  loss: 0.343561  eta: 0h0m
# spanish
$ fasttext supervised -input clean_data_txt_es/train_bot_human_data.txt -output clean_data_txt_es/bot_human_model
Read 4M words
Number of words:  557394
Number of labels: 2
Progress: 100.0%  words/sec/thread: 2262350  lr: 0.000000  loss: 0.174278  eta: 0h0m
$ fasttext supervised -input clean_data_txt_es/train_gender_data.txt -output clean_data_txt_es/gender_model
Read 1M words
Number of words:  319688
Number of labels: 2
Progress: 100.0%  words/sec/thread: 2278621  lr: 0.000000  loss: 0.359351  eta: 0h0m
```
3. Test.
```bash
# english
$ fasttext test clean_data_txt_en/bot_human_model.bin clean_data_txt_en/test_bot_human_data.txt
N	82400
P@1	0.914
R@1	0.914
Number of examples: 82400
$ fasttext test clean_data_txt_en/gender_model.bin clean_data_txt_en/test_gender_data.txt
N	41600
P@1	0.756
R@1	0.756
Number of examples: 41600
# spanish
$ fasttext test clean_data_txt_es/bot_human_model.bin clean_data_txt_es/test_bot_human_data.txt
N	60000
P@1	0.899
R@1	0.899
Number of examples: 60000
$ fasttext test clean_data_txt_es/gender_model.bin clean_data_txt_es/test_gender_data.txt
N	31700
P@1	0.727
R@1	0.727
Number of examples: 31700
```

