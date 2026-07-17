# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless kubernetes intro

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless kubernetes intro.pdf`
**Tipo:** `.pdf`
**Dimensione:** 4032.0 KB
**Ultima modifica:** 02/07/2026 09:24

---

Software DeveloperUnità Formativa (UF): Containers, Microservizi -ServerlessDocente: Denis MaggiorottoTitolo argomento: Introduzione a kubernetes


KubernetesL’orchestratore di container per eccellenza


154
Dal monolite ai micro servizi


155
Lo sviluppo diventa agile


156
WaterfallVs Agile


157
Il movimento DevOps


158
I principi del DevOps(CALMS)


159
Gli strumenti del DevOps(solo una piccola parte)


160
Le applicazioni diventano multi container (microservices)


Troppi container?
161


Perché Kubernetes
162


Cos’è Kubernetes
163
Kubernetesis an open sourcecontainer orchestration engine for automating deployment, scaling, and management of containerized applications. The open sourceproject is hosted by the Cloud Native Computing Foundation.


Kubernetesdal 2017 è il secondo progetto OO dopo Linux
164


LAB
165
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 18 –Kubernetes

L’architettura di Kubernetesed il Pod

L’architettura di Kubernetes
167


L’architettura di Kubernetes
168


L’architettura di Kubernetes
169


L’architettura di Kubernetes
170


Eseguire un’applicazione su Kubernetes
171


KubernetesAPIs
172


KubernetesAPIs
173


KubernetesAPIs
174


KubernetesAPIs
175


Minikube
176


Pods
177


Multi container Pods
178
E’ possibile inserire più di un Container all’interno del Pod.Questa pratica è utile per avere uno o più Containers che supportano il Container principale (Sidecar pattern)


Podsreplicas
179
Quando il carico utente aumenta, la pratica comune è quella di aumentare il fattore di replica dei Pod(le istanze) e non il numero di container in un singolo Pod

Runningthe first Pod
180


Runningthe first Pod
181


Podscon YAML
182
Ogni risorsa Kubernetespuò esser descritta in YAML, la cui struttura di base è formata dalle seguenti chiavi (tutte obbligatorie) 

Podscon YAML
183
apiVersionrappresenta la versione delle API che useremo per creare la nostra risorsa (in questo caso un Pod). E’ necessario specificare l’apiVersioncorretta per ogni risorsa (vedi tabella).


Podscon YAML
184
kindrappresenta il tipo di risorsa da creare. In questo caso il Pod


Podscon YAML
185
metadataracchiude delle informazioni fondamentali per il Pod. Qui vediamo il nome (obbligatorio) ed una label(app). Parleremo delle labelin seguito.


Podscon YAML
186
spec(specification)racchiude i containers che il Podavrà al suo interno. La struttura di specdipende dal tipo di risorsa (in questo caso Pod).


Podscon YAML
187
$ kubectlcreate –f pod-definition.yml


Altri Podscon YAML
188
Single containerMulti container

LAB
189
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 19 –Pod

ReplicationController, ReplicaSete Deployment

Podlifecycle(Podstatus)
191


ReplicationController(deprecato in favore di ReplicaSet)
192


ReplicationController
193


ReplicationController
194


ReplicationController
195
Per specificare il numero di repliche aggiungiamo:

ReplicationController
196
$ kubectlcreate –f rc-definition.yml
$ kubectlget replicationcontroller
$ kubectlget pods

LAB
197
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 20 –ReplicationController

ReplicaSet
198


ReplicaSet
199
Con il Selector, ReplicaSetpuò anche gestire Podche non ha creato


ReplicaSet
200
$ kubectlcreate –f replicaset-definition-definition.yml
$ kubectlget replicaset
$ kubectlget pods

Labelsand Selectors
201


Labelsand Selectors
202
tier
tier

Labelsand Selectors
203


Labelsand Selectors
204


Labelsand Selectors
205


Scaling
206
$ kubectlreplace –f replicaset-definition.yml


Scaling
207
$ kubectlscale –replicas=6 replicaset-definition.yml$ kubectlscale –replicas=6 replicasetmyapp-replicaset

LAB
208
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 21 –ReplicaSet
