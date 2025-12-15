import os

import uvicorn


if __name__ == "__main__":
    # Railway/other PaaS will set PORT; default to 8000 for local/dev
    port_str = os.environ.get("PORT", "8000")
    try:
        port = int(port_str)
    except ValueError:
        port = 8000

    uvicorn.run("src.app:app", host="0.0.0.0", port=port)


