---
tags:
    - OpenAI
    - ChatGPT
    - Generative AI
---

# OpenAI CEO Sam Altman on AI for the Next Era

We are sharing the video transcript of OpenAI CEO Sam Altman on AI for the Next Era. The video is available on YouTube. We are also demonstrating how to generate meaningful new content using ChatGPT on a long form content like a video transcript. Specifically, we are using the video transcript to generate a summary of the video, a list of key entities, and a Mermaid.js diagram of the relationships between the entities. This is a powerful way to learn about the topics covered in the video. As we see more customer requests for such content generation, we will create more summaries and diagrams for the video transcripts. Generating this content yourself using GPT-3 Davinci model for automation can be a costly proposition (roughly $150+ for the length of this transcript). We are making this content available to you for free using our paid ChatGPT plus account. Please let us know if you find this useful.

## Introduction

<div class="video-wrapper">
  <iframe width="1280" height="720" src="https://www.youtube.com/embed/WHoWGNQRXb0" frameborder="0" allowfullscreen></iframe>
</div>

Here is the prompt we have engineered to generate the new content for this transcript. We use "as an expert" and "step by step" to indicate that the new content should be written in a step by step manner. We use "based on the following text" to indicate that the new content should be based on the text in the transcript chunk. We use "start generating a summary of the text in your own words" to indicate that the new content should be a summary of the text in the transcript chunk. We use "use the summary and text to extract and list key entities and types of entities like people, compaines, products, technologies, and processes" to indicate that the new content should be a list of key entities and types of entities. We use "describe the relationship between the entities using Mermaid.js diagram notation using a fenced code block" to indicate that the new content should be a Mermaid.js diagram of the relationships between the entities.

``` yaml title="ChatGPT Prompt"
As an expert in this subject perform these actions 
step by step based on the following text:
1. Start generating a summary of the text in your own words.
2. Use the summary and text to extract and list key entities and 
types of entities like people, compaines, products, technologies, and processes.
3. Describe the relationship between the entities using Mermaid.js 
diagram notation using a fenced code block.

Text: <replace with transcript text chunk>

Summary: 
```

The prompt generates following summary of the video transcript. It also generates a list of key entities and a Mermaid.js diagram of the relationships between the entities.

!!! info "ChatGPT Summary"
    The text discusses the potential business opportunities that can arise from the use of very large language models through APIs. The author believes that with the quality of language models expected to improve in the coming years, there will be a serious challenge to Google's search product. The author also suggests that human-level chatbot interfaces, new medical services, and education services can become very large companies. The use of language interfaces and powerful models will be a new technological platform, leading to the creation of many new companies. The author suggests that creating an enduring differentiated business is key to success, and a middle layer of startups that tune existing large models may become important.

    **Key entities**

    - People: Sam Altman
    - Companies: Google, Dolly, co-pilot, startups
    - Products: very large language models, APIs, multimodal models
    - Technologies: language interfaces, chatbots
    - Processes: creating enduring differentiated businesses, tuning large models

``` mermaid
graph LR
A(Google) --> B(search product)
A --> C(enduring differentiated business)
D(AI businesses) --> C
E(startups) --> F(tuning existing large models)
E --> D
G(very large language models) --> H(APIs)
G --> I(multimodal models)
J(medical services) --> D
K(education services) --> D
L(language interfaces) --> D
M(powerful models) --> C
```

> The above content is generated based on following transcript chunk of roughly 3,500 characters.

