import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';

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

    return this.http.post(url, data, httpOptions).pipe(
       retry(1),
       catchError(this.handleError)
     );
   }

  private handleError(error) {
    let errorMessage = '';
    console.log(error);
    if (error.error instanceof ErrorEvent) {
      errorMessage = `Error: ${error.error.message}`;
    } else {
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    window.alert(errorMessage);
    return throwError(errorMessage);
  }
}
