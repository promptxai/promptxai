---
title: Flan 20B
description: Instruction tuned with Flan, receptive field of 2048, no mode tokens, trained on C4 corpus
tags:
  - Instruction tuning
  - Flan
  - UL2
  - T5
  - Apache
  - Google AI
---

# Flan 20B

**Instruction tuned with Flan, receptive field of 2048, no mode tokens, trained on C4 corpus**

| Publisher | License | Version | Release |
| --- | --- | --- | --- |
| Google AI | Apache | 20B | Q2 2022 |

## Model Summary

This text describes the release of a new open source Flan 20B model that was trained on top of the already open sourced UL2 20B checkpoint. It has the same configuration as the original UL2 20B model, except that it has been instruction tuned with Flan. It is expected to improve the usability of the original UL2 model and has been released on Apache license. The text also discusses the relative improvements of Flan-UL2 20B compared to other models in the Flan series, as well as the limitations of Flan-style models. Finally, it is noted that the release of Flan-UL2 20B expands the size ceiling of the current Flan-T5 models by approximately 2x.

## Model Resources

[🤗 Hugging Face](https://huggingface.co/google/flan-ul2) | [📄 Research Paper](https://arxiv.org/abs/2205.05131) | [🎬 Demo](https://huggingface.co/spaces/ybelkada/i-like-flan-ul2) | [📖 About Model](https://www.yitay.net/blog/flan-ul2-20b)

## Model Details

**Size:** 19.5B parameters

**Use Cases:** N-shot prompting, few-shot in-context learning

**Training corpus:** C4 corpus

**Training method:** UL2 objective

**Evaluation method:** Big-Bench hard and MMLU

**Compute:** 7-8 times faster than Flan-PaLM 62B

**Features:** Expands size ceiling of Flan-T5 models by 2x

**Limitations:** Instruction tuned on primarily academic tasks, not ideal for open ended generation

**Strengths:** Best open source model at the moment on Big-Bench hard and MMLU

