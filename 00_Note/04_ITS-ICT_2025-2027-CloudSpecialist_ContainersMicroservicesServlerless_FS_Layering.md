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
