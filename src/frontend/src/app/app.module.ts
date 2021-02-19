import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ModelFormComponent } from './model-form/model-form.component';
import { HealthComponent } from './health/health.component';
import { VisualizationsComponent } from './visualizations/visualizations.component';

@NgModule({
  declarations: [
    AppComponent,
    ModelFormComponent,
    HealthComponent,
    VisualizationsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
