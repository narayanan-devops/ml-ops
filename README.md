#  Submission details

1. Submission document structure .  Each sub directory has readme file to explain about the contents in the directory.
	```
	├── README.md
	├── app
	│   ├── Dockerfile
	│   ├── README.md
	│   ├── main.py
	│   ├── openapi.json
	│   ├── requirements.txt
	│   └── swagger.yaml
	└── k8s
	    ├── 00-deps
	    │   └── README.md
	    ├── 01-cluster
	    │   ├── 01-cluster.yaml
	    │   ├── 02-cluster-autoscaler.yaml
	    │   ├── README.md
	    │   └── cluster-create.log
	    └── 03-deployment
	        ├── README.md
	        └── deployment.yaml
	```
2. Code are commented inline and explained the usage of the configs in the readme file too.
3. App directory contains the code and requirements for running the application.
4. K8s directory has details  about the dependencies  installation, cluster creation and its config, and deployment configs and how to use those configs for acheive the target.


## High Level details:

1. At the python code,  bundled the  models into the docker image  so as to read from the local storage instead of downloading it everytime, to reduce the boot time of the container.
2. Used K8s cluster with two different nodegroups for  high availability. One for  the cluster components and other for  GPU workloads.
3. Used GPU for  good inference  performance and  used taints and toleration  combination to use the resources in the best way.
4. Used cluster autoscalar to  scale up and down  the GPU nodes only whenever it is necessary to save cost.
5. All the K8s worker nodes are spot nodes to have cost reduction and  get most performance at better cost.
6. Added more instance pool  of spot nodes to achieve less spot interruption rate.
7. Added required addons like, cluster autoscalar role, ALB ingress controller, EFS, FSX controller as part of the EKS addon itself.

##  Gotchas / To Do / What  can be better
1. Add  inference AWS instance(Inf instance family)  to have better cost to performance.
2. Use sagemaker to wrap the code to run with AWS way of managing the ML model.
3. Use EFS for model storage, so  that we can multi attach the volume on EKS nodes with EFS CSI drivers. So we can download once and use it across.
4. If we move to sagemaker, we can host the model at s3 itself.


# ML Assignment
Please implement a translation inference service that runs on Kubernetes and provides a RESTful API on port 9527.

The translation model is `M2M100`, and the example can be found in `app/translation_example.py`.

You should first fork this repository, and then send us the code or the url of your forked repository via email. 

**Please do not submit any pull requests to this repository.**


## Delivery
- **app/Dockerfile**: To generate an application image
- **k8s/deployment.yaml**: To deploy image to Kubernetes
- Other necessary code

## Input/Output

When you execute this command:
```bash
curl --location --request POST 'http://127.0.0.1:9527/translation' \
--header 'Content-Type: application/json' \
--data-raw '{
    "payload": {
        "fromLang": "en",
        "records": [
            {
                "id": "123",
                "text": "Life is like a box of chocolates."
            }
        ],
        "toLang": "ja"
    }
}'
```

Should return:
```bash
{
   "result":[
      {
         "id":"123",
                
      }
   ]
}
```

## Bonus points
- Clean code
- Scalable architecture
- Good inference performance
- Efficient CPU/GPU utilization
