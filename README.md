# Bots and Gender Profiling

Notes are in `notes.md` and are work-in-progress.

## Setup
```bash
$ conda env create -f environment.yml
$ source activate bot_gender
```
## Experiments with [fasttext](https://fasttext.cc)

### Prepare data
```bash
# for fasttext
$ python code/prep_data.py --out_format txt --lang en
$ python code/prep_data.py --out_format txt --lang es
# for fastai
$ python code/prep_data.py --out_format csv --lang en --train_test_split 1.0
$ python code/prep_data.py --out_format csv --lang es --train_test_split 1.0
```

### Run notebooks with papermill
- fastai notebook:
```bash
papermill fastai_nb.ipynb papermill_out/fastai_nb_gender_en.ipynb -p LANG en -p TASK gender
papermill fastai_nb.ipynb papermill_out/fastai_nb_gender_es.ipynb -p LANG es -p TASK gender
papermill fastai_nb.ipynb papermill_out/fastai_nb_bot_human_en.ipynb -p LANG en -p TASK bot_human
papermill fastai_nb.ipynb papermill_out/fastai_nb_bot_human_es.ipynb -p LANG es -p TASK bot_human
```
For english, fastai uses wt103 pretrained model by default.
For spanish, I downloaded pretrained model from here:
https://drive.google.com/drive/folders/1CZftqrMg-MRH9yXV7FRBv6J_NOtBiK-2
See this thread for more details: https://forums.fast.ai/t/ulmfit-spanish/29715/5

- fasttext notebook:
```bash
papermill fasttext_nb.ipynb papermill_out/fasttext_nb_gender_en.ipynb -p LANG en -p TASK gender
papermill fasttext_nb.ipynb papermill_out/fasttext_nb_gender_es.ipynb -p LANG es -p TASK gender
papermill fasttext_nb.ipynb papermill_out/fasttext_nb_bot_human_en.ipynb -p LANG en -p TASK bot_human
papermill fasttext_nb.ipynb papermill_out/fasttext_nb_bot_human_es.ipynb -p LANG es -p TASK bot_human
```