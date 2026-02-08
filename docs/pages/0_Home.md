# **Homepage**

Welcome! You don't need to create a project from scratch for this workshop. Instead, we'll work with a sample repository from the updated NSO Sandbox.

In this project, you'll discover the real benefits of NetDevOps by exploring open-source testing and automation tools. You'll build your own setup and see how implementing CI/CD concepts can improve the quality and reliability of deployments through thorough testing and version control.

### **Section 1:** Introduction to CI/CD, Automation, and NSO Verification

In this section, we'll introduce key concepts such as Continuous Integration and Continuous Deployment (CI/CD), automation, and the basics of NSO (Network Services Orchestrator). We'll also discuss source version control, focusing on GitLab.

### **Section 2:** CI/CD Pipelines with NSO

Here, we'll dive into the concept of a CI/CD pipeline. You'll learn how to create, execute, and trigger automated processes, and see how CI/CD pipelines can be used for developing and deploying NSO service packages.

### **Section 3:** Automated Testing

This section covers the role of automated testing within the CI/CD pipeline. We'll demonstrate how to implement automated tests for NSO service packages using Robot Framework and basic pre-commit checks, ensuring they meet requirements and function correctly before deployment.

---

## **Guide Conventions**

Throughout this workshop you'll see two styles of highlighted block:

<div class="instruction" markdown>

**Instruction** — A green block like this tells you to **do something**. Follow the steps described to proceed with the lab.

</div>

**Informational** — A blue block like this provides background context or explains a concept. You don't need to act on these, but they'll help you understand what's happening.
{: .card }

---

## **Lab Topology**

---

Here's a brief overview of the dCloud setup used in this lab:

<div class="card" markdown>

- **Development NSO:** The development NSO deployment manages network devices within the CML.
- **Production NSO:** The main NSO deployment manages network devices within the CML.
- **Developer Workstation (DevBox):** A Linux VM for developing new services, running tests, and initiating pipelines.
- **Developer Tools (DevTools):** Another Linux VM equipped with various tools needed for lab activities.

</div>

![Lab Topology](../assets/topology_lab.jpg)
