---
tags:
  - Knowledge Management
  - Consulting Industry
  - ChatGPT Model
  - Diagram Generation
---

# Generating Diagrams From World Knowledge

Mermaid.js is a JavaScript library that can be used to generate diagrams from text using a simple, human-readable syntax. You can ask ChatGPT to generate code for a diagram using the Mermaid.js syntax.

!!! info "Guide"
    Describe what the diagram should illustrate and what kind of diagram to generate. 
    Instruct ChatGPT to generate Mermaid.js code for the diagram.

## Visualizing movie scripts
In the following prompt we are expecting ChatGPT to decipher the contents of the diagram based its knowledge of the movie Inception. We do not have to explictly describe any of the characters, locations, or events in the movie.

```yaml title="ChatGPT Prompt"
Generate Mermaid.js code for a context diagram that shows the main characters 
and their relationships in the movie Inception. # (1)!
Include their interactions with external entities such as locations and events, 
using the →| Relationship | syntax to indicate the relationships between 
the different entities, using subgraphs for characters, locations, and events.
```

1. :bulb: Replace `movie Inception` with name of any movie, book, or play you want to generate a context diagram for.

The completion from ChatGPT is Mermaid.js code that can be used to generate a context diagram like below.

``` mermaid
graph LR;
    subgraph "Characters"
        Cobb(Cobb)
        Mal(Mal)
        Arthur(Arthur)
        Ariadne(Ariadne)
        Eames(Eames)
        Yusuf(Yusuf)
        Saito(Saito)
    end
    subgraph "Locations"
        Paris(Paris)
        Tokyo(Tokyo)
        USA(USA)
    end
    subgraph "Events"
        Inception(Inception)
    end
    Cobb --> Mal
    Cobb --> Arthur
    Cobb --> Ariadne
    Cobb --> Eames
    Cobb --> Yusuf
    Cobb --> Saito
    Paris --> Inception
    Tokyo --> Inception
    USA --> Inception
    Cobb -->|Married To| Mal
    Cobb -->|Works With| Arthur
    Cobb -->|Works With| Ariadne
    Cobb -->|Works With| Eames
    Cobb -->|Works With| Yusuf
    Cobb -->|Works For| Saito
    Cobb -->|Located In| Paris
    Cobb -->|Located In| Tokyo
    Cobb -->|Located In| USA
    Mal -->|Located In| Paris
    Arthur -->|Located In| Paris
    Ariadne -->|Located In| Paris
    Eames -->|Located In| Paris
    Yusuf -->|Located In| Paris
    Saito -->|Located In| Paris
```

## Generating visual summaries of books

Let us try a variation of the prompt. This time we are expecting ChatGPT to decipher the contents of the diagram based its knowledge of the book The Unicorn Project.

```yaml title="OpenAI GPT-3 Prompt"
Generate Mermaid.js code for a context diagram that shows the main entities 
and their relationships in the book The Unicorn Project.
Include the interactions between entities using the →| Relationship | syntax 
to indicate the relationships between the different entities, 
using subgraphs clustering entities of similar class.
```

Here is the context diagram generated for the book.

``` mermaid
graph LR;

subgraph The Unicorn Project
  DevOpsTeam[DevOps Team] -->|manages| DevOpsToolchain[DevOps Toolchain]
  DevOpsTeam -->|uses| DevOpsPipeline[DevOps Pipeline]
  DevOpsTeam -->|uses| CIPlatform[CI Platform]
  DevOpsTeam -->|uses| PerformanceTesting[Performance Testing]
  DevOpsTeam -->|uses| SecurityTesting[Security Testing]
  DevOpsTeam -->|uses| AutomatedTesting[Automated Testing]
  DevOpsTeam -->|uses| Monitoring[Monitoring]
end

subgraph The Business
  BusinessOwner[Business Owner] -->|oversees| ProductOwner[Product Owner]
  ProductOwner -->|manages| BusinessTeam[Business Team]
end

subgraph The Engineering Team
  EngineeringTeam[Engineering Team] -->|manages| EngineeringToolchain[Engineering Toolchain]
  EngineeringTeam -->|uses| VersionControl[Version Control]
  EngineeringTeam -->|uses| TDD[TDD]
  EngineeringTeam -->|uses| Refactoring[Refactoring]
  EngineeringTeam -->|uses| PairProgramming[Pair Programming]
  EngineeringTeam -->|uses| CodeReview[Code Review]
end

DevOpsToolchain --> CIPlatform
DevOpsToolchain --> PerformanceTesting
DevOpsToolchain --> SecurityTesting
DevOpsToolchain --> AutomatedTesting
DevOpsToolchain --> Monitoring

EngineeringToolchain --> VersionControl
EngineeringToolchain --> TDD
EngineeringToolchain --> Refactoring
EngineeringToolchain --> PairProgramming
EngineeringToolchain --> CodeReview

CIPlatform --> DevOpsPipeline
DevOpsPipeline --> BusinessTeam
BusinessTeam --> ProductOwner
```

## Automating diagram generation

You can write automation to generate such diagrams from world knowledge using OpenAI API within few lines of code. In the following code we import the OpenAI API, initialize the API key, and generate the completion in less than five lines of code.

```python title="OpenAI API"
import openai
openai.api_key = os.getenv("OPENAI_KEY")
openai_model = 'text-davinci-003'
completion = openai.Completion.create(
    prompt=prompt, 
    model=openai_model,
    temperature=0.6,
    max_tokens=500)
mermaid_code = completion.choices[0].text
```
