import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { ModelFormComponent } from './model-form/model-form.component';
import { VisualizationsComponent } from './visualizations/visualizations.component';
import { HealthComponent } from './health/health.component';

const routes: Routes = [
  { path: '', redirectTo: '/form', pathMatch: 'full' },
  { path: 'form', component: ModelFormComponent },
  { path: 'visualizations', component: VisualizationsComponent },
  { path: 'health', component: HealthComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
