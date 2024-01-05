from flaskr import create_app  # Import create_app from your package

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