ht let's start a little bit more pragmatic but then we'll Branch out so one of the things I think a lot of folks
here are interested in is based off the apis that very large models will create
what are the real business opportunities like what are the ways to look forward and then how given the the apis will be
available to multiple players how do you create distinctive businesses on him yeah
um so I I think so far we've been in the realm where it's you know you can do like an incredible copywriting business
or you can do like a sort of like Education Service or whatever um but we I don't think we've yet seen
the kind of like people go after the like you know trillion dollar like take on Google's
um and I think that's about to happen like maybe it'll be successful maybe Google will do it themselves but like I
would guess that with the quality of of language models we'll see in the coming years
um you know there will be like a serious challenge to Google for the first time for for a search product
um and I think people are really starting to think about like how did the fundamental things change um and that's going to be really
powerful uh I think that a like a human level chat bot interface that actually works
this time around like I I think like you know many of these trends that like we all made fun of were just too early like
the chatbot thing was good it was just too early now it can work and I think you know having like new medical
services that are done through that where you get great advice or new Education Services like this these are
going to be very large companies I think we'll get multimodal models and not that much longer and that'll open up new
things I think people are doing amazing work with sort of agents that can use computers to do things for you use
programs and this idea of like a language interface um where you know you say a natural
language what you want in this kind of like dialogue back and forth you can iterate and refine it and the computer just does it for you you see some of
this uh with like Dolly and co-pilot in very early ways but I think this is going to be a massive Trend and you know
very large businesses will get built with this as the interface and more generally that like these very powerful
models will will be one of the genuine new technological platforms which we haven't really had
since mobile and there's always like an explosion of new companies right after so that'll be cool and and what do you
what do you things are given that the large language model we provided as an API service what are the
things that you think that folks who are thinking about these kind of AI businesses should think about is how do
you create an enduring differentiated business so you know they're they're I think there
will be a small handful of like fundamental large models out there that other people build on but right now what
happens is you know company makes large language model API other people build on
top of it and I think there will be a middle layer that becomes really important where uh
I'm like skeptical of all of the startups that are trying to sort of train their own models I don't think that's going to keep going but what I
think will happen is there'll be a whole new set of startups that take an existing very large model of the future
and tune it uh which is not just fine-tuning like all the things you can do I think there will be a lot of access
provided to create the model for medicine or using a computer 

## Data Flywheel Process

!!! info "ChatGPT Summary"
    The text discusses the potential value that can be created in a middle layer of companies that create unique versions of language models through a data flywheel process. The author believes that a systemic mistake is to assume that language models will not generate fundamentally new knowledge and add to the sum total of human scientific knowledge. The text also explores how AI can contribute to science, including the use of dedicated science products and tools that increase productivity, as well as the potential for AI to become an AI scientist and self-improve.

    **Key entities**

    - People: Kevin Scott
    - Companies: AlphaFold, bio companies
    - Products: language models, science products, tools
    - Technologies: AI, data flywheel process
    - Processes: creating unique versions of language models, scientific development, automation of AI developers' jobs

``` mermaid
graph LR
A(bio companies) --> B(value creation)
C(AI) --> D(self-improvement)
C --> E(automation of AI developers' jobs)
F(science products) --> G(value creation)
H(tools) --> G
```

or like the
kind of like friend or whatever and then those those companies will create a lot
of enduring value because they will have like a special version of they won't have to have created the base model but
they will have created something they can use just for themselves or share with others that has this unique data
flywheel going that sort of improves over time and all of that so I think there will be a lot of value created in
that middle layer and what do you think some of the most surprising ones will be it's a little bit like for example you know a surprise
from a couple years ago and we talked a little bit to Kevin Scott about this this morning as we opened up which is
train on the internet do code right so so what do you think some of the the
surprises will be of you didn't realize it reached that far
I think the biggest like systemic mistake in thinking people are making right now is they're like all right you
know maybe I was skeptical but this language model thing is really going to work and sure like images video too but but it's not going to be generating net
new knowledge for Humanity it's just going to like do what other people have done and you know that's still great that's still like brings the marginal
cost of intelligence very low but it's not it's not going to go like create fundamentally new it's not going to cure
cancer it's not going to add to the sum total of human scientific knowledge and that is what I think will turn out to be
wrong that most surprises the current experts in the field yep so uh let's go to science then there's the next thing
what are some of the things whether it's building on the apis you know uh use of
apis by scientists where what are some of the places where science will get accelerated and how so I think there's
two things happening now and then a bigger third one later um one is there are these science dedicated products whatever like Alpha
fold and those are adding huge amounts of value and you're gonna see in this like like way more and way more I like I
think I if I were like you know had time to do something else I
would be so excited to like go after a bio company right now like I think you can just do amazing things there
um the anyway but there's like another thing that's happening which is like tools
that just make us all much more productive uh that help us think of new research directions that sort of write a
bunch of our code so you know we can be twice as productive and that impact on like the net output of one engineer a
scientist I think will be the surprising way that AI contributes to science that is like outside of the obvious models
but even just seeing now like what I think these tools are capable of doing copilot is an example there's you know
be much cooler stuff than that um that will be a significant like change to the way that technological
development scientific development happens but then so those are the two that I think are like huge now and uh
lead to like just an acceleration of progress but then the big thing um that I think people are starting to
explore is um I hesitate to use this word because I think there's one one way it's used
which is fine and one that is more scary but uh like AI that can start to be like
an AI scientist and self-improve and so when like can we automate like can we
automate our own jobs as AI developers very first the very first thing we do can that help us like solve the really
hard alignment problems 

