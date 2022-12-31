
# Dependencies Installation

 This document will guide you with the dependencies installed for testing the repository.

  ## eksctl

****Binary to launch the K8s cluster.****
 
To download the latest release for mac & Linux, run:

```
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

sudo mv /tmp/eksctl /usr/local/bin
```
Alternatively, macOS users can use [Homebrew](https://brew.sh/):

 ```
 brew tap weaveworks/tap
brew install weaveworks/tap/eksctl
```
 
or [MacPorts](https://www.macports.org/):

```
port install eksctl
```
and Windows users can use [chocolatey](https://chocolatey.org/):

 ```
chocolatey install eksctl
```
or [scoop](https://scoop.sh/):
```
scoop install eksctl
```

For more info on this installation please follow the below links:
1. https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html
2. https://eksctl.io/introduction/?h=install#installation

## kubectl

  **Binary used to communicate to EKS cluster's API server.**

### Install kubectl binary with curl on Linux

Download the latest release with the command:
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && chmod +x kubectl && sudo mv kubectl /usr/local/bin
```

**### Install kubectl binary on Mac**

For Intel Chips:
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl" && chmod +x kubectl && sudo mv kubectl /usr/local/bin
```

For M1 Chips:
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl" && chmod +x kubectl && sudo mv kubectl /usr/local/bin
```

For more info on this installation please follow the below links:
1. https://kubernetes.io/docs/tasks/tools/#kubectl