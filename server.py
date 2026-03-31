from app import createApp


app = createApp()


if __name__ == "__main__":
    app.run(host="192.168.216.235", debug=True, port=5000)