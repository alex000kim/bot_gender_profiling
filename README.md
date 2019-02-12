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
$ python code/fasttext_exp/prep_data.py --lang en
```
2. Train fasttext classifier.
```bash
$ fasttext supervised -input clean_data_fasttext_en/train_bot_human_data.txt -output clean_data_fasttext_en/bot_human_model
Read 5M words
Number of words:  672512
Number of labels: 2
Progress: 100.0%  words/sec/thread: 2266008  lr: 0.000000  loss: 0.163347  eta: 0h0m
$ fasttext supervised -input clean_data_fasttext_en/train_gender_data.txt -output clean_data_fasttext_en/gender_model
Read 2M words
Number of words:  397698
Number of labels: 2
Progress: 100.0%  words/sec/thread: 2356782  lr: 0.000000  loss: 0.343561  eta: 0h0m
Progress: 100.0%  words/sec/thread: 2395386  lr: 0.000000  loss: 0.147270  eta: 0h0m
```
3. Test.
```bash
$ fasttext test clean_data_fasttext_en/bot_human_model.bin clean_data_fasttext_en/test_bot_human_data.txt
N	82400
P@1	0.914
R@1	0.914
Number of examples: 82400
$ fasttext test clean_data_fasttext_en/gender_model.bin clean_data_fasttext_en/test_gender_data.txt
N	41600
P@1	0.756
R@1	0.756
Number of examples: 41600
```
