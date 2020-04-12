import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BackApiService {

  constructor(private http: HttpClient) {
  }

  public getWeather(data) {
    const url = `http://localhost:8080/weather`

    const httpOptions = {
        headers: new HttpHeaders({
            'Content-Type':  'application/json',
            'Access-Control-Allow-Origin': '*'
        })
    };

    return this.http.post(url, data, httpOptions);
   }
}
