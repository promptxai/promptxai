---
tags:
  - Generative AI
  - Hugging Face
description: >- 
    We will setup a development environment with Jupyter Notebook. 
    We will install the minimum set of dependencies required to get started developing 
    using deep learning transformer models available at Hugging Face.
---

# 5 Minutes Generative AI Developer Setup

No this is not a click-bait title. We will use Hugging Face to do all the heavy lifting, however if you have a Mac laptop, you can download a pre-trained deep learning model, perform computer vision inference and visual question answering on a random image from Wikipedia, run a Jupyter Notebook with the demo, all this in 5 minutes flat.

First, you should be running the latest Python on your system with Python package manager upgraded to the latest.

```bash
python --version
# should return Python 3.10.x or higher as on Jan'23
pip --version
# should return pip 22.3.x or higher as on Jan'23
```

Follow this guide for [Mac OS X](https://docs.python-guide.org/starting/install3/osx/) if you do not have the latest Python. If installing specific version of Python for managing dependencies then follow [this thread](https://apple.stackexchange.com/questions/237430/how-to-install-specific-version-of-python-on-os-x) to install using `pyenv` Python version manager. If required upgrade pip to the latest using the following command.

```bash
pip install --user --upgrade pip
```

We will now create a virtual environment for our MLOps setup so that our dependencies are isolated and do not conflict with the system installed packages. We will follow [this guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) for creating and managing the virtual environment. First change to the directory where we will develop our application.

```bash
python -m venv env
```

If you run ls env you will see following folders and files created.

```bash
bin        include    lib        pyvenv.cfg
```

Now we can activate our virtual environment like so. You will notice that development directory prefixed with the (env) to indicate you are now running in the virtual environment.

```bash
. env/bin/activate
```

You can confirm that you are not running inside the virtual environment with its own Python.

```bash
which python
## should return /Users/.../env/bin/python
```

To leave the virtual environment using deactivate command. Re-enter using same command as earlier.

Now we are ready to install our dependencies for running Hugging Face Transformer models with PyTorch.

```bash
pip install torch torchvision transformers
```

We can test our installation with the following script.

```bash title="Test Installation"
python -c "from transformers import pipeline; \
print(pipeline('sentiment-analysis')('we love you'))"

# [{'label': 'POSITIVE', 'score': 0.9998704195022583}]
```

Now we can setup our development environment which is Jupyter Notebook and [Jupyter Widgets](https://ipywidgets.readthedocs.io/en/stable/index.html).

```bash
pip install notebook ipywidgets
```

Let us also save our setup in the requirements.txt file.

```bash
pip freeze > requirements.txt
```

One last thing we will do is to setup a custom cache directory for our models and datasets downloaded when using Hugging Face. Edit your bash script. On zsh shell this is the  ~/.zshrc file. This is required as the default cache directory is in the home directory which is not a good idea as it will fill up your home directory with large files. When you run Hugging Face API for the first time, it will download the models and datasets to the default cache directory. You can change the default cache directory by setting the environment variables.

```bash title="~/.zshrc"
export TRANSFORMERS_CACHE="/Users/.../cache/transformers"
export HUGGINGFACE_HUB_CACHE="/Users/.../cache/hub"
export HF_HOME="/Users/.../cache/huggingface"
```

That is it! We setup a development environment with Jupyter Notebook. We installed the minimum set of dependencies required to get started developing using deep learning transformer models available at Hugging Face.

We can now test visual question answering transformer model using sample from Hugging Face. Try this in your python shell or a Jupyter Notebook.

```python title="Visual Question Answering"

from transformers import pipeline

vqa = pipeline(model="impira/layoutlm-document-qa")
vqa(
    image="https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png",
    question="What is the invoice number?",
)

# [{'score': 0.42514941096305847, 'answer': 'us-001', 'start': 16, 'end': 16}]
```

The above code snippet uses the [LayoutLM](https://huggingface.co/transformers/model_doc/layoutlm.html) model to perform visual question answering on a given invoice image. The model is trained on the [DocQuery](https://huggingface.co/spaces/impira/docquery) dataset.

As on Feb'23, even ChatGPT does not support multimodal question and answering. However, thanks to pre-trained transformer models available at Hugging Face, we could setup a development envirionment to perform visual question answering in 5 minutes :smile:

