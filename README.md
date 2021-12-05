# perf-lab

Cloud Performance Example Lab

Example based on [cilium demo](https://docs.cilium.io/en/v1.9/gettingstarted/memcached/).

## Building components

### Prerequisites

Install and set up minikube

    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube
    
    minikube start
    minikube dashboard # optional (CTRL+Z and then 'bg')

Set up weavescope

    git clone https://github.com/weaveworks/scope --depth 1 --branch=master ~/scope
    cd scope
    kubectl apply -f examples/k8s
    kubectl port-forward svc/weave-scope-app -n weave 4040:80

Finally, point your browser to [http://127.0.0.1:4040]([http://127.0.0.1:4040]).

### a-wing, x-wing and tracker

Docker build with

    eval $(minikube docker-env)
    docker build . -t a-wing:latest -f a-wing/Dockerfile
    docker build . -t x-wing:latest -f x-wing/Dockerfile
    docker build . -t tracker:latest -f tracker/Dockerfile

To run locally add `; docker run -it --name <img_name> --rm <img_name>:latest` to the end of the build lines.

### Deploy on minikube

    kubectl apply -f sw-setup.yaml
