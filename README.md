# Security Pulse Monitor (SPM)

Live MeDo App: (https://app-blvqgqf4hk3l.appmedo.com/)

Watch Demo Video: https://youtu.be/23g5CE6OtNw?si=RCRf6ACVaJtsc_dX

## About The Project
As developers, we face an invisible enemy every day: Security bugs. A single leaked API key in a YAML file or a catastrophic Regular Expression (ReDoS) can crash a server or expose user data. We realized that traditional linters only check syntax and manual security audits take hours, creating a massive "security tax." We wanted to build a world where creators can build without boundaries. That inspired us to create Security Pulse Monitor (SPM)—a real-time, zero-lag security plugin for the MeDo platform that acts as an invisible shield.

(Note: Built entirely using the MeDo platform's AI generation capabilities during the Build with MeDo Hackathon.)

## Key Features
The plugin performs real-time auditing by scanning files quietly in the background. It features AST auto-remediation to intelligently rewrite code without breaking logic. Our resilient batch auto-fix engine treats every file independently to prevent rollbacks. Additionally, developers can press Ctrl+D to activate the multi-cursor AST fix preview to see the exact locations our engine is going to fix across the code.

## Files in this Repository
This repository contains our strategic pitch deck presentation named security_pulse_master_deck.html, along with api.py, which is the demo vulnerable file we used in our video presentation.
