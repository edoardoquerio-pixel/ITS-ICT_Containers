# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless Kubernetes Networking

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless Kubernetes Networking.pdf`
**Tipo:** `.pdf`
**Dimensione:** 2164.2 KB
**Ultima modifica:** 02/07/2026 09:27

---

Kubernetesnetworking

Podnetwork 
228


Kubernetesnetworks
229
Nodesnetwork: la rete a cui sono collegati i nodi del cluster (es: 192.168.1.0/24)Podnetwork: la rete (software-defined) su cui vengono attaccati i Pod(es: 10.244.0.0/16)

Podnetwork single node
230


Podnetwork multi node
231


Podnetwork
232
X

Come raggiungere un Pod
233


Come raggiungere un Pod
234


Services
235


Services network
236
▪Service network: la rete (software-deﬁned) su cui vengono attaccati i Service (es: 10.96.0.0/16)

Tipologie di Services
237


Service NodePort
238


Service NodePort
239
Servono per esporre i Podal do fuori del cluster Kubernetes.Aprono una porta su tutti i nodi e la redirigonosulla porta aperta dai Pod.

Service NodePort
240


Service NodePort
241


Service NodePort
242


Service NodePort
243


Service NodePort
244


Service NodePort
245


Service NodePort
246


Service ClusterIP
247
Servono per fare comunicare i Podfra di loro, non sono raggiungibili dall’esterno del cluster.

Service ClusterIP
248
ClusterIPService
ClusterIPService

Service ClusterIP
249


Service ClusterIP
250


Service ClusterIP
251


Service LoadBalancer
252


Services
253


Services
254


LAB
255
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 23 –ServiceAssignment06 -ExposeDeploymentsusingServices

Ingress
256


Ingress
257


Lab 24 -Ingress
258
traefik-ingress-service (NodePort)
traefik-ingressapiVersion: extensions/v1beta1kind: Ingress…
nginx-service (ClusterIP) whoami-service (ClusterIP)whoami-deploymentnginx-deployment

LAB
259
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 24 –IngressAssignment07 -ExposeDeploymentsusingIngress
