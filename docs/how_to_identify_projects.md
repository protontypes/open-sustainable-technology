# How to Identify Open Source Projects in Sustainability and Climate

This document outlines a methodology for identifying relevant open-source projects in the areas of sustainability and climate, building upon the existing efforts of the Open Sustainable Technology initiative.

## 1. Understanding the Scope and Principles

Before beginning the search, it is crucial to understand the core principles and criteria for project inclusion as defined by OpenSustain.tech. Projects should:

*   Align with the [Open Sustainability Principles](https://github.com/protontypes/open-sustainable-technology/blob/main/docs/OpenSourceSustainabilityEcosystem_080423.pdf).
*   Be instrumental in preserving/restoring natural ecosystems, supporting climate change mitigation/adaptation, or enabling environmental sustainability through open technology, methods, data, knowledge, intelligence, or tools.
*   Be actively used or developed by others outside the core project or organization.
*   Be structured and documented for maintenance, reuse, and extendability.
*   Be published under an open-source license.

## 2. Leveraging Keyword-Based Search

The [ost_keywords.txt](https://github.com/protontypes/open-sustainable-technology/blob/main/ost_keywords.txt) file provides a valuable starting point with a list of terms frequently associated with open-source projects in this domain. These keywords can be used to formulate targeted search queries across various platforms.

**Example Keywords:**

*   `mass`, `content`, `concentration`, `radioactivity`, `atmosphere`, `water`, `carbon`, `energy`, `climate`, `biodiversity`, `renewable energy`, `solar`, `wind`, `hydrology`, `emissions`, `pollution`, `deforestation`, `conservation`, `sustainable development`.

**Search Platforms:**

*   **GitHub:** Utilize advanced search filters to combine keywords with programming languages (e.g., `python`, `R`, `Java`) and repository characteristics (e.g., `stars:>5`, `updated:>2023-01-01`). To search the projects READMEs, use the search terms such as this: `in:readme biodiversity stars:>5`. Find more here about [GitHub's advanced search](https://github.com/search/advanced). 
*   **GitLab, Bitbucket, [Zenodo](https://zenodo.org/):** Extend searches to these platforms using similar keyword-based approaches.
*   **Academic Search Engines (e.g., Google Scholar, Semantic Scholar):** Search for research papers that mention open-source tools or datasets related to sustainability. Look for terms like "open-source software," "open data," "GitHub repository," in conjunction with sustainability keywords.
*   **Specialized Search Engines/Indexes:** Explore platforms like [Libraries.io](https://libraries.io/), [PyPi](https://pypi.org/), [rdrr.io](https://rdrr.io/) for package-level discovery.

## 3. Exploring Existing Networks and Communities

*   **GitHub Namespace and Stars of strong GitHub users in Sustainability:** Searching GitHub Stars or the [namespaces of users](https://opensustain.tech/spreadsheet/) and organisations in sustainability and climate is an efficient and easy way to discover missing projects. Follow these people on various people to stay updated.
*   **Using LLM prompts to discover missing projects:** Various prompts can help you to identify any missing projects on OpenSustain.tech. Although most LLMs are familiar with some of the projects listed on OpenSustain.tech, it is helpful to provide details of the existing projects. Could you please help me find further active open-source projects on GitHub and other open-source platforms that are missing from OpenSustain.tech? Here is a subsection of the [existing projects](https://opensustain.tech/) and a [raw markdown copy of the project list](https://raw.githubusercontent.com/protontypes/open-sustainable-technology/main/README.md).
*   **Open Source Communities:** Engage with existing open-source communities focused on environmental science, climate change, or sustainable technology. Forums, mailing lists, and social media groups can be excellent sources for discovering new projects.
*   **Conferences and Workshops:** Attend virtual or in-person conferences and workshops related to AI/ML for sustainability. Projects are often presented and discussed at these events.
*   **[Journal of Open Source Software (JOSS)](https://joss.theoj.org/):** Regularly review publications in JOSS for newly published open-source research software relevant to the domain.
*   **Crowdsourcing and Interviews:** As highlighted in the OpenSustain.tech methodology report, direct engagement with domain experts and practitioners through interviews or crowdsourcing initiatives can uncover valuable projects not easily found through automated means.

## 4. Analyzing Project Suitability

Once potential projects are identified, evaluate them against the OpenSustain.tech criteria. Pay close attention to:

*   **Active Development:** Check commit history, recent pull requests, and issue activity.
*   **Community Engagement:** Look for signs of external contributions, active discussions, and responsiveness from maintainers.
*   **Documentation:** Assess the clarity and completeness of project documentation, including installation guides, usage examples, and contribution guidelines.
*   **Licensing:** Verify that the project is released under a recognized open-source license.
*   **Testing:** In some cases, it is possible to test a project's website or tool quickly. 

## 5. Contributing to the Open Sustainable Technology Database

For any newly identified projects that meet the criteria, follow the [CONTRIBUTING.md](https://github.com/protontypes/open-sustainable-technology/blob/main/CONTRIBUTING.md) guidelines to add them to the Open Sustainable Technology database via a pull request. Ensure to provide all necessary details and a clear description of the project's relevance to sustainability.

By following this comprehensive approach, we can collectively enhance the visibility and impact of open-source projects driving environmental sustainability.
