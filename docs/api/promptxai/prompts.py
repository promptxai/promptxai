from promptxai import utils

def extract_model_card(model_attributes: list, text_content: str) -> str:
    """Extracts the model card from a text.

    Args:
        model_attributes (list): The model attributes to extract.
        text_content (str): The text to extract the model card from.

    Returns:
        prompt (str): Prompt for model card extraction.
        tokens (int): Number of tokens to pass on to max_tokens.
    """
    prompt = '''Extract model attribute values from text and 
    return a code-fenced JSON object with {'attribute'='value'} pairs.
    Where attribute does not exist, set value to Unknown.
    The model attributes are - '''
    prompt += ', '.join(model_attributes) + '.\n\n'
    prompt += 'Text: ' + text_content

    tokens = 500
    return prompt, tokens

def summarize(text_content: str) -> str:
    """Summarizes the text.

    Args:
        text_content (str): The text to summarize.

    Returns:
        prompt (str): Prompt for text summarization.
        tokens (int): Number of tokens to pass on to max_tokens.
    """
    prompt_base = '''Summarize the text

        Text: 
        '''
    prompt='{prompt_base}{text}'.format(prompt_base=prompt_base, text=text_content)
    tokens = 300
    return prompt, tokens