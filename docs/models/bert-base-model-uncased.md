---
title: BERT base model (uncased)
description: Transformers model pretrained on a large corpus of English data in a self-supervised fashion
tags:
  - Masked language modeling
  - MLM
  - English language
  - Transformers model
---

# BERT base model (uncased)

**Transformers model pretrained on a large corpus of English data in a self-supervised fashion**

| Publisher | License | Version | Release |
| --- | --- | --- | --- |
| Hugging Face team | Unknown | Unknown | Unknown |

## Model Summary

BERT is a transformers model pretrained on a large corpus of English data in a self-supervised fashion. It was introduced in a paper and first released in a repository. It is uncased, meaning it does not differentiate between English and english. It can be used for masked language modeling or next sentence prediction, but is primarily intended to be fine-tuned on downstream tasks such as sequence classification, token classification or question answering. It was trained on 4 cloud TPUs for one million steps with a batch size of 256 and a sequence length of 128 tokens for 90% of the steps and 512 for the remaining 10%. When fine-tuned on downstream tasks, it achieves good results on Glue test results.

## Model Resources

[🤗 Hugging Face](https://huggingface.co/bert-base-uncased) | [🐱 Github](https://github.com/google-research/bert) | [📃 Research Paper](https://arxiv.org/abs/1810.04805)

!!! info

    This model card was generated using [PromptxAI API](/api/promptxai-api) querying recent web content sources with large language model generations. As of Feb 2023 it is not possible to query models like GPT-3 (via applications like ChatGPT) on the latest web content. This is because the model is trained on a static dataset and is not updated with new web content. PromptxAI API solves this problem by chaining recent web content sources with large language model outputs. This allows you to query models like GPT-3 on latest web content.


## Model Details

**Size:** Unknown

**Use Cases:** Sequence classification, token classification or question answering

**Training corpus:** BookCorpus, English Wikipedia

**Training method:** Adam optimizer, learning rate of 1e-4, β1=0.9, β2=0.999, weight decay of 0.01, learning rate warmup for 10,000 steps and linear decay of the learning rate after

**Evaluation method:** Glue test results

**Compute:** 4 cloud TPUs in Pod configuration (16 TPU chips total)

**Features:** Lowercased and tokenized using WordPiece and a vocabulary size of 30,000

**Limitations:** Primarily aimed at being fine-tuned on tasks that use the whole sentence (potentially masked) to make decisions

**Strengths:** Can use lots of publicly available data

