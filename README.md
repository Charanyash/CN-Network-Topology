# CN-Network Topology Project 

Welcome to the Network Topology Project repository! This repository contains all the necessary resources related to our project focused on network topology analysis. Below, you'll find an overview of the repository structure and how to navigate through its contents.

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Data](#data)
  - [Raw Data](#raw-data)
  - [Processed Data](#processed-data)
- [Code](#code)


## Project Overview

Our project aims to analyze network topology using various data analysis and visualization techniques. We explore raw network data, process it, and generate insights through visualizations and data-driven findings.

## Repository Structure

The repository is organized into the following main sections:

- **Raw Data**: Contains Raw Data (10 folders each contain 5 .txt files) generated using traceroute command in linux.
- **Visualization Data** : Contains data used for visualization processed used dataextraction.ipynb file
- **Code**: Includes scripts and notebooks for data processing, analysis, and visualization.
- **Visualization**: Generated the visuailization using graphviz.

## Data

### Raw Data

The raw data directory contains the original network data files that were collected for analysis. These files are generated as txt files.

### Visualization Data

In the processed data directory, you'll find the cleaned and transformed versions of the raw data. These processed datasets are ready for analysis and visualization.

## Code

The code directory is where you'll find all the scripts and notebooks related to our data analysis pipeline. This section is further organized as follows:

- **TraceRouteAutomation.ipynb** : Used to trace the routes from each source to destination
- **DataExtraction.ipynb**: Used to extract key paramaters like ASN, IP Range, IP Location, ..etc from raw data.
- **Visualization.ipynb**:  Used to generate the visualization.pdf which uses graphiz library to view the network topology.

