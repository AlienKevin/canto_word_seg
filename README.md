# finetune-ckip-transformers
Create training files to fine-tune Hugging Face models to use with [CKIP Transformers](https://github.com/ckiplab/ckip-transformers). This is part of creating Hongkongese models using the same method.

## Overview

Hugging Face provides examples for [token classification](https://huggingface.co/docs/transformers/main/en/task_summary#token-classification). CKIP Transformers uses BI encoding to indicate word segmentation. For a sentence 點解 啊 ?, the line in the file looks like `{"words": ["點", "解", "啊", "?"], "ner": ["B", "I", "B", "B"]}`

Fine-tuning with this training data creates a model that can be loaded and used by CKIP Transformers (for non-bert models, some code changes to use different tokenizers will be needed).

## Instructions
1. Install [PyCantonese](https://pycantonese.org/) to use the HKCanCor dataset
2. Download training data from [The Second International Chinese Word Segmentation Bakeoff](http://sighan.cs.uchicago.edu/bakeoff2005/) and place cityu_training.utf8 and/or as_training.utf8 in /data
3. Run finetune_hkcancor.py and finetune_cityu.py (uncomment some lines if as_training.utf8 is used). finetune_hkcancor.json and finetune_cityu.json will be created
4. Merge/shuffle the created files if needed
5. Install Hugging Face Transformers from [source](https://github.com/huggingface/transformers/)
6. Go to transformers/examples/pytorch/token-classification/
7. Run fine-tuning with the training file `python run_ner.py --model_name_or_path toastynews/electra-hongkongese-base-discriminator --train_file finetune_hkcancor.json --output_dir tn_electra_base_hkcancor --do_train`

## Versions
The following software versions were used.
* pycantonese 3.4.0

## Results
Pycantonese
=== data/finetune_hkcancor.json performance ===
{'_': {'precision': 0.930427875815865, 'recall': 0.8747986908410826, 'f1': 0.9017561592759819, 'number': 153992}, 'overall_precision': 0.930427875815865, 'overall_recall': 0.8747986908410826, 'overall_f1': 0.9017561592759819, 'overall_accuracy': 0.9476581289826684}
=== data/finetune_cityu.json performance ===
{'_': {'precision': 0.7944436742039783, 'recall': 0.8342125575467241, 'f1': 0.813842573238576, 'number': 1456208}, 'overall_precision': 0.7944436742039783, 'overall_recall': 0.8342125575467241, 'overall_f1': 0.813842573238576, 'overall_accuracy': 0.9074799890512801}

Cantoseg
=== data/finetune_hkcancor.json performance ===
{'_': {'precision': 0.9263396414687723, 'recall': 0.8681035378461219, 'f1': 0.8962766046603622, 'number': 153992}, 'overall_precision': 0.9263396414687723, 'overall_recall': 0.8681035378461219, 'overall_f1': 0.8962766046603622, 'overall_accuracy': 0.9453274156356153}
=== data/finetune_cityu.json performance ===
{'_': {'precision': 0.8558331862318752, 'recall': 0.8223646621911156, 'f1': 0.8387651905869052, 'number': 1456208}, 'overall_precision': 0.8558331862318752, 'overall_recall': 0.8223646621911156, 'overall_f1': 0.8387651905869052, 'overall_accuracy': 0.9277729754643846}

CyberCan-LTR
=== data/finetune_hkcancor.json performance ===
{'_': {'precision': 0.831404034182225, 'recall': 0.7625720816665801, 'f1': 0.7955018883262486, 'number': 153992}, 'overall_precision': 0.831404034182225, 'overall_recall': 0.7625720816665801, 'overall_f1': 0.7955018883262486, 'overall_accuracy': 0.8913639632044829}
=== data/finetune_cityu.json performance ===
{'_': {'precision': 0.7963653549354226, 'recall': 0.8146315636227791, 'f1': 0.8053949040283223, 'number': 1456208}, 'overall_precision': 0.7963653549354226, 'overall_recall': 0.8146315636227791, 'overall_f1': 0.8053949040283223, 'overall_accuracy': 0.9042656745151905}

CyberCan-RTL
=== data/finetune_hkcancor.json performance ===
{'_': {'precision': 0.8305877855570265, 'recall': 0.7619097095953037, 'f1': 0.7947678415991818, 'number': 153992}, 'overall_precision': 0.8305877855570265, 'overall_recall': 0.7619097095953037, 'overall_f1': 0.7947678415991818, 'overall_accuracy': 0.8908779846767995}
=== data/finetune_cityu.json performance ===
{'_': {'precision': 0.7997499199193082, 'recall': 0.8178268489116939, 'f1': 0.8086873767328697, 'number': 1456208}, 'overall_precision': 0.7997499199193082, 'overall_recall': 0.8178268489116939, 'overall_f1': 0.8086873767328697, 'overall_accuracy': 0.9067382881559977}
