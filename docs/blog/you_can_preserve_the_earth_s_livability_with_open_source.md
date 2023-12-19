# You can preserve the Earth's livability with open source


 _Tobias Augspurger_  [:fontawesome-brands-twitter:](https://twitter.com/protontypes) · :octicons-calendar-24: May 23, 2022

**Why actions rooted in open source culture can make a big impact.**

Earth's uniqueness in creating a stable environment for life in a completely hostile space is a miracle. Various life forms have taken billions of years to build up the natural resources humans depend on, such as a protective atmosphere, fertile soil, stable weather, and clean drinking water.

As a movement to democratize technology development and knowledge creation, open source has the potential to become the central driver in preserving this stability. Here are four different ways you can preserve the livability of the planet by using, supporting, and participating in open source projects, and more than 20 resources to help you get started.

## Measure, optimize, and reduce
Before taking action, it is important to assess your impact on the environment in a scientific way. With more accurate information, you can focus your efforts where the most potential lies. Open science discloses the models behind these measurements, which reduces uncertainties in the long term through continuous improvement and observation. Open source tools make it possible to remain objective and make meaningful comparisons to guide decision making.

These decisions happen constantly, both in the consumption of everyday resources and in the use and development of digital products. Software developers find their work in digital products all over the world. Measuring and reducing the energy consumption of these products is the goal of open source tools like [Scaphandre](https://github.com/hubblo-org/scaphandre) , [Cloud Carbon Footprint](https://github.com/cloud-carbon-footprint/cloud-carbon-footprint), and [kube-green](https://github.com/kube-green/kube-green). These tools help you track power consumption, estimate carbon emissions, and even shut down resources when they are not needed.

<figure markdown>
  ![](https://opensource.com/sites/default/files/2022-05/cloud-carbon-footprint.jpeg)
  <figcaption> Figure 1: Cloud Carbon Footprint is an open-source project, sponsored by Thoughtworks Inc
(Cloud Carbon Footprint, Apache License, Version 2.0) </figcaption>
</figure>

The open source platform [electricityMap](https://app.electricitymap.org/map) calculates and predicts the carbon intensity of electric power consumption within electrical grids worldwide on an hourly basis. You or your business can take action by using this information to shift computation to times when there is a high share of renewable energy sources in the electricity grid, thereby reducing emissions.

The open source community of [OpenEnergyMonitor](https://openenergymonitor.org/) enables people to monitor and understand the electrification of their homes. Open hardware and open source tools created by OpenEnergyMonitor track and log usage data from multiple categories, including electric vehicles, heat pumps, and photovoltaics. Their learning platform offers a deep understanding of the possibilities for increasing the use of sustainable energy in your household and becoming energy independent. At the heart of it all is the [emonPi](https://github.com/openenergymonitor/emonpi) energy monitor and base station, which can bring together information about your energy consumption from multiple sensor nodes.


<figure markdown>
  ![](https://opensource.com/sites/default/files/2022-05/my-solar-pv.jpeg)
  <figcaption> Figure 2: The OpenEnergyMonitor Solar PV monitor provides real-time and historical information on solar generation and on-site consumption.
(OpenEnergyMonitor, CC BY-SA 4.0) </figcaption>
</figure>



## Understand the planet

The Earth is a highly complex system, which makes it vitally important to better understand the impact humans have on this system. Several open science and open source projects are working to improve transparency and cooperation in this area. Various tutorials offer beginners an introduction to the programming languages and tools used in this field. These tutorials allow you to improve your programming skills while simultaneously learning more about the environment.

[An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/) provides a beginner-friendly introduction to the use of open source Python tools, how these tools can be used, and data science in general. Instead of introducing the basics of Python with routine robotics projects, learners discover how to use Python and programming tools to interpret data about the planet.

<figure markdown>
  ![](https://opensource.com/sites/default/files/2022-05/sea_ice_map.png)
  <figcaption> Figure 3: Understanding and representing earth observation data, such as this map of sea ice concentration, is a central part of the Introduction to Earth and Environmental Data Science course.
(Ryan Abernathey, CC BY-SA 4.0) </figcaption>
</figure>
[The Climate Laboratory](https://brian-rose.github.io/ClimateLaboratoryBook/home.html) provides the perfect starting point for getting a deeper understanding of climate change and the physical science behind it. Like the previous example, this course includes tutorials to use Python, one of the main tools for climate scientists today. The textbook is a living document that has been created around [climlab](https://github.com/brian-rose/climlab) to provide a powerful but entry-level friendly tool for climate modeling.


<figure markdown>
  ![](https://opensource.com/sites/default/files/2022-05/transient-cesm_41_0.png)
  <figcaption> Figure 4: You can learn to make maps illustrating surface air temperature anomalies due to CO2 doubling </figcaption>
</figure>


[Earth Lab](https://www.earthdatascience.org/) provides Earth data science lessons that will help you learn how to work with data in the R and Python programming languages. All course material is open source. Nonspecialists who enroll in the Earth data analytics online course help ensure that understanding how the planet works is not just an academic exercise but also a field of knowledge used in all parts of society.

## Observe the planet

Satellites provide a unique tool to map the state of the planet. Even small changes in our ecosystems such as greenhouse gas emissions, land use change, biodiversity loss, soil drought, or water pollution can be measured with high temporal and spatial resolution.. The data collected here are calibrated to the highest scientific standards and therefore provide an objective view of Earth. Recent years have seen a massive democratization of data and software tools in this field. NASA and ESA have published many data sets and tools from various satellite missions under a free license.

The condition of even the most remote forests can be assessed with the help of satellite images in different spectra. All kinds of forest health indicators can be derived from data, like [deforestation risk](https://github.com/ghislainv/forestatrisk), [wildfire risk](https://github.com/pyronear/pyro-vision), or [tree detection](https://github.com/weecology/DeepForest). By using and improving these tools, you can actively contribute to preserving this ecosystem. Only by measuring and disclosing such information can environmentalists demonstrate that habitats are being lost.

You can also learn how to process satellite data using modern image processing algorithms such as neural networks. One of the most robust communities in this field is [Global Forest Watch](https://www.globalforestwatch.org/map/). Here, multiple datasets are combined to give an interactive overview of the health of forests worldwide.


<figure markdown>
  ![](https://opensource.com/sites/default/files/2022-05/notebooks_get_started_30_0.png)
  <figcaption> Figure 5: Spatial probability of deforestation on Guadeloupe </figcaption>
</figure>


Projects like [Resource Watch](https://resourcewatch.org/) and [Radiant Earth](https://www.radiant.earth/) provide entry-level platforms for people anywhere to understand natural resources based on Earth-observation technology. NASA provides its own open source platform, [NASA Harvest](https://nasaharvest.org/), to map the state of crops, providing essential information about food security. Another way to get insights about possible hunger crises is the measurement of soil moisture, which is also possible from space with packages like [smapr](https://github.com/ropensci/smapr).

The ever-increasing resolution of satellite data in recent years means that even the impact of individual companies on the environment can be measured. This new field of science is called spatial finance, and its purpose is to guide business development and investment in alignment with good sustainability practices. The first open datasets in this field track the locations and  companies involved in [cement production](https://www.cgfi.ac.uk/spatial-finance-initiative/geoasset-project/geoasset-databases/), [iron and steel production](https://www.cgfi.ac.uk/spatial-finance-initiative/geoasset-project/geoasset-databases/), and [global coal, oil, and gas supply chains](https://github.com/Lkruitwagen/global-fossil-fuel-supply-chain). The [Carbon Mapper](https://carbonmapperdata.org/map) platform shows how to build pressure on companies by disclosing methane and carbon dioxide sources.


<figure markdown>
  ![](https://opensource.com/sites/default/files/2022-05/all_assets.jpeg)
  <figcaption> Figure 6: Global coal, oil, and gas asset-level data
(Lucas Kruitwagen, MIT License) </figcaption>
</figure>


## Demand openness

Environmental catastrophes are often accompanied by a cover-up and manipulation of scientific findings and information. This applies to climate change as well as local environmental impacts. UN Secretary-General Antonio Guterres has given a clear warning following the release of the international climate change report, which shows no trend reversal in global warming and the loss of biodiversity in 2022.

> We are on a pathway to global warming of more than double the 1.5°C limit agreed in Paris. Some government and business leaders are saying one thing, but doing another. Simply put, they are lying. And the results will be catastrophic. This is a climate emergency.

<figure markdown>
  ![](https://opensource.com/sites/default/files/2022-05/tutorials_pyam_first_steps_65_1.png)
  <figcaption> Figure 7: With the help of pyam you can process the data behind the latest UN report and thus better understand the different scenarios.
(pyam, Apache license) </figcaption>
</figure>


One of the easiest ways to change course is to consistently demand open science concerning environmental issues. Openness is a key indicator of sustainable development, because anyone pursuing truly sustainable intentions is interested in refining their conclusions through open scientific discourse. Openness will also help prevent greenwashing, or the practice of promoting a company's sustainability efforts through marketing while scientific findings and conclusions about environmental impacts are downplayed or held private.

The next time you buy products that claim to be carbon neutral, ask for independent studies and data. If a politician demands questionable measures for environmental protection, ask for open model calculations and open access studies on this topic. Do you want to invest in a sustainable investment fund? Ask for open scientific studies, data, and models on why this investment is sustainable. Demanding openness in all these ways helps limit greenwashing and ensures that companies' environmental impacts are verifiable, accountable, and traceable.
