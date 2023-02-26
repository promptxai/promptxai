---
title: DALL·E Mini
description: Generate images based on text prompts for research and personal consumption
tags:
  - Image generation
---

# DALL·E Mini

**Generate images based on text prompts for research and personal consumption**

| Model Provider | Model License | Model Version | Model Release |
| --- | --- | --- | --- |
| Hugging Face | Unknown | DALL·E Mini and DALL·E Mega | June 9, 2022 |

## Model Summary

This model card focuses on the DALL·E Mini model, which is used to generate images based on text prompts for research and personal consumption. Intended uses include supporting creativity, creating humorous content, and providing generations for people curious about the model’s behavior. The model was trained on unfiltered data from the Internet, limited to pictures with English descriptions, and the model developers discuss the limitations of the model further in the DALL·E Mini technical report. The model developers used 3 datasets for the model and the model is 27 times smaller than the original DALL·E and was trained on a single TPU v3-8 for only 3 days. DALL·E Mega is still training and has been training for about 40-45 days on a TPU v3-256. The model should not be used to intentionally create or disseminate images that create hostile or alienating environments for people, and using the model to generate content that is cruel to individuals is a misuse of this model.

## Model Resources

[🤗 Hugging Face](https://huggingface.co/dalle-mini/dalle-mini) | [🐱 Github](https://github.com/borisdayma/dalle-mini) | [🌐 Website](https://www.craiyon.com/)

!!! info

    This model card was generated using [PromptxAI API](../api/promptxai-api) querying recent web content sources with large language model generations. As of Feb 2023 it is not possible to query models like GPT-3 (via applications like ChatGPT) on the latest web content. This is because the model is trained on a static dataset and is not updated with new web content. PromptxAI API solves this problem by chaining recent web content sources with large language model outputs. This allows you to query models like GPT-3 on latest web content.

## Model Details

**Task:** Generating images based on text prompts

**Model Parameters:** 27 times smaller than the original DALL·E and was trained on a single TPU v3-8 for only 3 days

**Model Training Data:** 2 million images for fine-tuning the image encoder, 15 million images for training the Seq2Seq model

**Model Evaluation Data:** Unknown

**Model Hyperparameters:** Unknown

**Model Training Procedure:** Images and descriptions pass through the system, fine-tuning the image encoder, training the Seq2Seq model

**Model Evaluation Procedure:** Comparing DALL·E Mini’s results with DALL·E-pytorch, OpenAI’s DALL·E, and models consisting of a generator coupled with the CLIP neural network model

**Model Strengths:** Generate images based on text prompts for research and personal consumption, supporting creativity, creating humorous content, and providing generations for people curious about the model’s behavior

**Model Limitations:** White and Western culture asserted as a default, and the model’s ability to generate content using non-English prompts is observably lower quality than prompts in English, may also reinforce or exacerbate societal biases

**Model Unique Features:** 27 times smaller than the original DALL·E and was trained on a single TPU v3-8 for only 3 days

**Model Comparison with Similar Models:** DALL·E-pytorch, OpenAI’s DALL·E, and models consisting of a generator coupled with the CLIP neural network model

**Model Use Cases:** Generate images based on text prompts for research and personal consumption, supporting creativity, creating humorous content, and providing generations for people curious about the model’s behavior

**Model Compute Infrastructure Required:** TPU v3-8 and TPU v3-256

