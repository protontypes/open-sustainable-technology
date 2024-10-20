# Closing the Gap: Accelerating environmental Open Source

__Tobias Augspurger__  [:fontawesome-brands-linkedin:](https://www.linkedin.com/in/tobias-augspurger/) :octicons-calendar-24: October 16, 2024

_Originally posted on [OpenSource.net](https://opensource.net/closing-the-gap-accelerating-environmental-open-source/)._

**A recap of my journey to discover how open digital infrastructure helps us to preserve our natural world.**

Four-year cycles – whether it’s a presidency, the FIFA cup, or a leap year – can be momentous. It’s been four years since the [Open Sustainable Technology](https://opensustain.tech/) project kicked off. At the time, most of the R&D team I’d built up over the previous five years had been fired from DHL/Streetscooter. To give back to the robotics community, we released the [Awesome Robotic Tooling](https://opensource.net/closing-the-gap-accelerating-environmental-open-source/[awesome-robotic-tooling](https://github.com/Ly0n/awesome-robotic-tooling)) list of the best tools for the various autonomous and electric trucks that we built. But how to continue on this path of free and collaborative innovation that I came to love over the years? I decided to shift my career to focus on open technology’s potential for positive long-term impact.

<figure markdown="span">
  ![OSS for Climate Logo](Screenshot_OST.webp){ width="600" }
  <figcaption>OpenSustain.tech landing page</figcaption>
</figure>

To my surprise, no one had yet compiled a comprehensive overview of Open Source Software (OSS) around climate change and sustainability. Sure, there were a few lists on various sustainability topics, but most of them were not updated or only represented a tiny part of this OSS ecosystem.

Thanks to the pandemic, my unemployment and the support of friends, the team published early results in September 2021. The feedback was overwhelming. We realized that almost no one had a good understanding of what Open Source could do to help fight climate change and protect our natural world. And no one was talking about the crucial role Open Source was already playing. To this day, Open Sustainable Technology is one of the world’s leading projects that scientifically analyses and advocates how open methods can accelerate a sustainable transition. The fact that a community-based project with no funding and just a few volunteers could archive this was both shocking and motivating at the same time.

## Understanding natural dynamics in Open Source

Typically, OSS ecosystems are created from a user perspective, based on the infrastructure being used, or as part of a larger technical framework or programming language. Few tried to map OSS ecosystems based on common real-world applications and issues. I regularly heard that our approach was crazy and technically unfeasible given the number of projects in the field. Since I was also starting a PhD in Atmospheric Science, I was able to leverage my studies to continue curating strong research projects in the field around the world for fun.

When the attention started to fade and most of the supporting contributors started working on other projects, an efficient way of deciding whether a project is worth listing or not was needed. The challenge with climate and sustainability projects is to filter out relevant projects from the noise. Which project can be reused and create added value for other OSS projects and developers? So instead of judging the quality of a project and its source code, I focused on external usage indicators like download numbers and issues from users outside of the projects.

My studies, previous work experience and various glossaries helped me find the relevant keywords. Clouds, for example, provide one of the most difficult aspects of climate forecasting, but it’s almost impossible to find relevant projects because they’re buried under a mass of cloud computing. The same goes for terms like ocean, sea, environment, atmosphere, battery and carbon.

> “The OSS community has a hard time gathering around relevant topics because they cannot find each other and are forced to reinvent the wheel over and over again. I’m still convinced that the main problem with OSS sustainability is the lack of a comprehensive search engine to help you find the right (active and documented) projects for your use case.”

A year into the project, I started to lose motivation. It’s a shame to see how many projects in this area don’t get any further development after their release, even if you see how hard they try to build community. I estimate that more than 95% of the thousands of repositories I reviewed are now inactive. Research in this area is incredibly exciting due to the diverse technologies and methods employed, but it also underscores the pressing nature of many environmental challenges. What kept me going was the unique insight I was able to create for myself and others. There’s a huge, untapped potential for OSS to make an impact on climate and biodiversity. This potential extends beyond scientific research to business practices and systemic changes for a sustainable future.

Openness about environmental models, data and statements is the most important indicator of genuine sustainability efforts. The very nature of environmental sustainability demands such openness: Our planet is simply too complex to argue with black boxes. Explaining, planning and forecasting requires a way to iterate in the open to improve assumptions and models over the long term.

## First insights

The database already showed clear trends, such as the lack of companies and for-profits. It also became clear that where traceable numbers are bad for business as usual, OSS and open science play a tiny role, even though software and high-quality numbers are highly relevant. So far, these include in particular carbon offsets, anything related to corporate ‘climate neutrality,’ corporate emissions, sustainable investment and carbon capture. As part of this ‘gap’ analysis, it’s clear that there is no existing open-source climate model with verifiable scientific data that can refute the claim of long-term environmental destruction caused by climate change. However, there are a variety of smaller and larger, along with their supporting data, that reinforce this alarming trend.

I started writing blog posts about the findings, e.g. about the [lack of OSS in sustainable investment](https://opensustain.tech/blog/openness_as_a_key_indicator_for_sustainable_investment/) and how this relates to the lack of reproducibility of collaborative sustainability ratings. To my surprise, these reached hundreds of thousands of people worldwide. After seeing how easy it was to innovate and create climate action with OSS, I kept giving talks and writing articles to motivate others. That said, I still don’t understand why the “Open Source Way” is so little understood, promoted and propagated in the climate and sustainability community. Accurate and transparent quantification of a technology’s sustainability can help mitigate the uncertainty caused by political manipulation and lobbying. Simply asking for open models and open science from relevant people for technologies such as biofuels or carbon capture would put an end to the misinformation in these fields.

<figure markdown="span">
  ![OSS for Climate Logo](eirini_and_tobias.webp){ width="600" }
  <figcaption>Malliaraki and the author.</figcaption>
</figure>

## First ecosystem analysis

At about that one-year mark, Eirini Malliaraki contacted me to report that she had a grant from [Subak](https://subak.org/) to help analyze the projects found so far. Without her help and the refreshed motivation, the project might have been abandoned. The two of us bolstered each other to write the first report on [The Open Source Sustainability Ecosystem](https://raw.githubusercontent.com/protontypes/open-source-in-environmental-sustainability/main/OpenSourceSustainabilityEcosystem_080423.pdf), with Josh Hopkins joining later on.

Fortunately, at the beginning of the project, we decided to focus on Git repositories. This allowed us to retrieve metadata about the projects and organizations using the APIs of the Git platforms. We also found Open Source ecosystem analysis in general to be a fascinating new scientific field. Introducing a new health indicator, like the [Development Distribution Score](https://report.opensustain.tech/chapters/development-distribution-score.html), allowed us to get a first impression of the community. As in a natural ecosystem, we can study similar quantities such as diversity of topics, organizational structures, global distribution and how these projects can be ‘preserved’.

At one of the conferences presenting our findings, met Andrew Nesbitt of [Ecosyste.ms](https://ecosyste.ms/). With his help, the analysis jumped to the next level. Download numbers from almost all package managers and citations of projects based on their DOI (Digital Object Identifier) were added to the metadata. Linking Open Source repositories to articles and papers using the DOI, which is available for a growing number of scientific projects, has greatly increased the amount of data available. Citations can be used to gauge the relevance of a project. More automation and various methods such as embedding, unearthed hundreds of additional projects. In addition to some online marketing for the ecosystem, we started to build some additional services for the projects collected, such as [ClimateTriage.com](https://climatetriage.com/), to help developers contribute and join an open-climate community.

## The challenge of keeping the lights on

However, with over 1,000 organizations and 2,000 projects, it was becoming increasingly difficult to find new projects. For many, the project became my personal project and I found it difficult to restore the sense of community and shared responsibility that existed in the beginning.

The team investigated whether new open access scientific publications could be discovered based on the keywords collected over the years. We also investigated how methods such as Natural Language Processing (NLP) and Large Language Models (LLM) could be applied to our dataset.

The roadblock? We weren’t able to find funding for this or most of our other work. Confession: This was largely my fault because I had avoided establishing a funding source and legal organization early on. With the project’s popularity surging to fourth place in the ecosystem with over 2,000 stars, I was optimistic about securing funding if needed.

Since almost all of the “awesome” lists in this space gave up years ago, we needed a strategy to maintain the existing one as more people started to rely on our insights and data. Otherwise, we would have failed in our mission, leaving behind a clustered space of OSS projects with little collaboration between them because they simply don’t know about each other.

## Future steps

To take Open Sustainable Technology to the next level, our community is leading the way in exploring various follow-up projects. These include creating a fund as an additional service for the Open Source ecosystem. Allocating funds to critical projects and their dependencies with low-health indicators could help maintain some of the most important infrastructure for our future. Distributing funding based on project metadata would significantly reduce the administrative overhead that funds struggle with. Relying on various [project metrics](https://opensource.net/?s=CHAOSS) would make a much more transparent how and why funding is distributed.

The team is also looking into creating a news feed about new environmental OSS projects as they’re published, based on keywords found over the years. Andrew came up with the idea of searching all new open-access papers with our keywords for software and data repositories.

That said, the path forward for the project isn’t crystal clear. Because it relies on my personal resources and volunteers, it’s impossible to draw up a detailed roadmap. Much depends on whether the future prototype we build takes off and creates strong ties between the community members. Fortunately, the project’s low running costs will enable us to sustain efforts to keep building this OSS climate and sustainability analysis and directory indefinitely. A free community offers many advantages, as we can innovate and express ourselves without restrictions like shareholders. I’ve learned this firsthand over the years.

## Get involved

I’m a firm believer that Open Source is one of the most important pieces of the climate change puzzle. It’s impossible to prove but to integrate environmental concerns into our number-driven economies, we need traceable software, data, and models. Without these, sustainability remains a mere concept. Recognizing open source’s potential in this area is crucial to bridging this gap.

Are you interested in helping out? Just join one of our [public workshops](https://opensustain.tech/contributing/#join-the-community) or donate to our [Open Collective](https://opencollective.com/open-sustainable-technology). You might also find a project that is welcoming new contributors via one of the Good First Issues we list on [ClimateTriage.com](https://climatetriage.com/).