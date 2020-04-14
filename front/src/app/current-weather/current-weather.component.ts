import { Component, OnInit } from '@angular/core';
import { BackApiService } from '../back-api.service';

@Component({
  selector: 'app-current-weather',
  templateUrl: './current-weather.component.html',
  styleUrls: ['./current-weather.component.css']
})
export class CurrentWeatherComponent implements OnInit {

   private weather = {}
   temp: any
   pres: any
   app_temp: any
   rh: any
   clouds: any
   wind_spd: any

  constructor(private api: BackApiService) {
  }

  getCurrentWeather(city, region, country) {
      const data = {
          query: `${city} ${region} ${country}`
      }

      this.api.getWeather(data)
              .subscribe(response => {
                  console.log(response);
                  this.weather = response['data'];
              })

       console.log(this.weather)

      this.temp = this.weather['temp']
      this.pres = this.weather['pres']
      this.app_temp = this.weather['app_temp']
      this.rh = this.weather['rh']
      this.clouds = this.weather['clouds']
      this.wind_spd = this.weather['wind_spd']
  }

  ngOnInit(): void {
  }

}
