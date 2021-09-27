# Detecting-security-attacks-in-cyber-physical-systems-a-comparison-of-mule-and-WSO2-intelligent-IoT-
This repository includes what is needed to replicate the experiments in the "Detecting security attacks in cyber-physical systems: a comparison of mule and WSO2 intelligent IoT architectures" article

you can find the datasets and patterns in this repository: https://data.mendeley.com/datasets/fvb9pp5xsh/1

This repository contains the following items:
- simulator.py, is used to send events from CSV files to CEP engines.
- Esper (folder), contains what you need to deploy Mule.
  -install_Anypointstudio.pdf, explains how to install anypoint studio. It must be installed before deploying Mule.
  -Mule deployment instructions.txt, explains step by step how to deploy mule.
  -IoTSecurityAttacks-patterns.epl, is the file with all the functional patterns.
  -mule_project.zip, is the Mule project.
  -FeatureAnomaly.epl and ProtocolAnomaly.epl, are separate specific patterns, it is not necessary to add it.
- Siddhi (folder), contains what you need to deploy WSO2.
  -Wso2-sp Instalaltion and deployment instructions.txt, explains how to install and deploy WSO2.
  -wso2application.siddhi, is the file with all the functional patterns.
  -FeatureAnomaly.siddhi and ProtocolAnomaly.siddhi, are separate specific patterns, it is not necessary to add it.
  
