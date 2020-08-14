from forecast.app import WeatherApp


if __name__ == '__main__':
    app = WeatherApp().create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
