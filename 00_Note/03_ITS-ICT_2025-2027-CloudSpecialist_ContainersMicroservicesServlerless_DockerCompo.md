# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless DockerCompose

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless DockerCompose.pdf`
**Tipo:** `.pdf`
**Dimensione:** 538.3 KB
**Ultima modifica:** 02/07/2026 09:24

---

Software DeveloperUnità Formativa (UF): Containers, Microservizi -ServerlessDocente: Denis MaggiorottoTitolo argomento: Docker Compose


DockerCompose


Cos’è DockerCompose
135
DockerCompose è uno strumento per definire ed eseguire applicazioni compose (multi-container) tramite Docker.Le applicazioni multi-container vengono definite «ascode» all’interno di uno o più file docker-compose.yamlper poi essere eseguite (o terminate) con un singolo comando.

Funzionalità
136
Tramite DockerCompose è possibile:
Eseguire ambienti applicativi multipli su di un singolo hostPreservare i dati in volumi quando i container vengono creatiRi-creare solo i container che sono cambiatiDefinire variabili che possono poi essere richiamate nel docker-compose.yamlfileSuddividere le dichiarazioni in file multipli

Verifica versione
137
Con Dockerfor Desktop, l’utility DockerCompose è già installataSu Linux invece:$ sudocurl-L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname-s)-$(uname-m)" -o /usr/local/bin/docker-composesudochmod+x /usr/local/bin/docker-compose

Verifica
138
$ docker-compose–versiondocker-composeversion1.25.4, build 8d51620a

Prima di DockerCompose
139
$ dockerbuild-t myapp.$ dockernetwork create frontend$ dockernetwork create backend$ dockerrun-d --network backendredis:alpine$ dockerrun-d -p5000:5000 --network frontend--namemy-applicationmyapp$ dockernetwork connectbackendmy-application

Con DockerCompose
140
$ docker-compose up

Nel file docker-compose.yaml
141
VersionServices-> Build-> Image-> Environment-> Ports-> VolumesVolumesNetworks

Esempio di docker-compose.yaml
142


Comandi utili
143
$ docker-compose upAvvio (aggiungere –d per background mode)
$ docker-compose psVerifica container in esecuzione
$ docker-compose logsVerifica dei logs
$ docker-compose downStop dei container e rimozione

Tutti i comandi docker-compose
144
build    Buildor rebuild services help     Get help on a command kill     Kill containers logs     View output from containers port     Print the public port for a port binding psList containers pull     Pulls service images rmRemove stopped containers run      Runa one-off command scale    Set number of containers for a service start    Startservices stop     Stopservices restart  Restartservices up       Create and start containers

Buildo image
145
E’ possibile referenziare un’immagine esistente
E’ possibile generare una nuova immagine

Depends_on
146
Determina le dipendenze tra container

Networks
147
Creazione delle networks
Utilizzo delle networks

Environment
148
E’ possibile definire variabili d’ambiente


Restart
149
Politica di restart:-No-Always-On-failure-Unless-stopped


Volumes
150Creazione dei volumi
Utilizzo dei volumi


LAB
151
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 17 –DockerComposeAssignment04 -Multicontainerapplicationwith DockerCompose
