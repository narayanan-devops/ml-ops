#  Cluster Explanation

we are going to create two node groups for Kubernetes worker nodes:

1.  _General_  node group - autoscaling group with Spot instances to run Kubernetes system workload and non-GPU workload
2.  _GPU_  node groups - autoscaling group with GPU-powered Spot Instances, that can scale from 0 to required number of instances and back to 0.  This will reduce cost for operating the GPU nodes.

EKS  Config explanations:
-   `ami: auto`  -  `eksctl`  automatically discover latest EKS-Optimized AMI image for worker nodes, based on specified AWS region, EKS version and instance type. See  [Amazon EKS-Optimized AMI](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html#gpu-ami)  chapter in User Guide
-   `instanceType: mixed`  - specify that actual instance type will be one of instance types defined in  `instancesDistribution`  section
-   `iam`  contains list of predefined and in-place IAM policies;  `eksctl`  creates a new  [IAM Role](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)  with specified policies and attaches this role to every EKS worker node. There are several IAM policies you are required to attach to every EKS worker node, 
	- More  details:  [Amazon EKS Worker Node IAM Role](https://docs.aws.amazon.com/eks/latest/userguide/worker_node_IAM_role.html)  section in User Guide and  [`eksctl`  IAM policies](https://eksctl.io/usage/iam-policies/)  documentation
-   `instancesDistribution`  - specify mixed instance policy for EC2 Auto Scaling Groups. 
	- More  details:  [MixedInstancesPolicy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_MixedInstancesPolicy.html)  documentation
-   `spotInstancePools`  - specifies number of Spot instance pools to use,  
	-  More  details: [Spot  instance Pools](https://alexei-led.github.io/post/eks_gpu_spot/#Spot-Instance-Pools)
-   `tags`  - AWS tags added to EKS worker nodes
    -   `[k8s.io/cluster-autoscaler/enabled](http://k8s.io/cluster-autoscaler/enabled)`  will use this tag for Kubernetes Cluster Autoscaler auto-discovery
-   `privateNetworking: true`  - all EKS worker nodes will be placed into private subnets
- `taints` - Used to skip  the scheduling of non-gpu workloads on GPU nodes.
##### EKS Optimized AMI image with GPU support

In addition to the standard Amazon EKS-optimized AMI configuration, the GPU AMI includes the following:

-   NVIDIA drivers
-   The  `nvidia-docker2`  package
-   The  `nvidia-container-runtime`  (as the default runtime)

Also the EKS  creation logs(cluster-creation.log)  shows that both the nodegroup selects  two  different  AMIs to  show  one  AMI is  EKS accelerated AMI.

# Cluster Creation

1. Setup the AWS access in your machine or the CI system where it has access for creating the cluster.
2. Use the file `01-cluster.yaml`  to create the cluster.
	```
	eksctl create -f 01-cluster.yaml
	```
3. The above process will create the cluster and update kubeconfig in your local kubeconfig location.  Attached the log in this current directory as log: `cluster-create.log`
4. After the cluster creation, we need to install the cluster autoscalar deployment. So when the GPU request came in, this deployment will take care of spawning the GPU node.  Also takes care of scaling up  and down of non gpu worker  group also.
	```
	kubectl  create -f 02-cluster-autoscaler.yaml
	```	