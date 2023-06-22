# Cantonese Word Segmentation Comparison
We use the segeval library to calculate Precision, Recall, F1, and Accuracy of various Cantonese segmenters on the HKCanCor and CityU word segmentation corpora.

## Results
### HKCanCor (16,162 sentences / 153,992 characters)
|Segmenter   | Precision | Recall | F1    | Accuracy |
|------------|-----------|--------|-------|----------|
|Pycantonese | 93.04     | 87.48  | 90.18 |  94.77   |
|Cantoseg    | 92.63     | 86.81  | 89.63 |  94.53   |
|CyberCan-LTR| 83.14     | 76.26  | 79.55 |  89.14   |
|CyberCan-RTL| 83.06     | 76.19  | 79.48 |  89.09   |

### CityU (53,019 sentences / 1,456,208 characters)
|Segmenter   | Precision | Recall | F1    | Accuracy |
|------------|-----------|--------|-------|----------|
|Pycantonese | 79.44     | 83.42  | 81.38 |  90.75   |
|Cantoseg    | 85.58     | 82.24  | 83.88 |  92.78   |
|CyberCan-LTR| 79.64     | 81.46  | 80.54 |  90.43   |
|CyberCan-RTL| 79.97     | 81.78  | 80.87 |  90.67   |

### CRF Segmenter on 10% randomly selected HKCanCor sentences
CRF-xx% means that the CRF model is trained on xx% of HKCanCor sentences. All models are tested on 10% of randomly selected HKCanCor sentences outside of the training set.

|Segmenter   | Precision | Recall | F1    | Accuracy |
|------------|-----------|--------|-------|----------|
|CRF-10%     | 89.91     | 90.17  | 90.04 |  94.11   |
|CRF-20%     | 91.28     | 91.48  | 91.38 |  94.97   |
|CRF-30%     | 91.75     | 91.85  | 91.80 |  95.28   |
|CRF-40%     | 92.19     | 92.37  | 92.28 |  95.55   |
|CRF-50%     | 92.26     | 92.48  | 92.37 |  95.57   |
|CRF-60%     | 92.45     | 92.61  | 92.53 |  95.64   |
|CRF-70%     | 92.61     | 92.60  | 92.61 |  95.67   |
|CRF-80%     | 92.86     | 92.81  | 92.83 |  95.87   |
|CRF-90%     | 93.03     | 93.03  | 93.03 |  95.95   |

## Raw Results

```
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
```

Test on 10% of HKCanCor sentences:
```
CRF-HKCanCor-10%
=== data/hkcancor_test.jsonl performance ===
{'_': {'precision': 0.8991069117266374, 'recall': 0.9016744548286605, 'f1': 0.9003888528839923, 'number': 15408}, 'overall_precision': 0.8991069117266374, 'overall_recall': 0.9016744548286605, 'overall_f1': 0.9003888528839923, 'overall_accuracy': 0.9410593389088012}

CRF-HKCanCor-20%
=== data/hkcancor_test.jsonl performance ===
{'_': {'precision': 0.9128351249838104, 'recall': 0.9148494288681205, 'f1': 0.913841166936791, 'number': 15408}, 'overall_precision': 0.9128351249838104, 'overall_recall': 0.9148494288681205, 'overall_f1': 0.913841166936791, 'overall_accuracy': 0.949721226602947}

CRF-HKCanCor-30%
=== data/hkcancor_test.jsonl performance ===
{'_': {'precision': 0.9175364667747163, 'recall': 0.918548805815161, 'f1': 0.9180423572146726, 'number': 15408}, 'overall_precision': 0.9175364667747163, 'overall_recall': 0.918548805815161, 'overall_f1': 0.9180423572146726, 'overall_accuracy': 0.952757865392274}

CRF-HKCanCor-40%
=== data/hkcancor_test.jsonl performance ===
{'_': {'precision': 0.9219407916045864, 'recall': 0.9236760124610592, 'f1': 0.9228075863186902, 'number': 15408}, 'overall_precision': 0.9219407916045864, 'overall_recall': 0.9236760124610592, 'overall_f1': 0.9228075863186902, 'overall_accuracy': 0.9555455993628037}

CRF-HKCanCor-50%
=== data/hkcancor_test.jsonl performance ===
{'_': {'precision': 0.9225689498899391, 'recall': 0.9248442367601246, 'f1': 0.9237051921955014, 'number': 15408}, 'overall_precision': 0.9225689498899391, 'overall_recall': 0.9248442367601246, 'overall_f1': 0.9237051921955014, 'overall_accuracy': 0.955694942254082}

CRF-HKCanCor-60%
=== data/hkcancor_test.jsonl performance ===
{'_': {'precision': 0.9245221898283122, 'recall': 0.9261422637590861, 'f1': 0.925331517686347, 'number': 15408}, 'overall_precision': 0.9245221898283122, 'overall_recall': 0.9261422637590861, 'overall_f1': 0.925331517686347, 'overall_accuracy': 0.9564416567104739}

CRF-HKCanCor-70%
=== data/hkcancor_test.jsonl performance ===
{'_': {'precision': 0.9261326755809425, 'recall': 0.92601246105919, 'f1': 0.9260725644187707, 'number': 15408}, 'overall_precision': 0.9261326755809425, 'overall_recall': 0.92601246105919, 'overall_f1': 0.9260725644187707, 'overall_accuracy': 0.9566905615292712}

CRF-HKCanCor-80%
=== data/hkcancor_test.jsonl performance ===
{'_': {'precision': 0.9285714285714286, 'recall': 0.9280893042575286, 'f1': 0.9283303038171903, 'number': 15408}, 'overall_precision': 0.9285714285714286, 'overall_recall': 0.9280893042575286, 'overall_f1': 0.9283303038171903, 'overall_accuracy': 0.9586818000796495}

CRF-HKCanCor-90%
=== data/hkcancor_test.jsonl performance ===
{'_': {'precision': 0.9302959501557633, 'recall': 0.9302959501557633, 'f1': 0.9302959501557633, 'number': 15408}, 'overall_precision': 0.9302959501557633, 'overall_recall': 0.9302959501557633, 'overall_f1': 0.9302959501557633, 'overall_accuracy': 0.9594782954998009}

```