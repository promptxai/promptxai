from promptxai import utils

def extract_model_card(text_content: str) -> str:
    """Extracts the model card from a text.

    Args:
        text_content (str): The text to extract the model card from.

    Returns:
        prompt (str): Prompt for model card extraction.
    """
    prompt_base = '''Match the attributes with values from text. Where values do not exist, set value to Unknown.
        
        Attributes:
        Model parameters
        Limitations of the model
        Strengths of the model
        Name of the model
        Company releasing the model
        Unique features of the model
        Comparison with similar models
        Use cases of the model
        Date of model release
        Compute infrastructure required for model
        Model license
        Model version
        Model description
        Model keywords
        Model task
        Model training data
        Model evaluation data
        Model hyperparameters
        Model training procedure
        Model evaluation procedure

        Text: 
        '''
    prompt='{prompt_base}{text}'.format(prompt_base=prompt_base, text=text_content)
    tokens = utils.chars_to_tokens(len(prompt_base) * 5)
    return prompt, tokens

def summarize(text_content: str) -> str:
    """Summarizes the text.

    Args:
        text_content (str): The text to summarize.

    Returns:
        prompt (str): Prompt for text summarization.
    """
    prompt_base = '''Summarize the text

        Text: 
        '''
    prompt='{prompt_base}{text}'.format(prompt_base=prompt_base, text=text_content)
    tokens = 300
    return prompt, tokens