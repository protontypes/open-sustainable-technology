<h1 align="center">Awesome Sustainable Technology </h1>
<h4 align="center"> Open development environments to preserve global energy supply and vital natural resources</h4>
<p align="center"><i>Find more information in the <a href="https://protontypes.eu/blog/2020/10/05/gathering-open-sustainable-technology/"> official blog post.</i></p>
  
<p align="center">
  <img src="earth.gif" alt="animated" height="350" style="object-fit:contain" title="Artwork by Eleanor Lutz" />
</p>
<h5 align="center"> Artwork by Eleanor Lutz </h5>

- [Renewable Energy Sources](#renewable-energy-sources)
  * [Photovoltaic](#photovoltaic)
  * [Wind Turbines](#wind-turbines)
  * [Hydro Energy](#hydro-energy)
  * [Geothermal Energy](#geothermal-energy)
  * [Bioenergy](#bioenergy)
- [Energy Storage](#energy-storage)
  * [Battery](#battery)
  * [Hydrogen](#hydrogen)
- [Energy Distribution and Grids](#energy-distribution-and-grids)
- [Energy Consumption](#energy-consumption)
  * [Buildings and Cities](#buildings-and-cities)
  * [Mobility and Transportation](#mobility-and-transportation)
  * [Industry](#industry)
- [Energy System Assessment](#energy-system-assessment)
  * [Modeling](#modeling)
  * [Analysis](#analysis)
  * [Optimization](#optimization)
  * [Monitoring and Control](#monitoring-and-control)
- [Datasets on Electricity Consumption and Generation](#datasets-on-electricity-consumption-and-generation)
- [Emissions and Greenhouse Gases](#emissions-and-greenhouse-gases)
  * [Carbon Footprint](#carbon-footprint)
  * [Observation](#observation)
  * [Carbon Capture](#carbon-capture)
- [Observation and Conservation of Ecosystems](#observation-and-conservation-of-ecosystems)
  * [Vegitation and Biodiversity](#vegitation-and-biodiversity)
  * [Ice and Poles](#ice-and-poles)
  * [Ocean and Climate](#ocean-and-climate)
- [Access and Monitoring of Resources](#access-and-monitoring-of-resources)
  * [Air](#air)
  * [Water](#water)
  * [Soil](#soil)
- [Circular Economy and Waste](#circular-economy-and-waste)
- [Further Sustainability](#further-sustainability)
  * [Public Resources](#public-resources)
  * [Open Sustainable Communities](#open-sustainable-communities)


## Guideline
### Energy Supply
Global energy supply is a central basis for human life. The following aspects should be the focus of attention in order to ensure global scalability:

* Decentralised supply
* High availability
* Low impact on vital natural resources such as climate, water, soil or forests
* High robustness and easy maintenance

In order to understand the impact on different ecosystems and other natural resources, these need to be monitored and recorded. Only in this way can the impact of our actions be understood on a global scale.

### Vital Natural Resources
All life on earth is based on the availability of limited natural resources. Ensuring quality and accessibility for all life forms is a central task for sustainable technology.

### Contribution and Maintenance

_Your contribution is necessary to keep this list alive, increase the quality and to expand it. The same applies to the projects listed here. You can read more about the list and how you can participate in the [Contribution Guide](CONTRIBUTING.md)._ Maintenance is carried out by [protontypes](https://protontypes.eu/). We are an _Open Accelerator for Free and Sustainable Innovation._

[![](https://img.shields.io/twitter/follow/protontypes?style=social)](https://twitter.com/protontypes)

## Renewable Energy Sources
### Photovoltaic
- [pvlib-python](https://github.com/pvlib/pvlib-python) - A set of documented functions for simulating the performance of photovoltaic energy systems.
- [pvfactors](https://github.com/SunPower/pvfactors) - Open-source view-factor model for diffuse shading and bifacial PV modeling.
- [gsee](https://github.com/renewables-ninja/gsee) -  Global Solar Energy Estimator.
- [PVMismatch](https://github.com/SunPower/PVMismatch) - An explicit Python PV system IV & PV curve trace calculator which can also calculate mismatch.
- [rdtools](https://github.com/NREL/rdtools) - is an open-source library to support reproducible technical analysis of time series data from photovoltaic energy systems.
- [Machine-Learning-for-Solar-Energy-Prediction](https://github.com/ColasGael/Machine-Learning-for-Solar-Energy-Prediction) - Predict the power production of a solar panel farm from weather measurements using machine learning.
- [elpv-dataset](https://github.com/zae-bayern/elpv-dataset) - A dataset of functional and defective solar cells extracted from EL images of solar modules.
- [feedinlib](https://github.com/oemof/feedinlib) - contains implementations of photovoltaic models to calculate electricity generation from a pv installation based on given solar radiation. Furthermore it contains all necessary pre-calculations.
- [photovoltaic](https://github.com/pvedu/photovoltaic) - is a library of python functions used in photovoltaics.
- [pvcaptest](https://github.com/pvcaptest/pvcaptest) - Collection of functions and jupyter notebooks to partially automate running a capacity test following ASTM E2848.
- [pvtrace](https://github.com/danieljfarrell/pvtrace) - Optical ray tracing for luminescent materials and spectral converter photovoltaic devices.
- [SolarPILOT](https://github.com/NREL/SolarPILOT) - Solar power tower layout and optimization tool.
- [solar-data-tools](https://github.com/slacgismo/solar-data-tools) - Some data analysis tools for working with historical PV solar time-series data sets.
- [SolarPV-DER-simulation-utility](https://github.com/sibyjackgrove/SolarPV-DER-simulation-utility) -  Allows user to run dynamics simulations for solar photovoltaic distributed energy resource connected to a stiff voltage source or to an external program.
- [bifacial_radiance](https://github.com/NREL/bifacial_radiance) - Toolkit for working with RADIANCE for the ray-trace modeling of Bifacial Photovoltaics.
- [autoXRD](https://github.com/PV-Lab/autoXRD) - is a python package for automatic XRD pattern classification of thin-films, tweaked for small and class-imbalanced datasets.
- [BayesProcess](https://github.com/PV-Lab/BayesProcess) - is a python package for Physics informed Bayesian network inference using neural network surrogate model for matching process / variable / performance in solar cells.
- [solcore5](https://github.com/qpv-research-group/solcore5) - A multi-scale, python-based library for the modelling of solar cells and semiconductor materials.
- [solax](https://github.com/squishykid/solax) - Read energy usage data from the real-time API on Solax solar inverters.
- [bifacialvf](https://github.com/NREL/bifacialvf) - Bifacial PV View Factor model for system performance calculation.
- [solar](https://github.com/oscarperpinan/solar) - allows for reproducible research both for photovoltaics systems performance and solar radiation.
- [SolarTherm](https://github.com/SolarTherm/SolarTherm) - Solar thermal power/fuel station performance simulation and optimization using Modelica.
- [Charge Controller Firmware](https://github.com/LibreSolar/charge-controller-firmware) - Firmware for Libre Solar MPPT/PWM charge controllers.


### Wind Turbines
- [makani](https://github.com/google/makani) - was a project to develop a commercial-scale airborne wind turbine, culminating in a flight test of the Makani M600 off the coast of Norway.
- [IEA-15-240-RWT](https://github.com/IEAWindTask37/IEA-15-240-RWT) - A 15 MW reference wind turbine repository developed in conjunction with IEA Wind.
- [windpowerlib](https://github.com/wind-python/windpowerlib) - The windpowerlib is a library to model the output of wind turbines and farms.
- [turbinesFoam](https://github.com/turbinesFoam/turbinesFoam) - is a library for simulating wind and marine hydrokinetic turbines in OpenFOAM using the actuator line method.
- [nalu-wind](https://github.com/Exawind/nalu-wind) - Solver for wind farm simulations targeting exascale computational platforms.
- [openfast](https://github.com/OpenFAST/openfast) - was created with the goal of being a community model developed and used by research laboratories, academia, and industry.
- [amr-wind](https://github.com/Exawind/amr-wind) - is a massively parallel, block-structured adaptive-mesh, incompressible flow sover for wind turbine and wind farm simulations.
- [QBlade](http://www.q-blade.org/#welcome) - provides a hands on design and simulation capabilities for HAWT and VAWT rotor design and shows all the fundamental relationships of design concepts and turbine performance in an easy and intuitive way.
- [OpenOA](https://github.com/NREL/OpenOA) - This library provides a framework for working with large timeseries data from wind plants, such as SCADA.
- [ROSCO](https://github.com/NREL/ROSCO) - NREL's Reference OpenSource Controller for wind turbine applications.
- [floris](https://github.com/NREL/floris) - A controls-oriented engineering wake model.
- [windtools](https://github.com/FZJ-IEK3-VSA/windtools) - The Wind Energy Generation Tools provides useful tools to assist in wind energy simulations.
- [PyWake](https://gitlab.windenergy.dtu.dk/TOPFARM/PyWake) - an AEP calculator for wind farms implemented in Python including a collection of wake models.
- [WISDEM](https://github.com/WISDEM/WISDEM) - Wind Plant Integrated System Design and Engineering Model.
- [LandBOSSE](https://github.com/WISDEM/LandBOSSE) - The Land-based Balance-of-System Systems Engineering model is a systems engineering tool that estimates the balance-of-system costs associated with installing utility scale wind plants (10, 1.5 MW turbines or larger).
- [OpenMDAO](https://github.com/OpenMDAO/OpenMDAO) - Optimization of Aerodynamic systems.
- [TopFarm2](https://gitlab.windenergy.dtu.dk/TOPFARM/TopFarm2) - is a Python package developed by DTU Wind Energy to help with wind-farm optimizations.
- [BasicDTUController](https://gitlab.windenergy.dtu.dk/OpenLAC/BasicDTUController) - The scope of this project is to provide an open-source open-access controller that can be used by the wind energy community as a reference.
- [WindEnergyToolbox](https://gitlab.windenergy.dtu.dk/toolbox/WindEnergyToolbox) - is a collection of Python scripts that facilitate working with (potentially a lot) of HAWC2,HAWCStab2, FAST or other text input based simulation tools.
- [windfarmGA](https://github.com/YsoSirius/windfarmGA) - Genetic algorithm to optimize the layout of windfarms.
- [wtphm](https://github.com/lkev/wtphm) - The Wind Turbine Prognostics and Health Management library processes wind turbine events data, as well as operational SCADA data for easier fault detection, prognostics or reliability research.
- [AirfoilPreppy](https://github.com/WISDEM/AirfoilPreppy) - A Python module for preprocessing and evaluating aerodynamic airfoil data, primarily for wind turbine applications.
- [GreenGuard](https://github.com/signals-dev/GreenGuard) - is a collection of end-to-end solutions for machine learning problems commonly found in monitoring wind energy production system
- [pv-terms](https://github.com/DuraMAT/pv-terms) - contains nomenclature for PV-relevant terms that are used in modeling and data analysis for PV systems.


### Hydro Energy
- [WecOptTool](https://github.com/SNL-WaterPower/WecOptTool) - allows users to perform wave energy converter device design optimization studies with constrained optimal control.
- [CACTUS](https://github.com/SNL-WaterPower/CACTUS) - is a turbine performance simulation code, based on a free wake vortex method, to study wind turbines and marine hydrokinetic devices.
- [hydro-power-database](https://github.com/energy-modelling-toolkit/hydro-power-database) - dataset tries to collect some basic information on all the European hydro-power plants.
- [MHKiT-Python](https://github.com/MHKiT-Software/MHKiT-Python) - provides the marine renewable energy community tools for data processing, visualization, quality control, resource assessment, and device performance.
- [hydropowerlib](https://github.com/hydro-python/hydropowerlib) - The hydropowerlib is designed to calculate feedin time series of run-of-the-river hydropower plants.

### Geothermal Energy
- [pygfunction](https://github.com/MassimoCimmino/pygfunction) - An open-source toolbox for the evaluation of thermal response factors of geothermal borehole fields.
- [geothermics](https://github.com/Japhiolite/geothermics) - Educational repository with Jupyter Notebooks all around the topic of geothermal energy.
- [energy2d](https://github.com/charxie/energy2d) - Interactive Heat Transfer Simulations for Everyone.
- [OpenGeoSys 6](https://gitlab.opengeosys.org/ogs/ogs) - is a scientific open source project for the development of numerical methods for the simulation of thermo hydro-mechanical-chemical processes in porous and fractured media.
- [FEHM](https://github.com/lanl/FEHM) - has proved to be a valuable asset on a variety of projects of national interest including Environmental Remediation of the Nevada Test Site, the LANL Groundwater Protection Program, geologic CO2 sequestration, Enhanced Geothermal Energy programs, Oil and Gas production, Nuclear Waste Isolation, and Arctic Permafrost.
- [thermo](https://github.com/CalebBell/thermo) - Thermodynamics, phase equilibria, transport properties and chemical database component of Chemical Engineering Design Library.


### Bioenergy
- [sashahafner/biogas](https://github.com/sashahafner/biogas) - Tools for biogas research in R: process biogas data and predict biogas production.
- [biosteam](https://github.com/BioSTEAMDevelopmentGroup/biosteam) - The Biorefinery Simulation and Techno-Economic Analysis Modules.
- [Multiscale_Ulva](https://github.com/alexliberzonlab/Multiscale_Ulva) - is a multi-reactor, algae farm, simulation base function that will be 
solved in time.


## Energy Storage

### Battery
- [foxBMS](https://github.com/foxBMS/foxbms) -  is a free, open and flexible development environment to design battery management systems. It is the first modular open source BMS development platform.
- [impedance.py](https://github.com/ECSHackWeek/impedance.py) - A Python package for working with electrochemical impedance data.
- [PyBaMM](https://github.com/pybamm-team/PyBaMM) - Fast and flexible physics-based battery models in Python.
- [ENNOID-BMS](https://github.com/EnnoidMe/ENNOID-BMS) - Open-Source: Modular BMS based on LTC68XX & STM32 MCU for up to 400V EV battery pack.
- [cellpy](https://github.com/jepegit/cellpy) - extract and tweak data from electrochemical tests of batterie cells.
- [prediction-of-battery-cycle](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation) - Data driven prediciton of battery cycle life before capacity degradation.
- [BatterySense](https://github.com/rlogiacco/BatterySense) - This is a simple Arduino library to monitor battery consumption of your battery powered projects, being LiPo, LiIon, NiCd or any other battery type, single or multiple cells: if it can power your Arduino you can monitor it!
- [beep](https://github.com/TRI-AMDD/beep) - is a set of tools designed to support Battery Evaluation and Early Prediction of cycle life corresponding to the research of the d3batt program and the Toyota Research Institute.
- [snl-quest](https://github.com/snl-quest/snl-quest) - An open source, Python-based software application suite for energy storage simulation and analysis developed by Sandia National Laboratories.
- [simses](https://gitlab.lrz.de/open-ees-ses/simses) - Software for techno-economic Simulation of Stationary Energy Storage Systems.
- [CAEBAT OAS](https://vibe.ornl.gov/#introduction) - a flexible, robust, and computationally scalable open-architecture framework that integrates multi-physics and multi- scale battery models.
- [universal-battery-database](https://github.com/Samuel-Buteau/universal-battery-database) - The Universal Battery Database is an open source software for managing Lithium-ion cell data.
- [open_BEA](https://gitlab.lrz.de/open-ees-ses/openbea) - Open Battery Models for Electrical Grid Applications.
- [lp_opt](https://gitlab.lrz.de/open-ees-ses/lp_opt) - Linear Programming Optimization Tool for Battery Energy Storage Systems.
- [SLIDE](https://github.com/davidhowey/SLIDE) - SLIDE is a C++ code that simulates degradation of lithium ion cell.
- [equiv-circ-model](https://github.com/batterysim/equiv-circ-model) - An equivalent circuit model for a battery cell, module, and pack.
- [long-live-the-battery](https://github.com/dsr-18/long-live-the-battery) - Predicting total battery cycle life time with machine learning.
- [ISEAFramework](https://github.com/FHust/ISEAFramework) - allows coupled electrical-thermal simulations of single storage systems (e.g. lithium ion batteries or double layer capacitors) or complete storage system packs.
- [Ampere](https://github.com/nealde/Ampere) - Advanced Model Package for ElectRochemical Experiments

### Hydrogen
- [OPEM](https://github.com/ECSIM/opem) - is a modeling tool for evaluating the performance of proton exchange membrane fuel cells.
- [gopem](https://github.com/ECSIM/gopem) - GOPEM is a graphical user interface of OPEM.
- [pem-dataset1](https://github.com/ECSIM/pem-dataset1) - Proton Exchange Membrane Fuel Cell Dataset.
- [HIM](https://github.com/FZJ-IEK3-VSA/HIM) - Hydrogen Infrastructure model for the analysis of spatially resolved hydrogen infrastructure pathways.
- [pandapipes](https://github.com/e2nIEE/pandapipes) - A pipeflow calculation tool that complements pandapower in the simulation of multi energy grids, in particular heat and gas networks.
- [The Hydrogen Risk Assessment Models](https://github.com/sandialabs/hyram) - is the first-ever software toolkit that integrates deterministic and probabilistic models for quantifying accident scenarios, predicting physical effects, and characterizing hydrogen hazards impact on people and structures.
- [OpenHPL](https://github.com/simulatino/OpenHPL) - is an open-source hydropower library that consists of hydropower unit models and is modelled using Modelica.
- [GasModels.jl](https://github.com/lanl-ansi/GasModels.jl) - A Julia/JuMP Package for Gas Network Optimization.


## Energy Distribution and Grids
- [SimBench](https://github.com/e2nIEE/simbench) - The objective of the research project SimBench is the development of a benchmark dataset to support research in grid planning and operation.
- [Egret](https://github.com/grid-parity-exchange/Egret) - is a Python-based package for electrical grid optimization based on the Pyomo optimization modeling language.
- [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur) - PyPSA-Eur: An Open Optimization Model of the European Transmission System.
- [Energy Transition Engine](https://github.com/quintel/etengine) - Calculation engine for the Energy Transition Model.
- [Open Smart Grid Platform](https://github.com/OSGP/open-smart-grid-platform) - is an open, generic, scalable and independent 'Internet of Things' platform, which enables various connected smart objects in the public space to be easily controlled and monitored.
- [PowerModels.jl](https://github.com/lanl-ansi/PowerModels.jl) - is designed to enable computational evaluation of emerging power network formulations and algorithms in a common platform.
- [PowerModelsAnnex.jl](https://github.com/lanl-ansi/PowerModelsAnnex.jl) - an extension of PowerModels.jl that provides a home for open-source sharing of preliminary and/or exploratory methods in power system optimization.
- [Power Grid Lib](https://github.com/power-grid-lib/pglib-opf) - This benchmark library is curated and maintained by the IEEE PES Task Force on Benchmarks for Validation of Emerging Power System Algorithms and is designed to evaluate a well established version of the the AC Optimal Power Flow problem.
- [pypownet](https://github.com/MarvinLer/pypownet) - A power network simulator with a Reinforcement Learning-focused usage.
- [Grid2Op](https://github.com/rte-france/Grid2Op) -  a testbed platform to model sequential decision making in power systems.
- [eDisGo](https://github.com/openego/eDisGo/) - Optimization of flexibility options and grid expansion for distribution grids based on PyPSA.
- [offgridders](https://github.com/rl-institut/offgridders) - Models and optimizes capacity & dispatch of electricity supply systems, off-grid or connected to a (weak) central grid.
- [RTS-GMLC](https://github.com/GridMod/RTS-GMLC) - Reliability Test System of the Grid Modernization Lab Consortium.
- [openmodelica-microgrid-gym](https://github.com/upb-lea/openmodelica-microgrid-gym) - An OpenAI Gym Environment for Microgrids.
- [OpenDSS](https://sourceforge.net/projects/electricdss/) - is an electric power Distribution System Simulator for supporting distributed resource integration and grid modernization efforts.


## Energy Consumption

### Buildings and Cities

- [hpxml](https://github.com/hpxmlwg/hpxml) - Home Performance XML is a data transfer standard for the home performance industry.
- [HPXML to Home Energy Score Translator](https://github.com/NREL/hescore-hpxml) - This translator script takes an HPXML file or directory of files as an input and generates HEScore inputs from it.
- [LoadProfileGenerator](https://github.com/FZJ-IEK3-VSA/LoadProfileGenerator) - Program for generating load curves for residential consumers. Agentbased and extremly detailed
- [The-building-data-genome-project](https://github.com/buds-lab/the-building-data-genome-project) - A collection of non-residential buildings for performance analysis and algorithm benchmarking.
- [VOLTTRON](https://github.com/VOLTTRON/volttron) - The platform provides services for collecting and storing data from buildings and devices and provides an environment for developing applications which interact with that data.
- [OpenEnergyMonitor](https://github.com/openenergymonitor) - Open-source energy monitoring tools to help us relate to our use of energy, our energy systems and the challenge of sustainable energy.
- [EnergyPlus](https://github.com/NREL/EnergyPlus) -  is a whole building energy simulation program that engineers, architects, and researchers use to model both energy consumption and water use in buildings.
- [OpenStudio](https://github.com/NREL/OpenStudio) -  is a cross-platform collection of software tools to support whole building energy modeling using EnergyPlus and advanced daylight analysis using Radiance.
- [BEMServer](https://github.com/HIT2GAP-EU-PROJECT/bemserver) - An open source Python server to deploy energy management solutions for buildings.
- [SEED](https://github.com/SEED-platform/seed) - Standard Energy Efficiency Data Platform™ is a web-based application that helps organizations easily manage data on the energy performance of large groups of buildings.
- [HPWHsim](https://github.com/EcotopeResearch/HPWHsim) - An open source simulation model for Heat Pump Water Heaters (HPWH).
- [OpenStudio-ERI](https://github.com/NREL/OpenStudio-ERI) - Calculates an Energy Rating Index (ERI) via an OpenStudio/EnergyPlus-based workflow. Building information is provided through an HPXML file.
- [OpenStudio-HPXML](https://github.com/NREL/OpenStudio-HPXML) - Modeling of residential buildings in EnergyPlus using OpenStudio/HPXML.
- [AixLib](https://github.com/RWTH-EBC/AixLib) - A Modelica model library for building performance simulations.
- [TEASER](https://github.com/RWTH-EBC/TEASER) - Tool for Energy Analysis and Simulation for Efficient Retrofit.
- [tespy](https://github.com/oemof/tespy) - provides a powerful simulation toolkit for thermal engineering plants such as power plants, district heating systems or heat pumps.
- [RC_BuildingSimulator](https://github.com/architecture-building-systems/RC_BuildingSimulator) - A Resistance Capacitance Model for an Energetic Simulation of a Building.
- [CEA](https://github.com/architecture-building-systems/CityEnergyAnalyst) - helps you to analyse the effects of building retrofits, land-use planning, district heating and cooling and renewable energy on the future costs, emissions and energy consumption of neighbourhoods and districts.
- [The Modelica Buildings](https://github.com/lbl-srg/modelica-buildings) - library is a free open-source library with dynamic simulation models for building energy and control systems.
- [StROBe](https://github.com/open-ideas/StROBe) - is an open web tool developed at the KU Leuven Building Physics Section to model the pervasive space for residential integrated district energy assessment simulations in the openIDEAS modeling environment.
- [NYCBuildingEnergyUse](https://github.com/mdh266/NYCBuildingEnergyUse) - predict the emission of green house gases from buildings by looking at their age, and water consumption as well as other energy consumption metrics.
- [Smart-Energy-Monitor](https://github.com/jonathanrjpereira/Smart-Energy-Monitor) - The goal is to accurately predict the monthly electricity bill of the household using minimum hardware & by acquiring electrical data at a single location.
- [Hotmaps](https://github.com/HotMaps/Hotmaps-toolbox-service) - The open source mapping and planning tool for heating and cooling. 
- [BuildSysPro](https://github.com/EDF-TREE/BuildSysPro) - is EDF's Modelica library for buildings, districts and energy systems modelling.
- [MPCPy](https://github.com/lbl-srg/MPCPy) - the python-based open-source platform for model predictive control in buildings.
- [obc](https://github.com/lbl-srg/obc) - Performance Evaluation, Specification, Deployment and Verification of Building Control Sequences. 
- [The Application Domain Extension (ADE) Energy](https://git.rwth-aachen.de/energyade/citygml-energy) - defines a standardized data model based on CityGML format for urban energy analyses, aiming to be a reference exchange data format between different urban modelling tools and expert databases.


### Mobility and Transportation

- [stplanr](https://github.com/ropensci/stplanr) - is a package for sustainable transport planning with R.
- [The Open Charge Point Protocol](https://github.com/NewMotion/ocpp) - is a network protocol for communication between electric vehicle chargers and a central backoffice system.
- [ocpp](https://github.com/mobilityhouse/ocpp) - Python implementation of the Open Charge Point Protocol.
- [docile-charge-point](https://github.com/NewMotion/docile-charge-point) - Scriptable OCPP charge point simulator and test tool.
- [MaaS Global](https://github.com/maasglobal/maas-schemas) - Mobility as a Service API - data model, tests, and validation.
- [CoopCycle](https://github.com/coopcycle/coopcycle-web) - is a self-hosted platform to order meals in your neighborhood and get them delivered by bike couriers.
- [EVNotify](https://github.com/EVNotify/EVNotify) -  allows you to monitor your electric vehicle and let you notify when the specified preset state of charge has been achieved.
- [icare](https://github.com/diowa/icare) - is an open source carpooling platform used as a basis for our commercial product Company Carpool.
- [Carpoolear](https://github.com/STS-Rosario/carpoolear) - is the first Argentine Facebook app that allow the users of this social network share car trips with other users.
- [UTD19](https://utd19.ethz.ch/) - Largest multi-city traffic dataset publically available.
- [OpenEVSE](https://github.com/OpenEVSE/ESP8266_WiFi_v2.x) - Open Source Electric Vehicle Charging Station.
- [navitia](https://github.com/CanalTP/navitia) - is an open-source web API, initially built to provide traveler information on urban transportation networks.
- [DeepMove](https://github.com/vonfeng/DeepMove) - Predicting Human Mobility with Attentional Recurrent Networks.
- [mobility-data-specification](https://github.com/openmobilityfoundation/mobility-data-specification) - A data standard to enable communication between mobility companies and local governments.
- [sumo](https://github.com/eclipse/sumo) - SUMO is an open source, highly portable, microscopic and continuous traffic simulation package designed to handle large networks. It allows for intermodal simulation including pedestrians and comes with a large set of tools for scenario creation.
- [OpenConcept](https://github.com/mdolab/openconcept) - A toolkit for conceptual MDAO of aircraft with unconventional propulsion architectures.
- [Open Charge Map](https://github.com/openchargemap/ocm-system) - is the global public registry of electric vehicle charging locations.
- [EVCC](https://github.com/andig/evcc) - is an extensible EV Charge Controller with PV integration implemented in Go.
- [SteVe](https://github.com/RWTH-i5-IDSG/steve) - provides basic functions for the administration of charge points, user data, and RFID cards for user authentication and was tested successfully in operation.
- [RISE-V2G](https://github.com/V2GClarity/RISE-V2G) - The only fully-featured reference implementation of the Vehicle-2-Grid communication interface ISO 15118.
- [simobility](https://github.com/sash-ko/simobility) - is a human-friendly Python framework that helps scientists and engineers to prototype and compare fleet optimization algorithms (autonomous and human-driven vehicles).
- [MobiVoc](https://github.com/vocol/mobivoc) - is an open vocabulary for future-oriented mobility solutions.
- [Transportr](https://github.com/grote/Transportr) - The public transport companion that respects your privacy and your freedom.
- [OneBusAway](https://github.com/OneBusAway/onebusaway-android) - The Open Source platform for Real Time Transit Info.
- [transitfeed](https://github.com/google/transitfeed) - A Python library for reading, validating, and writing transit schedule information in the GTFS format.
- [node-gtfs](https://github.com/BlinkTagInc/node-gtfs) - Import GTFS transit data into SQLite and query routes, stops, times, fares and more.
- [Public Transport Enabler](https://github.com/schildbach/public-transport-enabler) - Unleash public transport data in your Java project.
- [osm2gtfs](https://github.com/grote/osm2gtfs) - Turn OpenStreetMap data and schedule information into GTFS.
- [Quetzal](https://github.com/systragroup/quetzal) - Quetzal is a modeling library designed for transport planning and traffic forecasts.
- [quetzal_germany](https://github.com/marlinarnz/quetzal_germany) - A four step transport model for Germany using the quetzal transport modelling suite.
- [MATSim](https://github.com/matsim-org/matsim-libs) - MATSim provides a toolbox to run and implement large-scale agent-based transport simulations.
- [OpenMobility](https://openmobility.eclipse.org/) - Driving the Evolution and Broad Adoption of Open Source Mobility Modelling and Simulation Technologies.
- [NoiseModelling](https://github.com/Ifsttar/NoiseModelling) - A free and open-source model to compute noise maps.
- [NoiseCapture](https://github.com/Ifsttar/NoiseCapture) - Android App dedicated to the measurement of environmental noise.
- [bikedata](https://github.com/ropensci/bikedata) - aims to enable ready importing of historical trip data from all public bicycle hire systems which provide data, and will be expanded on an ongoing basis as more systems publish open data.
- [CyclOSM](https://github.com/cyclosm/cyclosm-cartocss-style) - is a CartoCSS map style designed with cycling in mind.
- [Gym Electric Motor](https://github.com/upb-lea/gym-electric-motor) - An OpenAI Gym Environment for Electric Motors.
- [BEAM](https://github.com/LBNL-UCB-STI/beam) - The Framework for Modeling Behavior, Energy, Autonomy, and Mobility in Transportation Systems.
- [WoBike](https://github.com/ubahnverleih/WoBike) - Public transport and multimodal routing apps could benefit from showing nearby bikes from bikesharing services. So here's a list showing the APIs of a few of these platforms.
- [multicycles](https://github.com/PierrickP/multicycles) - aggregates on one map, more than 100 share vehicles like bikes, scooters, mopeds and cars.
- [pybikes](https://github.com/eskerda/pybikes) - provides a set of tools to scrape bike sharing data from different websites and APIs, thus providing a coherent and generalized set of classes and methods to access this sort of information.
- [sustainable-mobility-api](https://gitlab.com/mshepherd/sustainable-mobility-api) - consists of a Python library and HTTP API for estimating the environmental impact of personal mobility.
- [ChargyDesktopApp](https://github.com/OpenChargingCloud/ChargyDesktopApp) - Chargy is a transparency software for secure and transparent e-mobility charging processes, as defined by the German "Eichrecht"
- [WWCP_OCPP](https://github.com/OpenChargingCloud/WWCP_OCPP) - Connectivity between the World Wide Charging Protocol (WWCP) and the Open Charge Point Protocol (OCPP v1.6/v2.0).
- [WWCP_Core](https://github.com/OpenChargingCloud/WWCP_Core) - The World Wide Charging Protocol Suite is a collection of protocols in order to connect market actors in the field of e-mobility solutions via scalable and secure Internet protocols


### Industry

- [Industry Energy Tool](https://github.com/NREL/Industry-Energy-Tool) -  is a calculator developed by NREL for projecting energy efficiency and fuel switching scenarios for the U.S. industrial sector energy use and emissions at the Census Region and county-level.
- [Industry Energy Data Book](https://github.com/NREL/Industry-energy-data-book) - summarizes the status of, and identifies the key trends in energy use and its underlying economic drivers across the four industrial subsectors: agriculture, construction, manufacturing, and mining.
- [CalTRACK](https://github.com/energy-market-methods/caltrack) - methods are developed in an open and transparent stakeholder process that uses empirical testing to define replicable methods for calculating normalized metered energy consumption using either monthly or interval data from an existing conditions baseline.
- [H2020 CATALYST](https://gitlab.com/project-catalyst) - Converting data centres in energy flexibility ecosystems


## Energy System Assessment

### Modeling

- [GCAM](https://github.com/JGCRI/gcam-core) - is a dynamic-recursive model with technology-rich representations of the economy, energy sector, land use and water linked to a climate model that can be used to explore climate change mitigation policies including carbon taxes, carbon trading, regulations and accelerated deployment of energy technology.
- [System Advisor Model](https://github.com/NREL/SAM) - is a simulation program for electricity generation projects. It has models for different kinds of renewable energy systems and financial models for residential, commercial, and utility-scale projects.
- [openTEPES](https://github.com/IIT-EnergySystemModels/openTEPES) - determines the investment plans of new facilities (generators, ESS and lines) for supplying the forecasted demand at minimum cost.
- [PowerGenome](https://github.com/gschivley/PowerGenome) - A tool to quickly and easily create inputs for power systems models.
- [load_forecasting](https://github.com/pyaf/load_forecasting) - Load forcasting on Delhi area electric power load using ARIMA, RNN, LSTM and GRU models.
- [REopt_Lite_API](https://github.com/NREL/REopt_Lite_API) - offers a subset of features from NREL's more comprehensive REopt model. Both models provide concurrent, multiple technology integration and optimization capabilities to help organizations meet their cost savings and energy performance goals.
- [pandapower](http://www.pandapower.org/) - An easy to use open source tool for power system modeling, analysis and optimization with a high degree of automation.
- [urbs](https://github.com/tum-ens/urbs) - A linear optimization model for distributed energy systems.
- [Dispa-SET](https://github.com/energy-modelling-toolkit/Dispa-SET) - allows to model a power system at any level of detail e.g. micro-grid, region, country, continent.
- [Calliope](https://github.com/calliope-project/calliope) - is a framework to develop energy system models, with a focus on flexibility, high spatial and temporal resolution, the ability to execute many runs based on the same base model, and a clear separation of framework  and model.
- [OSeMOSYS](https://github.com/OSeMOSYS/OSeMOSYS) - is an open source modelling system for long-run integrated assessment and energy planning. It has been employed to develop energy systems models from the scale of continents (African Power Pools, South America, EU28+2) down to the scale of countries, regions and village.
- [REVUB](https://github.com/VUB-HYDR/REVUB) - The main objective is to model how flexible operation of hydropower plants can help renewable electricity mixes with variable solar and wind power to provide reliable electricity supply and load-following services.
- [FINE](https://github.com/FZJ-IEK3-VSA/FINE) -  provides a framework for modeling, optimizing and assessing energy systems.
- [CoMPAS](https://github.com/com-pas/compas-architecture) - was formed to develop open source software components related to IEC 61850 model implementation (profile management) and configuration of a power industry Protection Automation and Control System.
- [PowerSimulations.jl](https://github.com/NREL-SIIP/PowerSimulations.jl) - is a Julia package for power system modeling and simulation of Power Systems operations.
- [PowerSystems.jl](https://github.com/NREL-SIIP/PowerSystems.jl) - provides a rigorous data model using Julia structures to enable power systems analysis and modeling.
- [Balmorel](https://github.com/balmorelcommunity/Balmorel) - is a partial equilibrium model for analysing the electricity and combined heat and power sectors in an international perspective.
- [DistAIX](https://git.rwth-aachen.de/acs/public/simulation/DistAIXFramework/distaix) - is a simulator for cyber-physical power systems that makes use of high performance computing techniques to scale up the simulation.
- [The Open Energy Ontology](https://github.com/OpenEnergyPlatform/ontology) - is a domain ontology of the energy-system modelling context.
- [nempy](https://github.com/UNSW-CEEM/nempy) - aims to enhance the Australia electricity industries modelling and analytical capabilities.
- [NEMO](https://github.com/bje-/NEMO) - The National Electricity Market Optimiser is a chronological dispatch model for testing and optimising different portfolios of conventional and renewable electricity generation technologies.
- [GlobalEnergyGIS](https://github.com/niclasmattsson/GlobalEnergyGIS) - Generates input data for energy models on renewable energy in arbitrary world regions using public datasets.
- [IDEAS](https://github.com/open-ideas/IDEAS) - Modelica library allowing simultaneous transient simulation of thermal and electrical systems at both building and feeder level.
- [Antares Simulator](https://github.com/AntaresSimulatorTeam/Antares_Simulator) - is an Open Source power system simulator to quantify the adequacy or the economic performance of interconnected energy systems, at short or remote time horizons.
- [Hierarchical Engine for Large-scale Infrastructure Co-Simulation](https://github.com/GMLC-TDC/HELICS) - Today the core uses are in the energy domain, where there is extensive and growing support for a wide-range of electric power system, natural gas, communications and control-schemes, transportation, buildings, and related domain tools.
- [oemof-solph](https://github.com/oemof/oemof-solph) - is a model generator for energy system modelling and optimisation.
- [oemof-thermal](https://github.com/oemof/oemof-thermal) -  provides tools to model thermal energy components as an extension of oemof.solph, e.g. compression heat pumps, concentrating solar plants, thermal storages and solar thermal collectors.
- [dpsim](https://git.rwth-aachen.de/acs/public/simulation/dpsim/dpsim) - is a real-time power system simulator that operates in the dynamic phasor as well as electromagentic transient domain.
- [VILLASnode](https://git.rwth-aachen.de/acs/public/villas/node) - Connecting real-time power grid simulation equipment
- [openENTRANCE](https://github.com/openENTRANCE/nomenclature) - The Horizon 2020 openENTRANCE project aims at developing, using and disseminating an open, transparent and integrated modelling platform for assessing low-carbon transition pathways in Europe.


### Analysis

- [Open Energy Platform](https://github.com/OpenEnergyPlatform/oeplatform) - aims to ensure quality, transparency and reproducibility in energy system research. It is a collection of various tools and information and that help working with energy related data.
- [PyPSA](https://github.com/PyPSA/PyPSA) - is a free software toolbox for simulating and optimising modern power systems that include features such as conventional generators with unit commitment, variable wind and solar generation, storage units, coupling to other energy sectors, and mixed alternating and direct current networks.
- [oemof](https://github.com/oemof/oemof) - Open Energy Modelling Framework - A python toolbox for energy system modelling and optimisation. A community driven, modular, flexible and generic software project.
- [pyGRETA](https://github.com/tum-ens/pyGRETA) - python Generator of REnewable Time series and mAps: a tool that generates high-resolution potential maps and time series for user-defined regions within the globe.
- [RESKit](https://github.com/FZJ-IEK3-VSA/RESKit) - A toolkit to help generate renewable energy generation time-series for energy systems analysis.
- [PowSyBl](https://github.com/powsybl/powsybl-core) - is an open source framework written in Java, that makes it easy to write complex software for power systems simulations and analysis.
- [PowSyBl Open Load Flow](https://github.com/powsybl/powsybl-open-loadflow) - is an open source implementation of the load flow API that can be found in PowSyBl Core. It supports AC Newtow-Raphson and linear DC calculation methods.
- [matpower](https://github.com/MATPOWER/matpower) - is a package of M-files for solving power flow, continuation power flow and optimal power flow problems using MATLAB or Octave.
- [energyRt](https://github.com/energyRt/energyRt) - Making Energy Systems Modeling as simple as a linear regression in R.
- [MVS](https://github.com/rl-institut/mvs_eland) - The multi-vector simulator allows the evaluation of local sector-coupled energy systems that include the energy carriers electricity, heat and/or gas.

### Optimization

- [reV](https://github.com/NREL/reV) - enables the efficient and scalable computation of renewable energy generation, levelized cost of energy, application of geospatial exclusion layers, and generation of renewable energy supply curves.
- [openCEM](https://github.com/openCEMorg/openCEM) - Capacity Expansion Model and Optimiser for the Australian National Energy Market.
- [energy-py](https://github.com/ADGEfficiency/energy-py) -  Reinforcement learning for energy systems.
- [glaes](https://github.com/FZJ-IEK3-VSA/glaes) - Geospatial Land Availability for Energy Systems.
- [onsset](https://github.com/OnSSET/onsset) - is a GIS based optimization tool that has been developed to support electrification planning and decision making for the achievement of energy access goals in currently unserved locations.
- [whobs-server](https://github.com/PyPSA/whobs-server) - This is the code for the online optimization of zero-direct-emission electricity systems with wind, solar and storage (using batteries and electrolysed hydrogen gas) to provide a baseload electricity demand, using the cost and other assumptions of your choice.
- [WHAT-IF](https://github.com/RaphaelPB/WHAT-IF) - Water, Hydropower, Agriculture Tool for Investment and Financing decision support tool.
- [CityLearn](https://github.com/intelligent-environments-lab/CityLearn) - Official reinforcement learning environment for demand response and load shaping.
- [rl-testbed-for-energyplus](https://github.com/IBM/rl-testbed-for-energyplus) - Reinforcement Learning Testbed for Power Consumption Optimization using EnergyPlus.

### Monitoring and Control

- [OpenEMS](https://github.com/OpenEMS/openems) - Open Source Energy Management System.
- [eemeter](https://github.com/openeemeter/eemeter) - An open source python package for implementing and developing standard methods for calculating normalized metered energy consumption and avoided energy use.
- [OperatorFabric](https://github.com/opfab/operatorfabric-core) - is a modular, extensible, industrial-strength and field-tested platform for use in electricity, water, and other utility operations.
- [energy-sparks](https://github.com/Energy-Sparks/energy-sparks) - an open source application that is designed to help schools improve their energy efficiency.


## Datasets on Electricity Consumption and Generation

- [The Public Utility Data Liberation Project](https://github.com/catalyst-cooperative/pudl) - makes US energy data easier to access and use.
- [Global Power Plant Database](https://github.com/wri/global-power-plant-database) - A comprehensive, global, open source database of power plants.
- [electricitymap-contrib](https://github.com/tmrowco/electricitymap-contrib) - A real-time visualisation of the CO2 emissions of electricity consumption.
- [entsoe-py](https://github.com/EnergieID/entsoe-py) - Python client for the ENTSO-E API (european network of transmission system operators for electricity).
- [time series](https://github.com/Open-Power-System-Data/time_series) - contains scripts that compile time series data of the European power system.
- [renewable power plant](https://github.com/Open-Power-System-Data/renewable_power_plants) - contains scripts to create lists of renewable power plants in Germany, Denmark, France and Poland, and daily time series of cumulated installed capacity per energy source type for Germany.
- [conventional power plants](https://github.com/Open-Power-System-Data/conventional_power_plants) - contains data on conventional power plants for Germany as well as other selected European countries. The data includes individual power plants with their technical characteristics.
- [open-MaStR](https://github.com/OpenEnergyPlatform/open-MaStR) - download and process German energy data from BNetzA database Marktstammdatenregister.
- [powerplantmatching](https://github.com/FRESNA/powerplantmatching) - A toolset for cleaning, standardizing and combining multiple power plant databases.
- [GeoNuclearData](https://github.com/cristianst85/GeoNuclearData) - Database with information about Nuclear Power Plants worldwide.
- [pyEIA](https://github.com/thomastu/pyEIA) - An Energy Information Administration API python client for researchers who just need data.
- [EIA](https://github.com/ropensci/eia) - An R package wrapping the US Energy Information Administration open data API.
- [atlite](https://github.com/PyPSA/atlite) - Light-weight version of Aarhus RE Atlas for converting weather data to power systems data.
- [NYISOToolkit](https://github.com/m4rz910/NYISOToolkit) - A collection of modules for accessing power system data, generating statistics, and creating visualizations from the New York Independent System Operator.
- [Photovoltaic time series for European countries](https://zenodo.org/record/2613651#.XRtJRP7Rapo) - Comprises 38 years-long hourly time series representing the photovoltaic capacity factors in every European country (EU-28 plus Serbia, Bosnia-Herzegovina, Norway, and Switzerland).
- [SolarData](https://github.com/dazhiyang/SolarData) - Download and manipulate some publicly available solar datasets.
- [UKgrid](https://github.com/RamiKrispin/UKgrid) - An R data package with the UK National Grid historical demand for electricity between April 2005 and October 2019.
- [USgrid](https://github.com/RamiKrispin/USgrid) - The hourly demand and supply of electricity in the US.

## Emissions and Greenhouse Gases

### Carbon Footprint
- [impact](https://github.com/mlco2/impact/) - Compute your ML model's emissions with our calculator and add the results to your paper with our generated latex template.
- [carbon footprint](https://github.com/protea-earth/carbon_footprint) - Calculate your carbon footprint easily using a command line interface.
- [CarbonFootprintEGU](https://github.com/milankl/CarbonFootprintEGU) - Travel carbon footprint of the European Geosciences Union General Assembly 2019.
- [Bloom](https://github.com/tmrowco/northapp-contrib) - is a SaaS that allow companies to become climate leaders, from calculating their climate impact to communicating about their climate efforts. It connects to as many data sources as possible to assess your carbon footprint and find mitigation opportunities.
- [NMF.earth app](https://github.com/NMF-earth/nmf-app) - Understand and reduce your carbon footprint seedling iOS & Android.
- [EnergyPATHWAYS](https://github.com/energyPATHWAYS/EnergyPATHWAYS) - model is a professional, open-source energy and carbon planning tool for use in evaluating long-term, economy-wide greenhouse gas mitigation scenarios.
- [CarbonFootprint](https://gitlab.com/aossie/CarbonFootprint) - A browser extension that displays carbon footprint information in multiple map services.
- [carbontracker](https://github.com/lfwa/carbontracker) - Track and predict the energy consumption and carbon footprint of training deep learning models.
- [experiment-impact-tracker](https://github.com/Breakend/experiment-impact-tracker) -  is meant to be a simple drop-in method to track energy usage, carbon emissions, and compute utilization of your system.

### Observation
- [ghg emissions indicator](https://github.com/bcgov/ghg-emissions-indicator) - R scripts for a GHG emissions indicator published on Environmental Reporting British Columbia.
- [DuMux](https://git.iws.uni-stuttgart.de/dumux-repositories/dumux) - is based on the DUNE framework and aims to provide a multitude of numerical models as well as flexible discretization methods for complex non-linear phenomena, such as CO2 sequestration, soil remediation, drug delivery in cancer therapy and more.
- [batch7 satellite ges](https://github.com/dataforgoodfr/batch7_satellite_ges/) - The goal of our project is to localize CO2 emissions on Earth based on the the carbon concentration data measured by the OCO-2 Satellite from NASA.
- [CO2 Emission Datasets](https://www.che-project.eu/data-portal) - The CHE Data Portal provides an interface to the distributed data used and made available through the project, either as input data sets or as resulting data sets.

### Carbon Capture
- [SimCCS](https://github.com/simccs/SimCCS) - is a software platform for carbon capture and storage infrastructure design.
- [FOQUS](https://github.com/CCSI-Toolset/FOQUS) - Framework for Optimization and Quantification of Uncertainty and Surrogates.
- [Carbon Capture and Storage](https://github.com/yohanesnuwara/carbon-capture-and-storage) - This is a complete modelling workflow that integrates reservoir simulation data, rock physics, time-lapse seismic, and geomechanics of CO2 injection in carbonate rock.

## Observation and Conservation of Ecosystems
### Vegitation and Biodiversity
- [carbon budget](https://github.com/wri/carbon-budget) - This model maps gross greenhouse gas emissions from forests between 2001 and 2015, gross carbon removals by forests between 2001, and the difference between them (net flux).
- [treeseg](https://github.com/apburt/treeseg/) - has been developed to near-automatically extract tree-level point clouds from high-density larger-area lidar point clouds acquired in forests.
- [fgeo](https://github.com/forestgeo/fgeo) - Analyze forest diversity and dynamics.
- [fgeo.biomass](https://github.com/forestgeo/fgeo.biomass) - Calculate biomass with allometric equations from the allodb package and ForestGEO data.
- [BIOMASS](https://github.com/umr-amap/BIOMASS) - R package for estimating aboveground biomass and its uncertainty in tropical forests.
- [forest](https://github.com/MetOffice/forest) - Forecast and Observation Research and Evaluation Survey Tool.
- [SEPAL](https://github.com/openforis/sepal) - System for Earth Observation Data Access, Processing and Analysis for Land Monitoring.
- [Forest Carbon database](https://github.com/forc-db/ForC) - Global Forest Carbon Database.
- [TreeLS](https://github.com/tiagodc/TreeLS) - High performance R functions for forest data processing based on Terrestrial Laser Scanning (but not only) point clouds.
- [TreeQSM](https://github.com/InverseTampere/TreeQSM) - Quantitative Structure Models of Single Trees from Laser Scanner Data.
- [DeepLidar](https://github.com/weecology/DeepLidar) - Geographic Generalization in Airborne RGB Deep Learning Tree Detection.
- [wildfire forecasting](https://github.com/esowc/wildfire-forecasting) - The project intends to reproduce the Fire Forecasting capabilities of GEFF using Deep Learning and develop further improvements in accuracy, geography and time scale through inclusion of additional variables or optimization of model architecture & hyperparameters.
- [caliver](https://github.com/ecmwf/caliver) - CALIbration and VERification of gridded fire danger models.
- [Global Forest Watch](https://github.com/Vizzuality/gfw) - Global Forest Watch: An online, global, near-real time forest monitoring tool.
- [gfw-mapbuilder](https://github.com/wri/gfw-mapbuilder) - library to build custom Forest Atlas web applications.
- [taxize](https://github.com/ropensci/taxize) - allows users to search over many taxonomic data sources for species names (scientific and common) and download up and downstream taxonomic hierarchical information.
- [rgbif](https://github.com/ropensci/rgbif) - Interface to the Global Biodiversity Information Facility API.
- [Global Biotic Interactions](https://github.com/globalbioticinteractions/globalbioticinteractions) - Global Biotic Interactions provides access to existing species interaction datasets.
- [lidR](https://github.com/Jean-Romain/lidR) - R package for airborne LiDAR data manipulation and visualisation for forestry application.
- [Digital Forestry Toolbox](https://github.com/mparkan/Digital-Forestry-Toolbox) - A collection of digital forestry tools for Matlab/Octave.
- [pyfor](https://github.com/brycefrank/pyfor) - Tools for analyzing aerial point clouds of forest data.
- [DeepForest](https://github.com/weecology/DeepForest) - Python Package for Tree Crown Detection in Airborne RGB imagery.
- [pyMETRIC](https://github.com/WSWUP/pymetric) - is a set of Python based tools developed for estimating and mapping evapotranspiration for large areas, utilizing the Landsat image archive.
- [vegMonitor](https://github.com/atreyasha/vegMonitor) - R-based Random Forest Algorithm to classify vegetation cover in Dharamshala Tehsil and conduct vegetation loss detection.
- [NeonTreeEvaluation](https://github.com/weecology/NeonTreeEvaluation) - Benchmark dataset for tree detection for airborne RGB, Hyperspectral and LIDAR imagery.
- [PyCrown](https://github.com/manaakiwhenua/pycrown) - Fast raster-based individual tree segmentation for LiDAR data.
- [canopyLazR](https://github.com/akamoske/canopyLazR) - R package to estimate leaf area density and leaf area index from airborne LiDAR point clouds.
- [forestlas](https://github.com/philwilkes/forestlas) - Code for generating metrics of forest vertical structure from airborne LiDAR data.
- [OpenTreeMap](https://github.com/OpenTreeMap/otm-core) - is a collaborative platform for crowdsourced tree inventory, ecosystem services calculations, urban forestry analysis, and community engagement.
- [WildfirePy](https://github.com/wildfirepy/wildfirepy) - a Python library for Wildfire GIS data analysis.
- [DeepTreeAttention](https://github.com/weecology/DeepTreeAttention) - Hyperspectral Image Classification with Attention Aided CNNs.
- [rebird](https://github.com/ropensci/rebird) - rebird is a package to interface with the eBird webservices a real-time, online bird checklist program.
- [rredlist](https://github.com/ropensci/rredlist) - R client for the IUCN Red List of threatened and endangered species.
- [OpenSimRoot](https://gitlab.com/rootmodels/OpenSimRoot) - is a source code for simulating root architecture, nutrient and water uptake and more.
- [PyETo](https://github.com/woodcrafty/PyETo) -  a Python library for calculating reference crop evapotranspiration, sometimes referred to as potential evapotranspiration.
- [burnr](https://github.com/ltrr-arizona-edu/burnr) - Basic tools to analyze forest fire history data (e.g. FHX) in R.
- [forestmangr](https://github.com/sollano/forestmangr) - R package for forest mensuration and management.



### Ice and Poles
- [Planet Snowcover](https://github.com/acannistra/planet-snowcover) -  is a project that pairs airborne lidar and Planet Labs satellite imagery with cutting-edge computer vision techniques to identify snow-covered area at unprecedented spatial and temporal resolutions.
- [MODIStsp](https://github.com/ropensci/MODIStsp) - An "R" package for automatic download and preprocessing of MODIS Land Products Time Series.
- [Sea ice drift](https://github.com/nansencenter/sea_ice_drift) - Sea ice drift from Sentinel-1 SAR imagery using open source feature tracking.
- [smrt](https://github.com/smrt-model/smrt) - Snow Microwave Radiative Transfert model to compute thermal emission and backscatter from snowpack.
- [PlantCV](https://github.com/danforthcenter/plantcv) -  Plant phenotyping using computer vision.
- [OGGM](https://github.com/OGGM/oggm) - is a modular open source model for glacier dynamics.
- [CICE](https://github.com/CICE-Consortium/CICE) - is a computationally efficient model for simulating the growth, melting, and movement of polar sea ice.
- [Icepack](https://github.com/CICE-Consortium/CICE-Icepack) - contains files for Icepack, the column physics of the sea ice model CICE.
- [PISM](https://github.com/pism/pism) - The Parallel Ice Sheet Model is an open source, parallel, high-resolution ice sheet model.
- [icepack](https://github.com/icepack/icepack) - Finite element modeling of glaciers and ice sheets.
- [DeepBedMap](https://github.com/weiji14/deepbedmap) - Using a deep neural network to better resolve the bed topography of Antarctica.
- [OSSP](https://github.com/wrightni/OSSP) - Open Source Algorithm for Detecting Sea Ice Surface Features in High Resolution Optical Imagery.
- [captoolkit](https://github.com/fspaolo/captoolkit) - NASA’s Cryosphere Altimetry Processing Toolkit

### Ocean and Climate
- [MOM6](https://github.com/NOAA-GFDL/MOM6) - Modular Ocean Model is a numerical representation of the ocean fluid with applications from the process scale to the planetary circulation scale.
- [MOM5](https://github.com/mom-ocean/MOM5) - MOM is a numerical ocean model based on the hydrostatic primitive equations. Development of the model is managed through this GitHub site.
- [The Flexible Modeling System](https://github.com/NOAA-GFDL/FMS) - is a software framework for supporting the efficient development, construction, execution, and scientific interpretation of atmospheric, oceanic, and climate system models.
- [Bergen Layered Ocean Model](https://github.com/NorESMhub/BLOM) - employs an isopycnic vertical coordinate, with near-isopycnic interior layers and variable density layers in the surface mixed boundary layer.
- [CliFlo](https://github.com/ropensci/clifro) - Easily download and visualise climate data from New Zealand's National Climate Database.
- [hector](https://github.com/JGCRI/hector) - an open source, object-oriented, simple global climate carbon-cycle model.
- [pyhector](https://github.com/openclimatedata/pyhector) - Python interface for the simple global climate carbon-cycle model Hector.
- [Apache Open Climate Workbench](https://github.com/apache/climate) - is an effort to develop software that performs climate model evaluations using model outputs from a variety of different sources.
- [NorESM](https://github.com/NorESMhub/NorESM) - Norwegian Earth System Model and Documentation.
- [CliMT](https://github.com/CliMT/climt) - is a Toolkit for building Earth system models in Python.
- [climlab](https://github.com/brian-rose/climlab) - Python package for process-oriented climate modeling.
- [ClimateModeling_courseware](https://github.com/brian-rose/ClimateModeling_courseware) - A collection of interactive lecture notes and assignments in Jupyter notebook format.
- [Oceananigans.jl](https://github.com/CliMA/Oceananigans.jl) - Fast and friendly fluid dynamics on CPUs and GPUs.
- [ClimateMachine.jl](https://github.com/CliMA/ClimateMachine.jl) - Climate Machine: an Earth System Model that automatically learns from data.
- [atlas](https://github.com/ecmwf/atlas) - A library for numerical weather prediction and climate modelling.
- [Climate-Change-Datasets](https://github.com/adventuroussrv/Climate-Change-Datasets) - Here is a list of Climate Change Public Datasets.
- [ESMValTool](https://github.com/ESMValGroup/ESMValTool) - A community diagnostic and performance metrics tool for routine evaluation of Earth system models in World Climate Research Programme.
- [NEMO](https://forge.ipsl.jussieu.fr/nemo/chrome/site/doc/NEMO/guide/html/NEMO_guide.html) - for Nucleus for European Modelling of the Ocean is a state-of-the-art modelling framework for research activities and forecasting services in ocean and climate sciences, developed in a sustainable way by a European consortium since 2008.
- [sedproxy](https://github.com/EarthSystemDiagnostics/sedproxy) - An R package for modelling sediment archived climate proxy records.
- [ICAR](https://github.com/NCAR/icar) - is a simplified atmospheric model designed primarily for climate downscaling, atmospheric sensitivity tests, and hopefully educational uses.
- [LESbrary.jl](https://github.com/CliMA/LESbrary.jl) - Generating a library of ocean turbulence large eddy simulation data to train ocean and climate models.
- [MetPy](https://github.com/Unidata/MetPy) - is a collection of tools in Python for reading, visualizing and performing calculations with weather data.
- [Isca](https://github.com/ExeClim/Isca) - is a framework for the idealized modelling of the global circulation of planetary atmospheres at varying levels of complexity and realism.
- [MPAS](https://github.com/MPAS-Dev/MPAS-Model) - The Model for Prediction Across Scales is a collaborative project for developing atmosphere, ocean, and other earth-system simulation components for use in climate, regional climate, and weather studies.
- [FAIR](https://github.com/OMS-NetZero/FAIR) - Finite Amplitude Impulse-Response simple climate-carbon-cycle model.
- [GOLD](https://code.google.com/archive/p/gold-omod/) - stands for Generalized Ocean Layer Dynamics and is a hybrid coordinate finite volume ocean model code funded by NOAA and developed by the ocean group at NOAA-GFDL and Princeton University.
- [FluxEngine](https://github.com/oceanflux-ghg/FluxEngine) - is an open source atmosphere ocean gas flux data processing toolbox.
- [eeweather](https://github.com/openeemeter/eeweather) - Fetch NCDC ISD, TMY3, or CZ2010 weather data that corresponds to ZIP Code Tabulation Areas or Latitude/Longitude.
- [rrricanes](https://github.com/ropensci/rrricanes) -  is a R library that extracts information from Atlantic and east Pacific hurricanes and tropical storms
- [GSODR](https://github.com/ropensci/GSODR) - Global Surface Summary of the Day ('GSOD') Weather Data Client for R.
- [stationaRy](https://github.com/rich-iannone/stationaRy) - Get hourly meteorological data from one of thousands of global stations.
- [weathercan](https://github.com/ropensci/weathercan) - This package makes it easier to search for and download multiple months/years of historical weather data from Environment and Climate Change Canada (ECCC) website.
- [hydroscoper](https://github.com/ropensci/hydroscoper) - R interface to the Greek National Data Bank for Hydrometeorological Information.
- [GLOCOFFS](https://github.com/WPringle/GLOCOFFS) - An ADCIRC-based global storm tide modeling system providing real-time forecasts of coastal flooding.
- [The Global Environmental Multiscale Model](https://gitlab.com/eccc/gem/gem) - is an integrated forecasting and data assimilation system developed by the Atmospheric Numerical Prediction Research Section, Meteorological Research Division, of Environment and Climate Change Canada
- [leaflet-velocity](https://github.com/danwild/leaflet-velocity) - Create a canvas visualisation layer for direction and intensity of arbitrary velocities (e.g. wind, ocean current).
- [OpenDrift](https://github.com/OpenDrift/opendrift) - is a software for modeling the trajectories and fate of objects or substances drifting in the ocean, or even in the atmosphere.
- [OceanSpy](https://github.com/hainegroup/oceanspy) -  is an open-source and user-friendly Python package that enables scientists and interested amateurs to analyze and visualize ocean model datasets.
- [Iris](https://github.com/SciTools/iris) - is a powerful, format-agnostic, community-driven Python package for analysing and visualising Earth science data.
- [Veros](https://github.com/team-ocean/veros) - powerful tool that makes high-performance ocean modeling approachable and fun.
- [oce](https://github.com/dankelley/oce) - R package for oceanographic processing.
- [podaacpy](https://github.com/nasa/podaacpy) - A python utility library for interacting with NASA JPL's Physical Oceanography Distributed Active Archive Center.
- [Ocean-Data-Map-Project](https://github.com/DFO-Ocean-Navigator/Ocean-Data-Map-Project) - is a Data Visualization tool that enables users to discover and view 3D ocean model output quickly and easily.
- [AIBECS.jl](https://github.com/JuliaOcean/AIBECS.jl) - is a Julia package that provides ocean biogeochemistry modelers with an easy-to-use interface for creating and running models of the ocean system.
- [marineHeatWaves](https://github.com/ecjoliver/marineHeatWaves) - is a module for python which implements the Marine Heatwave (MHW) definition of Hobday et al.
- [heatwaveR](https://github.com/robwschlegel/heatwaveR) - contains the original functions from the RmarineHeatWaves package that calculate and display marine heatwaves according to the definition of Hobday et al. (2016).
- [MITgcm](https://github.com/MITgcm/MITgcm) - flexible non-hydrostatic formulation enables it to efficiently simulate fluid phenomena over a wide range of scales.
- [hyfo](https://github.com/Yuanchao-Xu/hyfo) - mainly focuses on data process and visulization in hydrology and climate forecasting.
- [climate](https://github.com/bczernecki/climate) - The goal of the climate R package is to automatize downloading of meteorological and hydrological data from publicly available repositories.
- [rdwd](https://github.com/brry/rdwd) - is an R package to select, download and read climate data from the German Weather Service.
- [rWBclimate](https://github.com/ropensci/rWBclimate) - is an R interface for the World Bank climate data used in the World Bank climate knowledge portal.
- [TECA](https://github.com/LBL-EESA/TECA) - the Toolkit for Extreme Climate Analysis, contains a collection of climate anlysis algorithms targetted at extreme event detection and analysis.
- [Climate Data Store Toolbox](https://cds.climate.copernicus.eu/toolbox/doc/index.html) - Dive into this wealth of information about the Earth's past, present and future climate.


## Access and Monitoring of Resources

### Air
- [CMAQ](https://github.com/USEPA/CMAQ) - Code base for the U.S. EPAs Community Multiscale Air Quality Model.
- [AMET](https://github.com/USEPA/AMET) - is a suite of software designed to facilitate the analysis and evaluation of predictions from meteorological and air quality models.
- [MLAir](https://gitlab.version.fz-juelich.de/toar/mlair) - Machine Learning on Air data is an environment that simplifies and accelerates the creation of new machine learning models for the analysis and forecasting of meteorological and air quality time series.
- [shoot-i-smoke](https://github.com/amaurymartiny/shoot-i-smoke) - See your city's air pollution measured in daily cigarettes.
- [airqmon](https://github.com/jsynowiec/airqmon) - A macOS menu bar application that displays live air quality data from the nearest sensor station.
- [opendata-stuttgart](https://github.com/opendata-stuttgart/sensors-software) - The maintained main firmware for the Luftdaten.Info Sensor.
- [AirCasting](https://github.com/HabitatMap/AirCasting) - the project aims to build a platform for gathering, visualization and sharing of environmental data.
- [openair: Tools for air quality data analysis](https://github.com/davidcarslaw/openair) - openair is an R package developed for the purpose of analyzing air quality data — or more generally atmospheric composition data.
- [ropensci](https://github.com/ropensci/ropenaq) - OpenAQ is a community of scientists, software developers, and lovers of open environmental data who are building an open, real-time database that provides programmatic and historical access to air quality data.
- [airQualityMeter](https://github.com/rpanfili/airQualityMeter) - Detects air particulate matter (PM - pm1, pm2.5, pm10) concentrations and sends data to an MQTT server.


### Water
- [Stormwater-Management-Model](https://github.com/USEPA/Stormwater-Management-Model) - is used for single event or long-term (continuous) simulation of runoff quantity and quality from primarily urban areas.
- [dataRetrieval](https://github.com/USGS-R/dataRetrieval) - This R package is designed to obtain USGS or EPA water quality sample data, streamflow data, and metadata directly from web services.
- [EGRET](https://github.com/USGS-R/EGRET) - An R-package for the analysis of long-term changes in water quality and streamflow, including the water-quality method Weighted Regressions on Time, Discharge, and Season.
- [WaterModels.jl](https://github.com/lanl-ansi/WaterModels.jl) - is designed to enable computational evaluation of historical and emerging water network formulations and algorithms using a common platform.
- [Tree-based Inland Hydraulic Routing Project](https://github.com/NOAA-OWP/t-route) - The program under development here seeks to effectively manage the traversal of a network of streams with defined hydraulic properties specifically for the purpose of hydraulic routing in an operational flood and water resources forecasting system.
- [Next Gen Water Modeling Framework](https://github.com/NOAA-OWP/ngen) - This framework includes an encapsulation strategy which focuses on the hydrologic data first, and then builds a functional abstraction of hydrologic behavior.
- [nhdplusTools](https://github.com/USGS-R/nhdplusTools) - This package is a growing set of tools for manipulation of hydrographic data using the NHDPlus data model.
- [The Safe Water Project](https://github.com/codeforboston/safe-water) - is a team of volunteers at Code for Boston who are using data modeling, data visualization and machine learning to predict, visualize, and share data about the presence of hazardous drinking and surface water contaminants in the United States.
- [HydroFunctions](https://github.com/mroberge/hydrofunctions) - A suite of convenience functions for working with hydrology data in an interactive Python session.
- [CWATM](https://github.com/CWatM/CWatM) - represents one of the new key elements of IIASAs Water program to assess water supply, water demand and environmental needs at global and regional level.
- [The General Lake Model](https://github.com/AquaticEcoDynamics/GLM) - is a water balance and one-dimensional vertical stratification hydrodynamic model.
- [nhdR](https://github.com/jsta/nhdR) - R interface to the US National Hydrography Dataset.
- [modflow6](https://github.com/MODFLOW-USGS/modflow6) - has been widely used by academics, private consultants, and government scientists to accurately, reliably, and efficiently simulate groundwater flow.
- [iMOD](https://oss.deltares.nl/web/imod/home) - is an easy to use Graphical User Interface + an accelerated Deltares-version of MODFLOW with fast, flexible and consistent sub-domain modeling techniques.
- [Imod-Python](https://gitlab.com/deltares/imod/imod-python) - is designed to help you in your MODFLOW groundwater modeling efforts
- [HydroShare](https://github.com/hydroshare/hydroshare) - HydroShare is a website and hydrologic information system for sharing hydrologic data and models aimed at giving users the cyberinfrastructure needed to innovate and collaborate in research to solve water problems.
- [pysheds](https://github.com/mdbartos/pysheds) - Simple and fast watershed delineation in python.
- [WhiteboxTools](https://github.com/jblindsay/whitebox-tools) - WhiteboxTools is an advanced geospatial data analysis platform.
- [CRITERIA3D](https://github.com/ARPA-SIMC/CRITERIA3D) - includes a numerical solution for three-dimensional water and heat flow in the soil, coupled surface and subsurface flow, meteorological data interpolation, radiation budget, crop development and crop water uptake.
- [Water Network Tool for Resilience](https://github.com/USEPA/WNTR) - is a Python package designed to simulate and analyze resilience of water distribution networks.
- [fasstr](https://github.com/bcgov/fasstr) - An R package to analyze, summarize, and visualize daily streamflow data.
- [KnowFlow](https://github.com/KnowFlow/KnowFlow_AWM) - KnowFlow Automatic Water Monitoring device is an open sourced tool enable everyone having access to first hand water quality data with low cost.
- [gwells](https://github.com/bcgov/gwells) - Groundwater Wells and Aquifers application for the Ministry of Environment in British Columbia.
- [waterquality](https://github.com/RAJohansen/waterquality) - Package designed to detect and quantify water quality and cyanobacterial harmful algal bloom (CHABs) from remotely sensed imagery.
- [LISFLOOD](https://github.com/ec-jrc/lisflood-code) - is a spatially distributed water resources model, developed by the Joint Research Centre of the European Commission since 1997.
- [FloodMapping](https://github.com/mikejohnson51/FloodMapping) - R package for flood forecasting via the National Water Model.
- [QGEP](https://github.com/qgep/QGEP) - A waste-water application based on QGIS in compliance with SIA-405.
- [PooPyLab_Project](https://github.com/toogad/PooPyLab_Project) - A biological wastewater treatment software.
- [aguaclara](https://github.com/AguaClara/aguaclara) - Python package for designing and performing research on AguaClara water treatment plants.
- [RTC-Tools](https://gitlab.com/deltares/rtc-tools) - a toolbox for control and optimization of water systems.


### Soil
- [SoilGrids250m](https://github.com/ISRICWorldSoil/SoilGrids250mGlobal) - spatial predictions of soil properties and classes at 250 m resolution.
- [Hyperspectral Soilmoisture Dataset](https://github.com/felixriese/hyperspectral-soilmoisture-dataset) - Hyperspectral benchmark dataset on soil moisture.
- [soilReports](https://github.com/ncss-tech/soilReports) - An R package that assists with the setup and operation of a collection of soil data summary, comparison, and evaluation reports.
- [AQP](https://github.com/ncss-tech/aqp) - Algorithms for Quantitative Pedology is a collection of code, ideas, documentation, and examples wrapped-up into several R packages.
- [sharpshootR](https://github.com/ncss-tech/sharpshootR) - Miscellaneous soil data management, summary, visualization, and conversion utilities to support soil survey.
- [soilDB](https://github.com/ncss-tech/soilDB) - Simplified Access to NCSS Soil Databases.
- [Landslides Detection](https://github.com/mhscience/landslides_detection) - Machine learning tool to detect landslides from optical satellite imagery.
- [pyTSEB](https://github.com/hectornieto/pyTSEB) - contains Python code for Two Source Energy Balance models (Priestley-Taylor TSEB-PT, Dual Time Difference DTD and TSEB with component soil and canopy temperatures TSEB-2T) for estimating sensible and latent heat flux based on measurements of radiometric surface temperature.
- [slga](https://github.com/obrl-soil/slga) - offers the ability to download geographic subsets of raster data from the Soil and Landscape Grid of Australia.
- [smapr](https://github.com/ropensci/smapr) - An R package for acquisition and processing of NASA (Soil Moisture Active-Passive) SMAP data.


## Circular Economy and Waste
- [ONEARMY](https://github.com/ONEARMY/community-platform) - A series of tools for the Precious Plastic community to collaborate around the world and tackle plastic waste.
- [Trash-ICRA19](https://conservancy.umn.edu/handle/11299/214366) - A Bounding Box Labeled Dataset of Underwater Trash.
- [TACO](https://github.com/pedropro/TACO) -  Trash Annotations in Context Dataset Toolkit.
- [circularity.ID Open Data Standard]( https://github.com/circularfashion/cf-circularity-id-standard) - The standard represents the results and findings of an extensive six-year research into the needs of stakeholders in the fashion industry to achieve a circular economy.
- [RecycleNet](https://github.com/sangminwoo/RecycleNet) - Effective trash classification model using only a small number of annotated images.
- [trashnet](https://github.com/garythung/trashnet) - Dataset of images of trash; Torch-based CNN for garbage image classification.


## Further Sustainability
### Public Resources
- [Awesome Clean Tech](https://github.com/nglgzz/awesome-clean-tech) - Clean technology is any process, product, or service that reduces negative environmental impacts through significant energy efficiency improvements, the sustainable use of resources, or environmental protection activities.
- [Awesome Open Climate Science](https://github.com/pangeo-data/awesome-open-climate-science) - Awesome Open Atmospheric, Ocean, and Climate Science.
- [Awesome Earth](https://github.com/philsturgeon/awesome-earth) - "What can I do about the climate crisis?" Here are 326 things you can do.
- [Awesome Open Geoscience](https://github.com/softwareunderground/awesome-open-geoscience) - Curated from repositories that make our lives as geoscientists, hackers and data wranglers easier or just more awesome.
- [Awesome Coastal](https://github.com/chrisleaman/awesome-coastal) - A curated list of awesome resources for coastal engineers and scientists.
- [Open Energy System Databases](https://en.wikipedia.org/wiki/Open_energy_system_databases) - employ open data methods to collect, clean, and republish energy-related datasets for open use.
- [Open Models](https://wiki.openmod-initiative.org/wiki/Open_Models) - This page lists energy models published under open source licenses.
- [Open Energy System Models](https://en.wikipedia.org/wiki/Open_energy_system_models) - are used to explore future energy systems and are often applied to questions involving energy and climate policy.
- [GlobalWindAtlas](https://globalwindatlas.info/) - Immediately start exploring windy areas.
- [GlobalSolarAtlas](https://globalsolaratlas.info/) - Start exploring solar potential.
- [Open Hardware Observatory](https://en.oho.wiki/wiki/Home) - Search engine and assessment platform for sustainable open hardware.
- [Open Source Ecology](https://www.opensourceecology.org/) - Developing of open source industrial machines that can be made for a fraction of commercial costs, and sharing the designs for free.
- [Digital Public Goods Alliance](https://digitalpublicgoods.net/) - is a multi-stakeholder initiative to accelerate the attainment of the sustainable development goals in low- and middle-income countries by facilitating the discovery, development, use of and investment in digital public goods.
- [Investment Framework for a More Sustainable World](https://github.com/My-Climate-Journey/climate-sustainability-investment-framework) - This framework was created as a tool for those seeking to make emissions reductions and sustainability related investments with the goal of mitigating the impacts of climate change, based on guidelines set forth by Chamath Palihapitiya in July 2020.

### Open Sustainable Communities
- [openmod-initiative](https://forum.openmod-initiative.org/) - We believe that more openness in energy modelling increases transparency and credibility, reduces wasteful double-work and improves overall quality.
- [sustainoss](https://sustainoss.org/) Sustainability doesn't just mean code. How can we make our work sustainable environmentally, too? How can we share our knowledge of open source with other groups in the world?
- [lfenergy](https://www.lfenergy.org/) - is an open source foundation focused on the power systems sector, hosted within The Linux Foundation.
- [protontypes](https://protontypes.eu/) - open accelerator for free and sustainable innovation.
- [Open Energy Family](https://github.com/OpenEnergyPlatform) - The Open Energy Family aims to ensure quality, transparency and reproducibility in energy system research. 


*Animation created with [An Animated Map of the Earth](https://github.com/eleanorlutz/earth_atlas_of_space) by [Eleanor Lutz](https://twitter.com/eleanor_lutz)*