## Business Opportunities

!!! info "ChatGPT Summary"
    The text discusses the potential business opportunities and impact of language models on various industries, including search, medical services, and education. The importance of the middle layer in the value chain is highlighted, which involves companies using unique versions of language models to create enduring value. The text also covers the potential of AI in science, with tools that make researchers more productive and the development of AI scientists that can automate jobs and help solve complex alignment problems. The alignment problem is defined as the challenge of building AGI that aligns with human goals, and self-improving systems are seen as a potential solution. Finally, the text mentions the evolution of language models as the most certain development in the near future.

    **Key entities**

    - People: Kevin Scott
    - Companies: Google, OpenAI
    - Products: AlphaFold
    - Technologies: language models, AI
    - Processes: alignment problem

``` mermaid
graph LR;
    subgraph Language models
    Language_models --> Enduring_value_companies
    Language_models --> Search_products
    Language_models --> Medical_services
    Language_models --> Education_services
    Language_models --> Language_interface_businesses
    Language_models --> Middle_layer
    Enduring_value_companies --> Special_version
    Middle_layer --> Tunes_existing_models
    end
    subgraph AI in science
    AI_in_science --> Science_dedicated_products
    AI_in_science --> Productivity_tools
    AI_in_science --> AI_scientists
    end
    subgraph Alignment problem
    Alignment_problem --> AGI
    AGI --> Self_improving_systems
    Self_improving_systems --> Alignment_research
    end
    Language_models --> Evolution_of_language_models
    AI_in_science --> Evolution_of_AI
```

that we don't know how to solve like that honestly I think is how it's going to happen um
the the scary version of self-improvement like the one from the science fiction books is like you know
editing your own code and changing your optimization algorithm and whatever else
um but there's a less scary version of self-improvement which is like kind of what humans do which is if we try to go
off and like discover new science uh you know that's like we come up with explanations we
test them we think like we whatever process we do uh that is like special to
humans teaching AI to do that I'm very excited
to see what that does for the total like I'm a big believer that the only real
driver of human progress and economic growth over the long term is the the structure the societal structure that
enables scientific progress and then scientific progress itself and uh like I
think we're gonna make a lot more of that well especially science that's deployed in technology say a little bit about how
what uh I think probably most people understand what the alignment problem is but it's probably worth four sentences
on the alignment problem yeah so the alignment problem is like we're going to make this incredibly
powerful system and like be really bad if it doesn't do what we want or or if
it sort of has you know goals that are uh either in conflict with ours um and
many Sci-Fi movies about what happens there or goals where it just like doesn't care about us that much and so the alignment problem is how do we build
AGI that that does what is in the best interest of humanity how do we make sure
that Humanity gets to determine the you know the future of humanity and how do
we avoid both like accidental misuse um like where something goes wrong we didn't intend intentional misuse where
like a bad person is like using an AGI for great harm even if that's what other person wants and then the kind of like
you know inner alignment problems where like what if this thing just becomes a creature that views this as a threat
um the the way that I think the self-improving systems help us is not necessarily by the nature of
self-improving but like we have some ideas about how to solve the alignment problem at small scale
um and we've you know been able to align open ai's biggest models better than we thought we'd we would at this point so that's good
um we have some ideas about what to do next um but we cannot honestly like look anyone in the eye and say we see at 100
years how we're going to solve this problem um but once the AI is good enough that we can ask it to like hey can you help
us do alignment research um I think that's going to be a new tool in the toolbox yeah like for example one
of the conversations you and I had is could we tell the uh the the agent don't
be racist right as opposed to trying to figure out all the different things where the weird correlative data that
exists on all the training settings everything else may lead to racist outcomes it could actually in fact do a
self-cleansing totally once the model gets smart enough that you can that it really understands what racism looks
like and how complex that is you can say don't be racist yeah exactly um
what do you think are the kind of Moon shots
that in terms of evolution of the next couple years that people should be looking out for
in terms of like evolution of where AI we'll go um
I'll start with like the higher certainty things I I think language models are going to go just much much
further 

