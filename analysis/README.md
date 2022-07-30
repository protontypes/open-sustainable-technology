# AwesomeCure
Analyze and cure awesome lists by mining data from listed Git projects.

Awesome lists play a central role within an open source ecosystem by providing an index to the various open source domains. Without this infrastructure, it would be impossible for newcomers to find out what tools, frameworks, data and communities exist. Maintaining an Awesome List requires removing inactive projects on a regular basis. Without these measures, new and still active projects get lost in the multitude of inactive projects. At the same time, they help to concentrate open source resources on active projects instead of reinventing the wheel over and over again.

AwesomeCure provides simple tools to analyze Git projects within an Awesome list and get an overview of the represented open source ecosystem. It uses the GitHub API to retrieve project metadata and generate various metrics about the state of the project. As a result, a CSV is created to sort and analyze the listed projects according to the different criteria. 

## Background

So-called Awesome List are a central part of the open source ecosystem. They allow developers to get an overview of open source projects in different areas. A cross-platform search engine for open source projects does not yet exist. Therefore, they represent the central dictionary for the most diverse areas within the open source ecosystem. The Awesome.re website offers a central point of contact here, as it provides an overview of all subdomains. The central task of this list is to make projects within a subject area easier to find. Thus, users can browse appropriate resources. At the same time, developers can check which projects already exist, so that resources are concentrated and the wheel is not always reinvented.

The OpenSustain.tech website is based on such an Awesome list, and we are currently working on an open source tooling to analyze the state of the open source ecosystem in the area of climate change related open source technology.

Most of the projects are linked to GitHub or GitLab repository of the underlying project. Therefore, we are able to analyze every project via the platform API to extract meta data from the listed projects. In this way, various health indicators are extracted for every active and listed project within the ecosystem like:

Last Activity
Elephant Factor ( How much does the project depend on a single person)
Number of Reviews per Pull Request
Ratio of Closed to Open Issue
Mean Time until an issue is closed
...
Here you will find the first running prototype for our study.

https://github.com/protontypes/AwesomeCure

The extracted data on the projects for our study: https://airtable.com/shr9we419r2TkpLkc

The data on the organizations with the ecosystem: https://airtable.com/shrBuNq6VkQQDzB36

I am convinced that the method of our study can be applied to other open source areas as well. Since all official Awesome lists are checked with a linter to the standard "awesome" format, we should be able to develop our tools generically so that they can be used everywhere. That is why we plan to release the tooling for our study as a seperated open source project. This should make it possible to easily repeat the study in the future and to transfer our method to other lists.

## Install

First, you need to clone the GitHub-Repo. Do something like:

```
git clone git@github.com:protontypes/AwesomeCure.git
```

Then, you need to install jupiter notebook:
(for example via pip, see all options on [their website](https://jupyter.org/install))

```
pip install jupyterlab
pip install notebook
```

Then, add a `.env` with your persoal git hub token (see more information on that [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). Then run:

```
jupyter notebook
```
a browser window should open, if not, click (or copy paste) the link from your terminal output.
