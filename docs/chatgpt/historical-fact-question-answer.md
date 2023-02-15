---
tags:
  - Research Function
  - Education Industry
  - ChatGPT Model
  - Dataset Generation
---
# Historical Fact Question Answer

You can ask ChatGPT any questions about historical facts and it will respond with the correct answer. ChatGPT is trained on a knowledge corpus of historical facts which includes Wikipedia and Encyclopedia Britannica among other sources.

!!! info "Guide"
    Ask question related to a historical fact about any entity like a famous personality, book, movie, product, or place and related attributes like location, age, distance, size, or weight.

## Attribute related to an entity
Here is an example of a simple prompt-completion sequence using ChatGPT. The human is asking a factual question. The model is asked to complete the question with the correct answer.

```yaml title="ChatGPT Prompt"
Where is the great pyramid located?
```

ChatGPT responds with a completion which is based on the knowledge corpus used for training the model.

!!! note "ChatGPT Completion"

    The Great Pyramid is located in Giza, Egypt.

## Citing source of historical fact

You could get more information from ChatGPT like citing the source of the answer.

```yaml title="ChatGPT Prompt"
Where is the great pyramid located? Cite the source of answer.
```

ChatGPT responds with a completion along with source of the answer.

!!! note "ChatGPT Completion"

    The Great Pyramid is located in Giza, Egypt. Source: https://www.britannica.com/topic/Great-Pyramid-of-Giza

## List of historical facts

You could also get structured data as completion by asking for the type of structure to return as completion.

```yaml title="ChatGPT Prompt"
List the 10 most popular pyramids and their locations.
```

ChatGPT responds with a completion which is a list of popular pyramids and their locations. Note that not all of them are located in Egypt.

!!! note "ChatGPT Completion"

    1. Great Pyramid of Giza, Egypt
    2. Khafre's Pyramid, Egypt
    3. Menkaure's Pyramid, Egypt
    4. Djoser's Pyramid, Egypt
    5. Pyramid of the Sun, Teotihuacán, Mexico
    6. Pyramid of the Moon, Teotihuacán, Mexico
    7. El Castillo, Chichen Itza, Mexico
    8. Temple of the Sun, Peru
    9. Temple of the Inscriptions, Palenque, Mexico
    10. Bent Pyramid, Egypt


## Create dataset of historical facts

You can create a dataset of historical facts related entities and their attributes.

```yaml title="Prompt"
Only respond using fenced code block with markdown which I can copy-paste 
to an editor. #(1)!

Tell me about the entity Mayan Civilisation. #(2)!
Create a table of few attributes of this entity in attribute name 
and value columns. Then create a table of 10 related entities with these 
attributes names as columns and values for each of the entities as rows.
```

1. :scissors: You can leave this out if you want to get the completion in a plain text format. In this case the table will be rendered in HTML.
2. :bulb: You can replace `Mayan Civilization` with any other historical entity.

ChatGPT responds with a completion which is a table of attributes and related entities as markdown in a fenced code block.

!!! note "ChatGPT Completion"
  
    **Mayan Civilisation**

    Attribute Name | Attribute Value
    --- | ---
    Location | Central America, present-day Mexico, Guatemala, Belize, Honduras, El Salvador and parts of Nicaragua
    Time Period | 2000 BC to 16th century AD
    Religion | Polytheistic, worshipped gods related to natural phenomena such as the sun, the moon, and agriculture
    Writing System | Hieroglyphic writing system, one of the few writing systems of the pre-Columbian Americas
    Architecture | Elaborate stone pyramids, plazas, palaces, and elaborate underground structures such as tombs and cisterns
    Mathematics and Astronomy | Highly advanced knowledge of mathematics and astronomy, including the use of zero as a place-holder and the calculation of a solar year to within five minutes
    Art | Highly developed art style, including elaborate murals, carvings, pottery, and weaving
    Collapse | The Mayan civilization declined and eventually collapsed in the 9th to 10th centuries, with reasons including environmental degradation, war, and societal problems

    **Related Entities**

    Entity | Location | Time Period | Religion | Writing System
    --- | --- | --- | --- | ---
    Olmecs | Mexico | 1400 BC - 400 BC | Polytheistic | Undeciphered script
    Teotihuacan | Mexico | 300 BC - 700 AD | Polytheistic | None
    Aztecs | Mexico | 13th to 16th century AD | Polytheistic | Nahuatl writing system
    Inca Empire | South America | 1438 AD to 1533 AD | Polytheistic | Quipu system of knots and colors
    Toltecs | Mexico | 900 AD to 1168 AD | Polytheistic | None
    Zapotecs | Mexico | 600 BC - 1521 AD | Polytheistic | Zapotec writing system
    Mixtecs | Mexico | 300 AD - 1521 AD | Polytheistic | Mixtec writing system
    Maya of Yucatán | Mexico | 600 AD to 1697 AD | Polytheistic | Hieroglyphic writing system
    Chichimeca | Mexico | 900 AD to 1500 AD | Polytheistic | None
    Purépecha | Mexico | 1000 AD to 1530 AD | Polytheistic | None