## Future of AI

!!! info "ChatGPT Summary"
    The speaker is excited about the algorithmic progress to come in the field of AI, including advancements in multimodal models and models that continuously learn. They predict that these advancements will unlock new applications and lead to a genuine technological revolution. They also believe that AI can help with new knowledge generation and advancing humanity. The speaker notes that many people are claiming to use AI in various areas, such as fusion, but these claims may be illusory.

    **Key entities**

    - Companies: Open AI
    - Products/Technologies: GPT, Transformers
    - Processes: algorithmic progress, new paradigm

``` mermaid
graph LR;
subgraph AI_Advancements
Multimodal_models --> New_applications
Continuously_learning_models --> Advancements_in_AI
New_paradigm --> Future_of_AI
end
subgraph AI_Impact
New_knowledge_generation --> Advancing_humanity
end
subgraph Illusory_AI_Claims
AI_+_Fusion --> Illusory_claims
end
```

than people think and we're like very excited to see what
happens there um I think it's like what a lot of people say about you know running out of compute running out of data like that's
all true but I think there's so much algorithmic progress to come that
that we're going to have like a very exciting time um another thing is I think we will get
true multimodal models working and so you know not just text and images but every modality you'd like in one model
able to easily like uh you know fluidly move between things
um I think we will have models that continuously learn so like right now if you use GPT whatever it's sort of like
stuck in time that it was trained and the more you use it it doesn't get any better and all of that I think we'll get that changed so very excited about all
of that and if you just think about like what that alone is going to unlock and
the sort of applications people will be able to build with that um that that that that that would be like a huge victory for all of us and
just like a like a massive step forward and a genuine technological Revolution if that
were all that happened um but I think we're likely to keep making
research progress into new paradigms as well um we've been like pleasantly surprised on the upside about
what seems to be happening and I think uh you know all these questions about like new knowledge generation how do we
really Advance Humanity uh I think there will be systems that can help us with that
so one thing I think would be useful to share because uh folks don't realize that you're
actually making these strong predictions from a fairly critical point of view not just a
you know we can take that Hill say a little bit about some of the areas that you think are current kind of
illusionally talked about like for example Ai and fusion oh yeah so I like
one of the unfortunate things that's happened is uh you know AI has become like the Mega
buzzword um which is usually a really bad sign I hope I hope it doesn't mean like the field is about to fall apart
um but historically that's like a very bad sign for you know new startup creation or whatever if everybody is like I'm this with AI and that's
definitely happening now um so like a lot of the you know we were talking about like are there all these people saying like I'm doing like these
you know RL models for Fusion or whatever and as far as we can tell they're all like much worse than what
like you know smart physicists to figure it out um I think it is just an area where people are going to say uh everything is
now this plus AI many things will be true I do think this will be like the biggest technological platform of the
Generation Um but I think it's like we like to make predictions where we can
be on the frontier understand predictably what the scaling laws look like or already have done the
research where we can say all right this new thing is going to work and make predictions out from that way and that's sort of like how we try to run open AI
um which is you know do the next thing in front of us when we have high confidence and Kate take 10 of the
company to just totally go off and explore which has led to huge wins and there
will be wait like oh I feel bad to say this like I I doubt
we'll still be using the Transformers in five years I hope we're not I hope we find something way better but the transform has obviously been remarkable
so I think it's important to always look for like you know where am I going to find the next the sort of the next
totally new paradigm um and

## Target Markets

!!! info "ChatGPT Summary"
    The speaker believes that making predictions through AI is not the only way, as it is essential to observe how something works predictably and gets better. They predict that the cost of intelligence and energy will trend towards zero, causing seismic shifts in society. The application of AI will seep into almost everything, and the cost structure will change. The speaker is uncertain about the metaverse's impact but thinks it has the potential to be a new container for software.

    **Key entities:** AI, Financial markets, Quant trading system, Intelligence, Energy, Metaverse, Computing, Simulation environments, Education, Entertainment

