import openai
import os

class OpenAI:
    """OpenAI wrapper."""
    default_model = 'text-davinci-003'

    def __init__(self):
        self.session_cost = 0
        self.run_tokens = 0
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def estimate_cost(self, tokens: int, model=default_model) -> float:
        """Estimate cost of tokens."""
        if 'davinci' in model.split('-'):
            estimate = tokens/1000 * 0.02
        elif 'curie' in model.split('-'):
            estimate = tokens/1000 * 0.002
        elif 'babbage' in model.split('-'):
            estimate = tokens/1000 * 0.0005
        elif 'ada' in model.split('-'):
            estimate = tokens/1000 * 0.0004
        return estimate

    def get_session_cost(self) -> float:
        """Get session cost."""
        return self.session_cost

    def get_tokens_usage(self) -> int:
        """Get run tokens."""
        return self.tokens_usage

    def text(self, prompt, temperature=0.9, max_tokens=70, model=default_model, **kwargs):
        """OpenAI Text Completion API wrapper."""
        response = openai.Completion.create(
            model=model, 
            prompt=prompt, 
            temperature=temperature, 
            max_tokens=max_tokens, 
            **kwargs)
        self.tokens_usage = response['usage']
        self.session_cost += self.estimate_cost(int(self.tokens_usage['total_tokens']), model)
        return response

