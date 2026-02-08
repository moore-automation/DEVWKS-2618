# Conclusion

In this workshop we explored how Cisco NSO can be integrated into a GitLab CI/CD pipeline to automate the development, testing, and deployment of network services.

Here's what we covered:

* **Connectivity & Environment** — Connected to the NSO Sandbox via VPN, verified access to the development and production NSO instances, and explored the lab topology.
* **Working with GitLab** — Created a `.gitlab-ci.yml` pipeline definition, committed it to the repository, and observed stages and jobs executing in GitLab.
* **Pipeline-Driven NSO Service Development** — Created a feature branch, updated the NSO loopback service template, and replaced the pipeline with a real CI/CD workflow that compiles, loads, and tests the package against the development NSO environment.
* **Adding Pre-Checks** — Added syntactical validation with xmllint and environmental checks with Robot Framework to the `.pre` stage, catching errors before the main pipeline runs.
* **Applying a Service** — Used a Python script with RESTCONF to apply the loopback service to a device in the development NSO instance, automated through the pipeline.
* **Compliance Reporting** — Created and ran an NSO compliance report to verify that the applied service configuration matches the intended state, providing visibility and assurance of deployment success.

This process demonstrates the complete lifecycle of developing, testing, and deploying network service changes within a CI/CD framework — ensuring reliability, consistency, and efficiency in managing network infrastructure.

We hope you now feel comfortable with the role these tools play in modern network automation and CI/CD workflows. Thank you for participating!

---