``` mermaid
graph LR
AI -- applies_to --> Financial_markets
AI -- applies_to --> Quant_trading_system
Intelligence -- trends_towards --> zero
Energy -- trends_towards --> zero
Intelligence -- affects_cost_of --> everything_else 
Energy -- affects_cost_of --> everything_else 
Metaverse -- may_impact --> Computing 
Metaverse -- may_impact --> Simulation_environments 
Metaverse -- may_impact --> Education 
Metaverse -- may_impact --> Entertainment 
Metaverse -- may_be_a --> container_for_software
```

but but I I think like that's the way to make predictions don't don't pay attention to the like AI for everything
like you know can I see something working and can I see how it predictably gets better and then of course leave room open for like the you can't plan
the greatness but sometimes it had the research breakthrough happens yep so I'm going to uh ask two more questions and
then open it up because I want to make sure that people have a chance to do this uh the broader discussion although
I'm trying to paint the broad picture so you can get the crazy aspirations as part of this
what do you think uh what do you think is going to happen vis-a-vis the application of AI to like
these very important systems like for example financial markets um you know because the very natural
thing would be is saying well let's let's do a high frequency Quant trading system on top of this and other kinds of
things what what is it is it just kind of being a neutral arms race is it is it what how do how what's your thought in
like it's almost like the life 3.0 yeah omega's point of view yeah um
I mean I think it is going to just seep in everywhere my basic model of the next decade is
that uh the cost of intelligence the marginal cost of intelligence and the marginal cost of energy are going to
Trend rapidly towards zero like surprisingly far and and those I think are two of the major inputs into the
cost of everything else except the cost of things we want to be expensive the status Goods whatever and and I think
you have to assume that's going to touch almost everything um because these like seismic shifts
that happen when like the whole cost structure of society change which happened many times before
um like the Temptation is always to underestimate those uh so I wouldn't like make a high
confidence prediction about anything that doesn't change a lot or that where that doesn't get to be applied
um but one of the things that is important is it's not like the thing Trends either Trends all the way to zero
they just Trend towards there and so it's like someone will still be willing to spend a huge amount of money on compute and
energy they will just get like unimaginable amount of intelligence energy they'll just get unimaginable amounts about that and so like who's
going to do that and where is it going to get the weirdest not because the cost comes way down but the amount spent actually goes way up yes the
intersection of the two curves yeah you know the thing got 10 or 100 thing got 100 times cheaper in the cost of energy
you know 100 million times cheaper in the cost of intelligence and I was still willing to spend a thousand times more
in today's dollars like what happens then yep
and then uh last of the buzzword Bingo part of the the future questions
metaverse and AI what do you what do you see coming in this you know
I think they're like both independently cool things it's not like totally clear to me yeah other than like how AI will
impact all Computing yeah well obviously Computing simulation environments Asians possibly possibly entertainment
certainly education right um you know like an AI tutor and so forth those those would be Baseline but
the question is is there anything that's occurred to you that's I I would bet that
the metaverse turns out in the upside case then which I think has a reasonable chance of happening the upside case the
metaverse turns out to be more like something on the order of the iPhone like a new
a new container for software 

## AI and the Metaverse

!!! note "ChatGPT Summary"
    The speaker believes that AI and the metaverse will revolutionize computer interaction, with the metaverse fitting into the new world of AI. They believe foundational technologies such as tpg3 will quicken iteration cycles in life science research, leading to new multi-billion dollar companies. Although some areas of life science research will be impacted by AI, human trials and bio's own pace will remain rate limiters. The speaker believes that AI can help create better simulators, leading to faster cycle times. However, the deep biological things like human interactions will not be changed by AI.

    **Key entities:** AI, Metaverse, Life science research, Pharma companies, Human trials, Bio, Startups, Simulators, Self-improvement

``` mermaid
graph LR
AI -- revolutionizes --> Computer_interaction
Metaverse -- fits_into --> New_world_of_AI
Tpg3 -- quickens --> Iteration_cycles_in_life_science_research
Life_science_research -- can_lead_to --> Multi-billion_dollar_companies
Bio -- remains --> Rate_limiter
AI -- helps_create --> Better_simulators
Better_simulators -- lead_to --> Faster_cycle_times
Human_interactions -- remain --> Unchanged_by_AI
```

