# Container Docker Kubernetes — Quaderno di Appunti

> **Materia:** 17_Container_Docker_Kubernetes
> **Data generazione:** Febbraio 2026
> **Corso:** ITS ICT Cloud Specialist 2025-2027

---

## Indice delle Sessioni

1. [ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless creiamo imm](#its-ict-2025-2027-cloudspecialist-containersmicroservicesservlerless-creiamo-imm)
2. [ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless deployments](#its-ict-2025-2027-cloudspecialist-containersmicroservicesservlerless-deployments)
3. [ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless DockerCompo](#its-ict-2025-2027-cloudspecialist-containersmicroservicesservlerless-dockercompo)
4. [ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless FS Layering](#its-ict-2025-2027-cloudspecialist-containersmicroservicesservlerless-fs-layering)
5. [ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless introduzion](#its-ict-2025-2027-cloudspecialist-containersmicroservicesservlerless-introduzion)
6. [ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless kubernetes ](#its-ict-2025-2027-cloudspecialist-containersmicroservicesservlerless-kubernetes-)
7. [ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless Kubernetes ](#its-ict-2025-2027-cloudspecialist-containersmicroservicesservlerless-kubernetes-)
8. [ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless networking](#its-ict-2025-2027-cloudspecialist-containersmicroservicesservlerless-networking)
9. [ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless YAML](#its-ict-2025-2027-cloudspecialist-containersmicroservicesservlerless-yaml)
10. [ITS-ICT 2025-2027-CloudSpecialist Microservices intro](#its-ict-2025-2027-cloudspecialist-microservices-intro)

---

# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless creiamo immagini

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless creiamo immagini.pdf`
**Tipo:** `.pdf`
**Dimensione:** 134.6 KB
**Ultima modifica:** 02/07/2026 09:27

---

Cloud SpecialistUnità Formativa (UF): Containers Microservizi ServerlessDocente: Denis MaggiorottoTitolo argomento: Creiamo immagini con Docker


Creare un container Docker con Node.js

Il Dockerfile
32
FROM image: Inizializza la builde setta l’immagine base sulla quale vengono eseguite le istruzioni che seguono.Es: FROM ubuntu:15.1RUN command: esegue un comando in un nuovo livello, sopra a quelli dell’immagine corrente e ne esegue la commit. L’immagine risultante viene usata dalle prossime istruzioni contenute nel Dockerfile.Es: RUN yuminstallhttpd

Il Dockerfile
33
EXPOSE port: informa Dockerche il container è in ascolto sulle porte di rete specificate in fase di runtime. È possibile specificare se la porta è in ascolto su TCP o UDP e il valore predefinito è TCP se il protocollo non è specificato.Es: EXPOSE 80EXPOSE 80/tcpENV key[=value]: Serve a settare una variabile d’ambiente che sarà disponibile all’interno del container. E’ possibile effettuare l’overraiddel valore dal comando dockerrun.Es:

Il Dockerfile
34
COPY srcdest : copia nuovi file o directory da <src> e li aggiunge al filesystemdel container nel percorso <dest>Es: COPY app/appADD srcdest : copia nuovi file o directory da <src> e li aggiunge al filesystemdel container nel percorso <dest>.A differenza di COPY, con ADD srcpuò essere una URL, in secondo luogo, è possibile estrarre un file tar dall'origine direttamente nella destinazione.Es: ADD http://myhost.com/file.txt/app

Il Dockerfile
35
USER user[:group]: imposta il nome utente (o UID) e il gruppo utente (o GID) da utilizzare durante l'esecuzione dell'immagine e per tutte le istruzioni RUN, CMD ed ENTRYPOINT che lo seguono nel DockerfileEs:USER oracle:oracleWORKDIR dir : imposta la directory di lavoro per tutte le istruzioni RUN, CMD, ENTRYPOINT, COPY e ADD che seguono nel DockerfileEs: WORKDIR /app

Il Dockerfile
36
ARG nome[=valore di default]: definisce una variabile che gli utenti possono passare in fase di compilazione con il comando dockerbuildutilizzando il flag--build-arg<varname>=<valore>.Es:ARG user=user1

Il Dockerfile
37
VOLUME path: crea un punto di mountcon il nome specificato e lo contrassegna come contenente volumi montati esternamente. I volumi esterni verranno poi montati dall’istruzione dockerrunEs:VOLUME /myvolLABEL chiave=’’valore’’ : aggiunge metadati a un'immagine. Una LABEL è una coppia chiave-valore. Es: LABEL version="1.0"

Il Dockerfile
38
ENTRYPOINT commandparam1 param2: Consente di configurare il processo che verrà eseguito dentro al container. Questo processo non potràessere modificato dal comando dockerrun.Es: ENTRYPOINT /usr/sbin/apache2ctl –D FOREGROUNDCMD commandparam1 param2: Consente di configurare il processo che verrà eseguito dentro al container. Questo processo potràessere modificato dal comando dockerrun.Es: CMD /usr/sbin/apache2ctl –D FOREGROUND

Il Dockerfile
39
Dockerfilereferencehttps://docs.docker.com/engine/reference/builder/

LAB
40
https://github.com/sunnyvale-academy/ITS-ICT_ContainersLab 06 –Node.jscontainers

Creare un container Dockercon Java

LAB
42
https://github.com/sunnyvale-academy/ITS-ICT_ContainersLab 07 –Java containers

Assignment
43
https://github.com/sunnyvale-academy/ITS-ICT_ContainersAssignment01 –Create a Redisserver image


---

# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless deployments

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless deployments.pdf`
**Tipo:** `.pdf`
**Dimensione:** 2673.8 KB
**Ultima modifica:** 02/07/2026 09:24

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
maxUnavailable: the maximum numberof podsthatcan be unavailableduringthe update process. Thiscan be an absolutenumberor percentageof the replicascount; the default is25%.maxSurge: the maximum numberof podsthatcan be createdover the desirednumberof pods. Againthiscan be an absolutenumberor a percentageof the replicascount; the default is25%.

Deployment rolloutand versioning
221


Deployment strategy
222
Recreate


Deployment strategy
223
RollingUpdate (default)


Deployment strategy
224


Deployment strategy
225
Recreate
Rollingupdate

LAB
226
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 20 –ReplicationControllerLab 21 –ReplicaSetLab 22 –Deployment


---

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


---

# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless FS Layering e Volumi

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless FS Layering e Volumi.pdf`
**Tipo:** `.pdf`
**Dimensione:** 888.7 KB
**Ultima modifica:** 02/07/2026 09:24

---

Cloud SpecialistUnità Formativa (UF): Containers Microservizi ServerlessDocente: Denis MaggiorottoTitolo argomento: FS Layeringe Volumi


File System layering

Containers layers
73
I containers (e le immagini) sono composti da layers(livelli).I livelli delle immagini sono Read Only(RM), il livello dei container è l’unico Read/Write (RW)

Containers layers
74
Immagine
$ dockerbuild-t expressweb.Step1 : FROM node:argonargon: Pullingfrom library/node......Status: Downloadednewerimage for node:argon---> 530c750a346eStep2 : RUN mkdir-p/usr/src/app---> Runningin 5090fde23e44---> 7184cc184ef8Removingintermediate container 5090fde23e44Step3 : WORKDIR /usr/src/app---> Runningin 2987746b5fba---> 86c81d89b023Removingintermediate container 2987746b5fbaStep4 : COPY package.json/usr/src/app/---> 334d93a151eeRemovingintermediate container a678c817e467Step5 : RUN npminstall---> Runningin 31ee9721cccb---> ecf7275feff3Removingintermediate container 31ee9721cccbStep6 : COPY . /usr/src/app---> 995a21532fceRemovingintermediate container a3b7591bf46dStep7 : EXPOSE 8080---> Runningin fddb8afb98d7---> e9539311a23eRemovingintermediate container fddb8afb98d7Step8 : CMD npmstart---> Runningin a262fd016da6---> fdd93d9c2c60Removingintermediate container a262fd016da6Successfullybuiltfdd93d9c2c60


Containers layers
75
Immagine
Container$ dockerrunexpressweb…


Containers layers
76
Più container creati dalla stessa immagine, condividono i layersdi quest’ultima con un enorme risparmio di spazio disco.


Containers layers
77
$ dockerps-asCONTAINER ID  IMAGE         COMMAND                 CREATED        STATUS                  PORTS  NAMES     SIZE05f427a92591  nginx:1.17.9  "/bin/bash-c 'sleep…"  12 daysago    Exited(1) 12 daysago         nginx_1   0B (virtual127MB)
-sizeisthe sizeon disk for the writablelayerof the container; alldata writtenin the container isstoredthere, and thisisnotsharedbetweencontainers-virtualsizeisthe sizeof the "read-only" layer(the image thatthe container wasstartedfrom) plus the sizeof the writablelayer(size).

Copy-on-writestrategy
78
Tutte le modifiche apportate dal container al filesystemsono memorizzate nel layerRW
Quando viene modificato un file esistente (presente nei layerRO dell’immagine), il driver di archiviazione esegue un'operazione di «copy-on-write». Per i driver aufs, overlaye overlay2, l'operazione di «copy-on-write» segue questa sequenza:
-Ricerca tra i livelli dell’immagine del file da modificare. Il processo inizia dal livello più recente (top) fino al livello base (down), un livello alla volta. -Esegue un'operazione di «copy» sulla prima occorrenza del file trovato, per copiarlo nel livello RW del container.-Le modifiche vengono apportate a questa copia del file e da quel momento il container non può vedere la copia del file esistente nel livello inferiore (RO).


Dati all’interno dei container
79
$ dockerrun-dit--namemy_container_1 acme/my-final-image:1.0 bash\&& dockerrun-dit--namemy_container_2 acme/my-final-image:1.0 bash38fa94212a419a082e6a6b87a8e2ec4a44dd327d7069b85892a707e3fc818544 1a174fc216cccf18ec7d4fe14e008e30130b11ede0f0f94a87982e310cf2e765
$ dockerpsCONTAINER ID IMAGE                   COMMAND  CREATED             STATUS                             1a174fc216cc acme/my-final-image:1.0 "bash"   About a minute ago  Up About a minute my_container_2 38fa94212a41 acme/my-final-image:1.0 "bash"   About a minute ago  Up About a minute my_container_1 
$ sudo ls/var/lib/docker/containers
$ sudo du-sh/var/lib/docker/containers/* 32K /var/lib/docker/containers/1a174fc216cccf18ec7d4fe14e008e30130b11ede0f0f94a87982e310cf2e765 32K /var/lib/docker/containers/38fa94212a419a082e6a6b87a8e2ec4a44dd327d7069b85892a707e3fc818544 

Dati all’interno dei container
80
$ sudo ls/var/lib/docker/containers
Il layerRW dei container, inizialmente è vuoto ed occupa all’incirca 32KB.La strategia Copy-on-writenon solo è più efficiente in termini di spazio, ma permette anche al container di essere veloce allo startup e shutdownSe Dockerdovesse creare un'intera copia dei livelli dell’immagine sottostante nel layerRW del container ogni volta che lo avvia, i tempi di startup e lo spazio su disco utilizzati aumenterebbero in modo significativo
QUINDI:I container non devono scrivere nel loro layerRW ma mantenerlo sempre di piccole dimensioni. I container devono persistere i dati ESCLUSIVAMENTE nei volumi (lezione successiva)

LAB
81
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 10 –FS layering

Software DeveloperUnità Formativa (UF): Containers -DockerDocente: Denis MaggiorottoTitolo argomento: Bindmounte volumi


Bindmounte volumi

Bindmounte volumi
Di default i container scrivono i file all’interno del loro RW layer, questo è sbagliato perché:
I dati verrebbero persi se il container viene cancellatoE’ difficile portare i dati al di fuori del containerIl layerRW risiede su di un singolo dockerhost, la soluzione non si presta se più container distribuiti su hostdiversi devono aver visibilità degli stessi datiIl layerRW di un container ha performance di scrittura e lettura pessimeScrivere nel layerRW di un container vuol dire farlo aumentare di dimensioni, il che rende più difficoltoso lo start e stop dello stesso
84

Dockere la persistenza dei dati
Dockeroffre tre  funzionalità per la persistenza dei dati:
85


VolumiI volumi sono la modalità consigliata per persistere dei dati da parte di un container, essi :Sono esterni al container, il quale li vede come fossero dei «dischi di rete»Sono facili da backupparee ripristinareVengono gestiti come un qualunque «oggetto Docker» tramite la DockerCLIFunzionano su Windows, Linux, MacPossono essere condivisi tra più container
86


Volumi
87
$ dockervolume create my-volList deivolumi:$ dockervolume lslocalmy-volInspect di un volume:$ dockervolume inspect my-vol[ {"Driver": "local","Labels": {},"Mountpoint": "/var/lib/docker/volumes/my-vol/_data","Name": "my-vol","Options": {},"Scope": "local" } ]
Rimozionedi un volume$ dockervolume rmmy-vol
Creazionedi un volume

Volumi
88
Start di un container e mount di un volume con --mount# --mount$ dockerrun -d \--name devtest\--mount source=my-vol,target=/app \nginx:latest
# -v$ dockerrun -d \--name devtest\-v my-vol:/app \nginx:latest
Start di un container e mount di un volume con -v

Popolazione di un volume con un container
89
# --mount$ dockerrun-d \--name=nginxtest \--mountsource=nginx-vol,destination=/usr/share/nginx/html \nginx:latest
# -v$ dockerrun-d \--name=nginxtest \-v nginx-vol:/usr/share/nginx/html \nginx:latest
 nginx-vol

Volumi read-only
90
# -v$ dockerrun-d \--name=nginxtest \-v nginx-vol:/usr/share/nginx/html:ro \nginx:latest
# --mount$ dockerrun-d \--name=nginxtest \--mountsource=nginx-vol,destination=/usr/share/nginx/html,readonly\nginx:latest

Volumi condivisi
91


Volumi condivisi
92
$ docker plugin install --grant-all-permissions vieux/sshfss$ dockervolume create --driver vieux/sshfs\-o sshcmd=test@node2:/home/test \-o password=testpassword\sshvolume$ dockerrun-d \--namesshfs-container\--volume-drivervieux/sshfs\--mountsrc=sshvolume,target=/app,volume-opt=sshcmd=test@node2:/home/test,volume-opt=password=testpassword\nginx:latest

Rimozione di volumi
93
$ docker volume rmmy-vol
$ dockervolume pruneRimozionedi tuttiI volume non utilizzati
Rimozionedi un volume

Bindmount
94
Le bindmountsono:La condivisione di aree di file systemdel Dockerhostcon il containerNormalmente sconsigliate al fine di persistere dei dati da parte del containerMeno sicure che i volumiDifficili da utilizzare per condividere i dati tra container in esecuzione su DockerhostdifferentiNon portabili tra SO differenti

Start di un container con bindmount
95
# --mount$ dockerrun -d \-it \--name devtest\--mount type=bind,source="$(pwd)"/target,target=/app \nginx:latest# -v$ dockerrun -d \-it \--name devtest\-v "$(pwd)"/target:/app \nginx:latest

Mount su directory piena
96
# --mount$ dockerrun-d \-it\--namebroken-container \--mounttype=bind,source=/tmp,target=/usr\nginx:latestdocker: Errorresponsefrom daemon: ociruntimeerror: container_linux.go:262: startingcontainer processcaused"exec: \"nginx\": executablefile notfoundin $PATH".
Nasconde il contenuto della directory sul container, a volte il container non funziona più

Read-onlybindmount
97
# --mount$ dockerrun -d \-it \--name devtest\--mount type=bind,source="$(pwd)"/target,target=/app,readonly\nginx:latest# -v$ dockerrun -d \-it \--name devtest\-v "$(pwd)"/target:/app:ro\nginx:latest

tmpfs
98
Le volumi tmpfssono:
Effimeri, perdono il contenuto allo stop del containerVeloci in scritturaUtilizzati quando il container deve produrre una grande quantità di dati, non particolarmente utiliFunzionano solo su Dockerhostlinux

tmpfs
99
# --mount$ dockerrun -d \-it \--name tmptest\--mount type=tmpfs,destination=/app \nginx:latest# --tmpfs$ dockerrun -d \-it \--name tmptest\--tmpfs/app \nginx:latest

Opzioni tmpfs
100
Option Descriptiontmpfs-size Size of the tmpfs mount in bytes. Unlimited by default.tmpfs-mode File mode of the tmpfsin octal. For instance,700or0770. Defaults to1777or world-writable.$ dockerrun -d \-it \--name tmptest\--mount type=tmpfs,destination=/app,tmpfs=1770 \nginx:latest

LAB
101
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 11 –VolumesLab 12 –BindmountsLab 13 –TmpFSmounts(solo per Linux e MacOS)
Assignment03 –Managebackups usingvolumes


---

# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless introduzione

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless introduzione.pdf`
**Tipo:** `.pdf`
**Dimensione:** 1450.5 KB
**Ultima modifica:** 02/07/2026 09:11

---

Cloud SpecialistUnità Formativa (UF): Containers Microservizi ServerlessDocente: Denis MaggiorottoTitolo argomento: Introduzione a Docker


Il docenteDenis Maggiorotto

Denis Maggiorotto•ManagingDirectorand shareholder@ Sunnyvale S.r.l.•20 yearsof experiencein ICT consulting•Senior Software / Enterprise Architect @ Major companies in public utility, telco, TV broadcastingand banking sector•Oracle UniversityPrincipalInstructorregardingJava technologies(Micro Edition, Standard Edition and Enterprise Edition) and Oracle'smiddlewareproducts.•IndependentIT professionaltrainer and public speaker
3

Sistemi virtuali
4


Denis Maggiorotto
•denis.maggiorotto@its-ictpiemonte.it@denismaggior8•https://www.linkedin.com/in/denismaggiorotto/https://github.com/denismaggior8
5


Introduzione a Docker…partendo dalla virtualizzazione del SO

Tipologie di virtualizzazione
7
Emulazione Permette l’esecuzione di un SO su una CPU completamente differente
Virtualizzazione piena (VirtualBox, Qemu)Esegue copie di SO completiPoco efficiente
Para-virtualizzazione(UML, Xen)Esegue SO completi su architetture particolari (es: XEN/x86)

Segregazione delle risorse
8


Vantaggi della virtualizzazione
9
Multi SO: Piu`SO sulla stessa macchina ﬁsica, più ambienti di esecuzione (eterogenei).
Sicurezza: eventuali attacchi da parte di malwareo spywaresono conﬁnati alla singola macchina virtuale
In ambito didattico: invece di assegnare ad ogni studente un account su una macchina ﬁsica, si assegna una macchina virtuale.
Risorse: Segregazione delle risorse della macchina ﬁsica (Host) su ciascuna macchina virtuale

Difetti della virtualizzazione
10
Spreco di risorse: le macchine virtuali possono occupare un bel po’ di risorse hardware: ogni macchina virtuale non esegue solo una copia di un certo sistema operativo ma sfrutta una copia virtuale di tutto l'hardware di cui lo stesso sistema operativo necessita per funzionare correttamente. Un approccio che necessita di RAM e che occupa parecchi cicli di CPU. Sempre più economico se paragonato all'utilizzo di più macchine a sé stanti ma gravoso dal punto di vista dell'occupazione delle risorse in alcuni frangenti.
Portabilità:Le tecnologie di virtualizzazione oggi presenti sul mercato non sono del tutto interoperabili, rendendo così le VM poco portabili tra prodotti di virtualizzazione differenti

I containers
11
Perché virtualizzareun’intera macchina, quando sarebbe possibile virtualizzaresolamente una piccola parte di essa?
I container sono una sorta di sistema operativo sempliﬁcato e virtualizzatosu quello ospitante, insieme a tutti i dati di cui necessita un’applicazione per essere eseguita: librerie, altri eseguibili, rami del ﬁle system, ﬁle di conﬁgurazione e script.
Ogni container vive in un contesto di esecuzione isolato, con un alto livello di astrazione e segregazione rispetto agli altri container e al sistema operativo sottostante.Storia dei container qui: https://www.internetpost.it/container-linux-storia-tecnologia/

I containers Docker
12
Dockerè un progetto open-source che semplifica l'esecuzione di applicazioni all'interno di container, utilizzando le funzionalità di isolamento delle risorse offerte dal kernelLinux,  come ad esempio cgroupe namespace, per consentire a container indipendenti di coesistere sulla stessa istanza di Linux, evitando però l'installazione e la manutenzione di una macchina virtuale.

Virtual machinesvs containers
13


Virtual machinesvs containers
14


Dockere Linux
15
libcontainer: fornisce un'implementazione per la creazione di container con snamespaces, cgroups, controllo di accesso al ﬁlesystem. Consente di gestire il ciclo di vita del containerslibvirt: libvirtè un'API open source, un demone e uno strumento di gestione di piattaforme di virtualizzazione (KVM, Xen, VMwareESXi, QEMU)LXC: è un ambiente di virtualizzazione a container, che opera a livello del sistema operativo e permette di eseguire diversi ambienti Linux virtuali isolati tra loro (container).systemd-nspawn: viene utilizzato per eseguire comandi o un SO in un namespace. Virtualizzacompletamente la gerarchia del ﬁle system, nonché l'albero dei processi, i vari sottosistemi IPC e il nome hoste dominio.cgroups: sono una caratteristica del kernelche consente di controllare e limitare l'utilizzo delle risorse (CPU, memoria, network I/O, disk I/O) da parte di un processo o gruppo di processi namespaces: il compito di namespaceè quello di permettere l’astrazione delle risorse (IPC, rete, punto di mountdi /, l’albero dei processi, gli utenti e i gruppi, risoluzione del nomi di rete) e isolarle dal resto del sistema


Vantaggi dei container Docker
16
Gli stessi di una macchina virtuale, con l’aggiunta di:
▪Portabilità delle immagini
▪Dimensioni più contenute
▪Risparmio risorse CPU e RAM non dovendo virtualizzarel’intero sistema operativo Guest
▪Facilità di distribuzione delle immagini
▪Miglior efﬁcienza nella gestione dello spazio disco
▪Tempi più ridotti nello startup e shutdown
▪Facilità di utilizzo anche in pipeline di CI/CD

Struttura e deﬁnizione delle componenti necessarie a creare un DockercontainerContainers, immagini, DockerHUB

Architettura di Docker
18


Componenti di Docker
19
Dockerhost: è il server su cui viene installato Dockere dove è presente il runtimenecessario ad avviare dei container.Dockerdaemon: è il processo che rimane in attesa degli «ordini» da parte del client (dockerCLI tool), per poi effettuare le operazioni necessarie ad eseguire o stoppare un container sul Dockerhost.dockerCLI tool: Si tratta di un toola linea di comando utilizzato per impartire istruzioni al Dockerdaemoned ottenere ad esempio l’esecuzione di container sul Dockerhost.Images: rappresentano la matrice dalla quale viene istanziato un container. Le immagini contengono tutto il necessario utilizzato dal container  per poter essere avviati ed erogare servizio. Le immagini possono estendere altre immagini e sono di natura immutevoli, ovvero per modificare un’immagine è necessario creare un’altra immagine che la estenda.Container: si tratta di un’istanza creata a partire da un’immagine. Il container è mantenuto in vita da un singolo processo, ovvero l’applicazione che è stata containerizzata.Dockerregistry: è un registro centralizzato, esposto su web, dove è possibile scaricare immagini da utilizzare per creare dei container.

Il nostro primo Dockercontainer
20
$ dockerrunhello-worldUnableto findimage 'hello-world:latest' locallylatest: Pullingfrom library/hello-world1b930d010525: Pull completeDigest: sha256:9572f7cdcee8591948c2963463447a53466950b3fc15a247fcad1917ca215a2fStatus: Downloadednewerimage for hello-world:latestHello from Docker!…
docker: comandorun: sottocomandohello-world: immagine. La versione dell’immagine non è stata speciﬁcata, default = latest

Sequenza di eventi
21
1) L’utente digita il comando dockerrun2)Il client (docker) invoca il rundel container al Dockerdaemon3)Il Dockerdaemon, ricevuto il comando di run, verifica l’assenza dell’immagine hello-world in locale sul Dockerhost4) Il Dockerdaemoncontatta il Dockerregistrye scarica l’immagine hello-world sul Dockerhost5) Terminato il download dell’immagine, il Dockerdaemonistanzia l’immagine ricavandone un container.6)Il container appena avviato stampa a video (standard output) il messaggio «Hello from Docker!»7) Il container, avendo esaurito il suo compito, termina 

Alcuni comandi utili
22
$ dockerpsCONTAINER ID        IMAGE      COMMAND      CREATED             STATUS      PORTS          NAMES
Stampa l’elenco dei container attivi (output vuoto signiﬁca nessun container attivo):
$ dockerps–aCONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS                      PORTS   NAMES0ec32c45c710        hello-world             "/hello"                 23 minutes ago      Exited(0) 23 minutes ago                  inspiring_borg
Stampa l’elenco di tutti i container creati:
Stampa l’elenco delle immagini scaricate$ dockerimagesREPOSITORY                                                              TAG                        IMAGE ID            CREATED  SIZE hello-world                                                             latestfce289e99eb9        13 monthsago       1.84kB

Alcuni comandi utili
23
$ dockerrm0ec32c45c7100ec32c45c710Rimozione di un container
Rimozione di un’immagine (tutti i container che la referenziano devono essere rimossi prima)$ dockerrmifce289e99eb9Untagged: hello-world:latestUntagged: hello-world@sha256:9572f7cdcee8591948c2963463447a53466950b3fc15a247fcad1917ca215a2fDeleted: sha256:fce289e99eb9bca977dae136fbe2a82b6b7d4c372474c9235adc1741675f587eDeleted: sha256:af0b15c8625bb1938f1d7b17081031f649fd14e6b233688eea3c5483994a66a3
$ dockerstart 0ec32c45c710ec85ba00ff30
Start di un container in stato Exited
$ dockerstop 0ec32c45c710ec85ba00ff30Stop di un container in stato Up

Creazione di un’immagine
24
$ dockerimagesREPOSITORY                  TAG        IMAGE ID            CREATED              SIZEubuntu15.04      d1b55fd07600        4 yearsago          131MBhello-new-image             1.0        080d4c508a92        Abouta minute ago   131MB
$ dockerbuild-t hello-new-image:1.0 .Sendingbuildcontextto Dockerdaemon2.048kBStep1/2 : FROM ubuntu:15.04---> d1b55fd07600Step2/2 : CMD echo"Hello new image!"---> Runningin d47bf5daca6cRemovingintermediate container d47bf5daca6c---> 080d4c508a92Successfullybuilt080d4c508a92Successfullytaggedhello-new-image:1.0
Builddell’immagine
List delle immagini
Creazione del DockerfileFROM ubuntu:15.04CMD echo"Hello by <NOME><COGNOME>!"-dichiarazione dell’immagine di base-istruzioni che verranno eseguite in fase di buildal ﬁne di creare la nuova immagine
$ dockerrunhello-new-image:1.0Hello by Denis Maggiorotto!Rundel container
1
2
3 4
!Ricordati di sostituire <NOME> e <COGNOME> con il tuo nome e cognome

DockerHub
25
Creazione di un’utenza su DockerHub(https://hub.docker.com)


Condivisione di un’immagine
26
$ dockerpush<dockerhubusername>/hello-new-image:1.0 The pushrefersto repository[docker.io/dennydgl1/hello-new-image]5f70bf18a086: Mountedfrom lorel/docker-stress-nged58a6b8d8d6: Pushed84cc3d400b0d: Pushed3cbe18655eb6: Pushed1.0: digest: sha256:11d580acb582a49a9b21ff746b28cfd2ebc33fe83c4113667f8017a0d373d341 size: 1149
Pushdell’immagine
Login a DockerHub$ dockerloginLogin Succeeded2
3
Tag dell’immagine$ dockertaghello-new-image:1.0 <dockerhubusername>/hello-new-image:1.01 !Ricordati di sostituire <dockerhubusername>con il tuo username creato su DockerHub

Veriﬁca l’immagine su DockerHub
27


Creazione di un container con l’immagine del compagno
28
Rundi un container scaricando l’immagine di un collega$ dockerrun<dockerhubusername>/hello-new-image:1.01 !Ricordati di sostituire <dockerhubusername>con lo username creato su DockerHubdal collega

LAB
29
https://github.com/sunnyvale-academy/ITS-ICT_ContainersLab 04 -Dockerimages and containers


---

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


---

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


---

# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless networking

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless networking.pdf`
**Tipo:** `.pdf`
**Dimensione:** 825.5 KB
**Ultima modifica:** 02/07/2026 09:24

---

Cloud SpecialistUnità Formativa (UF): Containers Microservizi ServerlessDocente: Denis MaggiorottoTitolo argomento: Container networking


Gestione della rete all'interno dei container

None network
46


None network
47
$ dockerrun-d --net none busyboxsleep10003a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3$ dockerexec-it3a82e2e4537ac9cde52fb69c3a471fd4809817a6165983f0bf5af08d67eeebe3 /bin/ash/ # ping8.8.8.8PING 8.8.8.8 (8.8.8.8): 56 data bytesping: sendto: Network isunreachable/ # ifconfiglo        Link encap:LocalLoopbackinetaddr:127.0.0.1  Mask:255.0.0.0UP LOOPBACK RUNNING  MTU:65536  Metric:1

Bridge network
48


Bridge network
49
$ dockernetwork lsNETWORK ID          NAME                DRIVER              SCOPE8dae0c4d0380        bridge              bridgelocal22530231e5cd        hosthostlocalbd5e44929d16        none                nulllocal

Bridge network
50
IP Range: 172.17.0.0 –172.17.255.255

Bridge network
51
$ dockerexec-itcontainer_1 ifconfigeth0      Link encap:Ethernet  HWaddr02:42:AC:11:00:02inetaddr:172.17.0.2  Bcast:172.17.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:10 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:796 (796.0 B)  TX bytes:0 (0.0 B)lo        Link encap:LocalLoopbackinetaddr:127.0.0.1  Mask:255.0.0.0UP LOOPBACK RUNNING  MTU:65536  Metric:1RX packets:0 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:1000RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
$ dockerrun-d --namecontainer_1 busyboxsleep100034886a41f5212abd8cd3aa4062479028899e78f32b44103bade6b67d88b76f75

Bridge network
52
$ dockerrun-d --namecontainer_2 busyboxsleep1000c8c34dad781a7a5778852de2e40fe922f6b4113759b94928d81c4753f7631b9a$ dockerexec-itcontainer_2 ifconfigeth0      Link encap:Ethernet  HWaddr02:42:AC:11:00:04inetaddr:172.17.0.4  Bcast:172.17.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:10 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:796 (796.0 B)  TX bytes:0 (0.0 B)lo        Link encap:LocalLoopbackinetaddr:127.0.0.1  Mask:255.0.0.0UP LOOPBACK RUNNING  MTU:65536  Metric:1RX packets:0 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:1000RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms---172.17.0.4 ping statistics ---

Bridge network
53
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms---172.17.0.4 ping statistics ---
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms---172.17.0.4 ping statistics ---
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms
$ dockerexec -it container_1 ping 172.17.0.4PING 172.17.0.4 (172.17.0.4): 56 data bytes64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.069 ms64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.076 ms---172.17.0.4 ping statistics ---2 packets transmitted, 2 packets received, 0% packet lossround-trip min/avg/max = 0.069/0.072/0.076 ms$ dockerexec-itcontainer_1 ping8.8.8.8PING 8.8.8.8 (8.8.8.8): 56 data bytes64 bytesfrom8.8.8.8: seq=0 ttl=117 time=33.251 ms---8.8.8.8 pingstatistics---1 packetstransmitted, 1 packetsreceived, 0% packetlossround-trip min/avg/max= 33.251/33.251/33.251ms

Bridge network
54
$ dockernetwork create --driver bridge my_bridge_network3d84cfb644d945ec14b1c9ed7f9e9fde10ae66edf41ce26d39fb60f16e00d16f$ dockernetwork inspectmy_bridge_network[{"Name": "my_bridge_network","Id": "3d84cfb644d945ec14b1c9ed7f9e9fde10ae66edf41ce26d39fb60f16e00d16f","Created": "2019-02-08T16:40:38.916055692Z","Scope": "local","Driver": "bridge","EnableIPv6": false,"IPAM": {"Driver": "default","Options": {},"Config": [{"Subnet": "172.19.0.0/16","Gateway": "172.19.0.1"

Bridge network
55
$ dockerrun-d --namecontainer_3  --net my_bridge_network busyboxsleep1000Dee203a2804a63935bea37f53d51f1b35b8e769124ca302351c4d192e1c94187$ dockerexec-itcontainer_3 ifconfigeth0      Link encap:Ethernet  HWaddr02:42:AC:13:00:02inetaddr:172.19.0.2  Bcast:172.19.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:16 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:1312 (1.2 KiB)  TX bytes:0 (0.0 B)…$ dockerstart container_1container_1$ dockerexec-itcontainer_1 ifconfig…eth0      Link encap:Ethernet  HWaddr02:42:AC:11:00:02inetaddr:172.17.0.2Bcast:172.17.255.255  Mask:255.255.0.0…$ dockerexec-itcontainer_3 ping172.17.0.2PING 172.17.0.2 (172.17.0.2): 56 data bytes…---172.17.0.2 ping statistics ---424 packets transmitted, 0 packets received, 100% packet loss

Bridge network
56
$ docker network connect bridge container_3$ dockerexec-itcontainer_3 ifconfigeth0      Link encap:Ethernet  HWaddr02:42:AC:13:00:02inetaddr:172.19.0.2  Bcast:172.19.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:36 errors:0 dropped:0 overruns:0 frame:0TX packets:434 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:2432 (2.3 KiB)  TX bytes:41972 (40.9 KiB)eth1      Link encap:Ethernet  HWaddr02:42:AC:11:00:04inetaddr:172.17.0.4  Bcast:172.17.255.255  Mask:255.255.0.0UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:9 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:726 (726.0 B)  TX bytes:0 (0.0 B)lo        Link encap:LocalLoopbackinetaddr:127.0.0.1  Mask:255.0.0.0UP LOOPBACK RUNNING  MTU:65536  Metric:1RX packets:0 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:1000RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)$ dockerexec-itcontainer_3 ping172.17.0.2PING 172.17.0.2 (172.17.0.2): 56 data bytes64 bytesfrom172.17.0.2: seq=0 ttl=64 time=0.489 ms64 bytesfrom172.17.0.2: seq=1 ttl=64 time=0.116 ms---172.17.0.2 pingstatistics---2 packetstransmitted, 2 packetsreceived, 0% packetlossround-trip min/avg/max= 0.082/0.160/0.489 ms$ dockernetwork disconnect bridge container_3

Host network
57
$ dockerrun-d --namecontainer_6 --net hostbusyboxsleep1000Baad65ed37ad53ab705bf9f9bbf50c779736bbda128859111f28fad24473421b$ dockerexec-itcontainer_6 ifconfigbr-3d84cfb644d9 Link encap:Ethernet  HWaddr02:42:4C:D0:FD:D5inetaddr:172.19.0.1  Bcast:172.19.255.255  Mask:255.255.0.0inet6 addr: fe80::42:4cff:fed0:fdd5/64 Scope:LinkUP BROADCAST MULTICAST  MTU:1500  Metric:1RX packets:434 errors:0 dropped:0 overruns:0 frame:0TX packets:26 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:35896 (35.0 KiB)  TX bytes:1676 (1.6 KiB)br-6b74b77377ec Link encap:Ethernet  HWaddr02:42:51:A1:81:6Binetaddr:172.18.0.1  Bcast:172.18.255.255  Mask:255.255.0.0UP BROADCAST MULTICAST  MTU:1500  Metric:1RX packets:0 errors:0 dropped:0 overruns:0 frame:0TX packets:0 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

Host network
58
docker0   Link encap:Ethernet  HWaddr02:42:25:25:B1:24inetaddr:172.17.0.1  Bcast:172.17.255.255  Mask:255.255.0.0inet6 addr: fe80::42:25ff:fe25:b124/64 Scope:LinkUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:103 errors:0 dropped:0 overruns:0 frame:0TX packets:220 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:0RX bytes:128663 (125.6 KiB)  TX bytes:18397 (17.9 KiB)eth0      Link encap:Ethernet  HWaddr08:00:27:2E:6E:CEinetaddr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0inet6 addr: fe80::a00:27ff:fe2e:6ece/64 Scope:LinkUP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1RX packets:146537 errors:0 dropped:0 overruns:0 frame:0TX packets:10959 errors:0 dropped:0 overruns:0 carrier:0collisions:0 txqueuelen:1000RX bytes:204339347 (194.8 MiB)  TX bytes:1083768 (1.0 MiB)

LAB
59
https://github.com/sunnyvale-academy/ITS-ICT_ContainersLab 08 –DockernetworkingAssignment02 -Multi-network Wordpressinstallation

Esposizione delle porte di un container

Esposizione di porte da un container
61
Prendiamo come esempio i seguenti container:
$ dockerrun--network bridge --namecontainer_1 httpd:latest…  
$ dockerrun--network bridge  --namecontainer_2 mysql:latest…  
httpd(Apache)
MySQL

Esposizione di porte da un container
62
XXBridge network
I container creati con una network di tipo «bridge», di default nonespongono le porte di rete sul dockerhost

Esposizione di porte da un container
63
Bridge network
Per poter accedere ai servizi, occorre rimapparele porte dei container su porte libere del dockerhost

Esposizione di porte da un container
64
Per farlo, usiamo il parametro –pseguito da una coppia di porte separate dal carattere :
$ dockerrun–p8080:80 --network bridge --namecontainer_1 httpd:latest…  
$ dockerrun–p6603:3306 --network bridge  --namecontainer_2 mysql:latest…  
httpd(Apache)
MySQL
Porta su dockerhost: porta del container 
Porta su dockerhost: porta del container 

Esposizione di porte da un container
65


Esposizione di porte da un container
66
Prendiamo come esempio i seguenti container:
$ dockerrun--network host--namecontainer_1 httpd:latest…  
$ dockerrun--network host--namecontainer_2 mysql:latest…  
httpd(Apache)
MySQL

Esposizione di porte da un container
67
Host network
I container creati con una network di tipo «host», di default espongono le porte di rete sul dockerhost

Esposizione di porte da un container
68
Prendiamo come esempio i seguenti container:
$ dockerrun--network none --namecontainer_1 httpd:latest…  
$ dockerrun--network none  --namecontainer_2 mysql:latest…  
httpd(Apache)
MySQL

Esposizione di porte da un container
69
None network
I container creati con una network di tipo «none», di default nonespongono servizi sall’esterno
XX

LAB
70
https://github.com/sunnyvale-academy/ITS-ICT_Containers
Lab 09 –Containers ports


---

# ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless YAML

**File:** `ITS-ICT 2025-2027-CloudSpecialist ContainersMicroservicesServlerless YAML.pdf`
**Tipo:** `.pdf`
**Dimensione:** 924.8 KB
**Ultima modifica:** 02/07/2026 09:24

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


Stringhe multilinea
122


Array di stringhe
123
Conventionalblock
Inlineformat

Oggetti annidati
124
L’indentazione è necessaria ed ottenuta con spazi (minimo 1, preferibile 2)

Array di oggetti
125
Conventionalblock
Inlineformat


Date
126


Dati binari
127
!!binaryindica la presenza di un contenuto codificato in Base64

Fine di un documento
128


Recap
129


Infine…
130
YAML è case sensitiveI file devono avere estensione .yaml(i .yml)Viene usata l’indentazione con spazi per delineare la struttura (oggetti)Il carattere TAB non è ammessoI commenti a singola linea hanno il carattere #separato con uno spazio dal testo che segue

Ulteriori informazioni
131
•Sito ufficiale: https://yaml.org•Ulteriori esempi: https://learnxinyminutes.com/docs/yaml/•Validatore online: http://www.yamllint.com


---

# ITS-ICT 2025-2027-CloudSpecialist Microservices intro

**File:** `ITS-ICT 2025-2027-CloudSpecialist Microservices intro.pdf`
**Tipo:** `.pdf`
**Dimensione:** 4212.4 KB
**Ultima modifica:** 02/07/2026 09:24

---

2025-2027 Cloud specialistUF: Containers-Microservices-ServlerlessDocente: Denis Maggiorotto

Il docenteDenis Maggiorotto

Denis Maggiorotto•ManagingDirectorand shareholder@ Sunnyvale S.r.l.•20 yearsof experiencein ICT consulting•Senior Software / Enterprise Architect @ Major companies in public utility, telco, TV broadcastingand banking sector•Oracle UniversityPrincipalInstructorregardingJava technologies(Micro Edition, Standard Edition and Enterprise Edition) and Oracle'smiddlewareproducts.•IndependentIT professionaltrainer and public speaker
3

Denis Maggiorotto
•denis.maggiorotto@its-ictpiemonte.it@denismaggior8•https://www.linkedin.com/in/denismaggiorotto/https://github.com/denismaggior8
4


MicroservicesIntroduzione

Microservices
L'architettura software a microservizisi riferisce ad una tecnica per progettare applicazioni flessibili ed altamente scalabili, scomponendo il software in servizi discreti che implementano specifiche funzioni di business. Questi servizi possono quindi essere sviluppati, distribuiti e scalati in modo indipendente.
6

Microservices
Ogni microserviziocomunica con altri servizi tramite API (Application Programming Interface) e protocolli standardizzati, e possono essere scritti in linguaggi differenti o con tecnologie differenti. Ciò differisce completamente dai sistemi costruiti con strutture monolitiche, in cui i servizi erano inestricabilmente interconnessi, e potevano essere scalati solo insieme.
7

Microservices
Poiché ogni servizio ha una funzionalità ben precisa, è molto più piccolo in termini di dimensioni e complessità. Il termine microservizioderiva da questo progetto di funzionalità discreta, non dalla sua dimensione fisica.
8

Microservices
9


Microservices
10
L’architettura a microserviziarriva per risolvere le problematiche di altre due architettura molto utilizzate in precedenza (e in alcuni casi utilizzate ancora oggi):MonoliticaSOA (Service OrientedArchitecture) 


Un po’ di storia

Architettura monolitica
12
L’architettura originale, dalla quale sono derivate le altreTutte le componenti software vengono eseguite in un singolo processoNon vi è alcun tipo di distribuzione delle sue componentiTutte le classi, le librerie ed altre componenti del software hanno un alto livello di dipendenza fra loroSpesso ci si riferisce a questi tipi di software col termine «Silo»

Architettura monolitica
13


Architettura monolitica
14
Spesso questi software non espongono nessuna interfaccia per essere utilizzati da altri software (API)

Architettura monolitica
15
Processo

Architettura monolitica
16
HR appPurchasingapp

Processo di sviluppo waterfall
17
Il modello waterfallè una scomposizione delle attività di progetto in fasi sequenziali e lineari, in cui ciascuna fase dipende dai risultati conseguiti dalla precedente e costituisce il prerequisito per la fase successiva. L'approccio è tipico del modello architetturale monolitico. Nello sviluppo del software, tende ad essere tra gli approcci meno iterativi e flessibili, poiché il progresso scorre in gran parte in una direzione ("verso il basso" come una cascata) attraverso le fasi di ideazione, avvio, analisi, progettazione, costruzione, test, implementazione e manutenzione .

Processo di sviluppo waterfall
18


Vantaggi architettura monolitica
19
Più facile da progettare (no rete, no latenza, no protocolli di comunicazione, tutto in un singolo processo)E’ più performante (no latenze di rete, no overheadper serializzazione/deserializzazioneoggetti, etc)E’ più facile da gestire (file di log centralizzati, unico processo da monitorare)

Service OrientedArchitecture (SOA)
20
Il termine fu coniano nel 1998Le applicazioni sono composte da processi che espongono servizi al mondo esternoOgni servizio «pubblicizza» le proprie funzionalità tramite file contenenti metadatiE’ modello architetturale che si basa molto sugli standard XML, XML Schema, XSLT, SOAP, WSDL, etc…Spesso viene fatto uso di Enterprise Service Bus (ESB) per mediare tra client e servizi o tra un servizio e l’altro (autenticazione, trasformazione, adattamento di protocollo)

Service OrientedArchitecture (SOA)
21


Service OrientedArchitecture (SOA)
22


Vantaggi architettura SOA
23
Dati e funzionalità vengono condivisi in modalità standardOgni servizio o client poteva esser scritto in linguaggi di programmazione differenti (polyglot)Ha consentito per la prima volta la comunicazione fra prodotti/linguaggi differenti utilizzando standard (XML, SOAP)

Problemi con architetture monolitiche e SOA
24
Architetture monolitiche e SOA hanno mostrato molti problemi (complessità, costi, tecnologia, etc)Molti problemi erano così rilevanti che hanno portato all’estinzione di alcuni modelli architetturali (SOA ad esempio)

Svantaggi architettura monolitica
25
Eseguibile (exe, jar, war, ear) di grandi dimensioniTempo di start/deploymolto lungo (minuti)Poco flessibile (la modifica più banale richiede una nuova versione dell’intera applicazione)Molti sviluppatori scrivono codice nello stesso repositori (conflitti in fase di merge, necessità di coordinamento tra team di grandi dimensioni)Scala molto difficilmente (il numero di utenti dev’essere noto in fase di progettazione e difficilmente può variare)

Svantaggi architettura monolitica
26
Non è adatta per internet-facingapp(il numero di utenti non è noto per definizione)Non consente rilasci molto frequentiL’applicazione è scritta con una singola tecnologia, cambiare tecnologia significa rifare l’applicazione (difficile sperimentare nuove tecnologie)Upgrade tecnologico deve coinvolgere l’intera applicazione, non solo una singola parteGestione poco efficiente delle risorse hardware (CPU, RAM). Tutte le risorse vengono utilizzate da tutte le componenti, senza compartimentalizzazione 

27
Singola architettura


28
Deploypoco efficienti


29
Uso delle risorse non compartimentalizzato


Svantaggi architettura SOA
30
Complessa da implementareMolti prodotti a pagamento (vendorlock-in)Maggior costo d’infrastruttura, di progetto e di gestioneESB molto costosoSpesso i tempi di sviluppo/gestione di architetture SOA decuplicavano rispetto a quelli necessari per architetture monoliticheL’applicazione SOA è divisa in servizi, ma è messa in produzione in modo monolitico, questa è la principale differenza con i microservizi

31
ESB complesso, costoso e di difficile gestione


Da monolite a microservizi
32


Microservizi
33
Il termine microserviziviene coniato nel 2011I problemi delle architetture monolitiche e SOA hanno ispirato il paradigma a microserviziCon i microservizii software sono modulari (invece che monolitici) ma con semplici API di comunicazione (REST/JSON invece di SOAP/XML)Nel 2014 Martin Fowlere James Lewis pubblicano il loro articolo «Microservices» ed il paradigma diventa molto popolare fino ad oggi

Microservizi
34
https://martinfowler.com/articles/microservices.html


I criteri che regolano i microservizi

Caratteristiche microservizi
36


I criteri che regolano i microserviziComponentizationvia Services

Componentizationvia Services
38
Il design modulare è sempre una buona ideaI componenti sono quelli che tutti insieme erogano la funzionalità applicativaLa modularità di solito è ottenuta tramite:Librerie/Moduli (richiamate direttamente dentro al processo)Servizi (esterni al processo, richiamati tramite protocolli)

Componentizationvia Services
39
Nel paradigma Microservizisi preferisce ottenere la modularità del software tramite ServiziLe librerie possono essere ancora utilizzate all’interno del servizio


Componentizationvia Services
40
Nel paradigma Microservizisi preferisce ottenere la modularità del software tramite ServiziLe librerie possono essere ancora utilizzate all’interno del servizio


Componentizationvia Services
41
Process
Process
Process
ProcessProcess

Componentizationvia Services
42


Componentizationvia Services
43
Perché utilizzare i servizi invece delle librerie per scomporre le applicazioni?Ogni servizio è deployabilesingolarmente (se modifico un microservizionon devo aggiornare l’intera applicazione)Ogni servizio può esser scritto in linguaggi differenti, le librerie funzionano solo con software o altre librerie scritte nello stesso linguaggioI Microservizihanno un’interfaccia ben definita (Web API)

I criteri che regolano i microserviziOrganizedaroundbusiness capabilities

Organizedaroundbusiness capabilities
45
Progetti tradizionali hanno dei teams focalizzati per tecnologie/competenze (UI, API, Business logic, DB, etc)
 Comunicazionelenta e difficoltosa

Organizedaroundbusiness capabilities
46
Progetti strutturati a microservizisono organizzati con un singolo team dedicato ad un singolo microservizio.Il Team ha un solo obiettivo, erogare il miglior microserviziopossibile Comunicazione snella, veloce


Organizedaroundbusiness capabilities
47
Lo scopo del singolo microservizioè legato ad una (ed una sola) funzionalità di business (bonifico, gestione contatore, anagrafica utente)


Organizedaroundbusiness capabilities
48
Perché l’organizzazione per «business capabilities» è migliore?
Processo di sviluppo più snello ed efficaceConfini meglio definiti (definiti dal business)

I criteri che regolano i microserviziProductsnotProjects

ProductsnotProjects
50
Con i progetti tradizionali, l’obbiettivo è quello di consegnare del codice funzionante. Questo paradigma produce i seguenti:
Il progetto finisce col primo rilascio in produzione, in alcuni casi addirittura primaQuando il progetto è concluso il team si sposta a lavorare sul prossimo Così facendo, non si instaura una relazione duratura con il cliente e le competenze vengono disperseSpesso i progetti producono applicazioni eccellenti ma molto lontane al desiderata del cliente 

ProductsnotProjects
51
Con il paradigma a Microservizil’obiettivo è quello di consegnare un prodotto, ne consegue che:Il prodotto è il vero fine, il progetto è solo il mezzo per arrivarciIl prodotto richiede supporto costante ed un rapporto con il cliente costante e duraturoSoprattutto, il team è responsabile della realizzazione del microserviziocosì come del supporto dopo averlo rilasciato («youbuildit, yourunit» by WernerVogels, AWS CTO)

ProductsnotProjects
52
Le motivazioni che hanno ispirato questo principio sono:Avere un cliente più soddisfattoCambiare la mentalità dello sviluppatore (più coinvolto in quello che sta producendo, più responsabile nella realizzazione perché un giorno dovrà manutenerlo)

I criteri che regolano i microserviziSmart endpointsand dumbpipes

Smart endpointsand dumppipes
54
Questo principio ha l’obiettivo di risolvere le problematiche introdotte dalle architetture SOA, quando, sebbene le applicazioni era composte da servizi, la loro orchestrazione era complessa e governata da moltissime tecnologie complementari (SOAP, WS-*).I Microserviziusano la forma più semplice di comunicazione, cosiddetta «dumppipes», ovvero protocolli semplici (REST/JSON invece di Web Service/XML)I Microservizinon creano una nuova tecnologia ma utilizzano quelle già offerte dal web (HTTP invece di SOAP)

Smart endpointsand dumppipes
55


Smart endpointsand dumppipes
56
Note importanti:La comunicazione diretta fra due servizi non è mai la soluzione migliore. Se un servizio cambiasse locazione (IP/porta) risulterebbe irraggiungibile dai client. Per questo spesso si utilizza una componente chiamata Service Gateway.Anche se la teoria originale incoraggiava l’uso di protocolli semplici (HTTP), negli ultimi anni sono nati altri protocolli, talvolta piuttosto complessi, per risolvere alcune inefficienze di quelli esistenti (gRPC, GraphQL, Kafka, RabbitMQ). Oggi questi protocolli fanno comunque parte del panorama tecnologico dei Microservizi.

Smart endpointsand dumppipes
57
Le motivazioni che hanno portato alla definizione di questo principio sono:Velocizzare gli sviluppi (interfacce complesse rallentano gli sviluppi).Migliorare la manutenibilità delle applicazioni (interfacce e protocolli complessi rendono complessa la gestione delle applicazioni).

I criteri che regolano i microserviziDecentralizedgovernance

Decentralizedgovernance
59
Nei progetti tradizionali esiste uno standard per qualsiasi cosaPiattaforma di sviluppoDatabaseFormato dei logGli standard vengono imposti ad ogni livello dell’applicazione, non c’è spazio per l’ autonomia decisionaleCon i microservizi, ogni team è autonomo nelle decisioni che riguardano il servizio che sviluppa/gestisceSiccome ogni team è responsabile del microservizio, prenderà decisioni migliori

Decentralizedgovernance
60
Le decisioni che il team dovrà prendere per il Microserviziopossono essere:La tecnologia di sviluppo da utilizzare (.NET, Node.js, Java, Go)Quali librerie utilizzare (a seconda della tecnologia possono variare)Come gestire la produzione dei log (standard output, Kafka, ELK)La tipologia di database (NoSQL, RDBMS)Tutte queste possibilità ci arrivano dalla natura dei Microservizie dal fatto che ognuno di essi è un processo a se stante il cui scopo è quello di fornire una funzionalità tramitol’uso di Web API.

Decentralizedgovernance
61
Le applicazioni composte da Microservizisono spesso definite «multilinguaggio» (polyglot), la decisione del linguaggio da utilizzare spetta al team responsabile del microserviziosenza preclusioni o scelte imposte dall’alto.


Decentralizedgovernance
62
I motivi che hanno ispirato questo principio sono:
Consentire la scelta della miglior tecnologia per erogare una funzionalità (servizio)Responsabilizzare maggiormente ogni team di sviluppo

I criteri che regolano i microserviziDecentralizeddata management

Decentralizeddata management
64
Nei sistemi tradizionali è comune immagazzinare i dati in un unico database.Il database centralizzato immagazzina i dati di ogni componente dell’applicazione (HR, Purchasing, etc..)


Decentralizeddata management
65
Con il paradigma a Microservizi, ogni Microservizioutilizza il proprio database (non sempre relazionale)

Decentralizeddata management
66
Note importanti: 
Il tema della decentralizzazione dei dati è il principio più controverso e dibattuto.La decentralizzazione dei database pone problematiche sulle transazioni distribuite, la duplicazione dei dati, la correlazione dei dati, etc.Non è sempre attuabile.Generalmente, se le complessità introdotte dall’applicazione di questo principio sono tante, è meglio desistere.

Decentralizeddata management
67
Perché potrebbe essere utile applicare questo principio: 
Poter usare il giusto database a seconda della tipologia di microservizio(NoSQL, RDBMS)Separare i database incoraggia l’isolamento dei dati

I criteri che regolano i microserviziInfrastructureautomation

Infrastructureautomation
69
Il paradigma SOA soffriva dell’assenza di strumenti (pochi, molto costosi, complessi)Alcuni strumenti sono molti utili nel semplificare/accelerare le operazioni di deployment:Test automatizzatiDeployment automatizzato 

Infrastructureautomation
70
Esistono molte fase del ciclo di vita di un microservizioche si possono automatizzare:


Infrastructureautomation
71
Per i Microservizil’automazione è fondamentale in quanto nascono per poter esser rilasciati, anche in produzione, ad intervalli molto più frequenti che con le architetture SOA e quella Monolitica.Il ciclo di vita di un Microservizionon può esser seguito manualmente.Esistono molti strumenti per ottenere l’automazione desiderata (JUnit, Maven, GitHubAction, Jenkins, GCP CloudBuild)


Infrastructureautomation
72


Infrastructureautomation
73
Qual è la motivazione che ha ispirato questo principio?
Avere dei cicli di sviluppo/rilascio molto più frequenti.

I criteri che regolano i microserviziDesign for failure

Design for failure
75
In un mondo distribuito e disomogeneo, molte aspetti tendono a rendere il software passibile di malfunzionamenti:Tanti microservizi= elevato traffico di rete   Latenze di rete/banda non sufficientiMicroservizioassenteCome faccio a risolvere queste problematiche? Durante la fase di scrittura del codice è necessario essere consapevoli che i disservizi possono capitare e prendere le opportune  precauzioni per gestire il disservizio nella maniera più indolore possibile.Inoltre, una parte importante la gioca il monitoraggio e l’osservabilità di un Microservizio

Design for failure
76
Microservizioassente
Rete assente

Design for failure
77


Design for failure
78
Qual’èla motivazione che ha ispirato questo principio?
Migliorare l’affidabilità dell’applicazione e quindi la userexperience

I criteri che regolano i microserviziEvolutionaryDesign

EvolutionaryDesign
80
La migrazione verso architetture a microservizidev’essere gradualeNon c’è bisogno di rifare tutta l’applicazione da zeroSi parte in piccolo e si aggiorna ogni parte separatamente

EvolutionaryDesign
81


Design di microservizi

Microservicesdesign
83
Per la progettazione di microservizideve seguire un metodo ben precisoEvitare di iniziare a scrivere codice prima di aver concluso la fase di design (Plan more, code less).La fase di design è critica per il successo dell’applicazione strutturata a microservizi(data la natura fortemente distribuita delle sue componenti) 

Software architectureprocess
84


Microservicesfocus
85


Microservicesfocus
86
MappingCommunicationpatterns


Mappingthe components
87
Forse il punto più importante nella costruzione del software a microserviziDefinisce la composizione dell’intera applicazioneUna volta svolta questa fase, è difficile cambiare l’architettura del software

Mappingthe components
88
Definire le componenti (servizi) che costituiranno il sistema sulla base di:Business requirements(requisiti funzionali)Functionalautonomy(autonomia funzionale)Data entities(entità)Data autonomy(autonomia dei dati)

Mappingthe components
89
Business requirements:L’elenco dei requisiti funzionali, costruito sui processi aziendali che l’applicazione dovrà servireEs: Gestione ordini(aggiungi ordine, rimuovi ordine) Gestione anagrafiche utenti (aggiunti utente)


Mappingthe components
90
Functionalautonomy:Il servizio non deve fornire funzionalità specifiche di altri business requirements.Es: Estrarre tutti gli ordini dell’ultima settimanaEstrarre tutti gli ordini di utenti con età > 20Possibili deroghe a questo principio, da ridurre al minimo


Mappingthe components
91
Data entities:Il servizio viene associato ad una entità.Es: OrdiniUtentiE’ possibile che le entità esposte da un microserviziosi riferiscano ad altre entità, ma solo tramite IDEs: Ordine -> ID Cliente 


Mappingthe components
92
Data autonomy:I dati gestiti dal microserviziosono atomiciIl microservizionon dipende da dati forniti da altri microserviziEs: Employeesservice utilizza i dati di AddressesserviceEmployeesservice include/fornisce anche l’indirizzo
Da evitare ma l’alternativa sarebbe peggio

Mappingthe components
93


Mappingthe components
94


Mappingthe components
95
Eccezione 1:Fornire tutti gli utenti residenti a NY con il numero di ordini effettuati da ciascuno


Mappingthe components
96
Eccezione 1:Soluzione 1: Il numero di ordini è immagazzinato nel DB dei customer.Il numero di ordini può non esser sempre sincronizzatoL’operazione di aggiornamento è semplice


Mappingthe components
97
Eccezione 1:Soluzione 2: Il microserviziodei customersinterroga il microserviziodegli orders

Mappingthe components
98
Eccezione 1:Soluzione 3: Viene creato un microservizioa cappello che interroga gli altri due ed aggrega le informazioni


Mappingthe components
99
Eccezione 2:Fornire tutti gli ordini presenti a sistema.Grosso volume di dati. Restituire una mole così grande di dati non è gestibile da un microservizio.


Mappingthe components
100
Eccezione 2:Soluzione 1: Vagliare la reale necessità di ottenere una mole così grande di informazioni.Se serve per fare reporting, utilizzare uno strumento che acceda direttamente al DB

Mappingthe components
101
Cross-cuttingservices: servizi di utilità, trasversali a tutta l’applicazione (autenticazione, autorizzazione, logging, caching)DEVONO essere inclusi nella fase di mapping

Communicationpatterns
102
Una comunicazione efficiente tra microserviziclient è fondamentaleE’ importante scegliere il pattern di comunicazione migliore a seconda della necessità

