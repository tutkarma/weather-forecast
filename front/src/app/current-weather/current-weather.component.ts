import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { BackApiService } from '../back-api.service';

@Component({
  selector: 'app-current-weather',
  templateUrl: './current-weather.component.html',
  styleUrls: ['./current-weather.component.css']
})
export class CurrentWeatherComponent implements OnInit {

  private data = {}
  temp: any
  pres: any
  app_temp: any
  rh: any
  clouds: any
  wind_spd: any
  outfit: any

  fieldFormControl = new FormControl('', [
    Validators.required,
  ]);

  constructor(private api: BackApiService) {
  }

  getCurrentWeather(city, region, country) {
      const data = {
          query: `${city} ${region} ${country}`
      }

      this.api.getWeather(data)
              .subscribe(
              response => {
                  this.data = response['data'];
              }, error => {
                  console.error(error);
              })

      this.temp = this.data['weather']['temp']
      this.pres = this.data['weather']['pres']
      this.app_temp = this.data['weather']['app_temp']
      this.rh = this.data['weather']['rh']
      this.clouds = this.data['weather']['clouds']
      this.wind_spd = this.data['weather']['wind_spd']
      this.outfit = this.data['recomendation']
  }

  ngOnInit(): void {
  }

}
