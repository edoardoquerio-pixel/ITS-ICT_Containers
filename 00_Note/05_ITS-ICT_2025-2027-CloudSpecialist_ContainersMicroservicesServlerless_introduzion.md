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
