---
title: BERT base model (uncased)
description: Pretrained model on English language using a masked language modeling (MLM) objective
tags:
  - Masked language modeling
  - MLM
  - English language
---

# BERT base model (uncased)

**Pretrained model on English language using a masked language modeling (MLM) objective**

| Model Provider | Model License | Model Version | Model Release |
| --- | --- | --- | --- |
| Google | Unknown | Unknown | Unknown |

## Model Summary

BERT is a transformers model pretrained on a large corpus of English data in a self-supervised fashion. It was introduced in a paper and first released in a repository. It is uncased, meaning it does not differentiate between English and english. It can be used for masked language modeling or next sentence prediction, but is mainly intended to be fine-tuned on downstream tasks such as sequence classification, token classification or question answering. It was trained on 4 cloud TPUs for one million steps with a batch size of 256 and a sequence length of 128 tokens for 90% of the steps and 512 for the remaining 10%. When fine-tuned on downstream tasks, it achieves good results on Glue test results.

## Model Resources

[🤗 Hugging Face](https://huggingface.co/bert-base-uncased) | [🐱 Github](https://github.com/google-research/bert) | [📃 Paper](https://arxiv.org/abs/1810.04805)


!!! info

    This model card was generated using [PromptxAI API](../api/promptxai-api) querying recent web content sources with large language model generations. As of Feb 2023 it is not possible to query models like GPT-3 (via applications like ChatGPT) on the latest web content. This is because the model is trained on a static dataset and is not updated with new web content. PromptxAI API solves this problem by chaining recent web content sources with large language model outputs. This allows you to query models like GPT-3 on latest web content.

## Model Details

**Task:** Masked language modeling or next sentence prediction

**Model Parameters:** Unknown

**Model Training Data:** BookCorpus, a dataset consisting of 11,038 unpublished books and English Wikipedia (excluding lists, tables and headers)

**Model Evaluation Data:** Glue test results

**Model Hyperparameters:** Adam with a learning rate of 1e-4, β1=0.9\beta_{1} = 0.9β1​=0.9 and β2=0.999\beta_{2} = 0.999β2​=0.999, a weight decay of 0.01, learning rate warmup for 10,000 steps and linear decay of the learning rate after

**Model Training Procedure:** Pretrained with two objectives

**Model Evaluation Procedure:** Fine-tuned on downstream tasks

**Model Strengths:** Can use lots of publicly available data, pretrained on a large corpus of English data in a self-supervised fashion

**Model Limitations:** Bias will also affect all fine-tuned versions of this model

**Model Unique Features:** Modified preprocessing with whole word masking has replaced subpiece masking

**Model Comparison with Similar Models:** GPT2

**Model Use Cases:** Sequence classification, token classification or question answering

**Model Compute Infrastructure Required:** 4 cloud TPUs in Pod configuration (16 TPU chips total)

