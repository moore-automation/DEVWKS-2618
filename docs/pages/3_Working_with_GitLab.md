# **Working with GitLab**

## GitLab Basics

This workshop uses [GitLab](http://devtools-gitlab.lab.devnetsandbox.local){:target="_blank"} as the source control and CI/CD platform. Before we build a pipeline, here are the key concepts you'll work with:

**Repositories** — GitLab organises code into projects, each backed by a Git repository. Changes are tracked through commits, and branches let you work on features without affecting the main codebase.
{: .card }

**Web IDE** — GitLab includes a browser-based editor so you can create and modify files directly, without needing a local development environment.
{: .card }

**CI/CD Pipelines** — A pipeline is a set of automated steps that run every time you push a change. In GitLab, pipelines are defined in a YAML file called `.gitlab-ci.yml` at the root of your repository.
{: .card }

**Stages & Jobs** — A pipeline is organised into stages (e.g. `build`, `test`, `deploy`). Each stage contains one or more jobs that run in parallel. Stages run sequentially — if any job in a stage fails, the pipeline stops.
{: .card }

**Runners** — Jobs are executed by runners. In the sandbox, a runner is already registered and configured with the tools you need.
{: .card }

For more details, see the GitLab CI/CD [documentation](https://docs.gitlab.com/ee/ci/yaml/){:target="_blank"}.

---

## Define the CI/CD Pipeline

In this project repository, you will store your files and add a `.gitlab-ci.yml` file that GitLab uses to define your pipeline. This file describes the stages and jobs that make up your automation workflow. Storing everything in the repository enables change tracking, collaboration, and easy rollback.

### **Task 1:** Open the Web IDE

<div class="instruction" markdown>

Open up the Default Project in [GitLab](http://devtools-gitlab.lab.devnetsandbox.local/developer/Default_Project){:target="_blank"} and select the Web IDE from the Edit dropdown.

</div>

![Default Project Page](../assets/create_gitlab_ci.jpg)

### **Task 2:** Create a New GitLab CI File

Next, create the pipeline definition in the GitLab repository. This triggers an initial execution of the pipeline because you are adding the `.gitlab-ci.yml` file to the repository. No changes will be made to the network devices yet, as you have not made any changes to the definition files.

![New File](../assets/new_file.jpg)

To save time, we've provided an example pipeline below. Create your `.gitlab-ci.yml` and copy and paste this into your new CI file:
{: .instruction }

```yaml
# Define the stages of the pipeline
stages:
  - build
  - test
  - deploy_prod

# Pre-requisite checks — runs before all stages
runner pre-reqs:
  stage: .pre
  when: on_success
  script:
    - echo "(Pre-reqs) Checking the environment"

# Step to compile the package in the development NSO environment
package-compilation:
  stage: build
  when: on_success
  except:
    - main
  script:
    - echo "(Build) Loading and compiling packages in the NSO dev container"

# Step to load the compiled package into the testing NSO environment
package-load:
  stage: build
  when: on_success
  except:
    - main
  script:
    - echo "(Build) Loading compiled packages to testing env NSO"
  dependencies:
    - package-compilation

# Step to test the loopback service in the NSO testing environment
test-loopback-service:
  stage: test
  when: on_success
  except:
    - main
  script:
    - echo "(Test) Deploying service in the NSO test env"
  dependencies:
    - package-load

# Step to clean up the development environment
cleanup:
  stage: .post
  only:
    - main
  allow_failure: true
  script:
    - echo "(Cleanup) Removing files from NSO Dev"

# Step to load the package tarball onto production NSO
load-production:
  stage: deploy_prod
  when: on_success
  only:
    - main
  script:
    - echo "(Load) Copying tarball to production NSO"

# Step to deploy the package on the production NSO environment
deploy-production:
  stage: deploy_prod
  when: on_success
  only:
    - main
  script:
    - echo "(Deploy) Deploying package on production NSO"
  dependencies:
    - load-production
```

!!! info "Understanding the pipeline flow"
    This pipeline uses `except` and `only` rules to control which jobs run on which branches:

    <div class="card" markdown>

    - **Feature branches** — the `build` and `test` stages run (`except: main`), validating your changes against the development NSO environment.
    - **Main branch** — only `deploy_prod` and `cleanup` run (`only: main`), deploying the validated package to production.
    - **Every push** — the `runner pre-reqs` job runs first (`.pre` stage) to verify the environment is ready.

    </div>

    The `dependencies` keyword ensures jobs run in the correct order — for example, `package-load` waits for `package-compilation` to complete.

For more details on the pipeline configuration, see the GitLab [documentation](https://docs.gitlab.com/ee/ci/yaml/){:target="_blank"}.

Commit your changes to the main branch by selecting the Source Control icon on the left with an appropriate message.
{: .instruction }

### **Task 3:** Examine the Pipeline Job

---

<div class="instruction" markdown>

Navigate to [Default Project Pipelines](http://devtools-gitlab.lab.devnetsandbox.local/developer/Default_Project/-/pipelines){:target="_blank"}.

</div>

Since you committed directly to the `main` branch, only the `deploy_prod` stage will execute — the `build` and `test` stages are skipped because of the `except: main` rules.


![GitLab pipeline page](../assets/dummy_pipeline.jpg)

To verify that the script executed properly, open the job details.
{: .instruction }

![Gitlab pipeline dummy job](../assets/pipeline_dummy_job.jpg)

To view detailed information about each stage, click on the `passed` button in the status column.
{: .instruction }

![Gitlab stages pipeline jobs](../assets/Gitlab_pipeline_stages_jobs.png)

---
