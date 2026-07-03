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
