# CI/CD Assessment

This project demonstrates a complete CI/CD workflow for a FastAPI application, covering containerization, automated validation, and deployment configuration.

## Overview

The repository includes:
- a Python FastAPI application
- Docker configuration for containerized deployment
- dependency management with UV
- automated testing and code quality checks
- Azure DevOps pipeline configuration
- Kubernetes deployment manifests

## Objectives

The goal of this project was to implement a production-style delivery flow using modern DevOps practices, including:
- clean branching strategy
- reproducible container builds
- runtime configuration through environment variables
- automated linting and testing
- deployment-ready Kubernetes resources

## Workflow

The application was structured to follow a typical development lifecycle:
1. Work on feature branches
2. Merge into a development branch for validation
3. Run CI checks for formatting, linting, and tests
4. Build and push a Docker image
5. Deploy the application using Kubernetes manifests

## Technologies

- Python
- FastAPI
- UV
- Docker
- Azure DevOps
- Kubernetes
- Ruff
- Pytest

## Skills Demonstrated

- CI/CD pipeline design
- Dockerization
- Dependency management
- Automated testing
- Infrastructure-as-code concepts
- Deployment configuration for cloud-native environments

## Outcome

This project showcases a practical understanding of how to build, validate, and deploy an application using modern DevOps tools and workflows.
