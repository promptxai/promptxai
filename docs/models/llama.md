---
title: LLaMA
description: Auto-regressive language model, based on the transformer architecture
tags:
  - Language model
  - transformer architecture
---

# LLaMA

**Auto-regressive language model, based on the transformer architecture**

| Model Provider | Model License | Model Version | Model Release |
| --- | --- | --- | --- |
| FAIR team of Meta AI | Non-commercial bespoke license | Version 1 | December 2022 - Feb 2023 |

## Model Summary

Meta AI's FAIR team developed the auto-regressive language model LLaMA between December 2022 and February 2023. It is based on the transformer architecture and comes in different sizes, ranging from 7B to 65B parameters. It is intended for research on large language models, such as exploring potential applications, understanding capabilities and limitations, and evaluating and mitigating biases, risks, and toxic and harmful content generations. The primary intended users are researchers in natural language processing, machine learning, and artificial intelligence. The model was trained on data from the Web, and thus reflects biases from this source. It was evaluated on RAI datasets to measure biases exhibited by the model, as well as on eight standard common sense reasoning benchmarks. The data used to train the model contains offensive, harmful, and biased content, and thus the model is not intended to inform decisions about matters central to human life. Risks and harms of large language models include the generation of harmful, offensive, or biased content, and incorrect information. As a foundational model, it should not be used for downstream applications without further investigation and mitigations of risks.

## Model Resources

[🐱 Github](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md) | [📃 Paper](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/) | [🔖 About Model](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/)

!!! info

    This model card was generated using [PromptxAI API](../api/promptxai-api) querying recent web content sources with large language model generations. As of Feb 2023 it is not possible to query models like GPT-3 (via applications like ChatGPT) on the latest web content. This is because the model is trained on a static dataset and is not updated with new web content. PromptxAI API solves this problem by chaining recent web content sources with large language model outputs. This allows you to query models like GPT-3 on latest web content.

## Model Details

**Task:** Research on large language models

**Model Parameters:** 7B, 13B, 33B and 65B parameters

**Model Training Data:** CCNet [67%], C4 [15%], GitHub [4.5%], Wikipedia [4.5%], Books [4.5%], ArXiv [2.5%], Stack Exchange[2%]

**Model Evaluation Data:** BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC, OpenBookQA, NaturalQuestions, TriviaQA, RACE, MMLU, BIG-bench hard, GSM8k, RealToxicityPrompts, WinoGender, CrowS-Pairs

**Model Hyperparameters:** Table 1 - Summary of LLama Model Hyperparameters

**Model Training Procedure:** Kneser-Ney language model and a fastText linear classifier

**Model Evaluation Procedure:** Evaluated on RAI datasets to measure biases exhibited by the model for gender, religion, race, sexual orientation, age, nationality, disability, physical appearance and socio-economic status, measure the toxicity of model generations, depending on the toxicity of the context used to prompt the model, evaluated on eight standard common sense reasoning benchmarks.

**Model Strengths:** Can be used for research on large language models, including exploring potential applications, understanding capabilities and limitations of current language models, and developing techniques to improve those

**Model Limitations:** Generates incorrect information, prone to generating toxic or offensive content

**Model Unique Features:** Auto-regressive language model, based on the transformer architecture

**Model Comparison with Similar Models:** Not applicable

**Model Use Cases:** Research on large language models, including exploring potential applications such as question answering, natural language understanding or reading comprehension, understanding capabilities and limitations of current language models, and developing techniques to improve those, evaluating and mitigating biases, risks, toxic and harmful content generations, hallucinations

**Model Compute Infrastructure Required:** Not specified

