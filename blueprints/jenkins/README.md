# jenkins

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

Jenkins is a free, open-source automation server that helps developers build, test, and deploy software by automating repetitive tasks in the software delivery pipeline.

## Requirements

- The host Docker socket is deliberately excluded. Use separately configured build agents.
- Complete Jenkins unlock and administrator setup before sharing the URL. Back up JENKINS_HOME.

## Credentials

No pre-deployment credential references.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/jenkinsci/jenkins
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/jenkins

Application license: Review upstream license and edition.
