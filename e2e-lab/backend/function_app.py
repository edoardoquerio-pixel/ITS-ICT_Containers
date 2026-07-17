import azure.functions as func
import json
import uuid
import logging
from datetime import datetime, timezone

app = func.FunctionApp()


@app.route(route="crea_richiesta", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(
    arg_name="doc",
    database_name="appdb",
    container_name="richieste",
    connection="COSMOS_CONNECTION_STRING",
)
def crea_richiesta(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info("Elaborazione richiesta POST per creare una nuova richiesta.")

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"errore": "JSON non valido"}),
            status_code=400,
            mimetype="application/json",
        )

    utente = req_body.get("utente")
    messaggio = req_body.get("messaggio")

    if not utente or not messaggio:
        return func.HttpResponse(
            json.dumps({"errore": "Campi obbligatori mancanti: utente, messaggio"}),
            status_code=400,
            mimetype="application/json",
        )

    documento = {
        "id": str(uuid.uuid4()),
        "utente": utente,
        "messaggio": messaggio,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "partitionKey": utente,
    }

    doc.set(func.Document.from_json(json.dumps(documento)))

    return func.HttpResponse(
        json.dumps(documento, ensure_ascii=False),
        status_code=201,
        mimetype="application/json",
    )


@app.route(route="lista_richieste", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_input(
    arg_name="docs",
    database_name="appdb",
    container_name="richieste",
    connection="COSMOS_CONNECTION_STRING",
    sql_query="SELECT * FROM c ORDER BY c.timestamp DESC",
)
def lista_richieste(req: func.HttpRequest, docs: func.DocumentList) -> func.HttpResponse:
    logging.info("Elaborazione richiesta GET per elencare le richieste.")

    items = []
    for doc in docs:
        items.append(json.loads(doc.to_json()))

    return func.HttpResponse(
        json.dumps(items, ensure_ascii=False),
        status_code=200,
        mimetype="application/json",
    )
