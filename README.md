<!--lint ignore awesome-badge--> <!--lint ignore double-link-->
# Open Sustainable Technology
[<img src="earth.png" align="right" width="350">](https://tabletopwhale.com/)

__A curated list of open technology projects to sustain a stable climate, energy supply, and natural resources.__ <br> <br> Your contribution is essential to keep this list alive. Read more about its origin and how you can participate in the [contribution guide](https://opensustain.tech/contributing/), [presentation slides](https://protontypes.eu/protontypes_open_sustainable_technology.pdf) and related [blog post](https://opensustain.tech/blog/gathering_open_sustainable_technology/). Please [write an email](mailto:tobias.augspurger@protontypes.eu) to give feedback, hints and ideas considering [OpenSustain.tech](https://opensustain.tech/) or [create an issue](https://github.com/protontypes/open-sustainable-technology/issues/new).

If you're looking for an entry point into domains like renewable energy, climate change, or earth science, check out the collection of tutorials in the [educational section](https://opensustain.tech/education/). 

[![](https://badgen.net/badge/icon/Follow%20Updates/009485?icon=twitter&label&scale=1.3)](https://twitter.com/protontypes) [![](https://badgen.net/badge/icon/Add%20a%20Project/009485?icon=git&label&scale=1.3)](https://github.com/protontypes/open-sustainable-technology/blob/main/CONTRIBUTING.md)  [![](https://badgen.net/badge/View/Database/009485?scale=1.3)](https://airtable.com/shr9we419r2TkpLkc)  

<!--toc-->
## Contents

- [Renewable Energy](#renewable-energy)
  - [Photovoltaics and Solar Energy](#photovoltaics-and-solar-energy)
  - [Wind Power](#wind-power)
  - [Hydro Power](#hydro-power)
  - [Geothermal Energy](#geothermal-energy)
  - [Bioenergy](#bioenergy)
- [Energy Storage](#energy-storage)
  - [Battery](#battery)
  - [Hydrogen](#hydrogen)
- [Energy Systems](#energy-systems)
  - [Energy Modeling and Optimization](#energy-modeling-and-optimization)
  - [Energy Monitoring and Control](#energy-monitoring-and-control)
  - [Energy Distribution and Grids](#energy-distribution-and-grids)
  - [Datasets on Energy Systems](#datasets-on-energy-systems)
- [Consumption of Energy and Resources](#consumption-of-energy-and-resources)
  - [Buildings and Heating](#buildings-and-heating)
  - [Mobility and Transportation](#mobility-and-transportation)
  - [Production and Industry](#production-and-industry)
  - [Computation and Communication](#computation-and-communication)
- [Emissions](#emissions)
  - [Carbon Intensity and Accounting](#carbon-intensity-and-accounting)
  - [Carbon Capture and Removel](#carbon-capture-and-removel)
  - [Emission Observation and Modeling](#emission-observation-and-modeling)
- [Ecological Footprint](#ecological-footprint)
  - [Life Cycle Assessment](#life-cycle-assessment)
  - [Circular Economy and Waste](#circular-economy-and-waste)
- [Earth Systems](#earth-systems)
  - [Biosphere](#biosphere)
  - [Cryosphere](#cryosphere)
  - [Hydrosphere](#hydrosphere)
  - [Atmosphere](#atmosphere)
- [Climate and Earth Science](#climate-and-earth-science)
  - [Earth and Climate Modeling](#earth-and-climate-modeling)
  - [Radiative Transfer](#radiative-transfer)
  - [Earth Observation and Climate Monitoring](#earth-observation-and-climate-monitoring)
  - [Meteorological Observation](#meteorological-observation) 
  - [Climate Data Processing and Access](#climate-data-processing-and-access)
  - [Integrated Assessment](#integrated-assessment)
- [Natural Resources](#natural-resources)
  - [Air Quality](#air-quality)
  - [Water Supply](#water-supply)
  - [Soil and Land](#soil-and-land)
  - [Agriculture and Nutrition](#agriculture-and-nutrition)
  - [Natural Hazard and Poverty](#natural-hazard-and-poverty)
- [Sustainable Development](#sustainable-development)
  - [Sustainable Development Goals](#sustainable-development-goals)
  - [Sustainable Investment](#sustainable-investment)
  - [Knowledge Platforms](#knowledge-platforms)
  - [Data Catalogs and Interfaces](#data-catalogs-and-interfaces)
  - [Curated Lists](#curated-lists)
- [Contributors](#contributors)
- [Artwork and License](#artwork-and-license)

<!--toc_end-->

## Renewable Energy

### Photovoltaics and Solar Energy

- [pvlib-python](https://github.com/pvlib/pvlib-python) - A set of documented functions for simulating the performance of photovoltaic energy systems.
- [pvfactors](https://github.com/SunPower/pvfactors) - Open source view-factor model for diffuse shading and bifacial PV modeling.
- [gsee](https://github.com/renewables-ninja/gsee) - Global Solar Energy Estimator.
- [PVMismatch](https://github.com/SunPower/PVMismatch) - An explicit Python PV system IV & PV curve trace calculator which can also calculate mismatch.
- [rdtools](https://github.com/NREL/rdtools) - An open source library to support reproducible technical analysis of time series data from photovoltaic energy systems.
- [Machine-Learning-for-Solar-Energy-Prediction](https://github.com/ColasGael/Machine-Learning-for-Solar-Energy-Prediction) - Predict the power production of a solar panel farm from weather measurements using machine learning.
- [elpv-dataset](https://github.com/zae-bayern/elpv-dataset) - A dataset of functional and defective solar cells extracted from EL images of solar modules.
- [feedinlib](https://github.com/oemof/feedinlib) - Contains implementations of photovoltaic models to calculate electricity generation from a PV installation based on given solar radiation. Furthermore it contains all necessary pre-calculations.
- [photovoltaic](https://github.com/pvedu/photovoltaic) - A Python library used in photovoltaics.
- [pvcaptest](https://github.com/pvcaptest/pvcaptest) - Collection of functions and Jupyter Notebooks to partially automate running a capacity test following ASTM E2848.
- [pvtrace](https://github.com/danieljfarrell/pvtrace) - Optical ray tracing for luminescent materials and spectral converter photovoltaic devices.
- [SolarPILOT](https://github.com/NREL/SolarPILOT) - Solar power tower layout and optimization tool.
- [solar-data-tools](https://github.com/slacgismo/solar-data-tools) - Data analysis tools for working with historical PV solar time-series data sets.
- [SolarPV-DER-simulation-utility](https://github.com/tdcosim/SolarPV-DER-simulation-utility) - Allows user to run dynamics simulations for solar photovoltaic distributed energy resource connected to a stiff voltage source or to an external program.
- [bifacial_radiance](https://github.com/NREL/bifacial_radiance) - Toolkit for working with RADIANCE for the ray-trace modeling of Bifacial Photovoltaics.
- [autoXRD](https://github.com/PV-Lab/autoXRD) - A Python package for automatic XRD pattern classification of thin-films, tweaked for small and class-imbalanced datasets.
- [BayesProcess](https://github.com/PV-Lab/BayesProcess) - A Python package for Physics informed Bayesian network inference using neural network surrogate model for matching process / variable / performance in solar cells.
- [solcore5](https://github.com/qpv-research-group/solcore5) - A multi-scale, Python-based library for the modeling of solar cells and semiconductor materials.
- [solax](https://github.com/squishykid/solax) - Read energy usage data from the real-time API on Solax solar inverters.
- [bifacialvf](https://github.com/NREL/bifacialvf) - Bifacial PV View Factor model for system performance calculation.
- [solaR](https://github.com/oscarperpinan/solar) - Allows for reproducible research both for photovoltaics systems performance and solar radiation.
- [SolarTherm](https://github.com/SolarTherm/SolarTherm) - Solar thermal power/fuel station performance simulation and optimization using Modelica.
- [LibreSolar](https://github.com/LibreSolar/bms-firmware) - Firmware for LibreSolar BMS boards based on bq769x0 or ISL94202.
- [Charge Controller Firmware](https://github.com/LibreSolar/charge-controller-firmware) - Firmware for LibreSolar MPPT/PWM charge controllers.
- [pvoutput](https://github.com/openclimatefix/pvoutput) - Python code for downloading PV data from PVOutput.org.
- [predict_pv_yield](https://github.com/openclimatefix/predict_pv_yield) - Use machine learning to map satellite imagery of clouds to solar PV yield.
- [solar-panel-detection](https://github.com/alan-turing-institute/solar-panel-detection) - Using a combination of AI (machine vision), open data and short-term forecasting, the project aims to determine the amount of solar electricity being put into the UK grid at a given time (i.e., "right now", or "nowcasting")
- [solarpy](https://github.com/aqreed/solarpy) - This package aims to provide a reliable solar radiation model, mainly based on the work of Duffie, J.A., and Beckman, W. A., 1974, "Solar energy thermal processes".
- [solariot](https://github.com/meltaxa/solariot) - Leverage your IoT enabled Solar PV Inverter to stream your solar energy usage data to a real time dashboard.
- [pvanalytics](https://github.com/pvlib/pvanalytics) - Quality control, filtering, feature labeling, and other tools for working with data from photovoltaic energy systems.
- [IonMonger](https://github.com/PerovskiteSCModelling/IonMonger) - A free and fast perovskite solar cell simulator with coupled ion vacancy and charge carrier dynamics in one dimension.
- [rayflare](https://github.com/qpv-research-group/rayflare) - Provide a flexible, user-friendly Python environment to model complex optical stacks, with a focus on solar cells.
- [pv-terms](https://github.com/DuraMAT/pv-terms) - Contains nomenclature for PV-relevant terms that are used in modeling and data analysis for PV systems.
- [StatisticalClearSky](https://github.com/slacgismo/StatisticalClearSky) - Statistical estimation of a clear sky signal from PV system power data.
- [Photovoltaic_Fault_Detector](https://github.com/RentadroneCL/Photovoltaic_Fault_Detector) - Model-definition is a deep learning application for fault detection in photovoltaic plants.
- [nasapower](https://github.com/ropensci/nasapower) - Aims to make it quick and easy to automate downloading NASA-POWER global meteorology, surface solar energy and climatology data in your R session as a tidy data frame tibble object for analysis and use in modeling or other purposes.
- [pvcompare](https://github.com/greco-project/pvcompare) - A model for comparing the benefits of different PV technologies in a specified local energy system in different energy supply scenarios.
- [SolTrace](https://github.com/NREL/SolTrace) - A software tool developed at NREL to model concentrating solar power (CSP) systems and analyze their optical performance.
- [CarrierCapture.jl](https://github.com/WMD-group/CarrierCapture.jl) - A set of codes to compute carrier capture and recombination rates in semiconducting compounds like solar cells.
- [honeybee](https://github.com/ladybug-tools/honeybee) - A Python library to create, run and visualize the results of daylight (RADIANCE) and energy analysis (EnergyPlus/OpenStudio).
- [Open Solar Project](https://github.com/opensolarproject/OSPController) - ESP32 Smart Solar Charger.
- [MPPT-Solar-Charger](https://github.com/danjulio/MPPT-Solar-Charger) - Supporting documentation and software for the MPPT Solar Charger.
- [Tonatiuh](https://github.com/iat-cener/tonatiuh) - A Monte Carlo ray tracer for the optical simulation of solar concentrating systems.
- [PV4GER](https://github.com/kdmayer/PV4GER) - Aims at democratizing and accelerating the access to photovoltaic systems data in Germany and beyond.
- [PV Free](https://github.com/BreakingBytes/pvfree) - A public API for PV modeling parameters.
- [Pysolar](https://github.com/pingswept/pysolar) - A collection of Python libraries for simulating the irradiation of any point on earth by the sun. It includes code for extremely precise ephemeris calculations.
- [PV_ICE](https://github.com/NREL/PV_ICE) - An open-source tool to quantify Solar Photovoltaics (PV) Energy and Mass Flows in the Circular Economy, from a Reliability and Lifetime approach.
- [Solar electricity Nowcasting](https://github.com/openclimatefix/nowcasting) - Build the world's best near-term forecasting system for solar electricity generation.
- [Solar Forecast Arbiter](https://github.com/SolarArbiter/solarforecastarbiter-core) - Core data gathering, validation, processing, and reporting package for the Solar Forecast Arbiter.
- [pv-system-profiler](https://github.com/slacgismo/pv-system-profiler) - Estimating PV array location and orientation from real-world power datasets.
- [A Global Inventory of Commerical-, Industrial-, and Utility-Scale Photovoltaic Solar Generating Units](https://github.com/Lkruitwagen/solar-pv-global-inventory) - Used to produce a global inventory of utility-scale solar photvoltaic generating station.
- [dGen](https://github.com/NREL/dgen) - Forecast PV adoption based on user specified configurations like electricity rate prices, electricity load growth, solar resource factors, and much more.

### Wind Power

- [IEA-15-240-RWT](https://github.com/IEAWindTask37/IEA-15-240-RWT) - A 15 MW reference wind turbine repository developed in conjunction with IEA Wind.
- [makani](https://github.com/google/makani) - A project to develop a commercial-scale airborne wind turbine, culminating in a flight test of the Makani M600 off the coast of Norway.
- [windpowerlib](https://github.com/wind-python/windpowerlib) - A library to model the output of wind turbines and farms.
- [turbinesFoam](https://github.com/turbinesFoam/turbinesFoam) - A library for simulating wind and marine hydrokinetic turbines in OpenFOAM using the actuator line method.
- [nalu-wind](https://github.com/Exawind/nalu-wind) - Solver for wind farm simulations targeting exascale computational platforms.
- [openfast](https://github.com/OpenFAST/openfast) - A multi-physics, multi-fidelity tool for simulating the coupled dynamic response of wind turbines and wind farms.
- [amr-wind](https://github.com/Exawind/amr-wind) - A massively parallel, block-structured adaptive-mesh, incompressible flow solver for wind turbine and wind farm simulations.
- [QBlade](http://www.q-blade.org/#welcome) - Provides a hands-on design and simulation capabilities for HAWT and VAWT rotor design and shows all the fundamental relationships of design concepts and turbine performance in an easy and intuitive way.
- [OpenOA](https://github.com/NREL/OpenOA) - This library provides a framework for working with large time series data from wind plants, such as SCADA.
- [ROSCO](https://github.com/NREL/ROSCO) - NREL's Reference OpenSource Controller for wind turbine applications.
- [floris](https://github.com/NREL/floris) - A controls-oriented engineering wake modeling framework for evaluating the impact of wind farm controls on AEP and wind farm design.
- [windtools](https://github.com/FZJ-IEK3-VSA/windtools) - The Wind Energy Generation Tools provides useful tools to assist in wind energy simulations.
- [PyWake](https://gitlab.windenergy.dtu.dk/TOPFARM/PyWake) - An AEP calculator for wind farms implemented in Python including a collection of wake models.
- [WISDEM](https://github.com/WISDEM/WISDEM) - Wind Plant Integrated System Design and Engineering Model.
- [WOMBAT](https://github.com/WISDEM/WOMBAT) - Windfarm Operations & Maintenance cost-Benefit Analysis Tool.
- [LandBOSSE](https://github.com/WISDEM/LandBOSSE) - The Land-based Balance-of-System Systems Engineering model is a systems engineering tool that estimates the balance-of-system costs associated with installing utility scale wind plants (10, 1.5 MW turbines or larger).
- [OpenMDAO](https://github.com/OpenMDAO/OpenMDAO) - Optimization of Aerodynamic systems.
- [TopFarm2](https://gitlab.windenergy.dtu.dk/TOPFARM/TopFarm2) - A Python package developed by DTU Wind Energy to help with wind-farm optimizations.
- [BasicDTUController](https://gitlab.windenergy.dtu.dk/OpenLAC/BasicDTUController) - The scope of this project is to provide an open source, open access controller that can be used by the wind energy community as a reference.
- [WindEnergyToolbox](https://gitlab.windenergy.dtu.dk/toolbox/WindEnergyToolbox) - A collection of Python scripts that facilitate working with (potentially a lot) of HAWC2,HAWCStab2, FAST or other text input based simulation tools.
- [windfarmGA](https://github.com/YsoSirius/windfarmGA) - Genetic algorithm to optimize the layout of wind farms.
- [wtphm](https://github.com/lkev/wtphm) - The Wind Turbine Prognostics and Health Management library processes wind turbine events data, as well as operational SCADA data for easier fault detection, prognostics or reliability research.
- [AirfoilPreppy](https://github.com/WISDEM/AirfoilPreppy) - A Python module for pre-processing and evaluating aerodynamic airfoil data, primarily for wind turbine applications.
- [GreenGuard](https://github.com/signals-dev/GreenGuard) - A collection of end-to-end solutions for machine learning problems commonly found in monitoring wind energy production system.
- [pyconturb](https://gitlab.windenergy.dtu.dk/pyconturb/pyconturb) - Constrained Stochastic Turbulence for Wind Energy Applications.
- [ORBIT](https://github.com/WISDEM/ORBIT) - Offshore Renewable Balance-of-system Installation Tool computes capital costs and activity times for offshore wind plant balance-of-system (everything besides the turbine) costs.
- [WindTurbineClassification](https://github.com/nmstreethran/WindTurbineClassification) - Specification of 'normal' wind turbine operating behaviour for rapid anomaly detection.
- [ANYstructure](https://github.com/audunarn/ANYstructure) - Offshore Steel structure calculation tool with automatic optimization and report generation.
- [windrose](https://github.com/python-windrose/windrose) - A graphic tool used by meteorologists to give a succinct view of how wind speed and direction are typically distributed at a particular location.
- [SHARPy](https://github.com/ImperialCollegeLondon/sharpy) - Simulation of High Aspect Ratio aeroplanes and wind turbines in Python.
- [WindSE](https://github.com/NREL/WindSE) - A Python package that uses a FEniCS backend to perform wind farm simulations and optimization.
- [WEIS](https://github.com/WISDEM/WEIS) - WEIS is a framework that combines multiple tools to enable design optimization of floating offshore wind turbines.
- [HAMS](https://github.com/YingyiLiu/HAMS) - An open-source computer program for the analysis of wave diffraction and radiation of three-dimensional floating or submerged structures.
- [brightwind](https://github.com/brightwind-dev/brightwind) - A Python library aims to empower wind resource analysts and establish a common industry standard toolset.
- [NRWAL](https://github.com/NREL/NRWAL) - A library of offshore wind cost equations.
- [welib](https://github.com/ebranlard/welib) - Wind energy library, python and matlab tools for wind turbines analyses.


### Hydro Power

- [WecOptTool](https://github.com/SNL-WaterPower/WecOptTool) - Allows users to perform wave energy converter device design optimization studies with constrained optimal control.
- [CACTUS](https://github.com/SNL-WaterPower/CACTUS) - A turbine performance simulation code, based on a free wake vortex method, to study wind turbines and marine hydrokinetic devices.
- [hydro-power-database](https://github.com/energy-modelling-toolkit/hydro-power-database) - Collects basic information on all the European hydro-power plants.
- [MHKiT-Python](https://github.com/MHKiT-Software/MHKiT-Python) - Provides the marine renewable energy community tools for data processing, visualization, quality control, resource assessment, and device performance.
- [hydropowerlib](https://github.com/hydro-python/hydropowerlib) - Designed to calculate feed-in time series of run-of-the-river hydropower plants.
- [HydroPowerSimulations.jl](https://github.com/NREL-SIIP/HydroPowerSimulations.jl) - Contains extensions on PowerSystems.jl and PowerSimulations.jl to enable enhanced hydropower representations.
- [OpenHPL](https://github.com/simulatino/OpenHPL) - An open source hydropower library that consists of hydropower unit models and is modeled using Modelica.
- [WEC-Sim](https://github.com/WEC-Sim/WEC-Sim) - Wave Energy Converter Simulator is an open source code for simulating wave energy converters.
- [BEMRosetta](https://github.com/BEMRosetta/BEMRosetta) - Used to model hydrodynamic forces in offshore devices like ships, offshore wind platforms and wave energy converters.
- [Capytaine](https://github.com/mancellin/capytaine) - A Python package for the simulation of the interaction between water waves and floating bodies in frequency domain.
- [reservoir](https://github.com/swd-turner/reservoir) - Tools for Analysis, Design, and Operation of Water Supply Storages.


### Geothermal Energy

- [pygfunction](https://github.com/MassimoCimmino/pygfunction) - An open source toolbox for the evaluation of thermal response factors of geothermal borehole fields.
- [geothermics](https://github.com/Japhiolite/geothermics) - Educational repository with Jupyter Notebooks all around the topic of geothermal energy.
- [multiphysics](https://github.com/charxie/multiphysics) - Interactive (Heat Transfer) Simulations for Everyone.
- [OpenGeoSys 6](https://gitlab.opengeosys.org/ogs/ogs) - A scientific open source project for the development of numerical methods for the simulation of thermo-hydro-mechanical-chemical processes in porous and fractured media.
- [FEHM](https://github.com/lanl/FEHM) - Has proved to be a valuable asset on a variety of projects of national interest including Environmental Remediation of the Nevada Test Site, the LANL Groundwater Protection Program, geologic CO2 sequestration, Enhanced Geothermal Energy programs, Oil and Gas production, Nuclear Waste Isolation, and Arctic Permafrost.
- [thermo](https://github.com/CalebBell/thermo) - Thermodynamics, phase equilibrium, transport properties and chemical database component of Chemical Engineering Design Library.
- [waiwera](https://github.com/waiwera/waiwera) - A parallel, open-source geothermal flow simulator.
- [fractoolbox](https://github.com/ICWallis/fractoolbox) - Python tools for structural geology and borehole image analysis which includes data handling, frequency and geometric analysis, and reservoir geomechanics.
- [GeoThermalCloud.jl](https://github.com/SmartTensors/GeoThermalCloud.jl) - A repository containing all the data and codes required to demonstrate applications of machine learning methods for geothermal exploration.


### Bioenergy

- [biogas](https://github.com/sashahafner/biogas) - Tools for biogas research in R: process biogas data and predict biogas production.
- [biosteam](https://github.com/BioSTEAMDevelopmentGroup/biosteam) - The Biorefinery Simulation and Techno-Economic Analysis Modules.
- [Multiscale_Ulva](https://github.com/alexliberzonlab/Multiscale_Ulva) - A multi-reactor, algae farm, simulation base function that will be solved in time.
- [BETYdb](https://github.com/PecanProject/bety) - Web-interface to the Biofuel Ecophysiological Traits and Yields Database.


## Energy Storage

### Battery

- [foxBMS](https://github.com/foxBMS/foxbms) - A free, open and flexible development environment to design battery management systems. It is the first modular open source BMS development platform.
- [impedance.py](https://github.com/ECSHackWeek/impedance.py) - A Python package for working with electro-chemical impedance data.
- [PyBaMM](https://github.com/pybamm-team/PyBaMM) - Fast and flexible physics-based battery models in Python.
- [liionpack](https://github.com/pybamm-team/liionpack) - A battery pack simulation tool that uses the PyBaMM framework.
- [ENNOID-BMS](https://github.com/EnnoidMe/ENNOID-BMS) - Open Source: Modular BMS based on LTC68XX & STM32 MCU for up to 400V EV battery pack.
- [cellpy](https://github.com/jepegit/cellpy) - Extract and tweak data from electro-chemical tests of battery cells.
- [prediction-of-battery-cycle](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation) - Data driven prediction of battery cycle life before capacity degradation.
- [BatterySense](https://github.com/rlogiacco/BatterySense) - A simple Arduino library to monitor battery consumption of your battery powered projects, being LiPo, LiIon, NiCd or any other battery type, single or multiple cells: if it can power your Arduino you can monitor it.
- [beep](https://github.com/TRI-AMDD/beep) - A set of tools designed to support Battery Evaluation and Early Prediction of cycle life corresponding to the research of the d3batt program and the Toyota Research Institute.
- [snl-quest](https://github.com/snl-quest/snl-quest) - An open source, Python-based software application suite for energy storage simulation and analysis developed by Sandia National Laboratories.
- [simses](https://gitlab.lrz.de/open-ees-ses/simses) - Software for techno-economic Simulation of Stationary Energy Storage Systems.
- [CAEBAT OAS](https://vibe.ornl.gov/#introduction) - A flexible, robust, and computationally scalable open-architecture framework that integrates multi-physics and multi- scale battery models.
- [universal-battery-database](https://github.com/Samuel-Buteau/universal-battery-database) - The Universal Battery Database is an open source software for managing Lithium-ion cell data.
- [open_BEA](https://gitlab.lrz.de/open-ees-ses/openbea) - Open Battery Models for Electrical Grid Applications.
- [lp_opt](https://gitlab.lrz.de/open-ees-ses/lp_opt) - Linear Programming Optimization Tool for Battery Energy Storage Systems.
- [SLIDE](https://github.com/davidhowey/SLIDE) - SLIDE is a C++ code that simulates degradation of lithium ion cell.
- [equiv-circ-model](https://github.com/batterysim/equiv-circ-model) - An equivalent circuit model for a battery cell, module, and pack.
- [long-live-the-battery](https://github.com/dsr-18/long-live-the-battery) - Predicting total battery cycle life time with machine learning.
- [ISEAFramework](https://git.rwth-aachen.de/isea/framework) - Allows coupled electrical-thermal simulations of single storage systems (e.g. lithium ion batteries or double layer capacitors) or complete storage system packs.
- [Ampere](https://github.com/nealde/Ampere) - Advanced Model Package for ElectRochemical Experiments.
- [StorageVET](https://github.com/epri-dev/StorageVET) - A valuation model for analysis of energy storage technologies and some other energy resources paired with storage.
- [offgridsystems](https://github.com/offgridsystems/Documents) - Data sheet and assembly manual, component data sheets, busbars and files needed to build no-weld wireless BMS DKblock style battery packs.
- [3d_milp](https://github.com/ElektrikAkar/3d_milp) - Energy Arbitrage Optimization With Battery Storage.
- [LIONSIMBA](https://github.com/lionsimbatoolbox/LIONSIMBA) - A Matlab framework based on a finite volume model suitable for Li-ion battery design, simulation, and control.
- [emobpy](https://gitlab.com/diw-evu/emobpy/emobpy) - An open tool for creating battery-electric vehicle time series from empirical data.
- [BattMo](https://github.com/BattMoTeam/BattMo) - The Battery Modelling Toolbox (BattMo) is a resource for continuum modelling of electrochemical devices in MATLAB.
- [Battery Archive](https://github.com/battery-lcf/batteryarchive) -  Easy visualization, analysis, and comparison of battery data across institutions.


### Hydrogen

- [OPEM](https://github.com/ECSIM/opem) - A modeling tool for evaluating the performance of proton exchange membrane fuel cells.
- [gopem](https://github.com/ECSIM/gopem) - GOPEM is a graphical user interface of OPEM.
- [pem-dataset1](https://github.com/ECSIM/pem-dataset1) - Proton Exchange Membrane Fuel Cell Dataset.
- [HIM](https://github.com/FZJ-IEK3-VSA/HIM) - Hydrogen Infrastructure model for the analysis of spatially resolved hydrogen infrastructure pathways.
- [pandapipes](https://github.com/e2nIEE/pandapipes) - A pipeflow calculation tool that complements pandapower in the simulation of multi energy grids, in particular heat and gas networks.
- [The Hydrogen Risk Assessment Models](https://github.com/sandialabs/hyram) - The first-ever software toolkit that integrates deterministic and probabilistic models for quantifying accident scenarios, predicting physical effects, and characterizing hydrogen hazards impact on people and structures.
- [GasModels.jl](https://github.com/lanl-ansi/GasModels.jl) - A Julia/JuMP Package for Gas Network Optimization.
- [SciGRID_gas](https://www.gas.scigrid.de/) - Methods to create an automated network model of the European gas transportation network.
- [Vehicle with Fuel Cell Powertrain](https://github.com/mathworks/Fuel-Cell-Vehicle-Model-Simscape) - Fuel cell electric vehicle with battery model and cooling system.
- [VirtualFCS](https://github.com/Virtual-FCS/VirtualFCS) - A Modelica library for hybrid hydrogen fuel cell and battery power systems.

## Energy Systems

### Energy Modeling and Optimization

- [Open Energy System Models](https://en.wikipedia.org/wiki/Open_energy_system_models) - Used to explore future energy systems and are often applied to questions involving energy and climate policy.
- [Open Energy System Databases](https://en.wikipedia.org/wiki/Open_energy_system_databases) - Employ open data methods to collect, clean, and republish energy-related datasets for open use.
- [Open Models](https://wiki.openmod-initiative.org/wiki/Open_Models) - This page lists energy models published under open source licenses.
- [System Advisor Model](https://github.com/NREL/SAM) - A simulation program for electricity generation projects. It has models for different kinds of renewable energy systems and financial models for residential, commercial, and utility-scale projects.
- [openTEPES](https://github.com/IIT-EnergySystemModels/openTEPES) - Determines the investment plans of new facilities (generators, ESS and lines) for supplying the forecasted demand at minimum cost.
- [PowerGenome](https://github.com/PowerGenome/PowerGenome) - A tool to quickly and easily create inputs for power systems models.
- [load_forecasting](https://github.com/pyaf/load_forecasting) - Load forecasting on Delhi area electric power load using ARIMA, RNN, LSTM and GRU models.
- [REopt_Lite_API](https://github.com/NREL/REopt_Lite_API) - Offers a subset of features from NREL's more comprehensive REopt model. Both models provide concurrent, multiple technology integration and optimization capabilities to help organizations meet their cost savings and energy performance goals.
- [pandapower](http://www.pandapower.org/) - An easy to use open source tool for power system modeling, analysis and optimization with a high degree of automation.
- [urbs](https://github.com/tum-ens/urbs) - A linear optimization model for distributed energy systems.
- [Dispa-SET](https://github.com/energy-modelling-toolkit/Dispa-SET) - Allows to model a power system at any level of detail e.g. micro-grid, region, country, continent.
- [Calliope](https://github.com/calliope-project/calliope) - A framework to develop energy system models, with a focus on flexibility, high spatial and temporal resolution, the ability to execute many runs based on the same base model, and a clear separation of framework and model.
- [Euro-Calliope](https://github.com/calliope-project/euro-calliope) - A model of the European electricity system built using Calliope.
- [OSeMOSYS](https://github.com/OSeMOSYS/OSeMOSYS) - An open source modeling system for long-run integrated assessment and energy planning. It has been employed to develop energy systems models from the scale of continents (African Power Pools, South America, EU28+2) down to the scale of countries, regions and villages.
- [REVUB](https://github.com/VUB-HYDR/REVUB) - The main objective is to model how flexible operation of hydropower plants can help renewable electricity mixes with variable solar and wind power to provide reliable electricity supply and load-following services.
- [FINE](https://github.com/FZJ-IEK3-VSA/FINE) - Provides a framework for modeling, optimizing and assessing energy systems.
- [CoMPAS](https://github.com/com-pas/compas-architecture) - Formed to develop open source software components related to IEC 61850 model implementation (profile management) and configuration of a power industry Protection Automation and Control System.
- [PowerSimulations.jl](https://github.com/NREL-SIIP/PowerSimulations.jl) - A Julia package for power system modeling and simulation of Power Systems operations.
- [PowerSystems.jl](https://github.com/NREL-SIIP/PowerSystems.jl) - Provides a rigorous data model using Julia structures to enable power systems analysis and modeling.
- [Balmorel](https://github.com/balmorelcommunity/Balmorel) - A partial equilibrium model for analyzing the electricity and combined heat and power sectors in an international perspective.
- [DistAIX](https://git.rwth-aachen.de/acs/public/simulation/DistAIXFramework/distaix) - A simulator for cyber-physical power systems that makes use of high performance computing techniques to scale up the simulation.
- [The Open Energy Ontology](https://github.com/OpenEnergyPlatform/ontology) - A domain ontology of the energy-system modeling context.
- [nempy](https://github.com/UNSW-CEEM/nempy) - Aims to enhance the Australian electricity industries modeling and analytical capabilities.
- [NEMO](https://github.com/bje-/NEMO) - The National Electricity Market Optimizer is a chronological dispatch model for testing and optimizing different portfolios of conventional and renewable electricity generation technologies.
- [GlobalEnergyGIS](https://github.com/niclasmattsson/GlobalEnergyGIS) - Generates input data for energy models on renewable energy in arbitrary world regions using public datasets.
- [IDEAS](https://github.com/open-ideas/IDEAS) - A Modelica library allowing simultaneous transient simulation of thermal and electrical systems at both building and feeder level.
- [Antares Simulator](https://github.com/AntaresSimulatorTeam/Antares_Simulator) - An Open Source power system simulator to quantify the adequacy or the economic performance of interconnected energy systems, at short or remote time horizons.
- [Hierarchical Engine for Large-scale Infrastructure Co-Simulation](https://github.com/GMLC-TDC/HELICS) - Today the core uses are in the energy domain, where there is extensive and growing support for a wide-range of electric power system, natural gas, communications and control-schemes, transportation, buildings, and related domain tools.
- [oemof-solph](https://github.com/oemof/oemof-solph) - A model generator for energy system modeling and optimization.
- [oemof-thermal](https://github.com/oemof/oemof-thermal) - Provides tools to model thermal energy components as an extension of oemof.solph, e.g. compression heat pumps, concentrating solar plants, thermal storage and solar thermal collectors.
- [dpsim](https://git.rwth-aachen.de/acs/public/simulation/dpsim/dpsim) - A real-time power system simulator that operates in the dynamic phasor as well as electromagnetic transient domain.
- [VILLASnode](https://git.rwth-aachen.de/acs/public/villas/node) - Connecting real-time power grid simulation equipment.
- [openENTRANCE](https://github.com/openENTRANCE/nomenclature) - The Horizon 2020 openENTRANCE project aims at developing, using and disseminating an open, transparent and integrated modeling platform for assessing low-carbon transition pathways in Europe.
- [Joulia.jl](https://github.com/JuliaEnergy/Joulia.jl) - A Large-Scale Spatial Power System Model for Julia.
- [The IDAES Toolkit](https://github.com/IDAES/idaes-pse) - Aims to provide multi-scale, simulation-based, open source computational tools and models to support the design, analysis, optimization, scale-up, operation and troubleshooting of innovative, advanced energy systems.
- [Temoa](https://github.com/TemoaProject/temoa) - Tools for Energy Model Optimization and Analysis (Temoa) is an open source modeling framework for conducting energy system analysis.
- [PowerSystemDataModel](https://github.com/ie3-institute/PowerSystemDataModel) - Provides an extensive data model capable of modeling energy systems with high granularity e.g. for bottom-up simulations.
- [PyPSA-Eur-Sec](https://github.com/PyPSA/pypsa-eur-sec) - A Sector-Coupled Open Optimisation Model of the European Energy System.
- [antaresViz](https://github.com/rte-antares-rpackage/antaresViz) - Visualize the results of Antares, an Open Source power system simulator meant to be used by anybody placing value in quantifying the adequacy or the economic performance of interconnected energy systems, at short or remote time horizons.
- [antaresRead](https://github.com/rte-antares-rpackage/antaresRead) - Import, manipulate and explore the results of an Antares simulation.
- [Spine-Toolbox](https://github.com/Spine-project/Spine-Toolbox) - An application to define, manage, and execute various energy system simulation models.
- [demandlib](https://github.com/oemof/demandlib) - With the demandlib you can create power and heat profiles for various sectors by scaling them to your desired demand.
- [dieter_py](https://gitlab.com/diw-evu/dieter_public/dieterpy) - An open source power sector optimization model that has been developed to investigate the role of electricity storage and sector coupling options in future scenarios with high shares of renewable energy sources.
- [OMEGAlpes](https://gricad-gitlab.univ-grenoble-alpes.fr/omegalpes/omegalpes) - Aims to be an energy systems modeling tool for linear optimization (LP, MILP).
- [deflex](https://github.com/reegis/deflex) - Flexible multi-regional energy system model for heat, power and mobility.
- [energy-py-linear](https://github.com/ADGEfficiency/energy-py-linear) - Optimizing energy systems using mixed integer linear programming.
- [switch-model](https://github.com/switch-model/switch) - Optimal planning model for power systems with large shares of renewable energy.
- [AnyMOD.jl](https://github.com/leonardgoeke/AnyMOD.jl) - Creating large scale energy system models with multiple periods of capacity expansion formulated as linear optimization problems.
- [FlexiGIS](https://github.com/FlexiGIS/FlexiGIS) - Extracts, filters and categorizes the geo-referenced urban energy infrastructure and allocates the required decentralized storage in urban settings.
- [EMMA](https://neon.energy/emma/) - A techno-economic model of the north-west European power market covering France, Benelux, Germany and Poland.
- [reVX](https://github.com/NREL/reVX) - Renewable Energy Potential(V) eXchange Toot.
- [CapacityExpansion.jl](https://github.com/YoungFaithful/CapacityExpansion.jl) - Future energy system planning (Generation and Transmission Capacity Expansion Planning) in Julia.
- [DPsim](https://github.com/sogno-platform/dpsim) - A solver library for dynamic power system simulation.
- [PyPSA meets Africa](https://github.com/pypsa-meets-africa/pypsa-africa) - A free and open source software project aiming to develop a powerful energy system model for Africa.
- [GenX](https://github.com/GenXProject/GenX) - A highly-configurable, open source electricity resource capacity expansion model that incorporates several state-of-the-art practices in electricity system planning to offer improved decision support for a changing electricity landscape.
- [Open Energy Platform](https://github.com/OpenEnergyPlatform/oeplatform) - Aims to ensure quality, transparency and reproducibility in energy system research. It is a collection of various tools and information and that help working with energy-related data.
- [PyPSA](https://github.com/PyPSA/PyPSA) - A free software toolbox for simulating and optimizing modern power systems that include features such as conventional generators with unit commitment, variable wind and solar generation, storage units, coupling to other energy sectors, and mixed alternating and direct current networks.
- [oemof](https://github.com/oemof/oemof) - Open Energy Modelling Framework - A Python toolbox for energy system modeling and optimization. A community driven, modular, flexible and generic software project.
- [pyGRETA](https://github.com/tum-ens/pyGRETA) - Python Generator of REnewable Time series and mAps: a tool that generates high-resolution potential maps and time series for user-defined regions within the globe.
- [RESKit](https://github.com/FZJ-IEK3-VSA/RESKit) - A toolkit to help generate renewable energy generation time series for energy systems analysis.
- [PowSyBl](https://github.com/powsybl/powsybl-core) - An open source framework written in Java, that makes it easy to write complex software for power systems simulations and analysis.
- [PowSyBl Open Load Flow](https://github.com/powsybl/powsybl-open-loadflow) - An open source implementation of the load flow API that can be found in PowSyBl Core. It supports AC Newtow-Raphson and linear DC calculation methods.
- [matpower](https://github.com/MATPOWER/matpower) - A package of M-files for solving power flow, continuation power flow and optimal power flow problems using MATLAB or Octave.
- [energyRt](https://github.com/energyRt/energyRt) - Making Energy Systems Modeling as simple as a linear regression in R.
- [MVS](https://github.com/rl-institut/multi-vector-simulator) - The multi-vector simulator allows the evaluation of local sector-coupled energy systems that include the energy carriers electricity, heat and/or gas.
- [PowNet](https://github.com/kamal0013/PowNet) - A least-cost optimization model for simulating the Unit Commitment and Economic Dispatch of large-scale (regional to country) power systems.
- [OpenIPSL](https://github.com/OpenIPSL/OpenIPSL) - A library of power system component models written in the Modelica language that can be used for power system dynamic analysis, such as phasor time-domain simulations.
- [RAMP](https://github.com/RAMP-project/RAMP) - A bottom-up stochastic model for the generation of high-resolution multi-energy profiles, conceived for application in contexts where only rough information about users' behaviour are obtainable.
- [POMATO](https://github.com/richard-weinhold/pomato) - An easy to use tool for the comprehensive analysis of the modern electricity market.
- [PowerGAMA](https://bitbucket.org/harald_g_svendsen/powergama/wiki/Home) - A lightweight simulation tool for high level analyses of renewable energy integration in large power systems.
- [Power System Analysis Toolbox](http://faraday1.ucd.ie/psat.html) - A Matlab toolbox for electric power system analysis and simulation.
- [USelectricity](https://github.com/RamiKrispin/USelectricity) - Forecast the US demand for electricity.
- [reV](https://github.com/NREL/reV) - Enables the efficient and scalable computation of renewable energy generation, levelized cost of energy, application of geospatial exclusion layers, and generation of renewable energy supply curves.
- [openCEM](https://github.com/openCEMorg/openCEM) - Capacity Expansion Model and Optimiser for the Australian National Energy Market.
- [energy-py](https://github.com/ADGEfficiency/energy-py) - Reinforcement learning for energy systems.
- [glaes](https://github.com/FZJ-IEK3-VSA/glaes) - Geospatial Land Availability for Energy Systems.
- [onsset](https://github.com/OnSSET/onsset) - A GIS based optimization tool that has been developed to support electrification planning and decision making for the achievement of energy access goals in currently unserved locations.
- [whobs-server](https://github.com/PyPSA/whobs-server) - This is the code for the online optimization of zero-direct-emission electricity systems with wind, solar and storage (using batteries and electrolysed hydrogen gas) to provide a baseload electricity demand, using the cost and other assumptions of your choice.
- [CityLearn](https://github.com/intelligent-environments-lab/CityLearn) - Official reinforcement learning environment for demand response and load shaping.
- [rl-testbed-for-energyplus](https://github.com/IBM/rl-testbed-for-energyplus) - Reinforcement Learning Testbed for Power Consumption Optimization using EnergyPlus.
- [tsam](https://github.com/FZJ-IEK3-VSA/tsam) - A Python package which uses different machine learning algorithms for the aggregation of time series.
- [TimeSeriesClustering](https://github.com/holgerteichgraeber/TimeSeriesClustering.jl) - Provides simple integration of multi-dimensional time-series data (e.g. multiple attributes such as wind availability, solar availability, and electricity demand) in a single aggregation process.
- [MESSAGEix](https://github.com/iiasa/message_ix) - A versatile, dynamic systems-optimization modeling framework developed by the IIASA Energy, Climate, and Environment (ECE) Program since the 1980s.
- [GridPath](https://github.com/blue-marble/gridpath) - A versatile simulation and optimization platform for power-system planning and operations.
- [Peaky Finders](https://github.com/kbaranko/peaky-finders) - A Plotly Dash application with helpful peak load visualizations and a day ahead forecasting model for five different ISOs.
- [Renewcast](https://github.com/derevirn/renewcast) - Forecasting renewable energy generation in EU countries with machine learning algorithms, based on Streamlit and sktime.
- [ANDES](https://github.com/cuihantao/andes) - Power system transient dynamics simulation with symbolic modeling and numerical analysis.
- [REISE.jl](https://github.com/Breakthrough-Energy/REISE.jl) - Renewable Energy Integration Simulation Engine.
- [ESDL](https://github.com/EnergyTransition/ESDL) - A modelling language created for the components in an energy system and their relations towards each other.
- [Transactive Energy Service System](https://github.com/slacgismo/TESS) - A platform to design, deploy, and operate transactive energy systems in electric utility retail environments.
- [Minpower](https://github.com/adamgreenhall/minpower) - An open source toolkit for students and researchers in power systems.
- [TIMES-Ireland Model](https://github.com/MaREI-EPMG) - Information on the Irish energy system as it is today and the best available projections for what the future technology and fuel options and demands will be.
- [Frictionless Energy data](https://sentinel-energy.github.io/friendly_data/) - Common medium to facilitate the flow of data between energy and environmental models in a way that can be automated.
- [Open Modeling Framework](https://github.com/dpinney/omf) - A set of Python libraries for simulating power systems behavior with an emphasis on cost-benefit analysis of emerging technologies.
- [PSP-UFU](https://github.com/Thales1330/PSP) - Open-Source Software with advanced GUI features and CAD tools for electrical power system studies.
- [Energy Policy Simulator](https://github.com/Energy-Innovation/eps-us) - The open-source United States Energy Policy Simulator estimates environmental and economic impacts of hundreds of climate and energy policies.
- [Open Energy Outlook](https://github.com/TemoaProject/oeo) - Examining U.S. energy futures to inform future energy and climate policy efforts.
- [OpenSTEF](https://github.com/OpenSTEF/openstef) - A Python package which is used to make short term forecasts for the energy sector.
- [EIAdata](https://github.com/Matt-Brigida/EIAdata) - Provides programmatic access to the Energy Information Administration's API.
- [Energy System Technology Data](https://github.com/PyPSA/technology-data) - Compilation of assumptions about energy system technologies such as cost, efficiency and lifetime that can be read by energy system modelling software.


### Energy Monitoring and Control

- [OpenEMS](https://github.com/OpenEMS/openems) - Open Source Energy Management System.
- [eemeter](https://github.com/openeemeter/eemeter) - An open source Python package for implementing and developing standard methods for calculating normalized metered energy consumption and avoided energy use.
- [OperatorFabric](https://github.com/opfab/operatorfabric-core) - A modular, extensible, industrial-strength and field-tested platform for use in electricity, water and other utility operations.
- [energy-sparks](https://github.com/Energy-Sparks/energy-sparks) - An open source application that is designed to help schools improve their energy efficiency.
- [emonpi](https://github.com/openenergymonitor/emonpi) - The OpenEnergyMonitor system has the capability to monitor electrical energy use / generation, temperature and humidity.
- [EmonLib](https://github.com/openenergymonitor/EmonLib) - Arduino Energy Monitoring Library.
- [Emoncms](https://github.com/emoncms/emoncms) - A powerful open source web application for processing, logging and visualizing energy, temperature and other environmental data.
- [FlexMeasures](https://github.com/SeitaBV/flexmeasures) - A platform for building energy flexibility services with forecasting and scheduling, written in Python & offering a USEF-conform API.
- [STM32 Energy Monitoring](https://github.com/openenergymonitor/STM32) - The following resources are a work in progress guide to using the STM32 platform for energy monitoring, being written as part of development work into the next generation of OpenEnergyMonitor hardware.


### Energy Distribution and Grids

- [SimBench](https://github.com/e2nIEE/simbench) - The objective of the research project SimBench is the development of a benchmark dataset to support research in grid planning and operation.
- [Egret](https://github.com/grid-parity-exchange/Egret) - A Python-based package for electrical grid optimization based on the Pyomo optimization modeling language.
- [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur) - An Open Optimization Model of the European Transmission System.
- [Energy Transition Engine](https://github.com/quintel/etengine) - Calculation engine for the Energy Transition Model.
- [ETM Pro](https://github.com/quintel/etmodel) - Professional interface of the Energy Transition model.
- [Open Smart Grid Platform](https://github.com/OSGP/open-smart-grid-platform) - An open, generic, scalable and independent 'Internet of Things' platform, which enables various connected smart objects in the public space to be easily controlled and monitored.
- [PowerModels.jl](https://github.com/lanl-ansi/PowerModels.jl) - Designed to enable computational evaluation of emerging power network formulations and algorithms in a common platform.
- [PowerModelsAnnex.jl](https://github.com/lanl-ansi/PowerModelsAnnex.jl) - An extension of PowerModels.jl that provides a home for open source sharing of preliminary and/or exploratory methods in power system optimization.
- [Power Grid Lib](https://github.com/power-grid-lib/pglib-opf) - This benchmark library is curated and maintained by the IEEE PES Task Force on Benchmarks for Validation of Emerging Power System Algorithms and is designed to evaluate a well established version of the the AC Optimal Power Flow problem.
- [pypownet](https://github.com/MarvinLer/pypownet) - A power network simulator with a Reinforcement Learning-focused usage.
- [Grid2Op](https://github.com/rte-france/Grid2Op) - A testbed platform to model sequential decision making in power systems.
- [eDisGo](https://github.com/openego/eDisGo/) - Optimization of flexibility options and grid expansion for distribution grids based on PyPSA.
- [offgridders](https://github.com/rl-institut/offgridders) - Models and optimizes capacity & dispatch of electricity supply systems, off-grid or connected to a (weak) central grid.
- [RTS-GMLC](https://github.com/GridMod/RTS-GMLC) - Reliability Test System of the Grid Modernization Lab Consortium.
- [openmodelica-microgrid-gym](https://github.com/upb-lea/openmodelica-microgrid-gym) - An OpenAI Gym Environment for Microgrids.
- [OpenDSS](https://sourceforge.net/projects/electricdss/) - An electric power Distribution System Simulator for supporting distributed resource integration and grid modernization efforts.
- [PowerDynamics.jl](https://github.com/JuliaEnergy/PowerDynamics.jl) - Provides all the tools you need to create a dynamic power grid model and analyze it.
- [InfrastructureSystems.jl](https://github.com/NREL-SIIP/InfrastructureSystems.jl) - Provides utilities to support data models for infrastructure modeling in NREL-SIIP.
- [openleadr](https://www.lfenergy.org/projects/openleadr/) - Open Automated Demand Response (OpenADR) is an open and interoperable information exchange model and emerging smart grid standard.
- [GridCal](https://github.com/SanPen/GridCal) - Aims to be a complete platform for power systems research and simulation.
- [pyehub](https://gitlab.com/energyincities/python-ehub) - A Python-based, modular and nestable implementation of the Energy Hub model (balancing demand and supply, system capacity sizing and network flows using Mixed-Integer Linear Programming).
- [origin](https://github.com/energywebfoundation/origin) - A set of toolkits that together provide a system for issuance and management of Energy Attribute Certificates.
- [Grid Singularity Energy Exchange Engine (D3A)](https://github.com/gridsingularity/gsy-e) - An interface to download and deploy interconnected, grid-aware energy marketplaces.
- [Backbone](https://gitlab.vtt.fi/backbone/backbone) - A generic energy network optimization tool written in GAMS.
- [APIS](https://github.com/SonyCSL/APIS) - Build a microgrid that utilizes variable renewable energy as the main power source and enhances the resilience of the power system.
- [pymgrid](https://github.com/Total-RD/pymgrid) - A Python library to generate and simulate a large number of microgrids.
- [SciGRID](https://power.scigrid.de/) - The focus will be on the European transmission grids, but the methods will be applicable more generally.
- [mosaik](https://gitlab.com/mosaik/mosaik) - A flexible Smart Grid co-simulation framework.
- [SmartGridToolbox](https://gitlab.com/SmartGridToolbox/SmartGridToolbox) - Designed to provide an extensible and flexible starting point for developing a wide variety of smart grid simulations and other applications.
- [OPEN](https://github.com/EPGOxford/OPEN) - The framework combines distributed energy resource modelling (e.g. for PV generation sources, battery energy storage systems, electric vehicles), energy market modelling, power flow simulation and multi-period optimisation for scheduling flexible energy resources.
- [GridLAB-D](https://github.com/slacgismo/gridlabd) - A distribution level power system simulator designed to allow users to create and analyze smart grid technologies.
- [Gym-ANM](https://github.com/robinhenry/gym-anm) - Design Reinforcement Learning environments that model Active Network Management tasks in electricity distribution networks.
- [SEAPATH](https://www.lfenergy.org/projects/seapath/) - Industrial grade open source real-time platform that can run virtualized automation and protection applications for the power grid industry.
- [Tools for the iTEM databases](https://github.com/transportenergy/database) - Contains tools for two databases maintained by iTEM, the International Transport Energy Modeling consortium.
- [PowerSimData](https://github.com/Breakthrough-Energy/PowerSimData) - Is part of a Python software ecosystem developed by Breakthrough Energy Sciences to carry out power flow study in the U.S. electrical grid.
- [Digital Twins Definition Language ontology for Energy Grid](https://github.com/Azure/opendigitaltwins-energygrid) - A global standard for energy grid assets management, power system operations modeling and physical energy commodity market.
- [SIMONA](https://github.com/ie3-institute/simona) - Provides a simulation toolbox to run and implement large-scale agent-based electricity grid simulations with focus on distribution grids.


### Datasets on Energy Systems

- [OpenNEM](https://github.com/opennem/opennem-fe) - Aims to make the wealth of public Australian Electricity Market data more accessible to a wider audience.
- [Open Power System Data](https://open-power-system-data.org/data-sources) - A list of primary data sources that are helpful for power system modeling of Europe.
- [The Public Utility Data Liberation Project](https://github.com/catalyst-cooperative/pudl) - Makes the US' energy data easier to access and use.
- [Global Power Plant Database](https://github.com/wri/global-power-plant-database) - A comprehensive, global and open source database of power plants.
- [electricitymap-contrib](https://github.com/tmrowco/electricitymap-contrib) - A real-time visualization of the CO2 emissions from electricity consumption.
- [entsoe-py](https://github.com/EnergieID/entsoe-py) - A Python client for the ENTSO-E API (European Network of Transmission System Operators for Electricity).
- [time series](https://github.com/Open-Power-System-Data/time_series) - Contains scripts that compile time series data of the European power system.
- [renewable power plant](https://github.com/Open-Power-System-Data/renewable_power_plants) - Contains scripts to create lists of renewable power plants in Germany, Denmark, France and Poland, and daily time series of cumulated installed capacity per energy source type for Germany.
- [conventional power plants](https://github.com/Open-Power-System-Data/conventional_power_plants) - Contains data on conventional power plants for Germany as well as other selected European countries. The data include individual power plants with their technical characteristics.
- [open-MaStR](https://github.com/OpenEnergyPlatform/open-MaStR) - Download and process German energy data from BNetzA database Marktstammdatenregister.
- [powerplantmatching](https://github.com/FRESNA/powerplantmatching) - A toolset for cleaning, standardizing and combining multiple power plant databases.
- [GeoNuclearData](https://github.com/cristianst85/GeoNuclearData) - Database with information about Nuclear Power Plants worldwide.
- [pyEIA](https://github.com/thomastu/pyEIA) - An Energy Information Administration API Python client for researchers who need data.
- [EIA](https://github.com/ropensci/eia) - An R package wrapping the US Energy Information Administration open data API.
- [atlite](https://github.com/PyPSA/atlite) - Light-weight version of Aarhus RE Atlas for converting weather data to power systems data.
- [NYISOToolkit](https://github.com/m4rz910/NYISOToolkit) - A collection of modules for accessing power system data, generating statistics, and creating visualizations from the New York Independent System Operator.
- [Photovoltaic time series for European countries](https://zenodo.org/record/2613651#.XRtJRP7Rapo) - Comprises 38 years-long hourly time series representing the photovoltaic capacity factors in every European country (EU-28 plus Serbia, Bosnia-Herzegovina, Norway, and Switzerland).
- [SolarData](https://github.com/dazhiyang/SolarData) - Download and manipulate some publicly available solar datasets.
- [UKgrid](https://github.com/RamiKrispin/UKgrid) - An R data package with the UK National Grid historical demand for electricity between April 2005 and October 2019.
- [USgrid](https://github.com/RamiKrispin/USgrid) - The hourly demand and supply of electricity in the US.
- [ESIOS](https://github.com/SanPen/ESIOS) - Comprehensive library to access the Spanish electricity market entity in Python.
- [energy-data](https://github.com/owid/energy-data) - Data on global energy consumption (primary energy, per capita, and growth rates), energy mix, electricity mix and other relevant metrics.
- [OpenEI](https://openei.org/wiki/Main_Page) - A knowledge-sharing online community dedicated to connecting people with the latest information and data on energy resources from around the world.
- [Power grid frequency data base](https://osf.io/by5hu/) - This data set contains precisely time stamped (GPS referenced) frequency data from several power grids around the world in one second resolution and 1 hour excerpts of raw data.
- [EnergyDataSimulationChallenge](https://github.com/enechange/EnergyDataSimulationChallenge) - Allows applicants to demonstrate their ability to analyze and develop software that makes use of big energy production data.
- [disaggregator](https://github.com/DemandRegioTeam/disaggregator) - A set of tools for processing of spatial and temporal disaggregations of demands of electricity, heat and natural gas.
- [The FfE Open Data Portal](http://opendata.ffe.de/) - Offers an overview of free datasets for modelling energy demand and generation.
- [DKA Solar Centre](http://dkasolarcentre.com.au/) - Online hub for sharing solar-related knowledge and data from the Northern Territory, Australia.
- [eiapy](https://github.com/systemcatch/eiapy) - A simple wrapper for the U.S. Energy Information Administration API. 
- [Power Station Dictionary](https://github.com/OSUKED/Power-Station-Dictionary) - A power station dictionary that enables mapping between various naming conventions and associated plant metadata.
- [ElexonDataPortal](https://github.com/OSUKED/ElexonDataPortal) - Wrapper for the Balancing Mechanism Reporting Service API to balance power flowing on to and off from the electricity Transmission System in Great Britain.
- [KoaVTracker](https://gitlab.com/diw-evu/koavtracker) - Energy targets in the coalition agreement of the German government vs. where we stand today.

## Consumption of Energy and Resources 

### Buildings and Heating 

- [hpxml](https://github.com/hpxmlwg/hpxml) - Home Performance XML is a data transfer standard for the home performance industry.
- [HPXML to Home Energy Score Translator](https://github.com/NREL/hescore-hpxml) - This translator script takes an HPXML file or directory of files as an input and generates HEScore inputs from it.
- [LoadProfileGenerator](https://github.com/FZJ-IEK3-VSA/LoadProfileGenerator) - A program for generating load curves for residential consumers. Agent-based and extremely detailed.
- [The-building-data-genome-project](https://github.com/buds-lab/the-building-data-genome-project) - A collection of non-residential buildings for performance analysis and algorithm benchmarking.
- [VOLTTRON](https://github.com/VOLTTRON/volttron) - A platform that provides services for collecting and storing data from buildings and devices. It provides an environment for developing applications that interact with data.
- [EnergyPlus](https://github.com/NREL/EnergyPlus) - A whole building energy simulation program that engineers, architects, and researchers use to model both energy consumption and water usage in buildings.
- [OpenStudio](https://github.com/NREL/OpenStudio) - A cross-platform collection of software tools to support whole building energy modeling using EnergyPlus and advanced daylight analysis using Radiance.
- [BEMServer](https://github.com/HIT2GAP-EU-PROJECT/bemserver) - An open source Python server to deploy energy management solutions for buildings.
- [SEED](https://github.com/SEED-platform/seed) - Standard Energy Efficiency Data Platform™ is a web-based application that helps organizations easily manage data on the energy performance of large groups of buildings.
- [HPWHsim](https://github.com/EcotopeResearch/HPWHsim) - An open source simulation model for Heat Pump Water Heaters (HPWH).
- [OpenStudio-ERI](https://github.com/NREL/OpenStudio-ERI) - Calculates an Energy Rating Index (ERI) via an OpenStudio/EnergyPlus-based workflow. Building information is provided through an HPXML file.
- [OpenStudio-HPXML](https://github.com/NREL/OpenStudio-HPXML) - Modeling of residential buildings in EnergyPlus using OpenStudio/HPXML.
- [AixLib](https://github.com/RWTH-EBC/AixLib) - A Modelica model library for building performance simulations.
- [TEASER](https://github.com/RWTH-EBC/TEASER) - Tool for Energy Analysis and Simulation for Efficient Retrofit.
- [pyCity](https://github.com/RWTH-EBC/pyCity) - A Python package for data handling and scenario generation of city districts and urban energy systems.
- [tespy](https://github.com/oemof/tespy) - Provides a powerful simulation toolkit for thermal engineering plants such as power plants, district heating systems or heat pumps.
- [RC_BuildingSimulator](https://github.com/architecture-building-systems/RC_BuildingSimulator) - A Resistance Capacitance Model for an Energetic Simulation of a Building.
- [City Energy Analyst](https://github.com/architecture-building-systems/CityEnergyAnalyst) - Helps you to analyze the effects of building retrofits, land-use planning, district heating and cooling and renewable energy on the future costs, emissions and energy consumption of neighborhoods and districts.
- [Modelica Buildings library](https://github.com/lbl-srg/modelica-buildings) - A free and open source library with dynamic simulation models for building energy and control systems.
- [StROBe](https://github.com/open-ideas/StROBe) - An open web tool developed at the KU Leuven Building Physics Section to model the pervasive space for residential integrated district energy assessment simulations in the openIDEAS modeling environment.
- [NYCBuildingEnergyUse](https://github.com/mdh266/NYCBuildingEnergyUse) - Predict the emission of greenhouse gases from buildings by looking at their age, and water consumption as well as other energy consumption metrics.
- [Smart-Energy-Monitor](https://github.com/jonathanrjpereira/Smart-Energy-Monitor) - The goal is to accurately predict the monthly electricity bill of the household using minimum hardware and by acquiring electrical data at a single location.
- [Hotmaps](https://github.com/HotMaps/Hotmaps-toolbox-service) - The open source mapping and planning tool for heating and cooling.
- [BuildSysPro](https://github.com/EDF-TREE/BuildSysPro) - EDF's Modelica library for buildings, districts and energy systems modeling.
- [MPCPy](https://github.com/lbl-srg/MPCPy) - The Python-based open source platform for model predictive control in buildings.
- [obc](https://github.com/lbl-srg/obc) - Performance Evaluation, Specification, Deployment and Verification of Building Control Sequences.
- [The Application Domain Extension](https://github.com/cstb/citygml-energy) - Defines a standardized data model based on CityGML format for urban energy analyses, aiming to be a reference exchange data format between different urban modeling tools and expert databases.
- [PLANHEAT Tool](https://github.com/Planheat/Planheat-Tool) - A QGIS plug-in based on an open source code, whose goal is to analyze, plan and simulate low carbon Heating & Cooling scenarios.
- [Energy Signature Analyser](https://gitlab.com/energyincities/energy-signature-analyser) - A toolbox to analyze energy signatures of buildings and compare the signatures of all buildings within an entire building stock.
- [BuildingSystems](https://github.com/UdK-VPT/BuildingSystems) - The Modelica open source BuildingSystems library is developed for dynamic simulation of the energetic behavior of single rooms, buildings and whole districts.
- [modelica-ibpsa](https://github.com/ibpsa/modelica-ibpsa) - A Modelica library for building and district energy systems developed within IBPSA Project 1.
- [project1](https://github.com/ibpsa/project1) - Creates open source software that builds the basis of next generation computing tools for the design and operation of building and district energy and control systems.
- [teb](https://github.com/TEB-model/teb) - A library to calculate the urban surface energy balance at neighborhood scale assuming a simplified canyon geometry.
- [tsib](https://github.com/FZJ-IEK3-VSA/tsib) - A Python package that builds up on different databases and models for creating consistent demand and production time series of residential buildings.
- [DHNx](https://github.com/oemof/DHNx) - This package provides an open toolbox for district heating and cooling network optimization and simulation models.
- [The Building Data Genome 2 Data-Set](https://github.com/buds-lab/building-data-genome-project-2) - Whole building non-residential hourly energy meter data from the Great Energy Predictor III competition.
- [BESOS](https://gitlab.com/energyincities/besos) - A collection of modules for the simulation and optimization of buildings and urban energy systems.
- [pythermalcomfort](https://github.com/CenterForTheBuiltEnvironment/pythermalcomfort) - Package to calculate several thermal comfort indices (e.g. PMV, PPD, SET, adaptive) and convert physical variables.
- [comfort_tool](https://github.com/CenterForTheBuiltEnvironment/comfort_tool) - A web interface for comfort model calculations and visualizations according to ASHRAE Standard-55, EN Standard 16798 and ISO Standard 7730.
- [resstock](https://github.com/NREL/resstock) - Helping states, municipalities, utilities, and manufacturers identify which building stock improvements save the most energy and money.
- [DSMR-reader](https://github.com/dsmrreader/dsmr-reader) - Used for reading the smart meter DSMR (Dutch Smart Meter Requirements) P1 port yourself at your home.
- [Multiscale Solar Water Heating](https://github.com/LBNL-ETA/MSWH) - Solar water heating system modeling and simulation for individual and community scale projects.
- [eplusr](https://github.com/hongyuanjia/eplusr) - Provides a rich toolkit of using whole building energy simulation program EnergyPlus directly in R, which enables programmatic navigation, modification of EnergyPlus, conducts parametric simulations and retrieves outputs.
- [Brick](https://github.com/BrickSchema/Brick) - An open-source effort to standardize semantic descriptions of the physical, logical and virtual assets in buildings and the relationships between them.
- [BETTER](https://github.com/LBNL-JCI-ICF/better) - Building Efficiency Targeting Tool for Energy Retrofits.
- [NILM](https://github.com/nilmtk/nilmtk) - Non-Intrusive Load Monitoring is the process of estimating the energy consumed by individual appliances given just a whole-house power meter reading.
- [volkszaehler.org](https://github.com/volkszaehler/volkszaehler.org) - A free smart meter implementation with focus on data privacy.
- [ModBus Measurement Daemon](https://github.com/volkszaehler/mbmd) - A daemon for collecting measurement data from smart meters and grid inverters over modbus.
- [HiSim](https://github.com/FZJ-IEK3-VSA/HiSim) - Simulation and analysis of household scenarios using modern components as alternative to fossil fuel based ones.
- [hplib](https://github.com/RE-Lab-Projects/hplib) - Database with efficiency parameters from public Heatpump Keymark datasets as well as parameter-sets and functions in order to simulate heat pumps.
- [Thermofeel](https://github.com/ecmwf-projects/thermofeel) - A library to calculate human thermal comfort indexes.
- [CBE Clima Tool](https://github.com/CenterForTheBuiltEnvironment/clima) - A web-based application built to support the need of architects and engineers interested in climate-adapted design.
- [Kiva](https://github.com/bigladder/kiva) - Used to calculate heat loss and gain on a timestep basis from building foundations.
- [Macquette](https://gitlab.com/retrofitcoop/macquette) - A whole house energy assessment tool, which models a building to produce a report to help householders under how their home performs now in terms of energy use and how it might be improved.

### Mobility and Transportation

- [stplanr](https://github.com/ropensci/stplanr) - A package for sustainable transport planning with R.
- [CO2MPAS-TA](https://github.com/JRCSTU/CO2MPAS-TA) - CO2MPAS is backward-looking longitudinal-dynamics CO2 and fuel-consumption simulator for light-duty vehicles.
- [wltp](https://github.com/JRCSTU/wltp) - Generate WLTC gear-shifts based on vehicle characteristics.
- [The Open Charge Point Protocol](https://github.com/NewMotion/ocpp) - A network protocol for communication between electric vehicle chargers and a central backoffice system.
- [ocpp](https://github.com/mobilityhouse/ocpp) - Python implementation of the Open Charge Point Protocol.
- [docile-charge-point](https://github.com/NewMotion/docile-charge-point) - Scriptable OCPP charge point simulator and test tool.
- [MaaS Global](https://github.com/maasglobal/maas-schemas) - Mobility as a Service API - data model, tests and validation.
- [CoopCycle](https://github.com/coopcycle/coopcycle-web) - A self-hosted platform to order meals in your neighborhood and get them delivered by bike couriers.
- [EVNotify](https://github.com/EVNotify/EVNotify) - Allows you to monitor your electric vehicle and let you notify when the specified preset state of charge has been achieved.
- [icare](https://github.com/diowa/icare) - An open source carpooling platform used as a basis for our commercial product Company Carpool.
- [Carpoolear](https://github.com/STS-Rosario/carpoolear) - The first Argentine Facebook app that allows the users of this social network to share car trips with other users.
- [UTD19](https://utd19.ethz.ch/) - Largest multi-city traffic dataset publicly available.
- [OpenEVSE](https://github.com/lincomatic/open_evse) - Firmware for OpenEVSE: Open Source Hardware J1772 Electric Vehicle Supply Equipment.
- [OpenEVSE WiFi gateway](https://github.com/OpenEVSE/ESP8266_WiFi_v2.x) - Uses an ESP8266 (ESP-12) which communicates with the OpenEVSE controller via serial utilizing the existing RAPI API serial interface.
- [navitia](https://github.com/CanalTP/navitia) - An open source web API, initially built to provide traveler information on urban transportation networks.
- [DeepMove](https://github.com/vonfeng/DeepMove) - Predicting Human Mobility with Attentional Recurrent Networks.
- [mobility-data-specification](https://github.com/openmobilityfoundation/mobility-data-specification) - A data standard to enable communication between mobility companies and local governments.
- [OpenConcept](https://github.com/mdolab/openconcept) - A toolkit for conceptual MDAO of aircraft with unconventional propulsion architectures.
- [Open Charge Map](https://github.com/openchargemap/ocm-system) - The global public registry of electric vehicle charging locations.
- [EVCC](https://github.com/andig/evcc) - An extensible EV Charge Controller with PV integration implemented in Go.
- [SteVe](https://github.com/RWTH-i5-IDSG/steve) - Provides basic functions for the administration of charge points, user data and RFID cards for user authentication and was tested successfully in operation.
- [RISE-V2G](https://github.com/V2GClarity/RISE-V2G) - The only fully-featured reference implementation of the Vehicle-2-Grid communication interface ISO 15118.
- [simobility](https://github.com/sash-ko/simobility) - A human-friendly Python framework that helps scientists and engineers to prototype and compare fleet optimization algorithms (autonomous and human-driven vehicles).
- [MobiVoc](https://github.com/vocol/mobivoc) - An open vocabulary for future-oriented mobility solutions.
- [Transportr](https://github.com/grote/Transportr) - The public transport companion that respects your privacy and your freedom.
- [OneBusAway](https://github.com/OneBusAway/onebusaway-android) - The Open Source platform for Real Time Transit Info.
- [transitfeed](https://github.com/google/transitfeed) - A Python library for reading, validating and writing transit schedule information in the GTFS format.
- [node-gtfs](https://github.com/BlinkTagInc/node-gtfs) - Import GTFS transit data into SQLite and query routes, stops, times, fares and more.
- [Public Transport Enabler](https://github.com/schildbach/public-transport-enabler) - Unleash public transport data in your Java project.
- [osm2gtfs](https://github.com/grote/osm2gtfs) - Turn OpenStreetMap data and schedule information into GTFS.
- [Quetzal](https://github.com/systragroup/quetzal) - A modeling library designed for transport planning and traffic forecasts.
- [quetzal_germany](https://github.com/marlinarnz/quetzal_germany) - A four step transport model for Germany using the quetzal transport modeling suite.
- [OpenMobility](https://openmobility.eclipse.org/) - Driving the Evolution and Broad Adoption of Open Source Mobility Modeling and Simulation Technologies.
- [NoiseModelling](https://github.com/Ifsttar/NoiseModelling) - A free and open source model to compute noise maps.
- [NoiseCapture](https://github.com/Ifsttar/NoiseCapture) - Android App dedicated to the measurement of environmental noise.
- [bikedata](https://github.com/ropensci/bikedata) - Aims to enable ready importing of historical trip data from all public bicycle hire systems which provide data. Will be expanded on an ongoing basis as more systems publish open data.
- [CyclOSM](https://github.com/cyclosm/cyclosm-cartocss-style) - A CartoCSS map style designed with cycling in mind.
- [Gym Electric Motor](https://github.com/upb-lea/gym-electric-motor) - An OpenAI Gym Environment for Electric Motors.
- [BEAM](https://github.com/LBNL-UCB-STI/beam) - The Framework for Modeling Behavior, Energy, Autonomy, and Mobility in Transportation Systems.
- [WoBike](https://github.com/ubahnverleih/WoBike) - Public transport and multimodal routing apps could benefit from showing nearby bikes from bikesharing services. So here's a list showing the APIs of a few of these platforms.
- [multicycles](https://github.com/PierrickP/multicycles) - Aggregates on one map, more than 100 share vehicles like bikes, scooters, mopeds and cars.
- [pybikes](https://github.com/eskerda/pybikes) - Provides a set of tools to scrape bike sharing data from different websites and APIs, thus providing a coherent and generalized set of classes and methods to access this sort of information.
- [sustainable-mobility-api](https://gitlab.com/mshepherd/sustainable-mobility-api) - Consists of a Python library and HTTP API for estimating the environmental impact of personal mobility.
- [ChargyDesktopApp](https://github.com/OpenChargingCloud/ChargyDesktopApp) - Chargy is a transparency software for secure and transparent e-mobility charging processes, as defined by the German "Eichrecht".
- [WWCP_OCPP](https://github.com/OpenChargingCloud/WWCP_OCPP) - Connectivity between the World Wide Charging Protocol (WWCP) and the Open Charge Point Protocol (OCPP v1.6/v2.0).
- [WWCP_Core](https://github.com/OpenChargingCloud/WWCP_Core) - The World Wide Charging Protocol Suite is a collection of protocols in order to connect market actors in the field of e-mobility solutions via scalable and secure Internet protocols.
- [openv2g](http://openv2g.sourceforge.net/) - The objective to start this project is primarily to support the ISO and IEC standardization process to specify the so called "Vehicle 2 Grid Communication Interface" (V2G CI) which became the ISO IEC 15118 specification by now.
- [RAMP-mobility](https://github.com/RAMP-project/RAMP-mobility) - A novel application of the RAMP main engine for generating bottom-up stochastic electric vehicles load profiles.
- [PCT](https://github.com/ITSLeeds/pct/) - The goal is to increase the accessibility and reproducibility of the data produced by the Propensity to Cycle Tool (PCT).
- [goat](https://github.com/goat-community/goat) - A tool capable of modeling walking and cycling accessibility.
- [gtfs-router](https://github.com/ATFutures/gtfs-router) - An R package for routing with GTFS (General Transit Feed Specification) data.
- [CityFlow](https://github.com/cityflow-project/CityFlow/) - A Multi-Agent Reinforcement Learning Environment for Large Scale City Traffic Scenario.
- [Complete_Street_Rule](https://github.com/d-wasserman/Complete_Street_Rule) - An ArcGIS CityEngine scenario oriented design tool intended to enable users to quickly create procedural generated multimodal streets.
- [tesla_powerwall](https://github.com/jrester/tesla_powerwall) - Python Tesla Powerwall API for consuming a local endpoint.
- [Vehicle Energy Dataset](https://github.com/gsoh/VED) - A large-scale dataset for vehicle energy consumption research.
- [gbfs](https://github.com/NABSA/gbfs) - Documentation for the General Bikeshare Feed Specification, a standardized data feed for shared mobility system availability.
- [Bike Index](https://github.com/bikeindex/bike_index) - Bike registration that works: online, powerful, free.
- [go-ocpp](https://github.com/voltbras/go-ocpp) - v1.5 and v1.6 Open Charge Point Protocol implementation in Golang.
- [EVMap](https://github.com/johan12345/EVMap) - Android app to access the goingelectric.de electric vehicle charging station directory.
- [emobility-smart-charging](https://github.com/SAP/emobility-smart-charging) - Smart charging algorithms with REST API for electric vehicle fleets.
- [open-ev-data](https://github.com/chargeprice/open-ev-data) - Open Dataset of Electric Vehicle specs.
- [SmartEVSE](https://github.com/SmartEVSE/smartevse) - Smart EVSE Electric Vehicle Charging Station.
- [BikeshareClient](https://github.com/andmos/BikeshareClient) - Dotnet library for integrating with GBFS bikeshare systems.
- [Growing Urban Bicycle Networks](https://github.com/mszell/bikenwgrowth) - Source code for the paper Growing Urban Bicycle Networks, exploring algorithmically the limitations of urban bicycle network growth.
- [A/B Street](https://github.com/a-b-street) - A traffic simulation game exploring how small changes to roads affect cyclists, transit users, pedestrians, and drivers.
- [enviroCar](https://github.com/enviroCar/enviroCar-app) - An Android App for collecting car sensor data for the enviroCar platform.
- [EVerest](https://github.com/EVerest/everest) - An open source software stack for EV charging infrastructure.
- [Streetmix](https://github.com/streetmix/streetmix) - Makes it easy for people to design public spaces together.


### Production and Industry

- [Industry Energy Tool](https://github.com/NREL/Industry-Energy-Tool) - A calculator developed by NREL for projecting energy efficiency and fuel switching scenarios for the U.S. industrial sector energy use and emissions at the Census Region and county-level.
- [Industry Energy Data Book](https://github.com/NREL/Industry-energy-data-book) - Summarizes the status of, and identifies the key trends in energy use and its underlying economic drivers across the four industrial subsectors: agriculture, construction, manufacturing, and mining.
- [CalTRACK](https://github.com/energy-market-methods/caltrack) - Methods are developed in an open and transparent stakeholder process that uses empirical testing to define replicable methods for calculating normalized metered energy consumption using either monthly or interval data from an existing conditions baseline.
- [OpenModelica](https://github.com/OpenModelica/OpenModelica) - An open source Modelica-based modeling and simulation environment intended for industrial and academic usage.

### Computation and Communication

- [H2020 CATALYST](https://gitlab.com/project-catalyst) - Converting data centres in energy flexibility ecosystems.
- [Energy-Languages](https://github.com/greensoftwarelab/Energy-Languages) - The complete set of tools for energy consumption analysis of programming languages, using Computer Language Benchmark Game.
- [energyusage](https://github.com/responsibleproblemsolving/energy-usage) - A Python package that measures the environmental impact of computation.
- [Green Cost Explorer](https://github.com/thegreenwebfoundation/green-cost-explorer) - See how much of your cloud bill is spent on fossil fuels, so you can do the right thing and switch.
- [Scaphandre](https://github.com/hubblo-org/scaphandre) - An open source software agent to track energy consumption of ICT services from the servers.
- [CPU Energy Meter](https://github.com/sosy-lab/cpu-energy-meter) - A Linux tool that allows to monitor power consumption of Intel CPUs at fine time intervals.
- [PowerAPI](https://github.com/powerapi-ng/powerapi) - A middleware toolkit for building software-defined power meters.
- [argos](https://github.com/marmelab/argos) - A tool to measure consumption of a given Docker command and see its performance evolution. Argos is able to measure CPU, memory and network usage of Docker containers for a given command. By measuring resource consumption of dockerized E2E tests, Argos allows to compare the consumption of an app between its different versions.
- [ecometer](https://gitlab.com/ecoconceptionweb/ecometer) - Loads websites, compute metrics (from network activity, loaded payloads and the web page), and uses them to assess the website's ecodesign maturity based on a list of best practices.
- [patch-node](https://github.com/patch-technology/patch-node) - The road to global carbon-neutrality will be through programmatic compensation.
- [co2.js](https://github.com/thegreenwebfoundation/co2.js) - A npm module for accessing the green web API, and estimating the carbon emissions from using digital services.
- [nvidia-co2](https://github.com/kylemcdonald/nvidia-co2) - Adds gCO2eq emissions to nvidia-smi.
- [The Low Impact Website](https://github.com/Organic-Basics/ob-low-impact-website) - Reduces data transfer by up to 70% in comparison to our regular website.
- [cryptoart-footprint](https://github.com/kylemcdonald/cryptoart-footprint) - Estimate the total emissions for popular CryptoArt platforms.
- [Cloud Carbon Footprint](https://github.com/cloud-carbon-footprint/cloud-carbon-footprint) - A tool to estimate energy use (kilowatt-hours) and carbon emissions (metric tons CO2e) from public cloud usage.
- [pyJoules](https://github.com/powerapi-ng/pyJoules) - A software toolkit to measure the energy footprint of a host machine along the execution of a piece of Python code.
- [Carbon free energy for Google Cloud regions](https://github.com/GoogleCloudPlatform/region-carbon-info) - Contains sustainability characteristics of Google Cloud regions in a machine readable format.
- [Carbon-API-2.0](https://gitlab.com/wholegrain/carbon-api-2-0) - Estimating the carbon emissions per page on thousands of sites by looking at the amount of data that they transfer on load.
- [FEEP](https://invent.kde.org/cschumac/feep) -  Improve the energy efficiency of free and open source software.
- [LEAF](https://github.com/dos-group/leaf) - Simulator for modeling energy consumption in cloud, fog, and edge computing environments.
- [ethereum-nft-activity](https://github.com/kylemcdonald/ethereum-nft-activity) - Estimate the total emissions for popular CryptoArt platforms.
- [kube-green](https://github.com/kube-green/kube-green) - A k8s operator to reduce CO2 footprint of your clusters.
- [ecoCode](https://github.com/cnumr/ecoCode) - Reduce the environmental footprint of your software applications with this cutting-edge sonarQube plugin.
- [Kepler](https://github.com/sustainable-computing-io/kepler) - Uses eBPF to probe energy related system stats and exports as Prometheus metrics.
- [Software Carbon Intensity Specification](https://github.com/Green-Software-Foundation/software_carbon_intensity) - A specification that describes how to calculate a carbon intensity for software applications.
- [Principles of Green Software Engineering](https://github.com/jawache/principles-green) - Are a core set of competencies needed to define, build and run sustainable software applications.


## Emissions

### Carbon Intensity and Accounting 

- [impact](https://github.com/mlco2/impact/) - Compute your ML model's emissions with our calculator and add the results to your paper with our generated LaTeX template.
- [carbon footprint](https://github.com/protea-earth/carbon_footprint) - Calculate your carbon footprint easily using a command line interface.
- [CarbonFootprintEGU](https://github.com/milankl/CarbonFootprintEGU) - Travel carbon footprint of the European Geosciences Union General Assembly 2019.
- [Bloom](https://github.com/tmrowco/bloom-contrib) - A SaaS that allow companies to become climate leaders, from calculating their climate impact to communicating about their climate efforts. It connects to as many data sources as possible to assess your carbon footprint and find mitigation opportunities.
- [NMF.earth app](https://github.com/NMF-earth/nmf-app) - iOS & Android app to understand and reduce your carbon footprint.
- [EnergyPATHWAYS](https://github.com/energyPATHWAYS/EnergyPATHWAYS) - The energyPATHWAYS Model is a professional, open source energy and carbon planning tool for use in evaluating long-term, economy-wide greenhouse gas mitigation scenarios.
- [CarbonFootprint](https://gitlab.com/aossie/CarbonFootprint) - A browser extension that displays carbon footprint information in multiple map services.
- [carbontracker](https://github.com/lfwa/carbontracker) - Track and predict the energy consumption and carbon footprint of training deep learning models.
- [experiment-impact-tracker](https://github.com/Breakend/experiment-impact-tracker) - Meant to be a simple drop-in method to track energy usage, carbon emissions, and compute utilization of your system.
- [green-ai](https://github.com/daviddao/green-ai) - The Green AI Standard aims to develop a standard and raise awareness for best environmental practices in AI research and development.
- [CodeCarbon](https://github.com/mlco2/codecarbon) - Track emissions from Compute and recommend ways to reduce their impact on the environment.
- [Carbonalyser](https://github.com/carbonalyser/Carbonalyser) - Allows to visualize the electricity consumption and greenhouse gases emissions that your Internet browsing leads to.
- [blockchain-carbon-accounting](https://github.com/opentaps/blockchain-carbon-accounting) - Code of the Carbon Accounting and Certification Working Group.
- [footprint](https://github.com/acircleda/footprint) - An R package to calculate carbon footprints from air travel based on IATA airport codes or latitude and longitude.
- [intensegRid](https://github.com/KKulma/intensegRid) - Provides information on national and regional carbon intensity, the amount of carbon emitted per unit of energy consumed, for the UK.
- [Carbonfact Models](https://github.com/kansoapp/carbonfact-models) - The carbon footprint models used by carbonfact.co.
- [CAMx](https://www.camx.com/) - A multi-scale photochemical modeling system for gas and particulate air pollution.
- [Open-Emission-Factors-DB](https://github.com/climatiq/Open-Emission-Factors-DB) - An open access, contributer-led database of emission factors, validated by the team at Climatiq.
- [Let's Wait Awhile](https://github.com/dos-group/lets-wait-awhile) - Simulator and datasets to research on carbon-aware temporal workload shifting.
- [elmada](https://github.com/DrafProject/elmada) - Dynamic electricity carbon emission factors and prices for Europe.
- [Environmental Footprint Data](https://github.com/Boavizta/environmental-footprint-data) - Aims to reference as much data as possible to help organizations to evaluate the environmental footprint of their information systems, applications and digital services.
- [UNFCCC emissions data](https://github.com/openclimatedata/unfccc-detailed-data-by-party) - UNFCCC Emissions data from the Detailed Data By Party interface.
- [Silicone](https://github.com/GranthamImperial/silicone) - Automated filling of detail in reported emission scenarios.


### Carbon Capture and Removel

- [Carbon Dioxide Removal Database](https://github.com/carbonplan/cdr-database) - Open science reports on carbon removal projects and technologies.
- [SimCCS](https://github.com/simccs/SimCCS) - A software platform for carbon capture and storage infrastructure design.
- [FOQUS](https://github.com/CCSI-Toolset/FOQUS) - Framework for Optimization and Quantification of Uncertainty and Surrogates.
- [Carbon Capture and Storage](https://github.com/yohanesnuwara/carbon-capture-and-storage) - This is a complete modeling workflow that integrates reservoir simulation data, rock physics, time-lapse seismic and geomechanics of CO2 injection in carbonate rock. <!--lint ignore awesome-spell-check-->
- [GEOSX](https://github.com/GEOSX/GEOSX) - A simulation framework for modeling coupled flow, transport, and geomechanics in the subsurface.
- [OpenIAM](https://gitlab.com/NRAP/OpenIAM) - An open source integrated assessment model developed by National Risk Assessment Partnership Phase II to facilitate risk assessment, management and containment assurance for geologic carbon sequestration projects.
- [CDRMEx](https://github.com/hsbay/cdrmex) - Carbon Dioxide Removal Modeling Experiments.

### Emission Observation and Modeling

- [Carbon Mapper](https://carbonmapperdata.org/) - Accelerate local climate action globally by locating, quantifying and tracking methane leaks and CO2 point-sources from space.
- [ghg emissions indicator](https://github.com/bcgov/ghg-emissions-indicator) - R scripts for a greenhouse gases emissions indicator published on Environmental Reporting British Columbia.
- [DuMux](https://git.iws.uni-stuttgart.de/dumux-repositories/dumux) - Based on the DUNE framework and aims to provide a multitude of numerical models as well as flexible discretization methods for complex non-linear phenomena, such as CO2 sequestration, soil remediation, drug delivery in cancer therapy and more.
- [oco2peak](https://github.com/dataforgoodfr/batch7_satellite_ges/) - The goal of our project is to localize CO2 emissions on Earth based on the the carbon concentration data measured by the OCO-2 Satellite from NASA.
- [CO2 Emission Datasets](https://www.che-project.eu/data-portal) - The CHE Data Portal provides an interface to the distributed data used and made available through the project, either as input data sets or as resulting data sets.
- [Global Carbon Budget](https://github.com/openclimatedata/global-carbon-budget) - An annual living data publication of carbon cycle sources and sinks, generated from multiple data sources and by multiple organisations and research groups.
- [emissions-api](https://github.com/emissions-api/emissions-api) - A solution that provides simple access to emissions data of climate-relevant gases.
- [eixport](https://github.com/atmoschem/eixport) - An R package that provides functions to read emissions from VEIN and from other models in different formats and export the emissions into the appropriate format suitable to other models.
- [EmissV](https://github.com/atmoschem/EmissV) - This package provides some methods to create emissions (with a focus on vehicular emissions) for use in numeric air quality models such as WRF-Chem.
- [vein](https://gitlab.com/ibarraespinosa/vein) - An R package to estimate Vehicular Emissions INventories.
- [The Community Emissions Data System](https://github.com/JGCRI/CEDS) - Produces consistent estimates of global air emissions species over the industrial era (1750 - present).
- [national-climate-plans](https://github.com/openclimatedata/national-climate-plans) - Intended Nationally Determined Contributions as provided in the UNFCCC registries, containing only the main document and using the English version if multiple are available.
- [PyChEmiss](https://github.com/quishqa/PyChEmiss) - A Python script to create the wrfchemi file from local emissions needed to run WRF-Chem model.
- [co2-data](https://github.com/owid/co2-data) - Data on CO2 and greenhouse gas emissions by Our World in Data.
- [X-STILT](https://github.com/uataq/X-STILT) - An atmospheric transport model that deals with vertically integrated column CO2 and potentially other trace gases.
- [stilt](https://github.com/uataq/stilt) - An open source Lagrangian particle dispersion model which is widely used to simulate the transport of pollution and greenhouse gases through the atmosphere.
- [OPGEE](https://github.com/arbrandt/OPGEE) - Oil Production Greenhouse Gas Emissions Estimator.
- [OpenGHG](https://github.com/openghg) - A cloud platform for greenhouse gas data analysis and collaboration.
- [Open Carbon Watch](https://github.com/OpenCarbonWatch) - We monitor greenhouse gases emission reports published by organizations, along with their legal obligations and their own commitments, and track them over time.
- [Methane-detection-from-hyperspectral-imagery](https://github.com/satish1901/Methane-detection-from-hyperspectral-imagery) - Deep Learning based Remote Sensing Methods for Methane Detection in Airborne Hyperspectral Imagery.
- [Methane Source Finder](https://methane.jpl.nasa.gov/) - Explore, analyze, and download methane plumes detected from airborne platforms on an interactive map alongside VISTA infrastructure, gridded methane estimates, and other additional data layers.
- [deep-smoke-machine](https://github.com/CMU-CREATE-Lab/deep-smoke-machine) - Deep learning models and dataset for recognizing industrial smoke emissions.
- [Ribbit Network Frog Sensor](https://github.com/Ribbit-Network/ribbit-network-frog-sensor) - The sensor for the world's largest crowdsourced network of open-source, low-cost, CO2 Gas Detection Sensors.
- [FIRECAM](https://github.com/tianjialiu/FIRECAM) - An online app for end-users to diagnose and explore regional differences in fire emissions from five global fire emissions inventories.
- [ESTA](https://github.com/mmb-carb/ESTA) - A command-line tool for processing raw emissions data into spatially and temporally-allocated emissions inventories, suitable for photochemicaly modeling or other analysis.
- [FlyingClimate](https://github.com/milankl/FlyingClimate) - Model the CO2 and non-CO2 effects like nitrogen oxide emissions and contrail formation to analyse aviation's total warming footprint.
- [ETS-Watch](https://github.com/OSUKED/ETS-Watch) - Provides a Python client for retrieving the latest data on the EU Emissions Trading System market and its participants.
- [Industrial Smoke Plume Detection](https://github.com/HSG-AIML/IndustrialSmokePlumeDetection) - Characterization of Industrial Smoke Plumes from Remote Sensing Data.
- [EDGAR](https://edgar.jrc.ec.europa.eu/) - Emissions Database for Global Atmospheric Research.
- [OpenGHGMap](https://openghgmap.net/) - A city-level CO2 emissions inventory for Europe.
- [GCP-GridFED](https://zenodo.org/record/3958283) - Gridded fossil CO2 emissions and related O2 combustion consistent with national inventories 1959-2018.
- [Integrated Carbon Observation System](https://github.com/ICOS-Carbon-Portal/pylib) - Produces standardised data on greenhouse gas concentrations in the atmosphere, as well as on carbon fluxes between the atmosphere, the earth and oceans.


## Ecological Footprint

### Life Cycle Assessment

- [exiobase](https://www.exiobase.eu/) - A global and detailed Multi-Regional Environmentally Extended Supply-Use Table (MR-SUT) and Input-Output Table (MR-IOT).
- [bonsai](https://github.com/BONSAMURAIS/bonsai) - The aim of BONSAI is to make reliable, unbiased sustainability information on products (product footprints) readily and freely available whenever and wherever it is needed to support product comparisons and decisions.
- [brightway2](https://github.com/brightway-lca/brightway2) - An open source framework for life cycle assessment.
- [carculator](https://github.com/romainsacchi/carculator) - Prospective environmental and economic life cycle assessment of vehicles made blazing fast.
- [Electricity Life Cycle Inventory](https://github.com/USEPA/ElectricityLCI) - A Python package that uses standardized facility release and generation data to create regionalized life cycle inventory (LCI) models for the generation, mix of generation, mix of consumption, and distribution of electricity to end users for the US, with embedded system processes of upstream fuel production and infrastructure.
- [uslci-content](https://github.com/uslci-admin/uslci-content) - Supplementary content for the U.S. Life Cycle Inventory Database.
- [OpenLCA](https://github.com/GreenDelta/olca-app) - An open source and free software for Sustainability and Life Cycle Assessment.
- [openlca-python-tutorial](https://github.com/GreenDelta/openlca-python-tutorial) - Explains the usage of the openLCA API from Python.
- [Global LCA Data Access Network](https://www.globallcadataaccess.org/) - Gathers life cycle dataset providers and other stakeholders who share the goal of improving sustainability-related decisions through enhanced, interoperable and global access to LCA datasets.
- [BioSTEAM_LCA](https://github.com/scyjth/biosteam_lca) - An agile life cycle assessment platform that enables a fast and flexible evaluation of the life cycle environmental impacts of biorefineries under uncertainty.
- [lca_algebraic](https://github.com/oie-mines-paristech/lca_algebraic) - A small layer above brightway2, designed for the definition of parametric inventories with fast computation of LCA impacts, suitable for Monte Carlo analysis.
- [Federal LCA Commons](https://www.lcacommons.gov/) - A central point of access to a collection of data repositories for use in Life Cycle Assessment.
- [Trase](https://github.com/Vizzuality/trase) - Brings unprecedented transparency to commodity supply chains revealing new pathways towards achieving a deforestation-free economy.
- [QSDsan](https://github.com/QSD-Group/QSDsan) - A package for the quantitative sustainable design of sanitation and resource recovery systems.
- [premise](https://github.com/romainsacchi/premise) - Coupling Integrated Assessment Models output with Life Cycle Assessment.
- [useeior](https://github.com/USEPA/useeior) - Estimating potential environmental impacts of goods and services in the US economy.
- [fedelemflowlist](https://github.com/USEPA/Federal-LCA-Commons-Elementary-Flow-List) - A Python package that generates and provides a standardized elementary flow list for use in life cycle assessment (LCA) data as well as mappings to convert data from other sources.


### Circular Economy and Waste

- [ONEARMY](https://github.com/ONEARMY/precious-plastic) - A series of tools for the Precious Plastic community to collaborate around the world and tackle plastic waste.
- [Trash-ICRA19](https://conservancy.umn.edu/handle/11299/214366) - A Bounding Box Labeled Dataset of Underwater Trash.
- [TACO](https://github.com/pedropro/TACO) - Trash Annotations in Context Dataset Toolkit.
- [circularity.ID Open Data Standard](https://github.com/circularfashion/cf-circularity-id-standard) - The standard represents the results and findings of an extensive six-year research into the needs of stakeholders in the fashion industry to achieve a circular economy.
- [RecycleNet](https://github.com/sangminwoo/RecycleNet) - Effective trash classification model using only a small number of annotated images.
- [trashnet](https://github.com/garythung/trashnet) - Dataset of images of trash. Torch-based CNN for garbage image classification.
- [OpenLitterMap](https://github.com/OpenLitterMap/openlittermap-web) - An open, interactive and accessible database of the world's litter and plastic pollution.
- [Recyclebot](https://www.appropedia.org/Recyclebot) - An open source waste plastic extruder that creates 3D printer filament from waste plastic and natural polymers.
- [pycirk](https://github.com/CMLPlatform/pycirk) - Model Circular Economy policy and technological interventions in Environmentally Extended Input-Output Analysis.
- [Global Plastic Navigator](https://github.com/WWF-Deutschland/marine-plastic-explorer) - Visualises the most recent and high-resolution data of current scientific publications on marine plastic pollution.
- [marine_debris_ML](https://github.com/NASA-IMPACT/marine_debris_ML) - Marine debris detection with commercial satellite imagery and deep learning.
- [ADVECTOR](https://github.com/TheOceanCleanupAlgorithms/ADVECTOR) - A whole-ocean marine debris transport model which is built to handle millions of particles and terabytes of data.
- [Surfrider Plastic Origins](https://github.com/surfriderfoundationeurope/The-Plastic-Origins-Project) - A citizen science project that uses AI to map plastic pollution in European rivers and share its data publicly.
- [MARIDA](https://github.com/marine-debris/marine-debris.github.io) - A marine debris-oriented dataset on Sentinel-2 satellite images.
- [Detect waste](https://github.com/wimlds-trojmiasto/detect-waste) - Detecting plastic waste in the environment to combat environmental pollution and promote circular economy.

## Earth Systems

### Biosphere

- [ECOSTRESS](https://ecostress.jpl.nasa.gov/) - The images acquired by ECOSTRESS are the most detailed temperature images of the surface ever acquired from space and can be used to measure the temperature of an individual farmers field and plants.
- [carbon budget](https://github.com/wri/carbon-budget) - This model maps gross greenhouse gas emissions from forests between 2001 and 2015, gross carbon removals by forests between 2001, and the difference between them (net flux).
- [treeseg](https://github.com/apburt/treeseg/) - Developed to near-automatically extract tree-level point clouds from high-density larger-area lidar point clouds acquired in forests.
- [fgeo](https://github.com/forestgeo/fgeo) - Analyze forest diversity and dynamics.
- [fgeo.biomass](https://github.com/forestgeo/fgeo.biomass) - Calculate biomass with allometric equations from the allodb package and ForestGEO data.
- [BIOMASS](https://github.com/umr-amap/BIOMASS) - An R package for estimating aboveground biomass and its uncertainty in tropical forests.
- [forest](https://github.com/MetOffice/forest) - Forecast and Observation Research and Evaluation Survey Tool.
- [SEPAL](https://github.com/openforis/sepal) - System for Earth Observation Data Access, Processing and Analysis for Land Monitoring.
- [Forest Carbon database](https://github.com/forc-db/ForC) - Global Forest Carbon Database.
- [TreeLS](https://github.com/tiagodc/TreeLS) - High performance R functions for forest data processing based on Terrestrial Laser Scanning (but not only) point clouds.
- [TreeQSM](https://github.com/InverseTampere/TreeQSM) - Quantitative Structure Models of Single Trees from Laser Scanner Data.
- [DeepLidar](https://github.com/weecology/DeepLidar) - Geographic Generalization in Airborne RGB Deep Learning Tree Detection.
- [wildfire forecasting](https://github.com/esowc/wildfire-forecasting) - The project intends to reproduce the Fire Forecasting capabilities of GEFF using Deep Learning and develop further improvements in accuracy, geography and time scale through inclusion of additional variables or optimization of model architecture and hyperparameters.
- [caliver](https://github.com/ecmwf/caliver) - CALIbration and VERification of gridded fire danger models.
- [Global Forest Watch](https://github.com/Vizzuality/gfw) - An online, global and near real-time forest monitoring tool.
- [gfw-mapbuilder](https://github.com/wri/gfw-mapbuilder) - A library to build custom Forest Atlas web applications.
- [taxize](https://github.com/ropensci/taxize) - Allows users to search over many taxonomic data sources for species names (scientific and common) and download up and downstream taxonomic hierarchical information.
- [rgbif](https://github.com/ropensci/rgbif) - Interface to the Global Biodiversity Information Facility API.
- [Global Biotic Interactions](https://github.com/globalbioticinteractions/globalbioticinteractions) - Global Biotic Interactions provides access to existing species interaction datasets.
- [lidR](https://github.com/Jean-Romain/lidR) - An R package for airborne LiDAR data manipulation and visualization for forestry application.
- [Digital Forestry Toolbox](https://github.com/mparkan/Digital-Forestry-Toolbox) - A collection of digital forestry tools for Matlab/Octave.
- [pyfor](https://github.com/brycefrank/pyfor) - Tools for analyzing aerial point clouds of forest data.
- [DeepForest](https://github.com/weecology/DeepForest) - Python Package for Tree Crown Detection in Airborne RGB imagery.
- [pyMETRIC](https://github.com/WSWUP/pymetric) - A set of Python based tools developed for estimating and mapping evapotranspiration for large areas, utilizing the Landsat image archive.
- [NeonTreeEvaluation](https://github.com/weecology/NeonTreeEvaluation) - Benchmark dataset for tree detection for airborne RGB, Hyperspectral and LIDAR imagery.
- [PyCrown](https://github.com/manaakiwhenua/pycrown) - Fast raster-based individual tree segmentation for LiDAR data.
- [canopyLazR](https://github.com/akamoske/canopyLazR) - An R package that estimates leaf area density and leaf area index from airborne LiDAR point clouds.
- [forestlas](https://github.com/philwilkes/forestlas) - Code for generating metrics of forest vertical structure from airborne LiDAR data.
- [OpenTreeMap](https://github.com/OpenTreeMap/otm-core) - A collaborative platform for crowdsourced tree inventory, ecosystem services calculations, urban forestry analysis and community engagement.
- [DeepTreeAttention](https://github.com/weecology/DeepTreeAttention) - Hyperspectral Image Classification with Attention Aided CNNs.
- [rebird](https://github.com/ropensci/rebird) - A package to interface with the eBird webservices a real-time, online bird checklist program.
- [rredlist](https://github.com/ropensci/rredlist) - An R client for the IUCN Red List of threatened and endangered species.
- [OpenSimRoot](https://gitlab.com/rootmodels/OpenSimRoot) - Source code for simulating root architecture, nutrient and water uptake and more.
- [PyETo](https://github.com/woodcrafty/PyETo) - A Python library for calculating reference crop evapotranspiration, sometimes referred to as potential evapotranspiration.
- [burnr](https://github.com/ltrr-arizona-edu/burnr) - Basic tools to analyze forest fire history data (e.g. FHX) in R.
- [forestmangr](https://github.com/sollano/forestmangr) - An R package for forest mensuration and management.
- [CART](https://github.com/jneme910/CART) - The Conservation Assessment Ranking Tool is designed for use in the conservation planning process to assess resource concerns, planned practices and site vulnerability.
- [forest-prediction](https://github.com/DS3Lab/forest-prediction) - Deep learning for deforestation classification and forecasting in satellite imagery.
- [BIRDS](https://github.com/Greensway/BIRDS) - This set of tools has been developed for systematizing biodiversity data review in order to evaluate whether a set of species observation are fit-for-use and help take decisions upon its use on further analysis.
- [PlantCV](https://github.com/danforthcenter/plantcv) - Plant phenotyping using computer vision.
- [FATES](https://github.com/NGEET/fates) - A cohort model of vegetation competition and co-existence, allowing a representation of the biosphere which accounts for the division of the land surface into successional stages.
- [forestatrisk](https://github.com/ghislainv/forestatrisk) - A Python package to model and forecast the risk of deforestation.
- [CRootBox](https://github.com/Plant-Root-Soil-Interactions-Modelling/CRootBox) - The focus of CRootBox is the simulation of different types of root architecture, and to provide a generic interface for coupling with arbitrary soil/environmental models, e.g., in order to determine the impact of specific root architectures on function.
- [Pyrovision](https://github.com/pyronear/pyro-vision) - Computer vision library for wildfire detection.
- [auk](https://github.com/CornellLabofOrnithology/auk) - eBird Data Extraction and Processing in R.
- [spocc](https://github.com/ropensci/spocc) - An R package to query and collect species occurrence data from many sources.
- [VIAME](https://github.com/VIAME/VIAME) - A computer vision application designed for do-it-yourself artificial intelligence including object detection, object tracking, image/video annotation, image/video search, image mosaicing, stereo measurement, rapid model generation, and tools for the evaluation of different algorithms.
- [ecodata](https://github.com/NOAA-EDAB/ecodata) - A data package for reporting on Northeast Continental Shelf ecosystem status and trends.
- [CODED](https://github.com/bullocke/coded) - An algorithm developed to monitor for low-magnitude forest disturbances using Landsat data.
- [OpenPlantPathology](https://github.com/openplantpathology/OpenPlantPathology) - Open Plant Pathology is an initiative that supports and promotes the spread of all open, transparent and reproducible practices in the field of plant pathology.
- [palmerpenguins](https://github.com/allisonhorst/palmerpenguins/) - The palmerpenguins data contains size measurements for three penguin species observed on three islands in the Palmer Archipelago, Antarctica.
- [robis](https://github.com/iobis/robis/) - Build and maintain a global alliance that collaborates with scientific communities to facilitate free and open access to, and application of, biodiversity and biogeographic data and information on marine life.
- [rfishbase](https://github.com/ropensci/rfishbase) - An R interface to the fishbase.org database.
- [PCSE](https://github.com/ajwdewit/pcse) - A framework developed for implementing crop simulation models developed in Wageningen.
- [Deep Plant Phenomics](https://github.com/p2irc/deepplantphenomics) - A platform for plant phenotyping using deep learning.
- [PlanktonIndividuals.jl](https://github.com/JuliaOcean/PlanktonIndividuals.jl) - This package simulates the behaviors of an ensemble of phytoplankton individuals.
- [redlistr](https://github.com/red-list-ecosystem/redlistr) - An R package that contains a set of tools suitable for calculating the metrics required for making assessments of species and ecosystems against the IUCN Red List of Threatened Species and the IUCN Red List of Ecosystems categories and criteria.
- [ALA4R](https://github.com/AtlasOfLivingAustralia/ALA4R) - The Atlas of Living Australia provides tools to enable users of biodiversity information to find, access, combine and visualise data on Australian plants and animals.
- [worldpa](https://github.com/FRBCesab/worldpa) - R interface to the World Database on Protected Areas.
- [pywdpa](https://github.com/ghislainv/pywdpa) - Python interface to the World Database on Protected Areas.
- [plant](https://github.com/traitecoevo/plant) - A package for modeling forest trait ecology and evolution.
- [PNVmaps](https://github.com/Envirometrix/PNVmaps) - Global Maps of Potential Natural Vegetation based on Machine Learning.
- [monitoring-ecosystem-resilience](https://github.com/alan-turing-institute/monitoring-ecosystem-resilience) - The focus is understanding vegetation patterns in semi-arid environments.
- [UVic-updates-opem](https://git.geomar.de/markus-pahlow/UVic-updates-opem) - Introduces optimality-based phytoplankton and zooplankton into the UVic-ESCM (version 2.9) with variable C:N:P(:Chl) stoichiometry for phytoplankton, diazotrophs and detritus.
- [Quantitative Plant](https://www.quantitative-plant.org/) - A website presenting image analysis software tools and models for plants.
- [phenocamr](https://github.com/bluegreen-labs/phenocamr) - Facilitates the retrieval and post-processing of PhenoCam time series.
- [OceanAdapt](https://github.com/pinskylab/OceanAdapt) - Provide information about the impacts of changing climate and other factors on the distribution of marine life to the National Climate Assessment, fisheries communities, policymakers, and to others.
- [Global Reforestation Opportunity Assessment](https://github.com/forc-db/GROA) - Quantify carbon sequestration in naturally regenerating forests around the world.
- [Plant-for-the-Planet](https://github.com/Plant-for-the-Planet-org/treecounter-app) - Allows you to plant trees with over 100 reforestation projects around the world.
- [Annotation Interface for Data-driven Ecology](https://github.com/microsoft/aerial_wildlife_detection) - Tools for detecting wildlife in aerial images using active learning.
- [Pyronear Risks](https://github.com/pyronear/pyro-risks) - The pyro-risks project aims at providing the pyronear-platform with a machine learning based wildfire forecasting capability.
- [Tree Mapper App](https://github.com/Plant-for-the-Planet-org/treemapper) - Tree Mapper extends the Plant-for-the-Planet App and allows on site coordinate submission during plantation.
- [biodivMapR](https://github.com/jbferet/biodivMapR) - An R package for α- and β-diversity mapping using remotely-sensed images.
- [Continuous Reforestation](https://github.com/protontypes/continuous-reforestation) - A GitHub Action for planting trees within your development workflow using the Reforestation as a Service (RaaS) API developed by DigitalHumani.
- [DiversiTree](https://github.com/DiversiTree/TreeDiversity) - Help urban foresters, planners, greeners, and ecologists in quantifying tree ecosystem diversity in cities.
- [forestatrisk](https://github.com/ghislainv/forestatrisk-tropics) - Forest refuge areas and carbon emissions from tropical deforestation in the 21st century.
- [DetecTree](https://github.com/martibosch/detectree) - A Pythonic library to classify tree/non-tree pixels from aerial imagery.
- [Sentinel-Tree-Cover](https://github.com/wri/sentinel-tree-cover) - This project maps tree extent at the ten-meter scale using open source artificial intelligence and satellite imagery.
- [Bioverse Labs](https://github.com/Bioverse-Labs/deep-learning) - Python scripts using usual frameworks in Deep Learning for pattern recognition on forest environments.
- [Tree Tracker](https://github.com/protect-earth/TreeTracker) - Used by people who plant trees so they don't have to manually type coordinates with pictures they took.
- [forest-risks](https://github.com/carbonplan/forest-risks) - Statistical models of forest carbon potential and risks.
- [rGEDI](https://github.com/carlos-alberto-silva/rGEDI) - An R Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) Data Visualization and Processing.
- [Wildfire Predictive Services](https://github.com/bcgov/wps) - Wildfire Predictive Services to support decision making in prevention, preparedness, response and recovery.
- [detectreeRGB](https://github.com/shmh40/detectreeRGB) - Tree crown delineation from RGB imagery, coupled with methods to delineate tree crowns from LiDAR data.
- [FSDL Deforestation Detection](https://github.com/karthikraja95/fsdl_deforestation_detection) - A deep learning approach to detecting deforestation risk, using satellite images and a deep learning model.
- [ForesToolboxRS](https://github.com/ytarazona/ForesToolboxRS) - Remote Sensing Tools for Forest Monitoring.
- [Gieß den Kiez](https://github.com/technologiestiftung/giessdenkiez-de) - Enable coordinated citizen participation in the irrigation of urban trees.
- [mobr](https://github.com/MoBiodiv/mobr) - Tools for analyzing changes in biodiversity across scales.
- [Forest Structural Complexity Tool](https://github.com/SKrisanski/FSCT) - Allowing plot scale measurements to be extracted automatically from most high-resolution forest point clouds from a variety of sensor sources.
- [Global ECMWF Fire Forecasting](https://git.ecmwf.int/projects/CEMSF/repos/geff/browse) - The model is a Fortran program to calculate fire danger indices from atmospheric inputs.
- [MAAP](https://github.com/MAAP-Project/maap-documentation) - Discover and use biomass relevant data, integrating the data for comparison, analysis, evaluation, and generation.
- [DynACof](https://github.com/VEZY/DynACof) - Process-based model computes plot-scale Net Primary Productivity, carbon allocation, growth, yield, energy, and water balance of coffee plantations according to management.
- [EU forest tree point data](https://gitlab.com/openlandmap/eu-forest-tree-point-data) - A compilation of analysis-ready point data for the purpose of vegetation and Potential Natural Vegetation mapping for the EU. 
- [iNaturalist](https://github.com/inaturalist/inaturalist) - Helps you identify the plants and animals around you.
- [Wildbook](https://github.com/WildMeOrg/Wildbook) - Blends structured wildlife research with artificial intelligence, citizen science, and computer vision to speed population analysis and develop new insights to help fight extinction.
- [Forest Scenario Planner](https://github.com/Ecotrust/forestplanner) - An online tool for forest management scenario planning.
- [PEcAn](https://github.com/PecanProject/pecan) - The Predictive Ecosystem Analyzer is an integrated ecological bioinformatics toolbox.
- [spanner](https://github.com/bi0m3trics/spanner) - Utilities to support landscape-, forest-, and tree-related data collection, manipulation, analysis, modelling, and visualization. 
- [Treetracker](https://github.com/Greenstand/treetracker-android) - Coordinates the digital capture of tree growth data in the field, allowing to establish employment for people living in extreme poverty based on tree planting.
- [ForestTools](https://github.com/andrew-plowright/ForestTools) - Detect and segment individual tree from remotely sensed data.
- [gfcanalysis](https://github.com/azvoleff/gfcanalysis) - Tools for working with Global Forest Change dataset.
- [FIREDpy](https://github.com/earthlab/firedpy) - Classifying fire events from the Collection 6 MODIS Burned Area Product.
- [BioPAL](https://github.com/BioPAL/BioPAL) - The BIOMASS Product Algorithm Laboratory hosts official tools for processing and analysing ESA's BIOMASS mission data.
- [phenofit](https://github.com/eco-hydro/phenofit/) - A state-of-the-art remote sensing vegetation phenology extraction package.
- [rnpn](https://github.com/usa-npn/rnpn) - R client for interacting with the USA National Phenology Network data web services.
- [California Forest Observatory](https://github.com/forestobservatory/cfo-api) - Python wrappers for accessing Forest Observatory data via the Salo API.


### Cryosphere

- [Planet Snowcover](https://github.com/acannistra/planet-snowcover) - A project that pairs airborne lidar and Planet Labs satellite imagery with cutting-edge computer vision techniques to identify snow-covered area at unprecedented spatial and temporal resolutions.
- [Sea ice drift](https://github.com/nansencenter/sea_ice_drift) - Sea ice drift from Sentinel-1 SAR imagery using open source feature tracking.
- [smrt](https://github.com/smrt-model/smrt) - Snow Microwave Radiative Transfer model to compute thermal emission and backscatter from snowpack.
- [OGGM](https://github.com/OGGM/oggm) - A modular open source model for glacier dynamics.
- [CICE](https://github.com/CICE-Consortium/CICE) - A computationally efficient model for simulating the growth, melting, and movement of polar sea ice.
- [PISM](https://github.com/pism/pism) - The Parallel Ice Sheet Model is an open source, parallel, high-resolution ice sheet model.
- [icepack](https://github.com/CICE-Consortium/Icepack) - Finite element modeling of glaciers and ice sheets.
- [DeepBedMap](https://github.com/weiji14/deepbedmap) - Using a deep neural network to better resolve the bed topography of Antarctica.
- [OSSP](https://github.com/wrightni/OSSP) - Open Source Algorithm for Detecting Sea Ice Surface Features in High Resolution Optical Imagery.
- [captoolkit](https://github.com/fspaolo/captoolkit) - NASA's Cryosphere Altimetry Processing Toolkit.
- [sea-ice](https://github.com/vannizhang/sea-ice) - Displays the monthly mean sea ice extent for the Arctic and Antarctic along with the historical median extent.
- [SIS2](https://github.com/NOAA-GFDL/SIS2) - Calculates the concentration, thickness, temperature, brine content and snow cover of an arbitrary number of ice thickness categories (including open water) as well as the motion of the complete pack.
- [FSM2](https://github.com/RichardEssery/FSM2) - The Flexible Snow Model is a multi-physics energy balance model of snow accumulation and melt, extending the Factorial Snow Model (Essery, 2015) with additional physics, driving and output options.
- [freshwater](https://github.com/GEUS-PROMICE/freshwater) - Greenland liquid water runoff from 1958 through 2019.
- [PyTrx](https://github.com/PennyHow/PyTrx) - Its primary purpose is to obtain velocities, surface areas, and distances from oblique, optical imagery of glacial environments.
- [ECCO-v4-Python-Tutorial](https://github.com/ECCO-GROUP/ECCO-v4-Python-Tutorial) - Contains several tutorials for using the ECCO Central Production Version 4 ocean and sea-ice state estimate.
- [icepyx](https://github.com/icesat2py/icepyx) - Python tools for obtaining and working with ICESat-2 data.
- [BedMachine](https://github.com/chadagreene/BedMachine) - Matlab tools for loading, interpolating, and displaying BedMachine ice sheet topography.
- [Iceberg Locations](https://github.com/Joel-hanson/Iceberg-locations) - Antarctic large iceberg positions derived from ASCAT and OSCAT-2.
- [GlaThiDa](https://gitlab.com/wgms/glathida) - Glacier Thickness Database.
- [SICOPOLIS](https://gitlab.awi.de/sicopolis/sicopolis) - A 3-d dynamic/thermodynamic model that simulates the evolution of large ice sheets and ice caps.
- [ALPGM](https://github.com/JordiBolibar/ALPGM) - Regional glacier evolution model based on deep learning and parametrizations.
- [Glacier Mapping From Satellite Imagery](https://github.com/krisrs1128/glacier_mapping) - Use computer vision to automatically segment debris and ice glaciers from satellite images.
- [DeepIceDrain](https://github.com/weiji14/deepicedrain) - Mapping and monitoring deep subglacial water activity in Antarctica using remote sensing and machine learning.
- [cosipy](https://github.com/cryotools/cosipy) - Solves the energy balance at the surface and is coupled to an adaptive vertical multi-layer subsurface module.
- [QGreenland](https://github.com/nsidc/qgreenland) - A free mapping tool to support interdisciplinary Greenland-focused research, teaching, decision making, and collaboration.


### Hydrosphere

- [Raven](https://github.com/Ouranosinc/raven) - Made to help scientists run hydrological modeling experiments with climate change projections.
- [NEMO](https://www.nemo-ocean.eu/) - A state-of-the-art modeling framework for research activities and forecasting services in ocean and climate sciences, developed in a sustainable way by a European consortium.
- [Bergen Layered Ocean Model](https://github.com/NorESMhub/BLOM) - Employs an isopycnic vertical coordinate, with near-isopycnic interior layers and variable density layers in the surface mixed boundary layer.
- [Oceananigans.jl](https://github.com/CliMA/Oceananigans.jl) - Fast and friendly fluid dynamics on CPUs and GPUs.
- [NEMO](https://forge.ipsl.jussieu.fr/nemo/wiki/Users) - Nucleus for European Modelling of the Ocean is a state-of-the-art modeling framework for research activities and forecasting services in ocean and climate sciences, developed in a sustainable way by a European consortium since 2008.
- [LESbrary.jl](https://github.com/CliMA/LESbrary.jl) - Generating a library of ocean turbulence large eddy simulation data to train ocean and climate models.
- [GOLD](https://code.google.com/archive/p/gold-omod/) - Stands for Generalized Ocean Layer Dynamics and is a hybrid coordinate finite volume ocean model code funded by NOAA and developed by the ocean group at NOAA-GFDL and Princeton University.
- [rrricanes](https://github.com/ropensci/rrricanes) - An R library that extracts information from Atlantic and east Pacific hurricanes and tropical storms.
- [hydroscoper](https://github.com/ropensci/hydroscoper) - An R interface to the Greek National Data Bank for Hydrometeorological Information.
- [OpenDrift](https://github.com/OpenDrift/opendrift) - A software for modeling the trajectories and fate of objects or substances drifting in the ocean, or even in the atmosphere.
- [OceanSpy](https://github.com/hainegroup/oceanspy) - An open source and user-friendly Python package that enables scientists and interested amateurs to analyze and visualize ocean model datasets.
- [Iris](https://github.com/SciTools/iris) - A powerful, format-agnostic, community-driven Python package for analyzing and visualizing Earth science data.
- [Veros](https://github.com/team-ocean/veros) - Powerful tool that makes high-performance ocean modeling approachable and fun.
- [oce](https://github.com/dankelley/oce) - An R package for oceanographic processing.
- [podaacpy](https://github.com/nasa/podaacpy) - A Python utility library for interacting with NASA JPL's Physical Oceanography Distributed Active Archive Center.
- [Ocean-Data-Map-Project](https://github.com/DFO-Ocean-Navigator/Ocean-Data-Map-Project) - A Data Visualization tool that enables users to discover and view 3D ocean model output quickly and easily.
- [marineHeatWaves](https://github.com/ecjoliver/marineHeatWaves) - A module for Python which implements the Marine Heatwave definition of Hobday et al. (2016).
- [heatwaveR](https://github.com/robwschlegel/heatwaveR) - Contains the original functions from the RmarineHeatWaves package that calculate and display marine heatwaves according to the definition of Hobday et al. (2016).
- [MITgcm](https://github.com/MITgcm/MITgcm) - A flexible non-hydrostatic formulation that efficiently simulates fluid phenomena over a wide range of scales.
- [VAPOR](https://github.com/NCAR/VAPOR) - The Visualization and Analysis Platform for Ocean, Atmosphere and Solar Researchers.
- [CoralNet](https://github.com/beijbom/coralnet) - A repository and resource for benthic image analysis.
- [Ferret](https://github.com/NOAA-PMEL/Ferret) - An interactive computer visualization and analysis environment designed to meet the needs of oceanographers and meteorologists analyzing large and complex gridded datasets.
- [ccpp-physics](https://github.com/NCAR/ccpp-physics) - The Common Community Physics Package is designed to facilitate the implementation of physics innovations in state-of-the-art atmospheric models, the use of various models to develop physics, and the acceleration of transition of physics innovations to operational NOAA models.
- [rnoaa](https://github.com/ropensci/rnoaa) - An R interface to many National Oceanic and Atmospheric Administration data sources.
- [parcels](https://github.com/OceanParcels/parcels) - Can be used to track passive and active particulates such as water, plankton, plastic and fish.
- [MOHID-Lagrangian](https://github.com/Mohid-Water-Modelling-System/MOHID-Lagrangian) - Mainly developed for oceanographic and fluvial modeling, application to atmospheric and other planetary settings should be trivial.
- [Mohid](https://github.com/Mohid-Water-Modelling-System/Mohid) - A modular finite volumes water-modeling system written in ANSI-Fortran95 using an Object-oriented programming philosophy, integrating diverse mathematical models and supporting graphical user interfaces that manage all the pre- and post-processing.
- [AIBECS.jl](https://github.com/JuliaOcean/AIBECS.jl) - A Julia package that provides ocean biogeochemistry modelers with an easy-to-use interface for creating and running models of the ocean system.
- [CDFTOOLS](https://github.com/meom-group/CDFTOOLS) - A Fortran package for analysis and diagnostics on NEMO ocean model output.
- [GOTM](https://github.com/gotm-model/code) - The General Ocean Turbulence Model is an ambitious name for a one-dimensional water column model for marine and limnological applications.
- [pyroms](https://github.com/ESMG/pyroms) - A collection of tools to process input and output files from the Regional Ocean Modeling System.
- [Intro to Physical Oceanography](https://github.com/rabernat/intro_to_physical_oceanography) - Course materials for Introduction to Physical Oceanography.
- [TSG-QC](https://git.outils-is.ird.fr/grelet/TSG-QC) - Analysis and validation of underway Sea Surface Temperature and Sea Surface Salinity measurements from a SeaBird Thermosalinograph.
- [WRF-Hydro](https://github.com/NCAR/wrf_hydro_nwm_public) - A community modeling system and framework for hydrologic modeling and model coupling.
- [rwrfhydro](https://github.com/NCAR/rwrfhydro) - A community-contributed tool box for managing, analyzing, and visualizing WRF Hydro (and HydroDART) input and output files in R.
- [PCR-GLOBWB_model](https://github.com/UU-Hydro/PCR-GLOBWB_model) - A large-scale hydrological model intended for global to regional studies.
- [HydroShare](https://github.com/hydroshare/hydroshare) - A collaborative website for better access to data and models in the hydrologic sciences.
- [SOILWAT2](https://github.com/DrylandEcology/SOILWAT2) - An ecosystem water balance simulation model.
- [dorado](https://github.com/passaH2O/dorado) - Simulating passive Lagrangian particle transport over flow-fields from any 2D shallow-water hydrodynamic model using a weighted random walk methodology.
- [Blueant](https://github.com/AustralianAntarcticDivision/blueant) - Environmental data for Antarctic and Southern Ocean science.
- [CO2SYS](https://github.com/jamesorr/CO2SYS-MATLAB) -  A MATLAB (or Octave) project to compute variables of ocean CO2 systems.
- [mocsy](https://github.com/jamesorr/mocsy) - Routines to model ocean carbonate system thermodynamics.
- [seacarb](https://github.com/jpgattuso/seacarb-git) - An R package that calculates various parameters of the carbonate system in seawater.
- [RivGraph](https://github.com/jonschwenk/RivGraph) - Extracting and quantifying graphical representations of river and delta channel networks from binary masks.
- [noaa_coops](https://github.com/GClunies/noaa_coops) -  A Python wrapper for the NOAA CO-OPS Tides & Currents Data and Metadata APIs.
- [COSIMA](https://github.com/COSIMA/cosima-cookbook) - Ocean and sea-ice model analysis tools and examples.
- [WaterDetect](https://github.com/cordmaur/WaterDetect) - End-to-end algorithm to generate open water cover mask, specially conceived for L2A Sentinel 2 imagery from MAJA1 processor, without any a priori knowledge on the scene.
- [FLAREr](https://github.com/FLARE-forecast/FLAREr) - Flexible, scalable, robust, and near-real time iterative ecological forecasts in lakes and reservoirs.
- [HyRiver](https://github.com/cheginit/HyRiver) - A Python software stack for retrieving hydroclimate data from web services.
- [Buhayra](https://github.com/jmigueldelgado/buhayra) - Obtaining water extent of small reservoirs in semi-arid regions from satellite data in real-time.
- [Wflow](https://github.com/Deltares/Wflow.jl) - A Julia package that provides a hydrological modeling framework, as well as several different vertical and lateral concepts that can be used to run hydrological simulations.
- [ParFlow](https://github.com/parflow/parflow) - An open-source, modular, parallel watershed flow model. 
- [River Runner](https://github.com/sdl60660/river-runner) - Visualize the path of a rain droplet from any point in the contiguous United States to its end point.
- [visGWDB](https://code.usgs.gov/map/gw/visGWDBmrva) - A framework for groundwater-level informatics.
- [LakePy](https://github.com/ESIPFed/LakePy) - Pythonic user-centered front-end to the Global Lake Level Database.
- [rivr](https://github.com/mkoohafkan/rivr) - Designed as an educational tool for students and instructors of undergraduate and graduate courses in open channel hydraulics.
- [Aqualink](https://github.com/aqualinkorg/aqualink-app) - A philanthropically funded system to help people manage their local marine ecosystems in the face of increasing Ocean temperatures.
- [argopy](https://github.com/euroargodev/argopy) - A global network of nearly 4000 autonomous probes measuring pressure, temperature and salinity from the surface to 2000m depth every 10 days.
- [eWaterCycle](https://github.com/eWaterCycle/ewatercycle) - Makes it easier to use hydrological models without having intimate knowledge about how to install and run the models.
- [RHESSys](https://github.com/RHESSys/RHESSys) - The Regional Hydro-Ecologic Simulation System.
- [tidyhydat](https://github.com/ropensci/tidyhydat) - An R package to import Water Survey of Canada hydrometric data and make it tidy.
- [PyCO2SYS](https://github.com/mvdh7/PyCO2SYS) - Marine carbonate system calculations in Python.
- [Pastas](https://github.com/pastas/pastas) - An open-source Python framework for the analysis of groundwater time series.
- [river-dl](https://github.com/USGS-R/river-dl) - Deep learning model for predicting environmental variables on river systems.
- [VIC](https://github.com/UW-Hydro/VIC) - A macroscale hydrologic model that solves full water and energy balances.
- [Badlands](https://github.com/badlands-model/badlands) - Basin and Landscape Dynamics is a long-term surface evolution model built to simulate landscape development, sediment transport and sedimentary basins formation from upstream regions down to marine environments.
- [qgs](https://github.com/Climdyn/qgs) - Models the dynamics of a 2-layer quasi-geostrophic channel atmosphere on a beta-plane, coupled to a simple land or shallow-water ocean component.
- [leaflet-velocity](https://github.com/danwild/leaflet-velocity) - Create a canvas visualization layer for direction and intensity of arbitrary velocities (e.g. wind, ocean current).


### Atmosphere

- [pyglow](https://github.com/timduly4/pyglow) - A Python module that wraps several upper atmosphere climatological models written in FORTRAN.
- [OasisPiWind](https://github.com/OasisLMF/OasisPiWind) - PiWind is a wind storm model for a small area of the UK.
- [Massive-Parallel Trajectory Calculations](https://github.com/slcs-jsc/mptrac) - A Lagrangian particle dispersion model for the analysis of atmospheric transport processes in the free troposphere and stratosphere.
- [ICAR](https://github.com/NCAR/icar) - A simplified atmospheric model designed primarily for climate downscaling, atmospheric sensitivity tests, and hopefully educational uses.
- [splitr](https://github.com/rich-iannone/splitr) - We can determine, from one or more receptor sites, where arriving air masses originated.
- [PyCHAM](https://github.com/simonom/PyCHAM) - CHemistry with Aerosol Microphysics in Python box model for Windows, Linux and Mac.
- [maja](https://github.com/CNES/MAJA) - An atmospheric correction and cloud screening software.
- [Mission Support System](https://github.com/Open-MSS/MSS) - A collaboration server to plan atmospheric research flights.
- [MiMA](https://github.com/mjucker/MiMA) - Model of an idealized Moist Atmosphere: Intermediate-complexity General Circulation Model with full radiation.
- [lowtran](https://github.com/space-physics/lowtran) - Atmospheric absorption extinction, scatter and irradiance model in Python and Matlab.
- [Elefridge.jl](https://github.com/esowc/Elefridge.jl) - Compressing atmospheric data into its real information.
- [MetPy](https://github.com/Unidata/MetPy) - A collection of tools in Python for reading, visualizing and performing calculations with weather data.
- [Isca](https://github.com/ExeClim/Isca) - A framework for the idealized modeling of the global circulation of planetary atmospheres at varying levels of complexity and realism.
- [FluxEngine](https://github.com/oceanflux-ghg/FluxEngine) - An open source atmosphere ocean gas flux data processing toolbox.
- [eeweather](https://github.com/openeemeter/eeweather) - Fetch NCDC ISD, TMY3, or CZ2010 weather data that corresponds to ZIP Code Tabulation Areas or Latitude/Longitude.
- [GRAL](https://github.com/GralDispersionModel/GRAL) - Provides a CFD model for the flow calculation around buildings or micrsocale terrain structures.
- [Chemical Lagrangian Model of the Stratosphere](https://jugit.fz-juelich.de/clams/CLaMS) - A world leader in simulating exchange processes in the atmosphere across transport barriers such as stratosphere-troposphere exchange.
- [GEOS-Chem](https://github.com/geoschem/geos-chem) - Advance understanding of human and natural influences on the environment through a comprehensive, state-of-the-science, readily accessible global model of atmospheric composition.
- [mHM](https://git.ufz.de/mhm/mhm) - The mesoscale Hydrological Model.
- [PyBox](https://github.com/loftytopping/PyBox) - A Python based box-model generator and simulator designed for atmospheric chemistry and aerosol studies.
- [SCREAM](https://github.com/E3SM-Project/scream) - A global atmosphere model targeted towards 3 km ("cloud resolving") resolution.
- [RRTMGP.jl](https://github.com/CliMA/RRTMGP.jl) - A Julia implementation of Rapid and accurate Radiative Transfer Model for General Circulation Models.
- [met.3D](https://gitlab.com/wxmetvis/met.3d) - Interactive three-dimensional visualization of numerical ensemble weather predictions and similar numerical atmospheric model datasets.
- [pyvortex](https://github.com/pankajkarman/pyvortex) - Equivalent Latitude and polar vortex edge calculation using Nash criteria.
- [gcpy](https://github.com/geoschem/gcpy) - A Python-based toolkit containing useful functions for working specifically with the GEOS-Chem model of atmospheric chemistry and composition.

## Climate and Earth Science

### Earth and Climate Modeling 
- [ESMValTool](https://github.com/ESMValGroup/ESMValTool) - A community diagnostic and performance metrics tool for routine evaluation of Earth system models in World Climate Research Programme.
- [The Flexible Modeling System](https://github.com/NOAA-GFDL/FMS) - A software framework for supporting the efficient development, construction, execution, and scientific interpretation of atmospheric, oceanic, and climate system models.
- [global-workflow](https://github.com/NOAA-EMC/global-workflow) - Global Superstructure/Workflow currently supporting the Finite-Volume on a Cubed-Sphere Global Forecast System.
- [sedproxy](https://github.com/EarthSystemDiagnostics/sedproxy) - An R package for modeling sediment archived climate proxy records.
- [pangeo](https://github.com/pangeo-data/pangeo) - A community platform for Big Data geoscience.
- [CMEPS](https://github.com/ESCOMP/CMEPS) - The Community Mediator for Earth Prediction Systems (CMEPS) is a NUOPC-compliant Mediator component used for coupling Earth system model component.
- [E3SM](https://github.com/E3SM-Project/E3SM) - A state-of-the-art fully coupled model of the Earth's climate including important biogeochemical and cryospheric processes.
- [E3SM Diagnostics Package](https://github.com/E3SM-Project/e3sm_diags) - Diagnostics package constructed for supporting the diagnostics task of DOE's Energy Exascale Earth System Model (E3SM) project.
- [MDTF-diagnostics](https://github.com/NOAA-GFDL/MDTF-diagnostics) - Analysis framework and collection of process-oriented diagnostics for weather and climate simulations.
- [The Community Earth System Model](https://github.com/ESCOMP/CESM) - Composed of separate models simultaneously simulating the Earth's atmosphere, ocean, land, river run-off, land-ice, and sea-ice, plus one central coupler/moderator component, it allows researchers to conduct fundamental research into the Earth's past, present, and future climate states.
- [ClimateBase.jl](https://github.com/JuliaClimate/ClimateBase.jl) - A Julia package offering basic functionality for analyzing data that are typically in the form used by climate sciences.
- [CLIMA-Land](https://github.com/CliMA/Land) - Everything within the Land model (Soil Plant Atmosphere Module, Land Hydrology, etc).
- [TECA](https://github.com/LBL-EESA/TECA) - The Toolkit for Extreme Climate Analysis, contains a collection of climate anlysis algorithms targetted at extreme event detection and analysis.
- [Climate_Indices](https://github.com/monocongo/climate_indices) - Contains Python implementations of various climate index algorithms which provide a geographical and temporal picture of the severity of precipitation and temperature anomalies useful for climate monitoring and research.
- [The Global Environmental Multiscale Model](https://gitlab.com/eccc/gem/gem) - An integrated forecasting and data assimilation system developed by the Atmospheric Numerical Prediction Research Section, Meteorological Research Division, of Environment and Climate Change Canada.
- [ClimateMachine.jl](https://github.com/CliMA/ClimateMachine.jl) - Climate Machine: an Earth System Model that automatically learns from data.
- [atlas](https://github.com/ecmwf/atlas) - A library for numerical weather prediction and climate modeling.
- [MOM6](https://github.com/NOAA-GFDL/MOM6) - A numerical representation of the ocean fluid with applications from the process scale to the planetary circulation scale.
- [MOM5](https://github.com/mom-ocean/MOM5) - A numerical ocean model based on the hydrostatic primitive equations. Development of the model is managed through this GitHub site.
- [CMIP6 Datasets](https://pcmdi.github.io/CMIP6/) - Provides an access to the outputs of the current phase 6 of the Coupled Model Intercomparison Project (CMIP). CMIP6 global climate models give a base to (almost) all we may know for the climate of the future.
- [hector](https://github.com/JGCRI/hector) - An open source, object-oriented, simple global climate carbon-cycle model.
- [pyhector](https://github.com/openclimatedata/pyhector) - A Python interface for the simple global climate carbon-cycle model Hector.
- [NorESM](https://github.com/NorESMhub/NorESM) - Norwegian Earth System Model and Documentation.
- [CliMT](https://github.com/CliMT/climt) - A Toolkit for building Earth system models in Python.
- [climlab](https://github.com/brian-rose/climlab) - A Python package for process-oriented climate modeling.
- [FAIR](https://github.com/OMS-NetZero/FAIR) - Finite Amplitude Impulse-Response simple climate-carbon-cycle model.
- [CLIMADA](https://github.com/CLIMADA-project/climada_python) - Stands for CLIMate ADAptation and is a probabilistic natural catastrophe impact model, that also calculates averted damage (benefit) thanks to adaptation measures of any kind (from grey to green infrastructure, behavioural, etc.).
- [ClimateMARGO.jl](https://github.com/ClimateMARGO/ClimateMARGO.jl) - A Julia implementation of MARGO, an idealized framework for optimization of climate change control strategies.
- [ClimateTools.jl](https://github.com/JuliaClimate/ClimateTools.jl) - A collection of commonly-used tools in climate science. Basics of climate field analysis are covered, with some forays into exploratory techniques associated with climate scenarios design.
- [MetSim](https://github.com/UW-Hydro/MetSim) - A meteorological simulator and forcing disaggregator for hydrologic modeling and climate applications.
- [ESMF](https://github.com/esmf-org/esmf) - The Earth System Modeling Framework is a suite of software tools for developing high-performance, multi-component Earth science modeling applications.
- [RegESM](https://github.com/uturuncoglu/RegESM) - Regional Earth System Model is designed to be a state-of-art coupled modeling system that allows using variety of different earth system model components as well as their integration with co-processing tool.
- [gis4wrf](https://github.com/GIS4WRF/gis4wrf) - A free and open source QGIS plug-in to help researchers and practitioners with their Advanced Research Weather Research and Forecasting modeling workflows.
- [MPAS](https://github.com/MPAS-Dev/MPAS-Model) - The Model for Prediction Across Scales is a collaborative project for developing atmosphere, ocean, and other earth-system simulation components for use in climate, regional climate, and weather studies.
- [pymt](https://github.com/csdms/pymt) - A Python toolkit for running and coupling Earth surface models.
- [Dragonfly for Grasshopper](https://github.com/ladybug-tools/dragonfly-legacy) - Legacy dragonfly plugin for large-scale climate and urban heat island modeling.
- [pyOSOAA](https://github.com/fnemina/pyOSOAA) - A python interface for the Ocean Successive Orders with Atmosphere radiative transfer.
- [ECRAD](https://github.com/ecmwf/ecrad) - A radiation scheme suitable for use in atmospheric weather and climate models.
- [ClimateModels.jl](https://github.com/gaelforget/ClimateModels.jl) - Uniform interface to climate models of varying complexity and completeness.
- [cmip56_forcing_feedback_ecs](https://github.com/mzelinka/cmip56_forcing_feedback_ecs) - Effective climate sensitivity, effective 2xCO2 radiative forcing, and radiative feedbacks for all CMIP5 and CMIP6 models that have published output from abrupt CO2 quadrupling experiments.
- [ECMWF Reanalyses](https://www.ecmwf.int/en/forecasts/datasets/browse-reanalysis-datasets) - A collection of reanalysis datasets produced the European Centre for Medium-Range Weather Forecasts (ERA family).
- [hn2016_falwa](https://github.com/csyhuang/hn2016_falwa) - A Python library for computing Finite-Amplitude Local Wave Activity from climate data.
- [climpred](https://github.com/pangeo-data/climpred) - Aims to be the primary package used to analyze output from initialized dynamical forecast models, ranging from short-term weather forecasts to long-term climate forecasts.
- [downscaleR](https://github.com/SantanderMetGroup/downscaleR) - An R package for empirical-statistical downscaling focusing on daily data and covering the most popular approaches (bias correction, Model Output Statistics, Perfect Prognosis) and techniques (e.g. quantile mapping, regression, analogs, neural networks).
- [DeepDownscaling](https://github.com/SantanderMetGroup/DeepDownscaling) - Deep learning approaches for statistical downscaling in climate.
- [Pymagicc](https://github.com/openscm/pymagicc) - A Python wrapper around the reduced complexity climate model. 
- [climateforcing](https://github.com/chrisroadmap/climateforcing) - An incomplete toolbox of scripts and modules used for analysis of climate models and climate data.
- [xgcm](https://github.com/xgcm/xgcm) - A Python package for analyzing general circulation model output data.
- [MPAS-Analysis](https://github.com/MPAS-Dev/MPAS-Analysis) - Provides analysis for the MPAS components of ACME.


### Radiative Transfer
- [RadiativeTransfer.jl](https://github.com/RadiativeTransfer/RadiativeTransfer.jl) - A full end-to-end modular software suite for radiative transfer and related atmospheric analysis.
- [libRadtran](http://www.libradtran.org/) - A collection of C and Fortran functions and programs for calculation of solar and thermal radiation in the Earth's atmosphere.
- [ARTS](https://github.com/atmtools/arts) - A radiative transfer model for the millimeter and sub-millimeter spectral range.
- [Py6S](https://github.com/robintw/Py6S) - A Python interface to the 6S Radiative Transfer Model.
- [RTE+RRTMGP](https://github.com/earth-system-radiation/rte-rrtmgp) - A set of codes for computing radiative fluxes in planetary atmospheres.
- [LBLRTM](https://github.com/AER-RC/LBLRTM) - Line-By-Line Radiative Transfer Model is an accurate and efficient line-by-line radiative transfer model derived from the Fast Atmospheric Signature Code.
- [Eradiate](https://github.com/eradiate/eradiate) - A next-generation radiative transfer model for Earth observation applications.
- [Juelich Rapid Spectral Simulation Code](https://github.com/slcs-jsc/jurassic) - The Juelich Rapid Spectral Simulation Code (JURASSIC) is a fast infrared radiative transfer model for the analysis of atmospheric remote sensing measurements.

### Earth Observation and Climate Monitoring 

- [ClimateSatellite.jl](https://github.com/JuliaClimate/ClimateSatellite.jl) - Julia package that downloads measurements and observational of climate satellite mission data.
- [canadaHCD](https://github.com/gavinsimpson/canadaHCD/) - Access Canadian Historical Climate Data from R.
- [climatedataguide](https://climatedataguide.ucar.edu/) - Search and access 212 datasets covering the Atmosphere, Ocean, Land and more. Explore climate indices, reanalyses and satellite data and understand their application to climate model metrics.
- [chirps](https://github.com/ropensci/chirps) - A quasi-global high-resolution rainfall data set, which incorporates satellite imagery and in-situ station data to create gridded rainfall time series for trend analysis and seasonal drought monitoring.
- [pylandtemp](https://github.com/pylandtemp/pylandtemp) - Global land surface temperature and emissivity from NASA's Landsat satellite images.
- [CRU TS](https://crudata.uea.ac.uk/cru/data/hrg/) - The gridded archive of the Climatic Research Unit (University of East Anglia) and NCAS. The dataset was derived by the interpolation of monthly climate observations from extensive networks of weather stations.
- [E-OBS](https://www.ecad.eu/download/ensembles/download.php) - The detailed gridded observations data archive for the whole of Europe.
- [ERA-NUTS](https://github.com/energy-modelling-toolkit/era-nuts-code) - A set of time-series of meteorological variables based on Copernicus Climate Change Service ERA5 reanalysis.
- [NOAA PSL Reanalyses](https://psl.noaa.gov/data/gridded/reanalysis/index.html) - A public reanalysis collection of the NOAA Physical Sciences Laboratory (NCEP, NARR, 20th Century Reanalysis).
- [MERRA- 2 Reanalysis](https://disc.sci.gsfc.nasa.gov/datasets?keywords=%22MERRA-2%22) - Produced by NASA Global Modeling and Assimilation Office (GMAO). Apart of the surface observations assimilates space-based ones as well.
- [ForestGEO](https://github.com/forestgeo/Climate) - This public repository is a portal for climate data and information for ForestGEO sites.
- [esa-climate-from-space](https://github.com/ubilabs/esa-climate-from-space) - The role of the Climate from Space application is to increase the visibility of the Climate Change Initiative programme and the role of ESA satellite data in climate science.
- [pygac](https://github.com/pytroll/pygac) - A Python package to read and calibrate NOAA and Metop AVHRR GAC and LAC data.
- [ecmwfr](https://github.com/bluegreen-labs/ecmwfr) - Provides easy access to the European Centre for Medium-Range Weather Forecasts web API services and Copernicus Climate Data Store from within R, matching and expanding upon the ECMWF Python tools.


### Meteorological Observation
- [stationaRy](https://github.com/rich-iannone/stationaRy) - Get hourly meteorological data from one of thousands of global stations.
- [weathercan](https://github.com/ropensci/weathercan) - This package makes it easier to search for and download multiple months/years of historical weather data from the Environment and Climate Change Canada (ECCC) website.
- [metR](https://github.com/eliocamp/metR) - Several functions and utilities that make R better for handling meteorological data in the tidy data paradigm.
- [climate](https://github.com/bczernecki/climate) - The goal of the climate R package is to automatize downloading of meteorological and hydrological data from publicly available repositories.
- [rdwd](https://github.com/brry/rdwd) - An R package to select, download and read climate data from the German Weather Service.


### Climate Data Processing and Access
- [cf-conventions](https://github.com/cf-convention/cf-conventions) - The conventions for CF (Climate and Forecast) metadata are designed to promote the processing and sharing of files created with the NetCDF API.
- [cf-python](https://github.com/NCAS-CMS/cf-python) - A CF-compliant Earth Science data analysis library.
- [xCDAT](https://github.com/xCDAT/xcdat) - An extension of xarray for climate data analysis on structured grids.
- [ipcc_sr15_scenario_analysis](https://github.com/iiasa/ipcc_sr15_scenario_analysis) - Scenario analysis notebooks for the IPCC Special Report on Global Warming of 1.5°C.
- [Geoclimate](https://github.com/orbisgis/geoclimate) - Geospatial processing toolbox for environmental and climate studies.
- [Meteostat Python](https://github.com/meteostat/meteostat-python) - Access and analyze historical weather and climate data with Python.
- [cmip6-downscaling](https://github.com/carbonplan/cmip6-downscaling) - Climate downscaling using CMIP6 data.
- [weather-tools](https://github.com/google/weather-tools) - A series of command-line tools to make common data engineering tasks easier for researchers in climate and weather.
- [Senses Toolkit](https://github.com/SensesProject/senses-toolkit) - Offers a range of modules to learn about and explore climate change scenarios.
- [loadeR](https://github.com/SantanderMetGroup/loadeR) - An R package for climate data access building on the NetCDF-Java API.
- [climate4R](https://github.com/SantanderMetGroup/climate4R) - A bundle of R packages for transparent climate data access, post-processing (including data collocation and bias correction / downscaling) and visualization.
- [MeteoInfo](https://github.com/meteoinfo/MeteoInfo) - GIS and scientific computation environment for meteorological community.
- [GSODR](https://github.com/ropensci/GSODR) - Global Surface Summary of the Day Weather Data Client for R.
- [easyclimate](https://github.com/VeruGHub/easyclimate) - Easy access to high-resolution daily climate data for Europe.
- [Climate categories](https://github.com/pik-primap/climate_categories) - Commonly used codes, categories, terminologies, and nomenclatures used in climate policy analysis in a nice Python package.
- [OpenClimateGIS](https://github.com/NCPP/ocgis) - A set of geoprocessing and calculation tools for CF-compliant climate datasets.
- [remote_climate_data](https://github.com/aaronspring/remote_climate_data) - A collection of remote climate data accessed via intake cached to disk.
- [AR6-WG1-Data-Compilation](https://github.com/openscm/AR6-WG1-Data-Compilation) - Compiles the data into a uniform, csv-based data format following the standard established by the Integrated Assessment Modeling Consortium and used by IPCC WG3.
- [IPCC AR6 Chapter 9 Figures](https://github.com/IPCC-WG1/Chapter-9) - Code and data for all figures from Chapter 9 of the IPCC AR6.
- [icclim](https://github.com/cerfacs-globc/icclim) - Python library for climate indices and climate indicators calculation.
- [DeepSphere](https://github.com/deepsphere/deepsphere-pytorch) - Learning on the sphere with a graph-based ConvNet.
- [JuliaClimate Notebooks](https://juliaclimate.github.io/GlobalOceanNotebooks/) - Notebooks that show Julia packages related to climate working in concert.
- [clisops](https://github.com/roocs/clisops) - Climate simulation operations.
- [Climate Data Store Toolbox](https://cds.climate.copernicus.eu/toolbox/doc/index.html) - Dive into this wealth of information about the Earth's past, present and future climate.
- [ATLAS](https://github.com/SantanderMetGroup/ATLAS) - Datasets, code and virtual workspace for the Climate Change ATLAS.
- [xclim](https://github.com/Ouranosinc/xclim) - A library of derived climate variables, i.e. climate indicators, based on xarray.
- [climpact](https://github.com/ARCCSS-extremes/climpact) - Calculate the ET-SCI climate extremes indices.
- [PRISM](https://github.com/ropensci/prism) - Download data from the Oregon PRISM climate data project.
- [CliFlo](https://github.com/ropensci/clifro) - Easily download and visualise climate data from New Zealand's National Climate Database.
- [hyfo](https://github.com/Yuanchao-Xu/hyfo) - Mainly focuses on data process and visualization in hydrology and climate forecasting.
- [rWBclimate](https://github.com/ropensci/rWBclimate) - An R interface for the World Bank climate data used in the World Bank climate knowledge portal.
- [aospy](https://github.com/spencerahill/aospy) - A Python package for automated analysis and management of gridded climate data.
- [NASAaccess](https://github.com/nasa/NASAaccess) - An R package that can generate gridded ASCII tables of climate (CIMP5) and weather data (GPM, TRMM, GLDAS) needed to drive various hydrological models (e.g. SWAT, VIC, RHESSys).
- [Cate](https://github.com/CCI-Tools/cate) - A software for ingesting, operating on and visualizing all ESA Climate Change Initiative data.
- [climetlab](https://github.com/ecmwf/climetlab) - A Python package aiming at simplifying access to climate and meteorological datasets, allowing users to focus on science instead of technical issues such as data access and data formats.
- [cdsapi](https://github.com/ecmwf/cdsapi) - Python API to access the Copernicus Climate Data Store.
- [netcdf-fortran](https://github.com/Unidata/netcdf-fortran) - The Unidata network Common Data Form (netCDF) is an interface for scientific data access and a set of freely-distributed software libraries that provide an implementation of the interface.
- [Data wrangling for the "IEA Net Zero by 2050" Roadmap](https://github.com/danielhuppmann/iea-netzero2050-datawrangler) - Transform data supporting the IEA Netzero2050 Roadmap (2021) to the IAMC format.
- [IceVarFigs](https://github.com/zmlabe/IceVarFigs) - Weather and climate graphics for science communication.
- [climaemet](https://github.com/rOpenSpain/climaemet) - An interface to download the climatic data of the Spanish Meteorological Agency directly from R using their API and create scientific graphs.
- [Climate Model Output Rewriter](https://github.com/PCMDI/cmor) - Produce CF-compliant netCDF files that fulfill the requirements of many of the climate community's standard model experiments.
- [NCL](https://github.com/NCAR/ncl) - The NCAR Command Language is a scripting language for the analysis and visualization of climate and weather data.
- [xskillscore](https://github.com/xarray-contrib/xskillscore) - An open source project and Python package that provides verification metrics of deterministic (and probabilistic from properscoring) forecasts with xarray.
- [getCRUCLdata](https://github.com/ropensci/getCRUCLdata) - Provides functions that automate importing CRU CL v. 2.0 climatology data into R.
- [hockeystick](https://github.com/cortinah/hockeystick) - Make essential Climate Change datasets easily available to non-climate experts.
- [cfgrib](https://github.com/ecmwf/cfgrib) - A Python interface to map GRIB files to the NetCDF Common Data Model following the CF Convention using ecCodes.
- [epwshiftr](https://github.com/ideas-lab-nus/epwshiftr) - Create future EnergyPlus Weather files using CMIP6 data.
- [bomrang](https://github.com/ropensci/bomrang) - Australian government Bureau of Meteorology (BOM) data client for R.
- [Intake-esm](https://github.com/intake/intake-esm) - An intake plugin for parsing an Earth System Model catalog and loading assets into xarray datasets.
- [h5netcdf](https://github.com/h5netcdf/h5netcdf) - A Python interface for the netCDF4 file format that reads and writes local or remote HDF5 files directly via h5py or h5pyd, without relying on the Unidata netCDF library.
- [rsoi](https://github.com/boshek/rsoi) - An R package to download the most up to date climate indices.
- [NCO](https://github.com/nco/nco) - Manipulates and analyzes data stored in netCDF-accessible formats.
- [pynco](https://github.com/nco/pynco) - Contains the module python nco, which implements a Python style access to the NetCDF Operators (NCO).
- [climateR](https://github.com/mikejohnson51/climateR) - An R package for getting point and gridded climate data by AOI.
- [esd](https://github.com/metno/esd) - Designed for climate and weather data analysis, empirical-statistical downscaling, and visualisation.

### Integrated Assessment

- [DICE.jl](https://github.com/Libbum/DICE.jl) - The Dynamic Integrated model of Climate and the Economy model family are a popular and capable type of simple Integrated Assessment Model of climate change economics pioneered by William Nordhaus.
- [LPJmL](https://gitlab.pik-potsdam.de/lpjml/LPJmL) - A process-based model that simulates climate and land-use change impacts on the terrestrial biosphere, the water and carbon cycle and on agricultural production.
- [ENGAGE](https://github.com/iiasa/ENGAGE-netzero-analysis) - Source code for figure generation and analysis of the ENGAGE netzero scenario analysis.
- [pyam](https://github.com/IAMconsortium/pyam) - A Python package for data-wrangling, analysis and visualization of integrated-assessment scenarios and energy systems modeling results.
- [GCAM](https://github.com/JGCRI/gcam-core) - A dynamic-recursive model with technology-rich representations of the economy, energy sector, land use and water linked to a climate model that can be used to explore climate change mitigation policies including carbon taxes, carbon trading, regulations and accelerated deployment of energy technology.


## Natural Resources

### Air Quality 

- [CMAQ](https://github.com/USEPA/CMAQ) - Code base for the U.S. EPA's Community Multiscale Air Quality Model.
- [AMET](https://github.com/USEPA/AMET) - A suite of software designed to facilitate the analysis and evaluation of predictions from meteorological and air quality models.
- [MLAir](https://gitlab.version.fz-juelich.de/esde/machine-learning/mlair) - Machine Learning on Air data is an environment that simplifies and accelerates the creation of new machine learning models for the analysis and forecasting of meteorological and air quality time-series.
- [shoot-i-smoke](https://github.com/shootismoke/mobile-app) - See your city's air pollution measured in daily cigarettes.
- [airqmon](https://github.com/jsynowiec/airqmon) - A macOS menu bar application that displays live air quality data from the nearest sensor station.
- [opendata-stuttgart](https://github.com/opendata-stuttgart/sensors-software) - The maintained main firmware for the Luftdaten.Info Sensor.
- [AirCasting](https://github.com/HabitatMap/AirCasting) - The project aims to build a platform for gathering, visualization and sharing of environmental data.
- [openair](https://github.com/davidcarslaw/openair) - An R package developed for the purpose of analyzing air quality data — or more generally atmospheric composition data.
- [ropenaq](https://github.com/ropensci/ropenaq) - A community of scientists, software developers and lovers of open environmental data who are building an open, real-time database that provides programmatic and historical access to air quality data.
- [airQualityMeter](https://github.com/rpanfili/airQualityMeter) - Detects air particulate matter (PM - pm1, pm2.5, pm10) concentrations and sends data to an MQTT server.
- [Air-Trends-Report](https://github.com/USEPA/Air-Trends-Report) - Source code for EPA's annual air trends report on air quality, emissions and visibility trends.
- [OpenAQ API Version 2](https://github.com/openaq/openaq-api-v2) - A web-accessible API that provides endpoints to query the real-time and historical air quality measurements on the platform.
- [OpenAQ Data Ingest Pipeline](https://github.com/openaq/openaq-fetch) - A tool to collect data for OpenAQ platform.
- [breethe-server](https://github.com/simplabs/breethe-server) - Breethe allows instant access to up to date air quality data for locations in Europe.
- [SMOKE](https://github.com/CEMPD/SMOKE) - Create emissions inputs for multiple air quality modeling systems with unmatched speed and flexibility.
- [inmap](https://github.com/spatialmodel/inmap) - A multi-scale emissions-to-health impact model for fine particulate matter (PM2.5) that mechanistically evaluates air quality and health benefits of perturbations to baseline emissions.
- [Open Source EMEP MSC-W model](https://github.com/metno/emep-ctm) - Designed to calculate air concentrations and deposition fields for major acidifying and eutrophying pollutants, photo-oxidants and particulate matter.
- [Rpollution](https://github.com/openvironment/Rpollution) - The goal of Rpollution is to assemble R functions to analyze air pollution data.
- [YETI](https://github.com/twollnik/YETI) - A bottom-up traffic emission calculation tool developed at the Institute for Advanced Sustainability Studies in Potsdam and built in Python.
- [PM2.5-GNN](https://github.com/shawnwang-tech/PM2.5-GNN) - A Domain Knowledge Enhanced Graph Neural Network For PM2.5 Forecasting.
- [rdefra](https://github.com/ropensci/rdefra) - Interact with the UK AIR Pollution Database from DEFRA.
- [rmweather](https://github.com/skgrange/rmweather) - An R package to conduct meteorological/weather normalisation on air quality so trends and interventions can be investigated in a robust way.
- [Safecast](https://github.com/Safecast/safecastapi) - Building out a network of sensors to monitor particulate matter in sizes PM1.0, PM2.5, PM10.
- [West Oakland Air Quality Project](https://github.com/openoakland/woeip) - A platform for impacted communities to understand their local air quality and advocate for environmental justice.
- [Sensor.Community](https://github.com/opendata-stuttgart/sensor.community) - Making the world a better place through community driven, open environmental data.
- [openSenseMap](https://github.com/sensebox/openSenseMap) - Wikipedia for environmental data in order to awaken and promote education, environmental and climate protection.
- [rfasst](https://github.com/JGCRI/rfasst) - Estimation of a consistent range of adverse health and agricultural effects attributable to air pollution for a GCAM scenario.
- [saqgetr](https://github.com/skgrange/saqgetr) - Import Air Quality Monitoring Data in a Fast and Easy Way.
- [Ozone](https://github.com/Milind220/Ozone) - An open-source package to easily obtain real-time, historical, or forecasted air quality data for anywhere in the world.

### Water Supply

- [Stormwater-Management-Model](https://github.com/USEPA/Stormwater-Management-Model) - Used for single event or long-term (continuous) simulation of runoff quantity and quality from primarily urban areas.
- [dataRetrieval](https://github.com/USGS-R/dataRetrieval) - This R package is designed to obtain USGS or EPA water quality sample data, streamflow data and metadata directly from web services.
- [EGRET](https://github.com/USGS-R/EGRET) - An R package for the analysis of long-term changes in water quality and streamflow, including the water-quality method Weighted Regressions on Time, Discharge, and Season.
- [WaterModels.jl](https://github.com/lanl-ansi/WaterModels.jl) - Designed to enable computational evaluation of historical and emerging water network formulations and algorithms using a common platform.
- [Tree-based Inland Hydraulic Routing Project](https://github.com/NOAA-OWP/t-route) - The program under development here seeks to effectively manage the traversal of a network of streams with defined hydraulic properties specifically for the purpose of hydraulic routing in an operational flood and water resources forecasting system.
- [Next Gen Water Modeling Framework](https://github.com/NOAA-OWP/ngen) - This framework includes an encapsulation strategy which focuses on the hydrologic data first, and then builds a functional abstraction of hydrologic behavior.
- [nhdplusTools](https://github.com/USGS-R/nhdplusTools) - This package is a growing set of tools for manipulation of hydrographic data using the NHDPlus data model.
- [The Safe Water Project](https://github.com/codeforboston/safe-water) - A team of volunteers at Code for Boston who are using data modeling, data visualization and machine learning to predict, visualize, and share data about the presence of hazardous drinking and surface water contaminants in the United States.
- [HydroFunctions](https://github.com/mroberge/hydrofunctions) - A suite of convenience functions for working with hydrology data in an interactive Python session.
- [CWATM](https://github.com/CWatM/CWatM) - Represents one of the new key elements of IIASAs Water program to assess water supply, water demand and environmental needs at global and regional level.
- [The General Lake Model](https://github.com/AquaticEcoDynamics/GLM) - A water balance and one-dimensional vertical stratification hydrodynamic model.
- [nhdR](https://github.com/jsta/nhdR) - An R interface to the US National Hydrography Dataset.
- [modflow6](https://github.com/MODFLOW-USGS/modflow6) - Has been widely used by academics, private consultants, and government scientists to accurately, reliably, and efficiently simulate groundwater flow.
- [iMOD](https://oss.deltares.nl/web/imod/home) - An easy to use Graphical User Interface + an accelerated Deltares-version of MODFLOW with fast, flexible and consistent sub-domain modeling techniques.
- [Imod-Python](https://gitlab.com/deltares/imod/imod-python) - Designed to help you in your MODFLOW groundwater modeling efforts.
- [pysheds](https://github.com/mdbartos/pysheds) - Simple and fast watershed delineation in Python.
- [WhiteboxTools](https://github.com/jblindsay/whitebox-tools) - WhiteboxTools is an advanced geospatial data analysis platform.
- [CRITERIA3D](https://github.com/ARPA-SIMC/CRITERIA3D) - Includes a numerical solution for three-dimensional water and heat flow in the soil, coupled surface and subsurface flow, meteorological data interpolation, radiation budget, crop development and crop water uptake.
- [Water Network Tool for Resilience](https://github.com/USEPA/WNTR) - A Python package designed to simulate and analyze resilience of water distribution networks.
- [fasstr](https://github.com/bcgov/fasstr) - An R package to analyze, summarize, and visualize daily streamflow data.
- [KnowFlow](https://github.com/KnowFlow/KnowFlow_AWM) - KnowFlow Automatic Water Monitoring device is an open source tool enabling everyone to have access to first hand water quality data with low cost.
- [gwells](https://github.com/bcgov/gwells) - Groundwater Wells and Aquifers application for the Ministry of Environment in British Columbia.
- [waterquality](https://github.com/RAJohansen/waterquality) - A package designed to detect and quantify water quality and cyanobacterial harmful algal bloom (CHABs) from remotely sensed imagery.
- [QGEP](https://github.com/qgep/QGEP) - A waste-water application based on QGIS in compliance with SIA-405.
- [PooPyLab_Project](https://github.com/toogad/PooPyLab_Project) - A biological wastewater treatment software.
- [aguaclara](https://github.com/AguaClara/aguaclara) - A Python package for designing and performing research on AguaClara water treatment plants.
- [RTC-Tools](https://gitlab.com/deltares/rtc-tools) - A toolbox for control and optimization of water systems.
- [EPANET](https://github.com/OpenWaterAnalytics/EPANET) - The Water Distribution System Hydraulic and Water Quality Analysis Toolkit.
- [pyswmm](https://github.com/OpenWaterAnalytics/pyswmm) - Python Wrapper for Stormwater Management Model.
- [SELEN](https://github.com/geodynamics/selen) - An open source Fortran code for the numerical solution of the Sea Level Equation for a spherical, layered, rotating earth with viscoelastic rheology.
- [rivamap](https://github.com/isikdogan/rivamap) - An Automated River Analysis and Mapping Engine.
- [PyGnome](https://github.com/NOAA-ORR-ERD/PyGnome) - It is designed to support oil and other hazardous material spills in the coastal environment.
- [VICRes](https://github.com/thanhiwer/VICRes) - The model simulates key hydrological processes occurring in a river basin (e.g. water and energy balances, streamflow routing), but does not account for the operations of artificial water reservoirs.
- [AWSM](https://github.com/USDA-ARS-NWRC/awsm) - Automated Water Supply Model was developed at the USDA Agricultural Research Service.
- [AED2](https://github.com/AquaticEcoDynamics/libaed2) - A community-driven library of modules and algorithms for simulation of "aquatic ecodynamics": water quality, aquatic biogeochemsitry, biotic habitat and aquatic ecosystem dynamics.
- [DORiE](https://ts-gitlab.iup.uni-heidelberg.de/dorie/dorie) - A Discontinuous Galerkin Solver for Soil Water Flow and Passive Solute Transport Based on DUNE.
- [wqbc](https://github.com/bcgov/wqbc) - An R package for water quality thresholds and index calculation for British Columbia.
- [Model My Watershed](https://github.com/WikiWatershed/model-my-watershed) - A watershed-modeling web app for citizens, conservation practitioners, municipal decision-makers, educators, and students.
- [AquaSat](https://github.com/GlobalHydrologyLab/AquaSat) - A data set to enable remote sensing of water quality for inland waters.
- [CDE](https://github.com/ropensci/cde) - Facilitates searching and download of the Water Framework Directive reporting data for all waterbodies from the EA website.
- [pyGSFLOW](https://github.com/pygsflow/pygsflow) - A set of Python modules to run the GSFLOW integrated hydrologic model program.
- [bcgroundwater](https://github.com/bcgov/bcgroundwater) - An R package to facilitate analysis and visualization of groundwater data from the British Columbia groundwater observation well network.
- [GSFLOW-GRASS](https://github.com/UMN-Hydro/GSFLOW-GRASS) - Generates inputs for and runs the coupled groundwater-surface water model "GSFLOW".
- [GWHAT](https://github.com/jnsebgosselin/gwhat) - A free, open source, and cross-platform interactive computer program whose main focus is the interpretation of observation well hydrographs.
- [Soil-Water-Balance](https://github.com/smwesten-usgs/swb) - A Modified Thornthwaite-Mather Soil-Water-Balance Code for Estimating Groundwater Recharge.
- [Long-term Trends in Groundwater Levels in B.C.](https://github.com/bcgov/groundwater-levels-indicator) - R scripts for an indicator on long-term trends in groundwater levels in British Columbia published on Environmental Reporting British Columbia.
- [GSFLOW](https://www.usgs.gov/software/coupled-ground-water-and-surface-water-flow-model-gsflow) - A coupled Groundwater and Surface-water FLOW model based on the integration of the USGS Precipitation-Runoff Modeling System and the USGS Modular Groundwater Flow Model.
- [canwqdata](https://github.com/bcgov/canwqdata) - An R package to download open water quality data from Environment and Climate Change Canada's National Long-term Water Quality Monitoring Data.
- [HASP](https://github.com/USGS-R/HASP/) - Hydrologic AnalySis Package.
- [CSHShydRology](https://github.com/CSHS-CWRA/CSHShydRology) - This is a collection of R functions used by the Canadian Association Society for Hydrological Sciences.
- [Liquid Prep](https://github.com/Call-for-Code/Liquid-Prep) - Offers an end-to-end solution for farmers looking to optimize their water usage; especially during times of drought.
- [flopy](https://github.com/modflowpy/flopy) - A Python package to create, run, and post-process MODFLOW-based models.
- [PCRaster](https://github.com/pcraster/pcraster) - A collection of tools and software libraries tailored to the construction of spatio-temporal environmental models.
- [Echopype](https://github.com/OSOceanAcoustics/echopype) - A package built to enable interoperability and scalability in ocean sonar data processing.
- [NeuralHydrology](https://github.com/neuralhydrology/neuralhydrology) - Python library to train neural networks with a strong focus on hydrological applications.
- [dataretrieval](https://github.com/USGS-python/dataretrieval) - A Python alternative to USGS-R's dataRetrieval package for obtaining USGS or EPA water quality data, streamflow data, and metadata directly from web services.
- [CWatM](https://github.com/iiasa/CWatM) - Assess water supply, water demand and environmental needs at global and regional level.
- [WWTP](https://gitlab.com/hotmaps/potential/WWTP) - EU28 Waste Water Treatment Plants.
- [AWH-Geo](https://github.com/AWH-GlobalPotential-X/AWH-Geo) - Tool and calculations for Global Potential of Harvesting Drinking Water from Air using Solar Energy.
- [RainfallRescue](https://github.com/ed-hawkins/rainfall-rescue) - Monthly rainfall observations taken in the UK and Ireland, covering the period 1677-1960.
- [pySTEPS](https://github.com/pySTEPS/pysteps) - An open-source and community-driven Python library for probabilistic precipitation nowcasting, i.e. short-term ensemble prediction systems.
- [reservatoriosBR](https://github.com/brunomioto/reservatoriosBR) - R package for Brazilian reservoirs data.
- [PyForecast](https://github.com/usbr/PyForecast) - A statistical modeling tool used by Reclamation water managers and reservoir operators to train and build predictive models for seasonal inflows and streamflows.
- [pyWaPOR](https://bitbucket.org/cioapps/wapor-et-look/) - Data manual and Algorithm to compute the evapotranspiration of large areas using remote sensing data.
- [HydroSHEDS](https://www.hydrosheds.org/) - Seamless hydrographic data for global and regional applications.


### Soil and Land

- [SoilGrids250m](https://github.com/ISRICWorldSoil/SoilGrids250m) - Global Spatial predictions of soil properties and classes at 250 m resolution.
- [SoilGrids](https://git.wur.nl/isric/soilgrids/soilgrids.notebooks/) - A system for automated soil mapping based on global soil profile and environmental covariate data at 250 m spatial resolution.
- [Hyperspectral Soilmoisture Dataset](https://github.com/felixriese/hyperspectral-soilmoisture-dataset) - Hyperspectral benchmark dataset on soil moisture.
- [soilReports](https://github.com/ncss-tech/soilReports) - An R package that assists with the setup and operation of a collection of soil data summary, comparison, and evaluation reports.
- [AQP](https://github.com/ncss-tech/aqp) - Algorithms for Quantitative Pedology is a collection of code, ideas, documentation, and examples wrapped-up into several R packages.
- [sharpshootR](https://github.com/ncss-tech/sharpshootR) - Miscellaneous soil data management, summary, visualization, and conversion utilities to support soil survey.
- [soilDB](https://github.com/ncss-tech/soilDB) - Simplified Access to NCSS Soil Databases.
- [Landslides Detection](https://github.com/mhscience/landslides_detection) - Machine learning tool to detect landslides from optical satellite imagery.
- [pyTSEB](https://github.com/hectornieto/pyTSEB) - Contains Python code for Two Source Energy Balance models (Priestley-Taylor TSEB-PT, Dual Time Difference DTD and TSEB with component soil and canopy temperatures TSEB-2T) for estimating sensible and latent heat flux based on measurements of radiometric surface temperature.
- [slga](https://github.com/obrl-soil/slga) - Offers the ability to download geographic subsets of raster data from the Soil and Landscape Grid of Australia.
- [smapr](https://github.com/ropensci/smapr) - An R package for acquisition and processing of NASA (Soil Moisture Active-Passive) SMAP data.
- [DRIP-SLIP](https://github.com/NASA-DEVELOP/DRIP-SLIP) - Detecting Realtime Increased Precipitation / Sudden Landslide Identification Product.
- [esa_cci_sm](https://github.com/TUW-GEO/esa_cci_sm) - Readers and converters for ESA CCI Soil Moisture image and time series data.
- [US_SoilGrids100m](https://github.com/aramcharan/US_SoilGrids100m) - Complete-coverage gridded predictions of soil properties (percent organic carbon, total nitrogen, bulk density, pH, and percent sand and clay) and classes (taxonomic great group and particle size in the control section) for the Conterminous U.S.
- [pytesmo](https://github.com/TUW-GEO/pytesmo) - Python Toolbox for the Evaluation of Soil Moisture Observations.
- [Drought Indices Map](https://github.com/imartinezl/drought-map) - This project attempts to find an accessible and friendly way to visualize data of drought indices in Spain from 1961 until 2017.
- [ml_drought](https://github.com/esowc/ml_drought) - A Machine Learning Pipeline to Predict Vegetation Health.
- [droughtwatch](https://github.com/wandb/droughtwatch) - Leverages deep learning and computer vision for drought resilience, using satellite images and human expert labels to detect drought conditions in Northern Kenya.
- [SoilHealthDB](https://github.com/jinshijian/SoilHealthDB) - Compiled data from a set of soil health measurements collected across 41 countries around the world, which includes 5,241 data entries from 281 published studies.
- [srdb](https://github.com/bpbond/srdb) - Global soil respiration database.
- [cosore](https://github.com/bpbond/cosore) - Data, metadata, and software tools for the COSORE database of continuous soil respiration measurements.
- [sidb](https://github.com/SoilBGC-Datashare/sidb) - Contains information on laboratory soil incubation experiments, with emphasis on time series of CO2 release.
- [ISRaD](https://github.com/International-Soil-Radiocarbon-Database/ISRaD) - Improve the use of radiocarbon as a constraint for understanding the soil carbon cycle.
- [PredictiveSoilMapping](https://github.com/Envirometrix/PredictiveSoilMapping) - Applying statistical and/or machine learning techniques to fit models for the purpose of producing spatial and/or spatiotemporal predictions of soil variables, i.e. maps of soil properties and classes at different resolutions.
- [OpenFLUID](https://github.com/OpenFLUID/openfluid) - A software environment for modeling and simulation of complex landscape systems.
- [Trends.Earth](https://github.com/ConservationInternational/trends.earth) - A QGIS plugin that supports monitoring of land change, including changes in productivity, land cover, and soil organic carbon.
- [pycoal](https://github.com/capstone-coal/pycoal) - A Python toolkit for characterizing Coal and Open-pit surface mining impacts on American Lands.
- [stats_for_soil_survey](https://ncss-tech.github.io/stats_for_soil_survey/) - Lecture material on "Statistics for Pedologists".
- [Simsphere](https://github.com/tjc181/simsphere) - A one-dimensional model that allows one to simulate the transfer of heat and moisture between plants, soil and atmosphere over a 24 hour day.
- [CryoGrid3](https://github.com/CryoGrid/CryoGrid3) - A one-dimensional land surface model dedicated to simulate ground temperatures in permafrost environments.
- [CNN-SoilTextureClassification](https://github.com/felixriese/CNN-SoilTextureClassification) - One-dimensional convolutional neural networks (CNN) for the classification of soil texture based on hyperspectral data.
- [EarthML](https://github.com/pyviz-topics/EarthML) - Improving, documenting, and illustrating how to use other, freely available, general-purpose open source projects to solve problems in the earth sciences.
- [STEP](http://step.esa.int/main/) - ESA is developing free open source toolboxes for the scientific exploitation of Earth Observation missions under the Scientific Exploitation of Operational Missions programme element.
- [globsim](https://github.com/geocryology/globsim) - Using global reanalyses for permafrost simulation.
- [rSFSW2](https://github.com/DrylandEcology/rSFSW2) - An R package to create soil water balance simulation experiment.
- [landscapemetrics](https://github.com/r-spatialecology/landscapemetrics) - Landscape Metrics for Categorical Map Patterns world_map in R.
- [SCOPE](https://github.com/Christiaanvandertol/SCOPE) - Simulation model for radiative transfer, photosynthesis and energy fluxes in vegetation and soil.
- [Demeter](https://github.com/JGCRI/demeter) - A land use land cover disaggregation and change detection model.
- [OpenLandMap](https://gitlab.com/openlandmap) - Data, services and web-apps providing access and interactive visualizations of the TB of high resolution data produced by the OpenGeoHub Foundation and contributing organizations.
- [PyLandStats](https://github.com/martibosch/pylandstats) - An open-source Pythonic library to compute landscape metrics.
- [NLMR](https://github.com/ropensci/NLMR) - R package to simulate neutral landscape models.
- [LT-GEE](https://github.com/eMapR/LT-GEE) - Google Earth Engine implementation of the LandTrendr spectral-temporal segmentation algorithm.
- [Full Lands INtegration Tool](https://github.com/moja-global/About_moja_global) - A modular system to estimate greenhouse gas emissions and removals by the land sector.
- [ismn](https://github.com/TUW-GEO/ismn) - Readers for the data from the International Soil Moisture Database.
- [soils-revealed](https://github.com/Vizzuality/soils-revealed) - Platform for direct visualization, analysis and reporting of soil organic carbon predictions and changes over time.
- [Soil Erosion Watch](https://github.com/SoilWatch/soil-erosion-watch) - A Google Earth Engine App to explore the state of the world's degraded soils.
- [Land Matrix](https://github.com/sinnwerkstatt/landmatrix) - Independent global land monitoring initiative that promotes transparency & accountability in decisions over large-scale land acquisitions.
- [SITS](https://github.com/e-sensing/sits) - Enables users to apply machine learning techniques for classifying image time series obtained from earth observation data cubes.
- [iSDAsoil](https://www.isda-africa.com/isdasoil/) - Open access soil property map with 30m resolution for Africa.
- [Landlab](https://github.com/landlab/landlab) - An open source Python package for numerical modeling of Earth surface dynamics.


### Agriculture and Nutrition

- [Farmbot](https://github.com/FarmBot/Farmbot-Web-App) - Humanity's open-source CNC farming machine.
- [MudPi](https://github.com/mudpi/mudpi-core) - A scalable smart garden system that allows you to maintain controls, monitor conditions, and sustainably manage resources of your garden.
- [OBIA4RTM](https://github.com/lukasValentin/OBIA4RTM) - Aims for plant parameter retrieval - relevant in smart farming applications - by using radiative transfer models and object-based image analysis that directly addresses actual user needs and policy demands in a highly efficient, flexible and scalable way.
- [Crop-Classification](https://github.com/bhavesh907/Crop-Classification) - Provides codes for crop classification using multi temporal satellite images.
- [DSSAT Cropping System Model](https://github.com/DSSAT/dssat-csm-os) - Has been used for many applications ranging from on-farm and precision management to regional assessments of the impact of climate variability and climate change.
- [MAgPIE](https://github.com/magpiemodel/magpie) - Model of Agricultural Production and its Impact on the Environment.
- [OBI](https://github.com/AgroCares/Open-Bodem-Index-Calculator) - The Open-Bodem-Index-Calculator is a tool that evaluates the soil of agricultural fields based on four main criteria: chemical, physical, biological and management.
- [Cycles](https://github.com/PSUmodeling/Cycles) - A daily time-step agroecosystem model that simulates the biophysical processes and management practices occurring within cropping systems and other land uses.
- [ApsimX](https://github.com/APSIMInitiative/ApsimX) - An agricultural modeling framework used extensively worldwide.
- [Resilience Atlas](https://github.com/ConservationInternational/resilienceatlas) - An interactive analytical tool for building understanding of the extent and severity of some of the key stressors and shocks that are affecting rural livelihoods, production systems, and ecosystems in the Sahel, Horn of Africa and South and Southeast Asia.
- [rice-awd-shb](https://github.com/adamhsparks/rice-awd-shb) - Research compendium for a report on the effects of using alternate wetting and drying irrigation techniques and nitrogen rates on sheath blight disease in rice paddies.
- [monica](https://github.com/zalf-rpm/monica) - A dynamic, process-based simulation model which describes transport and bio-chemical turn-over of carbon, nitrogen and water in agro-ecosystems.
- [OpenFarm](https://github.com/openfarmcc/OpenFarm) - A free and open database and web application for farming and gardening knowledge.
- [Agridat](https://github.com/kwstat/agridat) - An extensive collection of datasets from agricultural experiments.
- [ss3sim](https://github.com/ss3sim/ss3sim) - An R package that facilitates flexible, rapid, and reproducible fisheries stock assessment simulation testing with the widely-used Stock Synthesis statistical age-structured stock assessment framework.
- [rfisheries](https://github.com/ropensci/rfisheries) - Interacting with fisheries databases at openfisheries.org.
- [Fisheries Stock Assessment](https://github.com/droglenc/FSA) - Provides R functions to conduct typical introductory fisheries analyses.
- [RFishBC](https://github.com/fishR-Core-Team/RFishBC) - Helps fisheries scientists collect measurements from calcified structures and back-calculate estimated lengths at previous ages.
- [mizer](https://github.com/sizespectrum/mizer) - An R package to run dynamic multi-species size-spectrum models of fish communities.
- [POSEIDON](https://github.com/CarrKnight/POSEIDON) - A fishery agent-based model.
- [Karrot](https://github.com/karrot-dev/karrot-frontend) - Web application for organization of foodsaving groups worldwide.
- [AquaCropR](https://bitbucket.org/anyelacamargo/aquacropr/) - Implementation of the AquaCrop crop growth model developed by FAO to address food security and assess the effect of the environment and management on crop production.
- [openfoodnetwork](https://github.com/openfoodfoundation/openfoodnetwork) - An online marketplace for local food. It enables a network of independent online food stores that connects farmers and food hubs with individuals and local businesses.
- [powerplant](https://github.com/Ecohackerfarm/powerplant) - Provides intelligent planting suggestions which maximize positive crop interaction for the mutual benefit of all your crops.
- [Trefle](https://github.com/treflehq/trefle-api) - A botanical JSON REST API for plants species, allowing you to search and query over all the registered species, and build the next gardening apps and farming robots.
- [HappyPlants](https://github.com/morkro/happy-plants) - Creating your own plant database in a visual way.
- [dormancyR](https://github.com/EduardoFernandezC/dormancyR) - Provide alternatives to common chill models used in horticulture to compute chill metrics in deciduous fruit tree orchards as well as functions to handle weather data.
- [seedr](https://github.com/efernandezpascual/seedr) - An R package that provides functions to fit hydro and thermal time germination models.
- [plantFEM](https://github.com/kazulagi/plantFEM) - A plant simulator based on Finite Element Method, which targets crops in fields. This software provides multi-physical simulations of agriculture for canopies, plants, and organs for farmers, breeders, and agronomists.
- [openfoodfacts-server](https://github.com/openfoodfacts/openfoodfacts-server) - Open Food Facts is a collaborative, free and open database of food products from around the world.
- [ramlegacy](https://www.ramlegacy.org/) - A compilation of stock assessment results for commercially exploited marine populations from around the world.
- [FABIO](https://github.com/martinbruckner/fabio_v1) - Forestry and Agriculture Biomass Input-Output Tables.
- [Food and Agriculture Organization Corporate Statistical Database](http://www.fao.org/faostat/en/#data) - Disseminates statistical data collected and maintained by the Food and Agriculture Organization.
- [Growstuff](https://github.com/Growstuff/growstuff) - Open source and open data platform that can predict when your plantings will be ready to harvest.
- [FarmOS](https://farmos.org/) - Open source web-based application for farm management, planning, and record keeping.
- [Is-Vegan](https://github.com/hmontazeri/is-vegan) - Helps you to find out which food ingredients are vegan / non-vegan.
- [fishRman](https://github.com/Shyentist/fish-r-man) - Shiny R Dashboard to easily query, download, analyse and visualise Global Fishing Watch data on fishing effort.
- [GlobalFishingWatch](https://github.com/GlobalFishingWatch/map-client) - Track commercial fishing activity worldwide on the free, user-friendly, interactive Global Fishing Watch map.
- [r4ss](https://github.com/r4ss/r4ss) - A fisheries stock assessment model written by Rick Methot.
- [AgroMo](https://github.com/hollorol/AgroMo) - An Integrated Assessment and Modelling software that integrates a crop, biogeochemical and a agro-economical model.
- [CropHarvest](https://github.com/nasaharvest/cropharvest) - Collects data from a variety of agricultural land use datasets and remote sensing products.
- [BreizhCrops](https://github.com/dl4sits/BreizhCrops) - A Satellite Time Series Dataset for Crop Type Identification.
- [VeganCheck.me](https://github.com/JokeNetwork/vegancheck.me) - A multilingual progressive web app, which scans the EAN or UPC codes of over 3.000.000 food- or non-food-products and simply tells you if it they're vegan or not. 
- [Sentinels for Common Agriculture Policy](https://github.com/Sen2Agri/Sen2Agri-System) - Aims at providing to the European and national stakeholders validated algorithms, products, workflows and best practices for agriculture monitoring relevant for the management. 
- [Automatic field delineation](https://github.com/sentinel-hub/field-delineation) - Generate automatic contours for agricultural parcels, given Sentinel-2 images.

### Natural Hazard and Poverty

- [PRISM](https://github.com/WFP-VAM/prism-frontend) - Assesses the potential risk and forecasts the impact of climate hazards on the most vulnerable communities, in order to design risk reduction activities and target disaster responses.
- [Flood Mapping](https://github.com/mikejohnson51/FloodMapping) - Flood forecasting via the National Water Model.
- [GLOCOFFS](https://github.com/WPringle/GLOCOFFS) - An ADCIRC-based global storm tide modeling system providing real-time forecasts of coastal flooding.
- [ML4Floods](https://github.com/spaceml-org/ml4floods) - An ecosystem of data, models and code pipelines to tackle flooding with machine learning.
- [CaMa](https://github.com/global-hydrodynamics/CaMa-Flood_v4) - Designed to simulate the hydrodynamics in continental-scale rivers.
- [Cahaba](https://github.com/NOAA-OWP/cahaba) - Flood inundation mapping and evaluation software configured to work with U.S. National Water Model.
- [Global Flood Database Scripts & Data](https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase) - Used to produce the Global Flood Database and assess changes in population exposed to floods.
- [LISFLOOD](https://github.com/ec-jrc/lisflood-code) - A spatially distributed water resources model, developed by the Joint Research Centre of the European Commission since 1997.
- [CanFlood](https://github.com/NRCan/CanFlood) - Flood Risk modelling toolbox for Canada.
- [HYDRAFloods](https://github.com/Servir-Mekong/hydra-floods) - An open source Python application for downloading, processing, and delivering surface water maps derived from remote sensing data.
- [OasisLMF](https://github.com/OasisLMF/OasisLMF) - An open source catastrophe modelling platform, free to use by anyone.
- [CAMS](https://github.com/CriticalAssetManagement/CAMS) - Critical Asset Management and Disaster Resilience for Islands, Cities, and Communities.

## Sustainable Development

### Sustainable Development Goals 

- [open-sdg](https://github.com/open-sdg/open-sdg) - A platform for collecting and disseminating data for the Sustainable Development Goal global indicators.
- [SustainBench](https://github.com/sustainlab-group/sustainbench) - Benchmarks for Monitoring the Sustainable Development Goals with Machine Learning.
- [OSDG](https://github.com/osdg-ai/osdg-tool) -  Tool that assigns Sustainable Development Goals labels to your input.
- [US Sustainable Development Goal indicators](https://github.com/GSA/sdg-indicators-usa) - U.S. National Reporting Platform for the Sustainable Development Goals.
- [SDGIO](https://github.com/SDG-InterfaceOntology/sdgio) - The repository for the Sustainable Development Goals Interface Ontology.
- [sdgindex](https://www.sdgindex.org/) - International Sustainable Development Reports.
- [sdg-tracker.org](https://github.com/owid/sdg-tracker.org) - Sustainable Development Goals tracker website.
- [SDGmapR](https://github.com/CMUSustainability/SDGmapR) - R functions and datasets related to the mapping of text to the United Nations 17 Sustainable Development Goals.
- [Europe Sustainable Development ReportS](https://eu-dashboards.sdgindex.org/) - Track the progress of the European Union and European Countries towards the Sustainable Development Goals.


### Sustainable Investment 

- [Integrated Valuation of Ecosystem Services and Tradeoffs](https://github.com/natcap/invest) - A family of tools for quantifying the values of natural capital in clear, credible, and practical ways.
- [The REgional Model of INvestments and Development](https://github.com/remindmodel/remind) - A modular open source multi-regional model incorporating the economy, the climate system and a detailed representation of the energy sector.
- [WHAT-IF](https://github.com/RaphaelPB/WHAT-IF) - Water, Hydropower, Agriculture Tool for Investment and Financing decision support tool.
- [Investment Framework for a More Sustainable World](https://github.com/My-Climate-Journey/climate-sustainability-investment-framework) - This framework was created as a tool for those seeking to make emissions reductions and sustainability related investments with the goal of mitigating the impacts of climate change, based on guidelines set forth by Chamath Palihapitiya in July 2020.
- [r2dii.analysis](https://github.com/2DegreesInvesting/r2dii.analysis) - Summarize key metrics attributed to the portfolio (e.g. production, emission factors), and calculate targets based on climate scenarios.
- [SBTi Temperature Alignment tool](https://github.com/OFBDABV/SBTi) - Helps companies and financial institutions to assess the temperature alignment of current targets, commitments, and investment and lending portfolios, and to use this information to develop targets for official validation.
- [Real-Impact-Tracker-Methodology](https://github.com/realimpat/Real-Impact-Tracker-Methodology/) - A methodology to assess the Real Impact of funds on social and environmental issues.
- [MimiFUND.jl](https://github.com/fund-model/MimiFUND.jl) - Used to perform cost-benefit and cost-effectiveness analyses of greenhouse gas emission reduction policies.
- [Asset-level Transition Risk in the Global Coal, Oil, and Gas Supply Chains](https://github.com/Lkruitwagen/global-fossil-fuel-supply-chain) - The global fossil fuel supply chain, mapped at the asset-level.
- [open-climate-investing](https://github.com/opentaps/open-climate-investing) - Application and data for analyzing and structuring portfolios for climate investing.
- [SSC](https://github.com/NREL/ssc) - Contains the source code for the technology and financial models contained within the National Renewable Energy Laboratory's System Advisor Model.
- [OS-Climate Data Commons](https://github.com/os-climate/os_c_data_commons) - Collect, normalize and integrate climate and ESG data from public and private sources.
- [XDC Model](https://gitlab.com/xdc-model/xdc) - Enable users, or any intereted subject, to understand and familiarize with the basic concepts of the X-Degree Compatibility methodology.
- [gfer](https://github.com/Yuanchao-Xu/gfer) - Designed for green finance and environmental risk research focused on data collecting and analyzing in green finance and environmental risk research and analysis.
- [WikiRate](https://github.com/wikirate/wikirate) - Facilitates research and analysis on complex topics in collaboration with partners, to make ESG data open, comparable and useful for all.


### Knowledge Platforms

- [Climate Watch](https://github.com/ClimateWatch-Vizzuality/climate-watch) - Offers open data, visualizations and analysis to help policymakers, researchers and other stakeholders gather insights on countries' climate progress.
- [Linux Foundation Energy Landscape](https://github.com/lf-energy/lfenergy-landscape) - This landscape is intended as a map to explore the open source projects in the energy sector, and also shows the member companies of the LF Energy Foundation.
- [Appropedia](https://www.appropedia.org/Welcome_to_Appropedia) - Shares knowledge to build rich, sustainable lives.
- [Open Hardware Observatory](https://en.oho.wiki/wiki/Home) - Search engine and assessment platform for sustainable open hardware.
- [Open Source Ecology](https://www.opensourceecology.org/) - Developing open source industrial machines that can be made for a fraction of commercial costs, and sharing the designs for free.
- [ProjectDrawdown](https://github.com/ProjectDrawdown/solutions) - The mission of Project Drawdown is to help the world reach "Drawdown"— the point in the future when levels of greenhouse gases in the atmosphere stop climbing and start to steadily decline, thereby stopping catastrophic climate change — as quickly, safely, and equitably as possible.
- [NOAA-Affiliated-Projects](https://github.com/NOAAGov/NOAA-Affiliated-Projects) - A list of GitHub accounts and repositories that are contributed to by National Oceanic and Atmospheric Administration staff from line offices and/or staff office throughout the organization.
- [Climatescape](https://climatescape.org/) - Discover the organizations solving climate change.
- [Airminers](http://www.airminers.org/) - The index of companies and projects mining carbon from the air for entrepreneurs, researchers, and funders to explore opportunities in carbon dioxide.
- [ENVO](https://github.com/EnvironmentOntology/envo) - A community-driven ontology for the representation of environments.
- [Open Climate Knowledge](https://github.com/petermr/climate) - An open research project for data mining Open Access papers related to Climate Change.
- [OpenClimate](https://github.com/YaleOpenLab/openclimate-demo) - An open source initiative exploring the application of distributed ledger technology and other emerging technologies, such as IoT, big data and machine learning, to the challenge of helping the world keep a transparent climate accounting system towards the climate targets.
- [ModularSensors](https://github.com/EnviroDIY/ModularSensors) - This Arduino library gives environmental sensors a common interface of functions for use with Arduino-compatible dataloggers.
- [OpenSourceSeeds](https://www.opensourceseeds.org/en) - Committed to re-establishing seed as a common good for all.
- [Transition Project](https://www.transitionproject.org/) - An Open Data Initiative designed to help enable rapid carbon abatement for cities worldwide.
- [Climate Strike Software](https://github.com/climate-strike/license) - Prevent oil and gas companies from co-opting your work and extracting more fossil fuels with this software license.
- [Ireland Energy Wiki by the National Retrofitting Modelling Group](https://energy-modelling-ireland.github.io/ireland-energy-wiki/) - Contains actively maintained listings of Irish energy-related resources.
- [Climate Impact Lab](http://www.impactlab.org/) - A team of economists, climate scientists, data engineers, and risk analysts are building the world's most comprehensive body of research quantifying the impacts of climate change, sector-by-sector and community-by-community around the world.
- [Climate change in the contiguous United States](https://github.com/washingtonpost/data-2C-beyond-the-limit-usa/) - The Washington Post's analysis of NOAA climate change data for the contiguous United States.
- [Regen Ledger](https://github.com/regen-network/regen-ledger) - Providing a structured database of claims regarding ecological state and change of state.
- [Stripe Climate Carbon Removal Purchases](https://github.com/stripe/carbon-removal-source-materials) - Source materials supporting Stripe Climate carbon removal purchases.
- [Salish Sea Wiki](https://salishsearestoration.org/) - A wiki oriented around human systems and ecological restoration (usually riparian / watershed) for the Salish Sea area (Northwestern US & BC Canada).
- [Justice40 Tool](https://github.com/usds/justice40-tool) - A tool to identify disadvantaged communities due to environmental, socioeconomic and health burdens.
- [Net Zero Tracker](https://zerotracker.net/) - Create the definitive global resource for collating, assessing and presenting the scale and quality of net zero pledges across nationals, sub-nationals, companies and other entities.
- [Credible Goals Database](https://www.embeddingproject.org/goals-database) - A public goals database containing leading sustainability goals and commitments set by large companies globally.
- [Digital Public Goods](https://github.com/DPGAlliance/publicgoods-candidates) - Accelerate the attainment of the sustainable development goals in low- and middle-income countries by facilitating the discovery, development, use of, and investment in digital public goods.
- [SWEET](https://github.com/ESIPFed/sweet) - Official repository for Semantic Web for Earth and Environmental Terminology Ontologies.
- [U.S. Climate Resilience Toolkit](https://toolkit.climate.gov/) - A website designed to help people find and use tools, information, and subject matter expertise to build climate resilience.

### Data Catalogs and Interfaces

- [Global Fishing Watch](https://globalfishingwatch.org/) - We use cutting-edge technology to visualise, track and share data about global fishing activity in near real-time and for free.
- [GlobalWindAtlas](https://globalwindatlas.info/) - Immediately start exploring windy areas.
- [GlobalSolarAtlas](https://globalsolaratlas.info/) - Start exploring solar potential.
- [Food and Agriculture Organization Map Catalog](https://data.apps.fao.org/) - Allows to easily share geographically referenced thematic information between different organizations.
- [The Subak Data Catalogue](https://data.climatesubak.org/) - Exists to make climate data more discoverable, more trusted and more connected.
- [EEA geospatial data catalogue](https://github.com/eea/geonetwork-eea) - Discover and access easily the geospatial data catalogue of the European Environment Agency.
- [Radiant MLHub Python Client](https://github.com/radiantearth/radiant-mlhub) - Open community commons for geospatial training data, machine learning models, and standards to encourage collaboration and share information.
- [owid-catalog](https://github.com/owid/owid-catalog-py) - A Pythonic API for working with Our World in Data catalog.
- [Global Environmental Database](https://db.cger.nies.go.jp/portal/geds/index) - Providing long-term monitoring data, data analysis results, output of models.
- [Resource Watch](https://github.com/resource-watch/resource-watch) - Features hundreds of data sets all in one place on the state of the planet's resources and citizens.
- [EarthData](https://earthdata.nasa.gov/) - Our vision is to make NASA's free and open Earth science data interactive, interoperable, and accessible for research and societal benefit both today and tomorrow.
- [owidR](https://github.com/piersyork/owidR) - An R Package for Interacting with Data from Our World in Data.
- [Custom Scripts Sentinel Hub](https://github.com/sentinel-hub/custom-scripts) - A repository of custom scripts to be used with Sentinel Hub.
- [OGC API - Environmental Data Retrieval](https://github.com/opengeospatial/ogcapi-environmental-data-retrieval) - A Web API that provides a family of lightweight interfaces for accessing Environmental Data resources.
- [eurostat R package](https://github.com/rOpenGov/eurostat) - R tools to access open data from Eurostat, the statistical office of the European Union.
- [giscoR](https://github.com/rOpenGov/giscoR) - An R API package that helps to retrieve data from Eurostat Geographic Information System of the Commission.
- [Digital Earth Africa Notebooks](https://github.com/digitalearthafrica/deafrica-sandbox-notebooks) - Using Earth observations to address social, environmental and economic changes on the Africa continent.
- [ESGF PyClient](https://github.com/ESGF/esgf-pyclient) -  A Python package designed for interacting with the Earth System Grid Federation system.
- [openEO](https://github.com/Open-EO/openeo-python-client) - Provides intuitive programming libraries to process a wide variety of earth observation datasets.
- [MeCCO](http://sciencepolicy.colorado.edu/icecaps/research/media_coverage/) - Open Database on the Media Coverage of Climate Change and Global Warming.
- [Climate Action Plans](https://github.com/mysociety/caps) - A simple, open database of local government climate action plan documents and emissions data.
- [earthdata](https://github.com/betolink/earthdata) - A Python library to search and access NASA datasets.
- [AI for Earth Data Sets](https://github.com/microsoft/AIforEarthDataSets) - Notebooks and documentation for AI-for-Earth-managed datasets on Azure.
- [wopr](https://github.com/wpgp/wopr) - An R package and Shiny application to provide API access to the WorldPop Open Population Repository.
- [rwlts](https://github.com/brazil-data-cube/rwlts) - Support governments in making decisions about the impact of human activities on the environment, planning the use of natural resources, conserving biodiversity and monitoring climate change.
- [The POWER Project](https://power.larc.nasa.gov/) - Provides solar and meteorological data sets from NASA research for support of renewable energy, building energy efficiency and agricultural needs.
- [Earthdata Search](https://github.com/nasa/earthdata-search) - A web application developed by NASA EOSDIS to enable data discovery, search, comparison, visualization, and access across EOSDIS' Earth Science data holdings.
- [sentinelhub-py](https://github.com/sentinel-hub/sentinelhub-py) - Download and process satellite imagery in Python using Sentinel Hub services.
- [Planetary Computer Data Catalog](https://github.com/microsoft/PlanetaryComputerDataCatalog) - Combines a multi-petabyte catalog of global environmental data with intuitive APIs and a flexible scientific environment.
- [Global Energy Monitor](https://globalenergymonitor.org/) - Studies the evolving international energy landscape, creating databases, reports, and interactive tools that enhance understanding.
- [STAC Index](https://github.com/stac-utils/stac-index) - Find STAC Catalogs, Collections, APIs, Software and Tools.
- [Eumap](https://gitlab.com/geoharmonizer_inea/eumap) - Comprises environmental, land cover, terrain, climatic, soil and vegetation layers covering the continental Europe at relatively fine spatial resolutions.
- [Open Data Science Europe Metadata Catalog](https://maps.opendatascience.eu/) - Building the Open Data Science Europe Portal, a freely-accessible viewer containing gridded layers for Europe at spatial resolutions of 30-m or better.
- [Satip](https://github.com/openclimatefix/Satip) - A library for satellite image processing providing all of the functionality necessary for retrieving, and storing EUMETSAT data.
- [MODIS](https://github.com/MatMatt/MODIS) - Provides automated access to the global online data archives LP DAAC, LAADS and NSIDC as well as processing capabilities such as file conversion, mosaicking, subsetting and time series.
- [MODIStsp](https://github.com/ropensci/MODIStsp) - An R package for automatic download and preprocessing of MODIS Land Products Time-Series.
- [ecmwf-opendata](https://github.com/ecmwf/ecmwf-opendata) - A package to simplify the download of ECMWF open data.
- [EarthDataLab.jl](https://github.com/JuliaDataCubes/EarthDataLab.jl) - Julia interface for Reading from the Earth System Datacube.
- [The CEDA Archive](https://archive.ceda.ac.uk/) - We host over 18 Petabytes of data from climate models, satellites, aircraft, met observations, and other sources.
- [Climate Data Dashboard of the ESA Climate Change Initiative](https://climate.esa.int/en/odp/#/dashboard) - Access global climate data produced through the ESA's Climate Change Initiative.
- [USGS](https://github.com/kapadia/usgs) - A python module for interfacing with the US Geological Survey's API.


### Curated Lists

- [Datasets APIs and open source projects related to Climate Change](https://github.com/KKulma/climate-change-data) - A curated list of APIs, open data and ML/AI projects on climate change.
- [Awesome Green Software](https://github.com/Green-Software-Foundation/awesome-green-software) - Research, tools, code, libraries and training to for building applications that emit less carbon into our atmosphere.
- [Awesome Sustainability Jobs](https://github.com/pogopaule/awesome-sustainability-jobs) - A curated list of companies in the sustainability sector that have jobs for devs.
- [Awesome Spectral Indices](https://github.com/davemlz/awesome-ee-spectral-indices) - A ready-to-use curated list of Spectral Indices for Remote Sensing applications.
- [Awesome Vegetation Index](https://github.com/px39n/Awesome-Vegetation-Index) - List of reference, applications of common Vegetation Indices for Multi-spectral, hyper-spectral and UAV images.
- [awesome-transit](https://github.com/CUTR-at-USF/awesome-transit) - Community list of transit APIs, apps, datasets, research, and software.
- [Awesome Coastal](https://github.com/chrisleaman/awesome-coastal) - A curated list of awesome resources for coastal engineers and scientists.
- [Awesome Agriculture](https://github.com/brycejohnston/awesome-agriculture) - Open source technology for agriculture, farming, and gardening.
- [Awesome ERDDAP](https://github.com/IrishMarineInstitute/awesome-erddap) - A data server that gives you a simple, consistent way to download subsets of gridded and tabular scientific datasets in common file formats and make graphs and maps.
- [Cryosphere Software, Data and Tools](https://github.com/awesome-cryosphere/cryosphere-links) - A prototype of a curated list of awesome data sources, models, tools and organizations related to the Cryosphere and its subspheres.
- [Awesome Clean Tech](https://github.com/nglgzz/awesome-clean-tech) - Clean technology is any process, product, or service that reduces negative environmental impacts through significant energy efficiency improvements, the sustainable use of resources, or environmental protection activities.
- [Awesome Open Climate Science](https://github.com/pangeo-data/awesome-open-climate-science) - Awesome Open Atmospheric, Ocean, and Climate Science.
- [Awesome Earth](https://github.com/philsturgeon/awesome-earth) - "What can I do about the climate crisis?" Here are 326 things you can do.
- [Awesome Open Geoscience](https://github.com/softwareunderground/awesome-open-geoscience) - Curated from repositories that make our lives as geoscientists, hackers and data wranglers easier or just more awesome.
- [Code against Climate Change](https://github.com/daviddao/code-against-climate-change) - A curated list of tech projects against climate change - hoping to inspire disruptive technological climate action.
- [Awesome Arctic Data](https://github.com/arctic-risk/awesome-arctic-data) - A curated list on data sources related to climate change in the arctic.
- [Awesome Remote Sensing Change Detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection) - List of datasets, codes, and contests related to remote sensing change detection.
- [Awesome-forests](https://github.com/blutjens/awesome-forests/) - A curated list of ground-truth forest datasets for the machine learning and forestry community.
- [awesome-earth-engine-apps](https://github.com/philippgaertner/awesome-earth-engine-apps) - An awesome list of all available Google Earth Engine Apps and user-specific App Galleries.
- [awesome-gee-community-datasets](https://github.com/samapriya/awesome-gee-community-datasets/) - Community Datasets & Data Commons in Google Earth Engine.
- [Urban & Regional Planning Resources](https://github.com/APA-Technology-Division/urban-and-regional-planning-resources) - Community list of data & technology resources concerning the built environment and communities.
- [Open Source Python Packages in Hydrology](https://github.com/raoulcollenteur/Python-Hydrology-Tools) - Holds a list of open source Python packages interesting to Hydrologists.
- [PO.DAAC](https://podaac.jpl.nasa.gov/datasetlist) - NASA Earth Observing System Data and Information System data center managed by the Earth Science Data and Information System Project.


## Contributors

<a href="https://github.com/protontypes/open-sustainable-technology/graphs/contributors">
  <img width="70%" src="https://contrib.rocks/image?repo=protontypes/open-sustainable-technology" />
</a>

## Artwork and License

Animation created with [An Animated Map of the Earth](https://github.com/eleanorlutz/earth_atlas_of_space) by [Eleanor Lutz](https://eleanorlutz.com/)

The artwork included in this repository are shared under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.

This work and all contributions to it are released into terms of the CC0 1.0 Universal Public Domain if not otherwise noted.

[![CC0](https://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)
