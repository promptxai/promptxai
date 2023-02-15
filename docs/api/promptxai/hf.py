from IPython.display import Image

# A function to convert between IPython.display Image to PIL Image
def display_to_pil(display):
    """Convert IPython.display.Image to PIL.Image"""
    if isinstance(display, Image):
        return display._repr_png_()
    else:
        raise TypeError("display must be IPython.display.Image")