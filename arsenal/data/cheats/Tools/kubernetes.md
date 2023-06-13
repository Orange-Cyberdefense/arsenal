# kubernetes

% kubernetes, k8s, kubectl

#platform/linux #target/local #cat/UTILS 

## Print all contexts
```
kubectl config get-contexts
```

## Print current context of kubeconfig
```
kubectl config current-context
```

## Set context of kubeconfig
```
kubectl config use-context <context>
```

## Print resource documentation
```
kubectl explain <resource>
```

## Get nodes (add option '-o wide' for details)
```
kubectl get nodes
```

## Get namespaces
```
kubectl get namespaces
```

## Get pods from namespace (add option '-o wide' for details)
```
kubectl get pods -n <namespace>
```

## Get pods from all namespace (add option '-o wide' for details)
```
kubectl get pods --all-namespaces
```

## Get services from namespace
```
kubectl get services -n <namespace>
```

## Get details from resource on namespace
```
kubectl describe <resource>/<name> -n <namespace>
```

## Print logs from namespace
```
kubectl logs -f pods/<name> -n <namespace>
```

## Get deployments
```
kubectl get deployments -n <namespace>
```

## Edit deployments
```
kubectl edit deployment/<name> -n <namespace>
```

## Drain node in preparation for maintenance
```
kubectl drain <name>
```

## Mark node as schedulable
```
kubectl uncordon <name>
```

## Mark node as unschedulable
```
kubectl cordon <name>
```

## Display resource (cpu/memory/storage) usage
```
kubectl top <type>
```