and you know a new way a new computer interaction thing and AI turns out to be
something on the order of like a legitimate technological Revolution um and so I think it's more like how the
metaverse is going to fit into this like new world of AI then AI fit into the metaverse but
low confidence the TBD all right questions
hey there how do you see uh Technologies uh foundational Technologies like tpg3
affecting um the pace of life science research specifically you can group in medical
research there and and sort of just quickening the iteration cycles and then what do you see as the rate limiter in
life science research and sort of where we won't be able to get past because they're just like laws of nature yeah
something like that um so I think the currently available
models are kind of not good enough to have like made a big impact on the field at least that's what like most like life
sciences researchers have told me they've all looked at it and they're like it's a little helpful in some cases um there's been some promising work in
genomics but like stuff on a bench top hasn't really impacted it I think that's going to change and I think uh this is
one of these areas where there will be these like you know new 100 billion to trillion dollar companies started those those areas are rare but like when you
can really change the way that if you can really make like a you know future Pharma company that is just hundreds of
times better than what's out there today that's going to be really different um as you mentioned there still will be like the rate limit of like bio has to
run at its own thing and human Trials take however long they take and that's so I think an interesting cut of this is
like where can you avoid that like where are the the synthetic bio companies that I've seen that have been most
interesting are the ones that find a way to like make the cycle time super fast um and that that benefits like an AI
That's giving you a lot of good ideas but you've still got to test them which is where things are right now um I'm a huge believer for startups that
like the thing you want is low costs and fast cycle times and if you have those you can then compete as a startup
against the big incumbents uh and so like I wouldn't go pick like cardiac disease is my first thing to go after
right now with like this kind of new kind of company um but you know using bio to manufacture
something that sounds great uh I think the other thing is the simulators are still so bad
and if I were an a if I were a bio means AI startup I would certainly try to work
on that somehow when do you think the AI Tech will help
create itself oh it's almost like a self-improvement will help make the simulators significantly better
um people are working on that now uh I I don't know quite how it's going but you
know there's very smart people are very optimistic about that yeah other questions
and I can keep going on questions I just want to make sure you guys had a chance this
uh here yes great Mike is coming awesome thank you
um I was curious what what aspects of Life do you think won't be changed by AI
um sort of did all of the deep biological things like I think we will still really
care about interaction with other people like we'll still have fun and like the reward you know systems of our brain are
still going to work the same way like we're still going to have the same like drives to kind of create new things and
you know compete for silly status

---

## Video Transcript Continued

