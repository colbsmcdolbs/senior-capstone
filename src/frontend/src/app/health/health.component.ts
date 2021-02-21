import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service'

@Component({
  selector: 'app-health',
  templateUrl: './health.component.html',
  styleUrls: ['./health.component.css']
})
export class HealthComponent implements OnInit {

  public modelLoadedResponse: boolean = null;
  public applicationHealthResponse: string = '';
  public isWaitingResponse: boolean = false;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {}

  public async checkHealth() {
    this.isWaitingResponse = true;
    const response = await this.apiService.getHealth();
    this.modelLoadedResponse = response.modelLoaded;
    this.applicationHealthResponse = response.apiStatus
    this.isWaitingResponse = false;
  }
}
