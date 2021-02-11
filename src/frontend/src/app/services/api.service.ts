import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  public apiUrl = 'http://api';

  constructor(private http: HttpClient) { }

  public async submitForm(formData: any): Promise<any> {
    const data = await this.http.post(`${this.apiUrl}/query`, [formData]).toPromise();
    return data;
  }
}
