# Container Docker Kubernetes — Appunti Strutturati per Sessione

> **Corso:** ITS ICT Cloud Specialist 2025-2027
> **Materia:** 17_Container_Docker_Kubernetes

---

## Indice delle Sessioni

1. [Introduzione a Container e Docker](#introduzione-a-container-e-docker)
2. [YAML per DevOps](#yaml-per-devops)
3. [Creazione Immagini Docker](#creazione-immagini-docker)
4. [FS Layering e Volumi](#fs-layering-e-volumi)
5. [Docker Compose](#docker-compose)
6. [Microservices](#microservices)
7. [Kubernetes — Introduzione](#kubernetes--introduzione)
8. [Kubernetes — Deployments](#kubernetes--deployments)
9. [Kubernetes — Networking](#kubernetes--networking)

---

## Introduzione a Container e Docker

### Materiali di Riferimento


## YAML per DevOps

### Materiali di Riferimento

- [`09_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_YAML.md`](00_Note/09_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_YAML.md)

#### Contenuto Estratto

---

Introduzione a YAML

Cos’è YAML
117
YAML, che sta per “YAML Ain’tMarkup Language”, è un linguaggio per la rappresentazione delle informazioni. Nasce come risposta, leggera e leggibile, a XML ed è molto utilizzato soprattutto per la costruzione di file di configurazione. A differenza del XML, per definire delle strutture, non si utilizzano i tagannidati, bensì gli spazi dell’indentazione.

XML vs JSON vs YAML
118


Inizio del documento
119


Chiavi e valori
120


Stringhe
121


Stringhe mult...

---

## Creazione Immagini Docker

### Materiali di Riferimento


## FS Layering e Volumi

### Materiali di Riferimento


## Docker Compose

### Materiali di Riferimento


## Microservices

### Materiali di Riferimento

- [`10_ITS-ICT_2025-2027-CloudSpecialist_Microservices_intro.md`](00_Note/10_ITS-ICT_2025-2027-CloudSpecialist_Microservices_intro.md)

#### Contenuto Estratto

---

2025-2027 Cloud specialistUF: Containers-Microservices-ServlerlessDocente: Denis Maggiorotto

Il docenteDenis Maggiorotto

Denis Maggiorotto•ManagingDirectorand shareholder@ Sunnyvale S.r.l.•20 yearsof experiencein ICT consulting•Senior Software / Enterprise Architect @ Major companies in public utility, telco, TV broadcastingand banking sector•Oracle UniversityPrincipalInstructorregardingJava technologies(Micro Edition, Standard Edition and Enterprise Edition) and Oracle'smiddlewareproduct...

---

## Kubernetes — Introduzione

### Materiali di Riferimento


## Kubernetes — Deployments

### Materiali di Riferimento

- [`02_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_deployments.md`](00_Note/02_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_deployments.md)

#### Contenuto Estratto

---

Software DeveloperUnità Formativa (UF): Containers, Microservizi -ServerlessDocente: Denis MaggiorottoTitolo argomento: KubernetesDeployments e Services


Deployment
210


Deployment
211


Deployment
212


Deployment
213


Deployment
214


Deployment
215


Deployment
216


Deployment
217


Deployment
218


Deployment
219


Deployment
220
maxUnavailable: the maximum numberof podsthatcan be unavailableduringthe update process. Thiscan be an absolutenumberor percentageof the replicascount; the...

---

## Kubernetes — Networking

### Materiali di Riferimento

- [`08_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_networking.md`](00_Note/08_ITS-ICT_2025-2027-CloudSpecialist_ContainersMicroservicesServlerless_networking.md)

#### Contenuto Estratto

---

Cloud SpecialistUnità Formativa (UF): Containers Microservizi ServerlessDocente: Denis MaggiorottoTitolo argomento: Container networking


Gestione della rete all'interno dei container

None network
46


None network
47
$ dockerrun-d --net none busyboxsleep10003a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3$ dockerexec-it3a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3 /bin/ash/ # ping8.8.8.8PING 8.8.8.8 (8.8.8.8): 56 data bytesping: sendto: Network isunreac...

---

