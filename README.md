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
Progress: 100.0%  words/sec/thread: 2400512  lr: 0.000000  loss: 0.141509  eta: 0h0m
$ fasttext supervised -input clean_data_fasttext_en/train_bot_human_data.txt -output clean_data_fasttext_en/bot_human_model
Read 5M words
Number of words:  672512
Number of labels: 2
Progress: 100.0%  words/sec/thread: 2395386  lr: 0.000000  loss: 0.147270  eta: 0h0m
```
3. Test.
```bash
$ fasttext test clean_data_fasttext_en/bot_human_model.bin clean_data_fasttext_en/test_bot_human_data.txt
N	82400
P@1	0.907
R@1	0.907
Number of examples: 82400
$ fasttext test clean_data_fasttext_en/gender_model.bin clean_data_fasttext_en/test_gender_data.txt
N	82400
P@1	0.912
R@1	0.912
Number of examples: 82400
```