and like you know form families and whatever
um so I think the the stuff that people cared about
50 000 years ago is more likely to be the stuff that people care about you know 100 years from now than 100 years
ago as an amplifier on that before we get to the next whatever the next question is
what do you think are the best utopian science fiction universes so far
good question um Star Trek is pretty good honestly
uh like I do like all of the ones that are sort of like you know we turn our Focus to like
exploring and understanding the universe as much as we can um
it's not this is not a utopian one well maybe I think the last question is like an incredible short story uh-huh yeah
that was what that came to mind yep uh I was expecting you to say Ian Banks on the culture those are great uh
I think science fiction is like there's not like one there's not like one sci-fi universe
that I could point to and say I think all of this is great but like the collective optimistic corner of sci-fi
which is like a smallish Corner um I'm excited about actually uh I took
a few days off to write a Sci-Fi story and I had so much fun doing it just about sort of like the optimistic case
of AGI um that it made me want to go like read a bunch more so I'm looking for
recommendations of more to read now um like the sort of less known stuff if you have anything I will I will get you
some great some recommendations so in a similar vein one of my favorite
sci-fi books is called childhood's End by Arthur Clark from like the 60s I think and the I guess the one sentence
summary is aliens come to the Earth try to save us and they just take our kids and leave everything else
so you know there's a slightly more optimistic than that but yes I mean
there's Ascension into the over mind is is is meant to be more utopian but yes okay uh you may not read it that way but
yes well also in our current Universe yes our current situation
um you know a lot of people think about family building and fertility and like some of us have
different people have different ways of approaching this but from where you stand what do you see as like the most
promising Solutions it might not be a technological solution but I'm curious what you think
other than everyone having 10 kids you know like how do we of everyone having 10 kids yeah how do you populate how do
you like how do you see family building coexisting with you know AGI
high tech it's this is like a question that comes up at open AI a lot like how do I think about you know how should one
think about having kids there's I think no consensus answer to this um there are people who say yeah I'm not
I was gonna I thought I always thought I was gonna have kids and now I'm not going to because of AGI like there's just for all the obvious reasons and I
think some less obvious ones there's people who say like well it's going to be the only thing for me to do in you know 15 20 years so of course I'm going
to have a big family like that's what I'm going to spend my time doing you know I'll just like raise great kids and then I think that's what'll bring me
fulfillment I think like as always it is a a personal decision I get very depressed when people are like I'm not
having kids because of AGI uh the EA Community is like I'm not doing that because they're all going to die they're kind of like a techno
optimists are like well it's just like you know I want to like merge into the AGI and go off exploring the universe
and it's going to be so wonderful and you know just I want total freedom but I think like all of those I find quite depressing
um I think having a lot of kids is great I you know want to do that now more than
I did even more than I did when I was younger and I I'm excited for it
what do you think will be the way that most users interact with Foundation models in five years do you think there'll be a number of verticalized AI
startups that essentially have adapted and fine-tuned Foundation models to an industry or do you think prompt
engineering will be something many organizations have as an in-house function I don't think we'll still be doing prompt Engineering in five years I
think it'll just be like you and this will be integrated everywhere but you will just like you know either with text
or voice depending on the context you you will just like interface in language
and get the computer to do whatever you want and uh that will you know apply to
like generate an image where maybe we still do a little bit of prompt engineering but you know it's kind of just going to get it to like go off and
do this research for me and do this complicated thing or just like you know be my therapist and help me figure out how to make my life better or like you
know go use my computer for me and do this thing or or any number of other things but I think the fundamental interface will be natural language
let me actually push on that a little bit before we get to the next question which is I mean to some degree just like we have
a wide range of human talents right now uh and taking a look for example a dolly when you have like a a great visual
thinker they can get a lot more out of Dolly because they know how to think more they know how to iterate the loop
through the the test don't you think that will be a general truth about most of these things so it isn't that why
would be natural language is the way you're doing it it will be there will be like almost an evolving set of human
talents about about going that extra mile 100 I just hope it's not like
figuring out to like hack the prompt by adding one magic word to the end that like changes everything else I I like
what will matter is like the quality of ideas and the understanding of what you want so the artist will still do the
best with image generation but not because they figured out to like add this one magic word at the end of it
because they were just able to like articulate it with a creative eye that you know I don't have certainly what they have is a vision and kind of how
their visual thinking and iterating through it yeah yeah well obviously it'll be that word or prompt now but
it'll iterate to to better all right uh at least we have a question here
hey thanks so much um uh I think the term AGI is used uh
thrown around a lot and um sometimes I've noticed my own discussions like the sources of
confusion has just come from people having different definitions of AGI and so it can kind of be the magic box where
everyone just kind of projects their their ideas onto it and I just want to get a sense from you what like how do
you think you know how would you define AGI and how do you think you'll know yeah it's a great point I think there's like
a lot of valid definitions to this but uh for me um AGI is basically the equivalent of a
median human that you could like you know hire as a co-worker um so and then they could like say do
anything that you'd be happy with a remote co-worker doing like just behind a computer which includes like you know
learning how to go be a doctor learn how to go be a very competent coder like there's a lot of stuff that a media
human is capable of getting good at and I think one of the skills of an AGI is not any particular Milestone but the The
Meta skill of learning to figure things out and that it can go decide to get good at whatever you need
um so for me like that's that's kind of like AGI and then Super intelligence is
when it's like smarter than all of humanity put together thanks
um just uh what would you say or in the next 20 30 years are some of the main
societal issues that will arise as AI continues to grow and what can we do today to mitigate those issues
obviously the economic impacts are huge and I think it's just like if it if it
is as Divergent as I think it could be for like some people doing incredibly well
and others not I think Society just won't tolerate at this time and so figuring out when we're gonna like
disrupt so much of economic activity and even if it's not all disrupted by 20 or
30 years from now I think it'll be clear that it's all going to be um what like what is the new social
contract like how do my guess is that the things that we'll have to figure out
are how we think about fairly Distributing wealth um access to AGI systems which will be
like kind of the commodity of the realm and governance like how we collectively decide what they can do what they don't
do things like that um and I think figuring out the answer to
those questions is is gonna just be huge I I'm optimistic that people will figure
out how to spend their time and be very fulfilled I think people worry about that in a little bit of a silly way I'm
sure what people do will be very different but we always solve this problem um
but I do think like the concept of wealth and access and governance those are all going to change and how
how we address those will will be huge actually one thing I don't know what
level of devs you can share that but one of the things I love about what openai and you
guys are doing is when you they think about these questions a lot themselves
and they initiate some research so you've initiated some research on this stuff yeah so we run the largest uh Ubi
experiment in the world I don't think that is uh we have a year and a half a
year and a quarter left in a five-year project I don't think that's like the only solution but I think it's a great thing to to be doing
um and you know I think like we should have like 10 more things like that that we
try um we also try with different ways to get sort of input from a lot of the groups that we think will be most affected and see how we can do that
early in the cycle um we've explored more recently like how this technology can be used used for
reskilling people that are going to be impacted early um we'll try to do a lot more stuff like that too yeah so they are the the
organization is actually in fact uh these are great questions addressing them and actually doing a
bunch of interesting research on it so next question hi so um creativity came up today in
several of the panels you know and um it seems to me that the way it's being used like you you have tools for human
creators to go and expand human creativity so where do you think the line is between these tools to to allow
a Creator to be more productive in artificial creativity itself so
um I I think and I think we're seeing this now that tools for creatives that that is going to be like the great
application of AI in the short term um people love it it's really helpful uh
and I think it is at least in what we're seeing so far um not replacing it is mostly enhancing
it's replacing in some cases uh but for the majority of like the kind of work
that people in these fields want to be doing it's enhancing and I think we'll see that Trend continue for a long time
um eventually yeah it probably is just like you know we look at 100 years okay it can do the whole creative job
um I think it's interesting that if you asked people 10 years ago uh about Holly
I was going to have an impact with a lot of confidence from almost most people you would have heard you know first it's
going to come for the blue collar jobs working in the factories truck drivers whatever then it will come for the kind
of like the low skill White Collar jobs then the very high skill like really high IQ uh white-collar jobs like a
programmer or whatever and then very last of all and maybe never it's gonna take the creative jobs and it's really
gone exactly and it's going exactly the other direction and I think this like isn't there's an interesting reminder in
here generally about how hard predictions are but more specifically about you know we're not always very aware
maybe even ourselves of like what skills are hard and easy like what uses most of our brain and what doesn't or how like
difficult bodies are to control or make or whatever we have one more question over here
hey thanks for being here so you mentioned that um you will be skeptical of any startup trying to train their own
language model and it would love to understand more so what I have heard and which might be wrong is that large
language models depend on data and compute and any startup can access to the same amount of data because it's
just like internet data and compute like different companies might have different compute but I guess I see a big players
can sell more compute so how good a large language model startup differentiate from another
how would the startup differentiate from another how would one large language model startup differentiate I think
it'll be this middle layer um I think in some sense the startups will train their own models just not from the beginning
uh they will take like you know base models that are are like
hugely trained with a gigantic amount of compute and data and then they will train on top of those to create you know
the model for each vertical and and that those startups so in some sense they are training their own models
just not not from scratch but they're doing the one percent of training that really matters for for whatever this use
case is going to be those startups I think they will be hugely successful and very differentiated startups there but
that'll be about the kind of like data flywheel that the startup is able to do the kind of like all of the pieces on
top of and Below uh like this could include prompt engineering for a while or whatever the sort of the kind of like
core base model I think that's just going to get too too
complex and too expensive and the world also just doesn't make enough chips
so Sam has a work thing he needs to get to so and as you probably can tell with
a very far far ranging thing Sam always expands my uh boundaries and a little
bit unlike the that when you're feeling depressed whether it's kids in a house you're the person I always turn to
probably I appreciate that yes so anyway I think I think like no one knows
like we're sitting on this like precipice of AI and like people like it's either gonna be like really great or really terrible
um you may as well like you gotta you gotta like plan for the worst you certainly
like it's not a strategy to say it's all going to be okay but you may as well like emotionally feel like we're going to get to the Great future and we'll
play as hard as you can to get there and play for it yes rather than like act from this place of like fear and despair all the time because if we acted from a
place of fear and paranoia we would not be where we are today so let's thank Sam for spending dinner with us thank you