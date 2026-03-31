from app import createApp


app = createApp()


if __name__ == "__main__":
    app.run(host="10.225.245.152", debug=True, port=5000)