import openai
import os
from promptxai import utils

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

class ModelCard:
    """Model card generator."""
    def __init__(self):
        self.huggingface_url = None
        self.github_url = None
        self.website_url = None
        self.paper_url = None
        self.custom_url = None

    def set_extract(self, model_card_extract: str):
        """Initialize the model card generator."""        
        extract_list = model_card_extract.splitlines()
        extract_list[0] = extract_list[0].replace('Attributes: ', '')
        separator = '=' if '=' in extract_list[1] else ':'
        # iterate over the list and extract the model card attributes
        for pair in extract_list:
            if pair.startswith('Model parameters'):
                self.model_parameters = pair.split(separator)[1].strip()
            elif pair.startswith('Limitations of the model'):
                self.limitations_of_the_model = pair.split(separator)[1].strip()
            elif pair.startswith('Strengths of the model'):
                self.strengths_of_the_model = pair.split(separator)[1].strip()
            elif pair.startswith('Name of the model'):
                self.model_name = pair.split(separator)[1].strip()
            elif pair.startswith('Company releasing the model'):
                self.model_provider = pair.split(separator)[1].strip()
            elif pair.startswith('Unique features of the model'):
                self.unique_features_of_the_model = pair.split(separator)[1].strip()
            elif pair.startswith('Comparison with similar models'):
                self.comparison_with_similar_models = pair.split(separator)[1].strip()
            elif pair.startswith('Use cases of the model'):
                self.use_cases_of_the_model = pair.split(separator)[1].strip()
            elif pair.startswith('Date of model release'):
                self.date_of_model_release = pair.split(separator)[1].strip()
            elif pair.startswith('Compute infrastructure required for model'):
                self.compute_infrastructure_required_for_model = pair.split(separator)[1].strip()
            elif pair.startswith('Model license'):
                self.model_license = pair.split(separator)[1].strip()
            elif pair.startswith('Model version'):
                self.model_version = pair.split(separator)[1].strip()
            elif pair.startswith('Model description'):
                self.model_description = pair.split(separator)[1].strip()
            elif pair.startswith('Model keywords'):
                self.model_keywords = pair.split(separator)[1].strip()
            elif pair.startswith('Model task'):
                self.model_task = pair.split(separator)[1].strip()
            elif pair.startswith('Model training data'):
                self.model_training_data = pair.split(separator)[1].strip()
            elif pair.startswith('Model evaluation data'):
                self.model_evaluation_data = pair.split(separator)[1].strip()
            elif pair.startswith('Model hyperparameters'):
                self.model_hyperparameters = pair.split(separator)[1].strip()
            elif pair.startswith('Model training procedure'):
                self.model_training_procedure = pair.split(separator)[1].strip()
            elif pair.startswith('Model evaluation procedure'):
                self.model_evaluation_procedure = pair.split(separator)[1].strip()

    # if any of the model card attributes are not set, set them to 'Unknown'
    def set_unknown(self):
        if not hasattr(self, 'model_parameters'):
            self.model_parameters = 'Unknown'
        if not hasattr(self, 'limitations_of_the_model'):
            self.limitations_of_the_model = 'Unknown'
        if not hasattr(self, 'strengths_of_the_model'):
            self.strengths_of_the_model = 'Unknown'
        if not hasattr(self, 'model_name'):
            self.model_name = 'Unknown'
        if not hasattr(self, 'model_provider'):
            self.model_provider = 'Unknown'
        if not hasattr(self, 'unique_features_of_the_model'):
            self.unique_features_of_the_model = 'Unknown'
        if not hasattr(self, 'comparison_with_similar_models'):
            self.comparison_with_similar_models = 'Unknown'
        if not hasattr(self, 'use_cases_of_the_model'):
            self.use_cases_of_the_model = 'Unknown'
        if not hasattr(self, 'date_of_model_release'):
            self.date_of_model_release = 'Unknown'
        if not hasattr(self, 'compute_infrastructure_required_for_model'):
            self.compute_infrastructure_required_for_model = 'Unknown'
        if not hasattr(self, 'model_license'):
            self.model_license = 'Unknown'
        if not hasattr(self, 'model_version'):
            self.model_version = 'Unknown'
        if not hasattr(self, 'model_description'):
            self.model_description = 'Unknown'
        if not hasattr(self, 'model_keywords'):
            self.model_keywords = 'Unknown'
        if not hasattr(self, 'model_task'):
            self.model_task = 'Unknown'
        if not hasattr(self, 'model_training_data'):
            self.model_training_data = 'Unknown'
        if not hasattr(self, 'model_evaluation_data'):
            self.model_evaluation_data = 'Unknown'
        if not hasattr(self, 'model_hyperparameters'):
            self.model_hyperparameters = 'Unknown'
        if not hasattr(self, 'model_training_procedure'):
            self.model_training_procedure = 'Unknown'
        if not hasattr(self, 'model_evaluation_procedure'):
            self.model_evaluation_procedure = 'Unknown'
        
    def set_summary(self, summary: str):
        """Set the model summary."""
        self.model_summary = summary
    
    def set_model_parameters(self, model_parameters: str):
        """Set the model parameters."""
        self.model_parameters = model_parameters

    def set_model_name(self, model_name: str):
        """Set the model name."""
        self.model_name = model_name

    def set_url(self, url: str, source: str):
        """Set the model source URL."""
        if source == 'huggingface':
            self.huggingface_url = url
        elif source == 'github':
            self.github_url = url
        elif source == 'website':
            self.website_url = url
        elif source == 'paper':
            self.paper_url = url
        elif source == 'custom':
            self.custom_url = url

    def get_url(self, source: str):
        """Get the model source URL."""
        if source == 'huggingface':
            return self.huggingface_url
        elif source == 'github':
            return self.github_url
        elif source == 'website':
            return self.website_url
        elif source == 'paper':
            return self.paper_url
        elif source == 'custom':
            return self.custom_url

    def generate_material_mkdown(self):
        """Generate the model card as Material for MkDocs Markdown."""
        model_card = '---\n'
        model_card += 'title: ' + self.model_name + '\n'
        model_card += 'description: ' + self.model_description + '\n'
        model_card += 'tags:\n'
        for tag in self.model_keywords.split(','):
            model_card += '  - ' + tag.strip() + '\n'
        model_card += '---\n\n'

        model_card += '# ' + self.model_name + '\n\n'
        model_card += '**' + self.model_description + '**\n\n'

        # render a markdown table with model provider, model license, model version, model parameters
        model_card += '| Model Provider | Model License | Model Version | Model Release |\n'
        model_card += '| --- | --- | --- | --- |\n'
        model_card += '| ' + self.model_provider + ' | ' + self.model_license + ' | ' + self.model_version + ' | ' + self.date_of_model_release + ' |\n\n'

        model_card += '## Model Summary\n\n'
        model_card += self.model_summary + '\n\n'

        model_card += '## Model Resources\n\n'
        if self.huggingface_url:
            model_card += '[🤗 Hugging Face]({url})'.format(url=self.huggingface_url)
        
        if self.github_url:
            model_card += ' | ' if self.huggingface_url else ''
            model_card += '[🐱 Github]({url})'.format(url=self.github_url)

        if self.website_url:
            model_card += ' | ' if self.huggingface_url or self.github_url else ''
            model_card += '[🌐 Website]({url})'.format(url=self.website_url)
        
        if self.paper_url:
            model_card += ' | ' if self.huggingface_url or self.github_url or self.website_url else ''
            model_card += '[📃 Paper]({url})'.format(url=self.paper_url)
        
        if self.custom_url:
            model_card += ' | ' if self.huggingface_url or self.github_url or self.website_url or self.paper_url else ''
            model_card += '[🔖 About Model]({url})'.format(url=self.custom_url)

        if self.huggingface_url or self.github_url or self.website_url or self.paper_url or self.custom_url:
            model_card += '\n\n'

        model_card += '## Model Details\n\n'

        # Render rest of the model card attributes as attribute name in bold: attribute value
        model_card += '**Task:** ' + self.model_task + '\n\n'
        model_card += '**Model Parameters:** ' + self.model_parameters + '\n\n'
        model_card += '**Model Training Data:** ' + self.model_training_data + '\n\n'
        model_card += '**Model Evaluation Data:** ' + self.model_evaluation_data + '\n\n'
        model_card += '**Model Hyperparameters:** ' + self.model_hyperparameters + '\n\n'
        model_card += '**Model Training Procedure:** ' + self.model_training_procedure + '\n\n'
        model_card += '**Model Evaluation Procedure:** ' + self.model_evaluation_procedure + '\n\n'
        model_card += '**Model Strengths:** ' + self.strengths_of_the_model + '\n\n'
        model_card += '**Model Limitations:** ' + self.limitations_of_the_model + '\n\n'
        model_card += '**Model Unique Features:** ' + self.unique_features_of_the_model + '\n\n'
        model_card += '**Model Comparison with Similar Models:** ' + self.comparison_with_similar_models + '\n\n'
        model_card += '**Model Use Cases:** ' + self.use_cases_of_the_model + '\n\n'
        model_card += '**Model Compute Infrastructure Required:** ' + self.compute_infrastructure_required_for_model + '\n\n'

        return model_card

    def save_markdown(self, generated_markdown: str, filename: str, folder: str):
        """Save the model card as a Markdown file."""
        filepath = folder + utils.search_friendly_filename(filename) + '.md'
        with open(filepath, 'w') as f:
            f.write(generated_markdown)
        return 'Model card saved as ' + filepath