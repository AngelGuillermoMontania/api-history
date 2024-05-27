from src.app import app

# Inicializa el servidor de Flask
if __name__ == "__main__":
    app.run(debug=True, port=3001)
    # debug = True, para que se reinicie el servidor cada vez que se haga un cambio en el código
