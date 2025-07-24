from fastapi import FastAPI
from starlette.response import Response 

app = FastAPI()
@app.get('/')
root()

@app.get("/{full_path:path}")


def catch_all(full_path: str):
    not_found_message = {"detail": f"Page '/{full_path}' not found"}
    return Response(
        content=json.dumps(not_found_message),
        status_code=404,
        media_type="application/json"
    )
