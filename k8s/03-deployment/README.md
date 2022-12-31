#  Application  deployment

1. Use kubectl  to deploy the manifest:
	```
	kubectl apply -f deployment.yaml
	```
2. Once the  deployment is created, you can see the deployment will trigger the autoscalar to launch the  GPU  optimized  node.
![Image of Trigger](https://photos.google.com/share/AF1QipOTinms5oNu1eGAPQWvivDaYyjVqOCVUhNEMUlsA42GlDg021GhWz655U-QNYc5Fg?key=Vk9vNW1lc3hEb21GMXhkb1p5UkMyV3laZ0tUb2Vn)

3. We  can  then port-forward the service which is part of deployment  to serve the request:
	```
	narayanan-sugumar@Narayanan-MacBook-Pro:~|⇒  kubectl port-forward service/translation-service 9527:9527
	Forwarding from 127.0.0.1:9527 -> 9527
	Forwarding from [::1]:9527 -> 9527
	```
4. Run the curl request to check  the response.
![API response](https://photos.app.goo.gl/9i3iTnfvNFqnYvRz8)


#  Manifest explanation

1. Manifest has  both  service and  deployment  config  for deploying and  exposing the  service.
2. The service  will  use the ClusterIP to expose  the  service.
3. Also we  are  using  nodeselector  and taint to place the deployment on GPU node.
4. It   has one request  of GPU core to have  inference running with the  GPU utilization.