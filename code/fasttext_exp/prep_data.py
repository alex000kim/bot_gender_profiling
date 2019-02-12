import argparse
import glob
import os
import random
import xml.etree.ElementTree
from pathlib import Path

import pandas as pd


def prep_all_data(xml_files, df_truth, clean_data_path, train_test_split):
    random.shuffle(xml_files)
    train_xml_files = xml_files[:int(train_test_split * len(xml_files))]
    test_xml_files = xml_files[int(train_test_split * len(xml_files)):]
    for train_or_test, xml_file_files in [['train', train_xml_files], ['test', test_xml_files]]:
        df_lst = []
        for xml_fpath in xml_file_files:
            author_id = os.path.basename(xml_fpath).split('.')[0]
            gender = df_truth.loc[df_truth['author_id'] == author_id]['gender'].values[0]
            bot_human = df_truth.loc[df_truth['author_id'] == author_id]['bot_human'].values[0]
            xml_root = xml.etree.ElementTree.parse(xml_fpath).getroot()
            bot_human_label = f'__label__{bot_human}'
            gender_label = f'__label__{gender}'
            author_data = {'bot_human': bot_human_label, 'gender': gender_label, 'text': []}
            for doc in xml_root[0]:
                text = doc.text.replace('\n', "").replace('"', '')
                author_data['text'].append(text)
            df = pd.DataFrame(author_data)
            df_lst.append(df)
        all_dfs = pd.concat(df_lst)
        bot_human_data_path = str(clean_data_path / f'{train_or_test}_bot_human_data.txt')
        gender_data_path = str(clean_data_path / f'{train_or_test}_gender_data.txt')
        all_dfs.to_csv(bot_human_data_path, columns=['bot_human', 'text'], index=False,
                       header=False, sep=' ')
        all_dfs.to_csv(gender_data_path, columns=['bot_human', 'text'], index=False,
                       header=False, sep=' ')


if __name__ == '__main__':
    random.seed(0)
    parser = argparse.ArgumentParser(description='Prepare data in fasttext format')
    parser.add_argument('--lang',
                        required=True,
                        type=str,
                        choices=['en', 'es'],
                        help='Language: en or es')
    parser.add_argument('--train_test_split',
                        type=float,
                        default=0.8,
                        help='Train/test split ration. Default is 0.8')

    args = parser.parse_args()
    lang = args.lang
    train_test_split = args.train_test_split
    proj_path = Path(__file__).parents[2]
    raw_data_path = proj_path / 'data'
    clean_data_path = proj_path / f'clean_data_fasttext_{lang}'
    os.makedirs(clean_data_path, exist_ok=True)
    lang_data_path = raw_data_path / lang
    xml_files = glob.glob(str(lang_data_path / '*.xml'))
    df_truth = pd.read_csv(lang_data_path / 'truth.txt', sep=':::', names=['author_id', 'bot_human', 'gender'],
                           engine='python')
    prep_all_data(xml_files, df_truth, clean_data_path, train_test_split)
