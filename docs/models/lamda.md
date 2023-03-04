---
title: LaMDA
description: Built by fine-tuning a family of Transformer-based neural language models specialized for dialog
tags:
  - Language Models for Dialog Applications
---

# LaMDA

**Built by fine-tuning a family of Transformer-based neural language models specialized for dialog**

| Model Provider | Model License | Model Version | Model Release |
| --- | --- | --- | --- |
| Google | Unknown | Unknown | Unknown |

## Model Summary

This post describes the LaMDA project, which is a family of Transformer-based neural language models specialized for dialog. LaMDA has three key objectives: Quality, Safety, and Groundedness, which are measured using carefully designed metrics. The model is trained in two stages: pre-training and fine-tuning. Pre-training is done on a dataset of 1.56T words, while fine-tuning is done on a dialog dataset restricted to back-and-forth dialog between two authors. Quality metrics generally improve with the number of model parameters, with or without fine-tuning, while Safety does not seem to benefit from model scaling alone, but does improve with fine-tuning. Groundedness improves as model size increases, but fine-tuning allows the model to access external knowledge sources and effectively shift some of the load of remembering knowledge to an external knowledge source. LaMDA's level of Sensibleness, Specificity and Interestingness unlocks new avenues for understanding the benefits and risks of open-ended dialog agents. Exploring new ways to improve the Safety metric and LaMDA's groundedness is the main focus going forward.

## Model Resources

[🐱 Github](https://github.com/conceptofmind/LaMDA-rlhf-pytorch) | [🌐 Website](https://blog.google/technology/ai/lamda/) | [🔖 About Model](https://ai.googleblog.com/2022/01/lamda-towards-safe-grounded-and-high.html)

!!! info

    This model card was generated using [PromptxAI API](/api/promptxai-api) querying recent web content sources with large language model generations. As of Feb 2023 it is not possible to query models like GPT-3 (via applications like ChatGPT) on the latest web content. This is because the model is trained on a static dataset and is not updated with new web content. PromptxAI API solves this problem by chaining recent web content sources with large language model outputs. This allows you to query models like GPT-3 on latest web content.

## Model Details

**Task:** Generate natural-language responses to given contexts, and classification tasks on whether a response is safe and high-quality

**Model Parameters:** 137B

**Model Training Data:** 1.56T words from public dialog data and other public web documents

**Model Evaluation Data:** Multi-turn two-author dialogs

**Model Hyperparameters:** Unknown

**Model Training Procedure:** Pre-train the model using GSPMD to predict every next token in a sentence, given the previous tokens; fine-tune the model to perform a mix of generative tasks to generate natural-language responses to given contexts, and classification tasks on whether a response is safe and high-quality

**Model Evaluation Procedure:** Collect responses from the pre-trained model, fine-tuned model, and human raters; ask a different set of human raters a series of questions to evaluate these responses against the Quality, Safety, and Groundedness metrics.

**Model Strengths:** Quality metrics (Sensibleness, Specificity, and Interestingness) generally improve with the number of model parameters, with or without fine-tuning

**Model Limitations:** Below human levels in safety and groundedness

**Model Unique Features:** Leverages external knowledge sources

**Model Comparison with Similar Models:** Quality gap to human levels can be narrowed, though the model’s performance remains below human levels in safety and groundedness

**Model Use Cases:** Natural language processing research, program synthesis, zero-shot learning, style transfer, as well as in the BIG-bench workshop

**Model Compute Infrastructure Required:** Unknown

