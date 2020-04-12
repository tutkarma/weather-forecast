import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { CurrentWeatherComponent } from './current-weather/current-weather.component';


const routes: Routes = [
    {path: '', redirectTo: '/weather', pathMatch: 'full'},
    {path: 'weather', component: CurrentWeatherComponent},
];

@NgModule({
  imports: [
      RouterModule.forRoot(routes),
      CommonModule,
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
